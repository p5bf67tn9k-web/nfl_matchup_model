"""The game calendar and team game sequence.

game_calendar   -- one row per game, fixture columns only (no scores, no lines),
                   with a timezone-aware ``kickoff_utc``.
team_game_seq   -- one row per (team, game), ordered chronologically, with an
                   integer ``team_game_index`` so that "last N games" is well
                   defined across byes and across the regular/postseason boundary
                   (leakage risk L-10).
"""
from __future__ import annotations

import functools

import polars as pl

from matchup.config import load_publish_lag
from matchup.store import load_source

# Fixture columns that are knowable months in advance. Everything else in the
# schedules file (scores, results, betting lines) is REFERENCE_ONLY and dropped.
GAME_CALENDAR_COLUMNS = [
    "game_id",
    "season",
    "week",
    "game_type",
    "gameday",
    "gametime",
    "weekday",
    "kickoff_utc",
    "kickoff_time_estimated",
    "home_team",
    "away_team",
    "location",
    "roof",
    "surface",
    "away_rest",
    "home_rest",
    "div_game",
    "stadium_id",
    "stadium",
]


def kickoff_expr(
    gameday: str = "gameday",
    gametime: str = "gametime",
    *,
    tz: str | None = None,
    fallback_local_time: str | None = None,
) -> pl.Expr:
    """Expr producing a tz-aware UTC kickoff from ``gameday`` + ``gametime``.

    ``gametime`` is US Eastern (verified in Phase 0 by cross-checking pbp.start_time
    against pbp.time_of_day). When ``gametime`` is null we substitute a conservative
    early-window local time so the resulting as-of cutoff is *earlier* (prefer false
    exclusion over false inclusion).
    """
    cfg = load_publish_lag()
    tz = tz or cfg.timezone
    fallback_local_time = fallback_local_time or cfg.kickoff_fallback_local_time

    gt = pl.col(gametime).fill_null(fallback_local_time)
    naive = (pl.col(gameday).cast(pl.Utf8) + pl.lit(" ") + gt).str.to_datetime(
        "%Y-%m-%d %H:%M", strict=False
    )
    return (
        naive.dt.replace_time_zone(tz, ambiguous="earliest")
        .dt.convert_time_zone("UTC")
        .alias("kickoff_utc")
    )


def build_game_calendar(seasons: list[int] | None = None) -> pl.DataFrame:
    key = tuple(sorted(seasons)) if seasons is not None else None
    return _build_game_calendar_cached(key)


@functools.lru_cache(maxsize=32)
def _build_game_calendar_cached(seasons: tuple[int, ...] | None) -> pl.DataFrame:
    sched = load_source("schedules", seasons=list(seasons) if seasons is not None else None)
    if sched.is_empty():
        raise RuntimeError("schedules source is empty; run ingest first")

    cfg = load_publish_lag()
    fallback = cfg.kickoff_fallback_local_time

    df = sched.with_columns(
        kickoff_expr(),
        (pl.col("gametime").is_null()).alias("kickoff_time_estimated"),
    )
    # gametime present but unparseable also counts as estimated
    df = df.with_columns(
        (pl.col("kickoff_time_estimated") | pl.col("kickoff_utc").is_null()).alias(
            "kickoff_time_estimated"
        )
    )
    # last-resort kickoff for rows where even the date failed to parse: noon UTC on gameday
    df = df.with_columns(
        pl.when(pl.col("kickoff_utc").is_null())
        .then(
            (pl.col("gameday").cast(pl.Utf8) + pl.lit(f" {fallback}"))
            .str.to_datetime("%Y-%m-%d %H:%M", strict=False)
            .dt.replace_time_zone(cfg.timezone, ambiguous="earliest")
            .dt.convert_time_zone("UTC")
        )
        .otherwise(pl.col("kickoff_utc"))
        .alias("kickoff_utc")
    )

    keep = [c for c in GAME_CALENDAR_COLUMNS if c in df.columns]
    cal = df.select(keep).sort(["kickoff_utc", "game_id"])

    _assert_no_reference_columns(cal)
    return cal


def _assert_no_reference_columns(cal: pl.DataFrame) -> None:
    banned = set(load_publish_lag().get("schedules").reference_only_columns)
    leaked = banned.intersection(cal.columns)
    if leaked:
        raise AssertionError(f"game_calendar leaked REFERENCE_ONLY columns: {sorted(leaked)}")


def build_team_game_sequence(seasons: list[int] | None = None) -> pl.DataFrame:
    key = tuple(sorted(seasons)) if seasons is not None else None
    return _build_team_game_sequence_cached(key)


@functools.lru_cache(maxsize=32)
def _build_team_game_sequence_cached(seasons: tuple[int, ...] | None) -> pl.DataFrame:
    cal = build_game_calendar(seasons=list(seasons) if seasons is not None else None)

    home = cal.select(
        "game_id", "season", "week", "game_type", "kickoff_utc", "kickoff_time_estimated",
        pl.col("home_team").alias("team"),
        pl.col("away_team").alias("opponent"),
        pl.lit(True).alias("is_home"),
    )
    away = cal.select(
        "game_id", "season", "week", "game_type", "kickoff_utc", "kickoff_time_estimated",
        pl.col("away_team").alias("team"),
        pl.col("home_team").alias("opponent"),
        pl.lit(False).alias("is_home"),
    )
    seq = pl.concat([home, away]).sort(["team", "kickoff_utc", "game_id"])
    seq = seq.with_columns(
        pl.int_range(pl.len()).over("team").alias("team_game_index"),
        pl.int_range(pl.len()).over(["team", "season"]).alias("team_game_index_season"),
    )
    return seq
