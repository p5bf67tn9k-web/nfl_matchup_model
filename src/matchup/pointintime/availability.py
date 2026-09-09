"""Publish-lag availability logic.

A source row describing a game G becomes knowable at::

    data_asof = kickoff_utc(G) + assumed_game_duration + publish_lag_days

Game-grained sources join to the calendar on ``game_id``. Week-grained sources
(player_stats, ngs, team_stats) treat the described team's (season, week) game as
G. Injuries are special-cased: ``date_modified`` when present, else the conservative
fallback cutoff.
"""
from __future__ import annotations

from datetime import datetime, timedelta

import polars as pl

from matchup.config import SourcePIT, load_publish_lag
from matchup.injuries.asof_rule import injury_asof_cutoff_expr

_GAME_GRAIN_JOIN = "game_id"
_WEEK_GRAIN_KEYS = ["season", "week", "team"]


def _game_available_expr(kickoff_col: str, lag_days: int | None) -> pl.Expr:
    cfg = load_publish_lag()
    dur = cfg.assumed_game_duration_hours
    lag = 0 if lag_days is None else lag_days
    return (
        pl.col(kickoff_col).dt.convert_time_zone("UTC")
        + pl.duration(hours=dur)
        + pl.duration(days=lag)
    ).alias("data_asof")


def source_available_at(
    kickoff_utc: datetime, lag_days: int | None, *, game_duration_hours: int | None = None
) -> datetime:
    """Scalar: when a stat row for a game kicking off at ``kickoff_utc`` is knowable."""
    cfg = load_publish_lag()
    dur = game_duration_hours if game_duration_hours is not None else cfg.assumed_game_duration_hours
    return kickoff_utc + timedelta(hours=dur) + timedelta(days=(lag_days or 0))


def _attach_kickoff_game_grain(df: pl.DataFrame, calendar: pl.DataFrame) -> pl.DataFrame:
    if _GAME_GRAIN_JOIN not in df.columns:
        raise ValueError("game-grained source is missing 'game_id'")
    return df.join(
        calendar.select("game_id", "kickoff_utc"), on="game_id", how="left"
    )


def _attach_kickoff_week_grain(
    df: pl.DataFrame, team_seq: pl.DataFrame, team_col: str
) -> pl.DataFrame:
    keys = ["season", "week"]
    missing = [k for k in [*keys, team_col] if k not in df.columns]
    if missing:
        raise ValueError(f"week-grained source missing keys: {missing}")
    right = team_seq.select(
        pl.col("season"),
        pl.col("week"),
        pl.col("team").alias(team_col),
        pl.col("kickoff_utc"),
        pl.col("game_id"),
    )
    return df.join(right, on=[*keys, team_col], how="left")


def available_asof(
    df: pl.DataFrame,
    source: str,
    asof_utc: datetime,
    *,
    calendar: pl.DataFrame,
    team_seq: pl.DataFrame,
    team_col: str = "team",
    keep_kickoff: bool = False,
) -> pl.DataFrame:
    """Return only rows of ``df`` knowable at ``asof_utc``, stamped with ``data_asof``.

    ``asof_utc`` is normally the target game's kickoff. Rows without a resolvable
    kickoff (bad join) are dropped (conservative).
    """
    pit: SourcePIT = load_publish_lag().get(source)
    grain = pit.grain

    if source == "injuries":
        return _injuries_available_asof(df, asof_utc, team_seq)

    if grain in ("play", "player-game", "team-game"):
        j = _attach_kickoff_game_grain(df, calendar)
    elif grain in ("player-week", "team-week", "player-team-week"):
        j = _attach_kickoff_week_grain(df, team_seq, team_col)
    else:
        raise ValueError(f"source {source!r} grain {grain!r} not supported by available_asof")

    j = j.with_columns(_game_available_expr("kickoff_utc", pit.publish_lag_days))
    out = j.filter(
        pl.col("data_asof").is_not_null() & (pl.col("data_asof") < pl.lit(asof_utc))
    )
    if not keep_kickoff:
        out = out.drop([c for c in ("kickoff_utc",) if c in out.columns])
    return out


def _injuries_available_asof(
    df: pl.DataFrame, asof_utc: datetime, team_seq: pl.DataFrame
) -> pl.DataFrame:
    """date_modified when present; conservative fallback cutoff otherwise.

    Rows are additionally filtered to the target's own (season, week): an injury
    report from a later week is never admitted.
    """
    right = team_seq.select("season", "week", "team", "kickoff_utc")
    j = df.join(right, on=["season", "week", "team"], how="left")
    j = j.with_columns(injury_asof_cutoff_expr("kickoff_utc"))

    has_dm = "date_modified" in j.columns
    if has_dm:
        dm = pl.col("date_modified").dt.convert_time_zone("UTC")
        data_asof = (
            pl.when(dm.is_not_null()).then(dm).otherwise(pl.col("injury_asof_cutoff"))
        )
    else:
        data_asof = pl.col("injury_asof_cutoff")

    j = j.with_columns(data_asof.alias("data_asof"))
    out = j.filter(
        pl.col("data_asof").is_not_null() & (pl.col("data_asof") < pl.lit(asof_utc))
    )
    return out.drop([c for c in ("kickoff_utc", "injury_asof_cutoff") if c in out.columns])
