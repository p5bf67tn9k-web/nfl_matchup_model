"""Normalize a windowed metric against the trailing 3 completed seasons."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import numpy as np
import polars as pl

from matchup.metrics.families import FAMILY_SPECS
from matchup.metrics.windows import entity_season_aggregate
from matchup.normalize.reference import (
    completed_seasons_asof,
    min_opportunities_for,
    season_is_completed,
)
from matchup.normalize.transforms import league_relative, percentile_rank, zscore

# metrics that legitimately cross zero -> use difference, not ratio, for league_relative
_DIFF_METRICS = {
    "epa_per_dropback", "dropback_success_rate", "cpoe", "adot", "epa_per_play",
    "pass_epa_per_dropback", "rush_epa_per_play", "rush_epa_per_att", "early_down_epa_per_play",
    "epa_per_target", "proe", "success_rate", "rush_success_rate", "pass_success_rate",
    "target_success_rate", "completion_pct", "catch_rate",
}


@dataclass
class ReferenceDistribution:
    family: str
    metric: str
    ref_seasons: list[int]
    values: np.ndarray          # entity-season metric values (min-opportunity filtered)
    n: int
    mean: float
    sd: float
    min_opportunities: int


def build_reference_distribution(
    family: str,
    metric: str,
    ref_game_metrics: pl.DataFrame,
    ref_seasons: list[int],
    *,
    min_opportunities: int | None = None,
) -> ReferenceDistribution:
    """``ref_game_metrics`` MUST already be restricted to completed prior seasons
    (the caller guarantees leak-safety). Builds an entity-season distribution of
    ``metric`` filtered to entities meeting the minimum opportunity bar."""
    if family not in FAMILY_SPECS:
        raise KeyError(family)
    mo = min_opportunities if min_opportunities is not None else min_opportunities_for(family)
    season_lvl = entity_season_aggregate(family, ref_game_metrics)
    if not season_lvl.is_empty():
        season_lvl = season_lvl.filter(
            pl.col("season").is_in(ref_seasons) & (pl.col("n_opportunities") >= mo)
        )
    vals = (
        season_lvl.get_column(metric).drop_nulls().to_numpy()
        if not season_lvl.is_empty() and metric in season_lvl.columns
        else np.array([])
    )
    mean = float(np.mean(vals)) if vals.size else float("nan")
    sd = float(np.std(vals, ddof=1)) if vals.size >= 2 else float("nan")
    return ReferenceDistribution(family, metric, sorted(ref_seasons), vals, int(vals.size),
                                 mean, sd, mo)


def normalize_value(value: float, ref: ReferenceDistribution, *, metric: str) -> dict:
    mode = "diff" if metric in _DIFF_METRICS else "ratio"
    return {
        f"{metric}_z": zscore(value, ref.values),
        f"{metric}_pct": percentile_rank(value, ref.values),
        f"{metric}_rel": league_relative(value, ref.values, mode=mode),
        f"{metric}_rel_mode": mode,
        "ref_seasons": ref.ref_seasons,
        "ref_n": ref.n,
        "ref_mean": ref.mean,
        "ref_sd": ref.sd,
        "ref_min_opportunities": ref.min_opportunities,
    }


def normalize_windowed(
    windowed_row: pl.DataFrame,
    family: str,
    metric: str,
    *,
    asof_utc: datetime,
    ref_game_metrics_provider,
    calendar: pl.DataFrame | None = None,
) -> pl.DataFrame:
    """Add ``<metric>_z/_pct/_rel`` + reference provenance to a single windowed row.

    ``ref_game_metrics_provider(seasons)`` returns that family's per-game metric
    table for the given seasons. It is only ever called with fully-completed
    seasons strictly before the prediction date.
    """
    if windowed_row.height != 1:
        raise ValueError("normalize_windowed expects exactly one windowed row")
    ref_seasons = completed_seasons_asof(asof_utc, calendar=calendar)
    if not ref_seasons:
        raise RuntimeError("no completed reference seasons available as of this date")
    for s in ref_seasons:
        if not season_is_completed(s, asof_utc, calendar):  # defensive re-check
            raise AssertionError(f"reference season {s} is not completed as of {asof_utc}")

    ref_gm = ref_game_metrics_provider(ref_seasons)
    ref = build_reference_distribution(family, metric, ref_gm, ref_seasons)

    value = windowed_row.get_column(metric).item()
    norm = normalize_value(value, ref, metric=metric) if value is not None else {
        f"{metric}_z": None, f"{metric}_pct": None, f"{metric}_rel": None,
        f"{metric}_rel_mode": None, "ref_seasons": ref.ref_seasons, "ref_n": ref.n,
        "ref_mean": ref.mean, "ref_sd": ref.sd, "ref_min_opportunities": ref.min_opportunities,
    }
    return windowed_row.with_columns([pl.lit(v).alias(k) for k, v in norm.items()])
