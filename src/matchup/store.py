"""Read access to the canonical parquet layer in data/processed/."""
from __future__ import annotations

import functools
import json
from pathlib import Path

import polars as pl

from matchup.config import REPO_ROOT, load_ingest


def _root() -> Path:
    return Path(REPO_ROOT / load_ingest().output_root)


def source_dir(source: str) -> Path:
    return _root() / source


@functools.lru_cache(maxsize=64)
def available_partitions(source: str) -> list[int]:
    d = source_dir(source)
    if not d.exists():
        return []
    out = []
    for p in sorted(d.glob("season=*")):
        man = p / "_manifest.json"
        if man.exists() and json.loads(man.read_text()).get("status") == "ok":
            out.append(int(p.name.split("=")[1]))
    return out


def read_manifest(source: str, season: int | None = None) -> dict:
    d = source_dir(source) / (f"season={season}" if season is not None else "")
    return json.loads((d / "_manifest.json").read_text())


_CACHE: dict[tuple, pl.DataFrame] = {}


def clear_cache() -> None:
    _CACHE.clear()
    available_partitions.cache_clear()


def load_source(
    source: str,
    seasons: int | list[int] | None = None,
    columns: list[str] | None = None,
    *,
    use_cache: bool = True,
) -> pl.DataFrame:
    """Load one or more season partitions of a canonical source.

    Raises FileNotFoundError if a requested season partition was never ingested,
    and returns 0 rows (typed) for partitions ingested but marked ``unavailable``.
    """
    d = source_dir(source)
    if not d.exists():
        raise FileNotFoundError(f"source {source!r} has not been ingested (missing {d})")

    flat = d / "data.parquet"
    if flat.exists() and not any(d.glob("season=*")):
        df = pl.read_parquet(flat)
        return df.select(columns) if columns else df

    if seasons is None:
        want = available_partitions(source)
    elif isinstance(seasons, int):
        want = [seasons]
    else:
        want = sorted(s for s in seasons if s in set(available_partitions(source)))

    key = (source, tuple(want), tuple(columns) if columns else None)
    if use_cache and key in _CACHE:
        return _CACHE[key]

    frames = []
    for yr in want:
        part = d / f"season={yr}" / "data.parquet"
        frames.append(pl.read_parquet(part))

    if not frames:
        out = pl.DataFrame()
    else:
        # season partitions can differ in schema (columns added/removed over the years,
        # e.g. injuries.date_modified dropped for 2025). diagonal_relaxed unions columns
        # and fills the gaps with nulls.
        df = pl.concat(frames, how="diagonal_relaxed")
        df = _normalize_keys(df)
        out = df.select(columns) if columns else df

    if use_cache:
        _CACHE[key] = out
    return out


def _normalize_keys(df: pl.DataFrame) -> pl.DataFrame:
    """Cast common join keys to consistent dtypes across sources.

    Some nflverse files type ``season``/``week`` as float (e.g. injuries: 2009.0).
    Downstream joins to the calendar need Int32.
    """
    casts = []
    for col in ("season", "week"):
        if col in df.columns and df.schema[col] != pl.Int32:
            casts.append(pl.col(col).cast(pl.Int32, strict=False).alias(col))
    return df.with_columns(casts) if casts else df
