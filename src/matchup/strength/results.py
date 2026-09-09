"""Game RESULTS accessor -- outcomes only, never a feature source.

Final scores and wins are legitimately known immediately after a game. This
module exposes them for RESEARCH (as the dependent variable) and for the weekly
snapshot record. It is deliberately separate from the as-of feature engine and
must never be joined into a feature frame -- a leakage test enforces this.

`data_asof` on every row = kickoff + assumed game duration, i.e. the result is
available right after the game and for no earlier as-of time.
"""
from __future__ import annotations

import functools

import polars as pl

from matchup.config import load_publish_lag
from matchup.pointintime.calendar import build_game_calendar
from matchup.store import load_source

_RESULT_COLS = ("home_score", "away_score")


@functools.lru_cache(maxsize=8)
def team_game_results(seasons: tuple[int, ...] | None = None) -> pl.DataFrame:
    """One row per (team, completed game): points_for / points_against /
    point_diff / won / tie, plus opponent, home flag, season, week, game_type,
    kickoff_utc and result-available `data_asof`.

    Only games that have actually been played (both scores present and kickoff in
    the past relative to the data) are returned.
    """
    sched = load_source("schedules", seasons=list(seasons) if seasons else None)
    if sched.is_empty():
        return pl.DataFrame()
    keep = [c for c in ("game_id", "season", "week", "game_type", "home_team", "away_team",
                        *_RESULT_COLS) if c in sched.columns]
    sched = sched.select(keep)
    if not set(_RESULT_COLS).issubset(sched.columns):
        return pl.DataFrame()

    cal = build_game_calendar().select("game_id", "kickoff_utc")
    dur_h = load_publish_lag().assumed_game_duration_hours

    played = (
        sched.join(cal, on="game_id", how="inner")
        .filter(pl.col("home_score").is_not_null() & pl.col("away_score").is_not_null())
        .with_columns((pl.col("kickoff_utc") + pl.duration(hours=dur_h)).alias("data_asof"))
    )
    if seasons:
        played = played.filter(pl.col("season").is_in(list(seasons)))

    home = played.select(
        "game_id", "season", "week", "game_type", "kickoff_utc", "data_asof",
        pl.col("home_team").alias("team"),
        pl.col("away_team").alias("opponent"),
        pl.lit(True).alias("is_home"),
        pl.col("home_score").alias("points_for"),
        pl.col("away_score").alias("points_against"),
    )
    away = played.select(
        "game_id", "season", "week", "game_type", "kickoff_utc", "data_asof",
        pl.col("away_team").alias("team"),
        pl.col("home_team").alias("opponent"),
        pl.lit(False).alias("is_home"),
        pl.col("away_score").alias("points_for"),
        pl.col("home_score").alias("points_against"),
    )
    out = pl.concat([home, away]).with_columns(
        (pl.col("points_for") - pl.col("points_against")).alias("point_diff"),
        (pl.col("points_for") > pl.col("points_against")).cast(pl.Int8).alias("won"),
        (pl.col("points_for") == pl.col("points_against")).cast(pl.Int8).alias("tie"),
    )
    return out.sort(["season", "team", "kickoff_utc"])


def latest_completed_week(season: int) -> int:
    """Highest regular-season week with >= 1 completed game for `season`; 0 if none."""
    res = team_game_results((season,))
    if res.is_empty():
        return 0
    reg = res.filter(pl.col("game_type") == "REG")
    return int(reg.get_column("week").max()) if not reg.is_empty() else 0


def team_record_through_week(season: int, through_week: int) -> pl.DataFrame:
    """Per-team W-L-T + points for/against/diff over REG weeks 1..through_week."""
    res = team_game_results((season,))
    if res.is_empty():
        return pl.DataFrame()
    reg = res.filter((pl.col("game_type") == "REG") & (pl.col("week") <= through_week))
    if reg.is_empty():
        return pl.DataFrame()
    return (
        reg.group_by("team")
        .agg(
            pl.len().alias("games"),
            pl.col("won").sum().alias("wins"),
            pl.col("tie").sum().alias("ties"),
            (pl.len() - pl.col("won").sum() - pl.col("tie").sum()).alias("losses"),
            pl.col("points_for").sum().alias("points_for"),
            pl.col("points_against").sum().alias("points_against"),
            pl.col("point_diff").sum().alias("point_diff"),
            pl.col("points_for").mean().alias("points_for_pg"),
            pl.col("points_against").mean().alias("points_against_pg"),
        )
        .with_columns(
            ((pl.col("wins") + 0.5 * pl.col("ties")) / pl.col("games")).alias("win_pct"),
        )
        .sort("team")
    )
