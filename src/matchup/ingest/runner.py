"""Ingest nflverse sources into the canonical parquet layer.

Design points
-------------
* The nflreadpy filesystem cache under ``data/raw/nflreadpy_cache`` is the immutable
  raw layer. We never mutate it.
* ``data/processed/<source>/season=YYYY/data.parquet`` is our canonical layer,
  partitioned by season. Sources with no season key write ``<source>/data.parquet``.
* Every partition gets a ``_manifest.json`` sidecar. Only ``ingested_at`` may differ
  between two runs against the same cache; ``content_sha256`` must match.
* A season nflverse has not published yet raises inside nflreadpy. We catch it and
  write an ``unavailable`` manifest instead of crashing (decision DC).
"""
from __future__ import annotations

import hashlib
import json
import warnings
from dataclasses import dataclass, field
from datetime import UTC, datetime
from importlib.metadata import version as _pkg_version
from pathlib import Path
from typing import Any

import nflreadpy as nfl
import polars as pl

from matchup.config import IngestConfig, load_ingest, load_publish_lag

# nflreadpy raises bare ValueError for out-of-range seasons and requests errors for 404s.
_UNAVAILABLE_ERRORS = (ValueError, ConnectionError, OSError)
_UNAVAILABLE_SIGNS = ("must be between", "404", "not found", "no such")

_HARD_MAX_SEASON = 2100  # ingest.yaml ranges are clamped by nflreadpy itself; this is a noop guard

_DATE_COLS = ("game_date", "gameday")


@dataclass
class SourceResult:
    source: str
    partitions_written: list[int | None] = field(default_factory=list)
    partitions_unavailable: list[int | None] = field(default_factory=list)
    total_rows: int = 0
    errors: list[str] = field(default_factory=list)


def configure_cache(cfg: IngestConfig | None = None) -> None:
    """Point nflreadpy at the repo-local filesystem cache."""
    from nflreadpy.config import update_config

    cfg = cfg or load_ingest()
    from matchup.config import REPO_ROOT

    update_config(
        cache_mode="filesystem",
        cache_dir=Path(REPO_ROOT / cfg.cache_root),
        cache_duration=7 * 86400,
        verbose=False,
    )


def processed_path(source: str, season: int | None, cfg: IngestConfig | None = None) -> Path:
    cfg = cfg or load_ingest()
    from matchup.config import REPO_ROOT

    root = Path(REPO_ROOT / cfg.output_root) / source
    return (root / f"season={season}" if season is not None else root) / "data.parquet"


def _is_unavailable(exc: Exception) -> bool:
    msg = str(exc).lower()
    return isinstance(exc, _UNAVAILABLE_ERRORS) and any(s in msg for s in _UNAVAILABLE_SIGNS)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def _data_date_range(df: pl.DataFrame) -> tuple[str | None, str | None]:
    for col in _DATE_COLS:
        if col in df.columns and df.height:
            s = df.get_column(col).cast(pl.Utf8, strict=False).drop_nulls()
            if len(s):
                return s.min(), s.max()
    return None, None


def _write_partition(
    df: pl.DataFrame,
    source: str,
    season: int | None,
    loader: str,
    loader_kwargs: dict[str, Any],
    cfg: IngestConfig,
) -> dict[str, Any]:
    out = processed_path(source, season, cfg)
    out.parent.mkdir(parents=True, exist_ok=True)
    # Deterministic write: stable column order, fixed compression, no embedded stats.
    df = df.select(sorted(df.columns))
    df.write_parquet(out, compression="zstd", statistics=False)

    pit = load_publish_lag().sources.get(source)
    dmin, dmax = _data_date_range(df)
    manifest = {
        "source": source,
        "season": season,
        "loader": loader,
        "loader_kwargs": loader_kwargs,
        "status": "ok",
        "unavailable_reason": None,
        "row_count": df.height,
        "column_count": df.width,
        "content_sha256": _sha256(out),
        "source_data_min_date": dmin,
        "source_data_max_date": dmax,
        "point_in_time_status": pit.point_in_time_status.value if pit else "UNKNOWN",
        "publish_lag_days": pit.publish_lag_days if pit else None,
        "publish_lag_type": pit.publish_lag_type if pit else "unknown",
        "nflreadpy_version": _pkg_version("nflreadpy"),
        "polars_version": pl.__version__,
        "ingested_at": datetime.now(UTC).isoformat(timespec="seconds"),
    }
    _write_manifest(out.parent, manifest)
    return manifest


def _write_unavailable(
    source: str, season: int | None, loader: str, reason: str, cfg: IngestConfig
) -> dict[str, Any]:
    out = processed_path(source, season, cfg)
    out.parent.mkdir(parents=True, exist_ok=True)
    pit = load_publish_lag().sources.get(source)
    manifest = {
        "source": source,
        "season": season,
        "loader": loader,
        "loader_kwargs": {},
        "status": "unavailable",
        "unavailable_reason": reason,
        "row_count": 0,
        "column_count": 0,
        "content_sha256": None,
        "source_data_min_date": None,
        "source_data_max_date": None,
        "point_in_time_status": pit.point_in_time_status.value if pit else "UNKNOWN",
        "publish_lag_days": pit.publish_lag_days if pit else None,
        "publish_lag_type": pit.publish_lag_type if pit else "unknown",
        "nflreadpy_version": _pkg_version("nflreadpy"),
        "polars_version": pl.__version__,
        "ingested_at": datetime.now(UTC).isoformat(timespec="seconds"),
    }
    _write_manifest(out.parent, manifest)
    return manifest


def _write_manifest(directory: Path, manifest: dict[str, Any]) -> None:
    (directory / "_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))


def _call_loader(loader: str, season: int | None, kwargs: dict[str, Any]) -> pl.DataFrame:
    fn = getattr(nfl, loader)
    if season is None:
        return fn(**kwargs)
    return fn(seasons=[season], **kwargs)


def ingest_source(
    source: str,
    cfg: IngestConfig | None = None,
    *,
    extra_seasons: list[int] | None = None,
) -> SourceResult:
    """Materialise one source's canonical partitions.

    ``extra_seasons`` lets the live pipeline probe not-yet-published seasons; each
    is attempted and recorded as ``unavailable`` if nflverse has no file yet.
    """
    cfg = cfg or load_ingest()
    configure_cache(cfg)
    if source not in cfg.sources:
        raise KeyError(f"{source!r} not in config/ingest.yaml")
    spec = cfg.sources[source]
    res = SourceResult(source=source)

    if spec.seasons == "none":
        seasons: list[int | None] = [None]
    elif spec.seasons == "all":
        # let nflreadpy decide the upper bound; load once, then partition by season
        seasons = ["__all__"]  # sentinel
    else:
        seasons = list(spec.season_list(_HARD_MAX_SEASON))
    if extra_seasons:
        seasons = [*seasons, *extra_seasons]

    for season in seasons:
        try:
            if season == "__all__":
                df = _call_loader(spec.loader, None, spec.kwargs)
                if "season" not in df.columns:
                    raise RuntimeError(f"{source}: expected a 'season' column for partitioning")
                for (yr,) in df.select("season").unique().sort("season").iter_rows():
                    part = df.filter(pl.col("season") == yr)
                    m = _write_partition(part, source, int(yr), spec.loader, spec.kwargs, cfg)
                    res.partitions_written.append(int(yr))
                    res.total_rows += m["row_count"]
                continue

            df = _call_loader(spec.loader, season, spec.kwargs)
            m = _write_partition(df, source, season, spec.loader, spec.kwargs, cfg)
            res.partitions_written.append(season)
            res.total_rows += m["row_count"]
        except Exception as exc:
            if _is_unavailable(exc):
                _write_unavailable(source, season if season != "__all__" else None,
                                   spec.loader, str(exc), cfg)
                res.partitions_unavailable.append(season if season != "__all__" else None)
                warnings.warn(f"{source} season={season}: unavailable ({exc})", stacklevel=2)
            else:
                res.errors.append(f"season={season}: {type(exc).__name__}: {exc}")
                raise
    return res


def ingest_all(
    cfg: IngestConfig | None = None, *, include_live_probe: bool = True
) -> dict[str, SourceResult]:
    cfg = cfg or load_ingest()
    from matchup.config import REPO_ROOT

    results: dict[str, SourceResult] = {}
    for source, spec in cfg.sources.items():
        extra = None
        if include_live_probe and spec.seasons not in ("all", "none"):
            extra = [s for s in cfg.live_seasons_probe if s > spec.seasons[1]]
        results[source] = ingest_source(source, cfg, extra_seasons=extra)

    top = {
        "ingested_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "nflreadpy_version": _pkg_version("nflreadpy"),
        "polars_version": pl.__version__,
        "sources": {
            s: {
                "written": r.partitions_written,
                "unavailable": r.partitions_unavailable,
                "total_rows": r.total_rows,
                "errors": r.errors,
            }
            for s, r in results.items()
        },
    }
    root = Path(REPO_ROOT / cfg.output_root)
    root.mkdir(parents=True, exist_ok=True)
    (root / "_ingest_manifest.json").write_text(json.dumps(top, indent=2, sort_keys=True))
    return results
