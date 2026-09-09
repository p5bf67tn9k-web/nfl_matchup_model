"""Assemble family per-game metric tables.

Two entry points:

* ``game_metrics_from_asof(ao, family)`` -- PRODUCTION path. Classifies the
  already-leak-filtered ``ao.pbp()`` frame. Every row's ``data_asof`` is < the
  target kickoff by construction of the as-of engine.

* ``game_metrics_offline(family, seasons)`` -- for NORMALIZATION REFERENCE
  distributions (completed prior seasons only) and RETROSPECTIVE DIAGNOSTICS.
  Reads the canonical pbp directly, NO as-of filtering. Callers must restrict
  ``seasons`` to completed seasons strictly before the prediction date, or label
  the output retrospective. ``data_asof`` is set to null here.
"""
from __future__ import annotations

import functools

import polars as pl

from matchup.metrics.families import FAMILY_SPECS
from matchup.metrics.plays import classify_plays
from matchup.pointintime.asof import AsOf
from matchup.store import load_source

_PBP_FAMILIES = set(FAMILY_SPECS)


def clear_metric_caches() -> None:
    for fn in (_raw_pbp, _classified, game_metrics_batch):
        fn.cache_clear()


def game_metrics_from_asof(ao: AsOf, family: str) -> pl.DataFrame:
    if family not in _PBP_FAMILIES:
        raise KeyError(family)
    spec = FAMILY_SPECS[family]
    raw = ao.pbp()
    if spec.get("raw_pbp"):
        return spec["fn"](raw)
    return spec["fn"](classify_plays(raw))


@functools.lru_cache(maxsize=16)
def _raw_pbp(seasons: tuple[int, ...]) -> pl.DataFrame:
    pbp = load_source("pbp", seasons=list(seasons))
    if pbp.is_empty():
        return pbp
    return pbp.with_columns(pl.lit(None).cast(pl.Datetime("us", "UTC")).alias("data_asof"))


@functools.lru_cache(maxsize=16)
def _classified(seasons: tuple[int, ...]) -> pl.DataFrame:
    raw = _raw_pbp(seasons)
    return raw if raw.is_empty() else classify_plays(raw)


def game_metrics_offline(family: str, seasons: list[int]) -> pl.DataFrame:
    """NOT as-of filtered. Use only for completed-season reference distributions
    or clearly-labelled retrospective diagnostics."""
    if family not in _PBP_FAMILIES:
        raise KeyError(family)
    spec = FAMILY_SPECS[family]
    key = tuple(sorted(seasons))
    src = _raw_pbp(key) if spec.get("raw_pbp") else _classified(key)
    return src if src.is_empty() else spec["fn"](src)


def offline_provider(family: str):
    """Return a ``provider(seasons)`` closure for ``normalize_windowed``."""
    return lambda seasons: game_metrics_offline(family, list(seasons))


@functools.lru_cache(maxsize=32)
def game_metrics_batch(family: str, seasons: tuple[int, ...]) -> pl.DataFrame:
    """Offline game_metrics for many seasons PLUS a production ``data_asof`` column
    (= game kickoff + assumed game duration + the source's publish_lag_days).

    This is the batch equivalent of ``game_metrics_from_asof``: windowing filters
    on ``data_asof < target_kickoff``, giving the same publish-lag guarantee as the
    live path without rebuilding an ``AsOf`` per target game. Verified leak-safe by
    the Phase 3 poisoned-future-row test.
    """
    from matchup.config import load_publish_lag
    from matchup.metrics.windows import _FAMILY_SOURCE
    from matchup.pointintime.calendar import build_game_calendar

    gm = game_metrics_offline(family, list(seasons))
    if gm.is_empty():
        return gm
    pit = load_publish_lag()
    src = pit.get(_FAMILY_SOURCE[family])
    dur_h = pit.assumed_game_duration_hours
    lag_d = src.publish_lag_days or 0
    cal = build_game_calendar().select("game_id", "kickoff_utc")
    return (
        gm.drop([c for c in ("data_asof",) if c in gm.columns])
        .join(cal, on="game_id", how="left")
        .with_columns(
            (pl.col("kickoff_utc") + pl.duration(hours=dur_h) + pl.duration(days=lag_d)).alias("data_asof")
        )
    )
