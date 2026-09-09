"""Windowing over an entity's GAME SEQUENCE (never week arithmetic).

Windows
-------
season_to_date : all of the entity's games in the target season before the target game
trailing_3     : the 3 most recent games before the target (may span seasons)
trailing_5     : the 5 most recent games before the target
prior_season   : all of the entity's games in (target_season - 1)

A bye week is simply the absence of a game row -> trailing windows span it
correctly; season_to_date is unaffected.

Output row = summed raw components + rates recomputed from the sums + provenance:
  metric family, entity_id, team, target_season, target_week, window, n_games,
  n_opportunities, first_game_id, last_game_id, data_asof (max over window),
  earliest_valid_season (from config), pit_source, pit_status.
"""
from __future__ import annotations

from datetime import datetime

import polars as pl

from matchup.config import load_publish_lag
from matchup.metrics.families import FAMILY_SPECS
from matchup.pointintime.calendar import build_game_calendar

WINDOWS = ("season_to_date", "trailing_3", "trailing_5", "prior_season")

# family -> the canonical source whose earliest_valid_season / pit_status applies
_FAMILY_SOURCE = {
    "qb": "pbp", "rb": "pbp", "wr": "pbp",
    "team_offense": "pbp", "team_defense": "pbp",
    "pass_protection": "pbp", "pass_rush": "pbp", "special_teams": "pbp",
}


def _attach_kickoff(game_metrics: pl.DataFrame) -> pl.DataFrame:
    cal = build_game_calendar().select("game_id", "kickoff_utc")
    return game_metrics.join(cal, on="game_id", how="left")


def _select_window(
    seq: pl.DataFrame, target_season: int, target_kickoff: datetime, window: str
) -> pl.DataFrame:
    # prefer a real production ``data_asof`` (kickoff + game duration + publish lag)
    # when the caller supplied one; otherwise fall back to raw kickoff order.
    if "data_asof" in seq.columns and seq.get_column("data_asof").null_count() == 0:
        cutoff_col = "data_asof"
    else:
        cutoff_col = "kickoff_utc"
    before = seq.filter(pl.col(cutoff_col) < pl.lit(target_kickoff)).sort("kickoff_utc")
    if window == "season_to_date":
        return before.filter(pl.col("season") == target_season)
    if window == "prior_season":
        return before.filter(pl.col("season") == target_season - 1)
    if window == "trailing_3":
        return before.tail(3)
    if window == "trailing_5":
        return before.tail(5)
    raise ValueError(f"unknown window {window!r}")


def window_metric(
    family: str,
    game_metrics: pl.DataFrame,
    *,
    entity_id: str,
    target_season: int,
    target_week: int,
    target_kickoff: datetime,
    window: str,
) -> pl.DataFrame:
    """Aggregate one entity's pre-target games into a single windowed row.

    ``game_metrics`` is the output of the family's ``*_game_metrics`` function
    (already as-of filtered upstream). Returns 0 rows if the entity has no
    qualifying games in the window.
    """
    if family not in FAMILY_SPECS:
        raise KeyError(family)
    spec = FAMILY_SPECS[family]
    if window not in WINDOWS:
        raise ValueError(window)
    if game_metrics.is_empty():
        return pl.DataFrame()

    gm = _attach_kickoff(game_metrics).filter(pl.col("entity_id") == entity_id)
    if gm.is_empty():
        return pl.DataFrame()

    win = _select_window(gm, target_season, target_kickoff, window)
    if win.is_empty():
        return pl.DataFrame()

    comp = [c for c in spec["components"] if c in win.columns]
    agg = win.select(
        [pl.col(c).sum().alias(c) for c in comp]
        + [
            pl.len().alias("n_games"),
            pl.col("data_asof").max().alias("data_asof"),
            pl.first("team").alias("team") if "team" in win.columns else pl.lit(None).alias("team"),
            pl.first("game_id").alias("first_game_id"),
            pl.last("game_id").alias("last_game_id"),
            pl.col("kickoff_utc").min().alias("first_game_kickoff"),
            pl.col("kickoff_utc").max().alias("last_game_kickoff"),
        ]
    )

    src = _FAMILY_SOURCE[family]
    pit = load_publish_lag().get(src)
    agg = agg.with_columns(
        pl.lit(family).alias("family"),
        pl.lit(entity_id).alias("entity_id"),
        pl.lit(spec["grain"]).alias("grain"),
        pl.lit(target_season).alias("target_season"),
        pl.lit(target_week).alias("target_week"),
        pl.lit(window).alias("window"),
        pl.col(spec["opportunity"]).alias("n_opportunities"),
        pl.lit(pit.earliest_valid_season).alias("earliest_valid_season"),
        pl.lit(src).alias("pit_source"),
        pl.lit(pit.point_in_time_status.value).alias("pit_status"),
    )

    # recompute rates from summed components
    rate_exprs = []
    for rate_name, (num, den) in spec["rates"].items():
        if num in agg.columns and den in agg.columns:
            rate_exprs.append(
                pl.when(pl.col(den) > 0).then(pl.col(num) / pl.col(den)).otherwise(None).alias(rate_name)
            )
    for out_name, comp_col in spec.get("extra", {}).items():
        if comp_col in agg.columns:
            rate_exprs.append(pl.col(comp_col).alias(out_name))
    agg = agg.with_columns(rate_exprs)

    front = [
        "family", "grain", "entity_id", "team", "target_season", "target_week",
        "window", "n_games", "n_opportunities", "data_asof", "pit_source",
        "pit_status", "earliest_valid_season", "first_game_id", "last_game_id",
        "first_game_kickoff", "last_game_kickoff",
    ]
    ordered = [c for c in front if c in agg.columns] + [c for c in agg.columns if c not in front]
    return agg.select(ordered)


def entity_season_aggregate(family: str, game_metrics: pl.DataFrame) -> pl.DataFrame:
    """One row per (entity_id, season): all of that season's games summed, rates
    recomputed. Used to build league-reference distributions for normalization.
    NOT an as-of view -- callers pass only completed-season game_metrics."""
    spec = FAMILY_SPECS[family]
    if game_metrics.is_empty():
        return pl.DataFrame()
    comp = [c for c in spec["components"] if c in game_metrics.columns]
    agg = game_metrics.group_by(["entity_id", "season"]).agg(
        [pl.col(c).sum().alias(c) for c in comp]
        + [pl.len().alias("n_games"),
           pl.first("team").alias("team") if "team" in game_metrics.columns else pl.lit(None).alias("team")]
    )
    rate_exprs = []
    for rate_name, (num, den) in spec["rates"].items():
        if num in agg.columns and den in agg.columns:
            rate_exprs.append(
                pl.when(pl.col(den) > 0).then(pl.col(num) / pl.col(den)).otherwise(None).alias(rate_name)
            )
    for out_name, comp_col in spec.get("extra", {}).items():
        if comp_col in agg.columns:
            rate_exprs.append(pl.col(comp_col).alias(out_name))
    agg = agg.with_columns(rate_exprs)
    return agg.with_columns(
        pl.lit(family).alias("family"),
        pl.col(spec["opportunity"]).alias("n_opportunities"),
    )


def window_all(
    family: str,
    game_metrics: pl.DataFrame,
    *,
    entity_ids: list[str],
    target_season: int,
    target_week: int,
    target_kickoff: datetime,
    windows: tuple[str, ...] = WINDOWS,
) -> pl.DataFrame:
    """Windowed rows for many entities x windows (used by diagnostics)."""
    frames = []
    for eid in entity_ids:
        for w in windows:
            r = window_metric(
                family, game_metrics, entity_id=eid, target_season=target_season,
                target_week=target_week, target_kickoff=target_kickoff, window=w,
            )
            if not r.is_empty():
                frames.append(r)
    return pl.concat(frames, how="diagonal_relaxed") if frames else pl.DataFrame()
