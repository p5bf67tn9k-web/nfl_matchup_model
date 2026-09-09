"""Normalization: reference-window selection (never current/future season) and
transform correctness."""
from __future__ import annotations

from datetime import UTC, datetime

import numpy as np
import polars as pl
import pytest

from matchup.metrics.build import game_metrics_from_asof, offline_provider
from matchup.metrics.windows import window_metric
from matchup.normalize.normalize import normalize_windowed
from matchup.normalize.reference import completed_seasons_asof, season_is_completed
from matchup.normalize.transforms import league_relative, percentile_rank, zscore
from matchup.pointintime.calendar import build_game_calendar

pytestmark = [pytest.mark.network]


# ------- transforms (pure, no I/O) ----------------------------------------- #
def test_zscore_percentile_league_relative():
    ref = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    assert zscore(2.0, ref) == 0.0
    assert abs(zscore(4.0, ref) - (2.0 / ref.std(ddof=1))) < 1e-12
    assert percentile_rank(2.0, ref) == 0.6  # {0,1,2} <= 2
    assert league_relative(3.0, ref, mode="diff") == 1.0
    assert league_relative(4.0, ref, mode="ratio") == 2.0
    assert zscore(1.0, np.array([5.0])) is None  # need >= 2


# ------- reference-window selection -------------------------------------- #
@pytest.mark.parametrize(
    ("dt", "expected"),
    [
        (datetime(2016, 9, 8, tzinfo=UTC), [2013, 2014, 2015]),
        (datetime(2019, 11, 1, tzinfo=UTC), [2016, 2017, 2018]),
        (datetime(2022, 10, 6, tzinfo=UTC), [2019, 2020, 2021]),
        (datetime(2026, 9, 10, tzinfo=UTC), [2023, 2024, 2025]),
    ],
)
def test_completed_seasons_matches_spec_examples(dt, expected):
    assert completed_seasons_asof(dt) == expected


def test_current_incomplete_season_never_in_reference():
    # mid-2024 season
    kick = build_game_calendar().filter(
        (pl.col("season") == 2024) & (pl.col("week") == 10)
    ).get_column("kickoff_utc").min()
    ref = completed_seasons_asof(kick)
    assert 2024 not in ref
    assert 2025 not in ref
    assert max(ref) == 2023
    assert not season_is_completed(2024, kick)


def test_normalize_windowed_logs_reference_and_never_future():
    kick = build_game_calendar().filter(
        pl.col("game_id") == "2024_10_DEN_KC"
    ).get_column("kickoff_utc").item()
    from matchup.pointintime.asof import AsOf

    gm = game_metrics_from_asof(AsOf(asof_utc=kick), "qb")
    row = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                        target_week=10, target_kickoff=kick, window="season_to_date")
    out = normalize_windowed(row, "qb", "epa_per_dropback", asof_utc=kick,
                             ref_game_metrics_provider=offline_provider("qb")).to_dicts()[0]
    assert out["ref_seasons"] == [2021, 2022, 2023]
    assert out["ref_n"] > 50
    assert 2024 not in out["ref_seasons"]
    assert out["epa_per_dropback_rel_mode"] == "diff"  # EPA crosses zero
    # z is finite
    assert out["epa_per_dropback_z"] is not None
