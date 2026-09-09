"""Which seasons form the normalization reference window for a prediction."""
from __future__ import annotations

from datetime import datetime

import polars as pl

from matchup.metrics._thresholds import load_thresholds
from matchup.pointintime.calendar import build_game_calendar

N_REFERENCE_SEASONS = 3


def season_is_completed(season: int, asof_utc: datetime, calendar: pl.DataFrame | None = None) -> bool:
    """A season is 'completed' as of ``asof_utc`` iff every one of its games has
    kicked off (its last game's kickoff is strictly before ``asof_utc``)."""
    cal = calendar if calendar is not None else build_game_calendar()
    games = cal.filter(pl.col("season") == season)
    if games.is_empty():
        return False
    return games.get_column("kickoff_utc").max() < asof_utc


def completed_seasons_asof(
    asof_utc: datetime,
    *,
    n: int = N_REFERENCE_SEASONS,
    calendar: pl.DataFrame | None = None,
) -> list[int]:
    """The ``n`` most recent fully-completed seasons before ``asof_utc``.

    Example: a Week 1 2016 prediction -> [2013, 2014, 2015];
             a Week 5 2022 prediction -> [2019, 2020, 2021];
             a Week 1 2026 prediction -> [2023, 2024, 2025].
    """
    cal = calendar if calendar is not None else build_game_calendar()
    seasons = sorted(
        int(s) for s in cal.get_column("season").unique().to_list()
    )
    completed = [s for s in seasons if season_is_completed(s, asof_utc, cal)]
    return completed[-n:]


def min_opportunities_for(family: str) -> int:
    t = load_thresholds()
    if family == "qb":
        return t["min_dropbacks_season_ref"]
    if family == "rb":
        return t["min_carries_season_ref"]
    if family == "wr":
        return t["min_targets_season_ref"]
    return t["min_team_plays_season_ref"]
