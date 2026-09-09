"""Join-throughs for week-grained external sources (NGS, PFR).

These sources are already (player, week) grained and leak-filtered by the as-of
engine. Here we just select the documented descriptive columns and attach
``earliest_valid_season`` + provenance. NO derivation, NO windowing beyond simple
opportunity-weighted means (documented), NO predictive claim.
"""
from __future__ import annotations

import polars as pl

from matchup.config import load_publish_lag
from matchup.pointintime.asof import AsOf

# source -> descriptive columns kept (as published by NGS; already opportunity-
# weighted within the week by NGS). NGS receiving/rushing weekly files carry no
# usable attempt-count column, so these are surfaced as-is per player-week.
NGS_SPEC = {
    "ngs_passing": [
        "avg_time_to_throw", "aggressiveness", "avg_air_yards_to_sticks",
        "completion_percentage_above_expectation", "expected_completion_percentage",
    ],
    "ngs_receiving": [
        "avg_separation", "avg_cushion", "avg_yac_above_expectation", "avg_expected_yac",
    ],
    "ngs_rushing": [
        "rush_yards_over_expected_per_att", "efficiency", "rush_pct_over_expected",
        "rush_yards_over_expected",
    ],
}

PFR_PASS_COLS = ["times_pressured", "times_pressured_pct", "times_blitzed", "times_hurried",
                 "times_hit", "times_sacked", "passing_bad_throw_pct", "passing_drops"]
PFR_DEF_COLS = ["def_pressures", "def_sacks", "def_missed_tackles", "def_missed_tackle_pct",
                "def_targets", "def_completions_allowed", "def_yards_allowed",
                "def_passer_rating_allowed", "def_completion_pct"]


def _tag(df: pl.DataFrame, source: str) -> pl.DataFrame:
    if df.is_empty():
        return df
    pit = load_publish_lag().get(source)
    return df.with_columns(
        pl.lit(source).alias("metric_source"),
        pl.lit(pit.earliest_valid_season).alias("earliest_valid_season"),
        pl.lit(pit.point_in_time_status.value).alias("pit_status"),
    )


def ngs_player_week(ao: AsOf, stat_type: str, team: str | None = None) -> pl.DataFrame:
    src = f"ngs_{stat_type}"
    df = ao.ngs(stat_type, team)
    if df.is_empty():
        return df
    cols = NGS_SPEC[src]
    keep = ["player_gsis_id", "team", "season", "week", "data_asof", *[c for c in cols if c in df.columns]]
    return _tag(df.select([c for c in keep if c in df.columns]), src)


def pfr_pass_player_week(ao: AsOf, team: str | None = None) -> pl.DataFrame:
    df = ao.pfr("pass", team)
    if df.is_empty():
        return df
    keep = ["pfr_player_id", "team", "opponent", "season", "week", "game_id", "data_asof",
            *[c for c in PFR_PASS_COLS if c in df.columns]]
    return _tag(df.select([c for c in keep if c in df.columns]), "pfr_pass")


def pfr_def_player_week(ao: AsOf, team: str | None = None) -> pl.DataFrame:
    df = ao.pfr("def", team)
    if df.is_empty():
        return df
    keep = ["pfr_player_id", "team", "opponent", "season", "week", "game_id", "data_asof",
            *[c for c in PFR_DEF_COLS if c in df.columns]]
    return _tag(df.select([c for c in keep if c in df.columns]), "pfr_def")
