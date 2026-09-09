"""Point-in-time / integrity checks for the weekly research workflow."""
from __future__ import annotations

from datetime import UTC, datetime

import polars as pl
import pytest

from matchup.metrics.build import clear_metric_caches
from matchup.store import clear_cache
from matchup.strength.results import latest_completed_week, team_game_results
from matchup.strength.team_metrics import build_team_metrics_weekly, reference_seasons_for
from matchup.strength.team_strength import team_strength_snapshot

pytestmark = [pytest.mark.network]


@pytest.fixture(autouse=True)
def _clean():
    clear_cache(); clear_metric_caches()
    yield
    clear_cache(); clear_metric_caches()


def test_results_are_completed_games_only():
    res = team_game_results((2024, 2025, 2026))
    assert not res.is_empty()
    now = datetime.now(UTC)
    # every returned game has already kicked off
    assert res.filter(pl.col("data_asof") > pl.lit(now)).is_empty()
    # 2026 has no completed games yet as of the fixture date
    assert res.filter(pl.col("season") == 2026).is_empty()


def test_reference_seasons_are_completed_and_before_target():
    for season in (2019, 2023, 2026):
        refs = reference_seasons_for(season)
        assert len(refs) == 3
        assert max(refs) < season
        assert refs == sorted(refs)


def test_no_future_week_contributes_to_a_snapshot():
    ml = build_team_metrics_weekly([2024])
    snap = team_strength_snapshot(ml, 2024, 6)
    # the snapshot's metric rows never come from a week after the target
    assert snap["metrics"].get_column("week").max() <= 6
    # a team's n_games through week 6 cannot exceed 6
    assert snap["metrics"].get_column("n_games").max() <= 6


def test_snapshot_is_deterministic():
    a = build_team_metrics_weekly([2023]).sort(["team", "week", "metric"])
    clear_metric_caches()
    b = build_team_metrics_weekly([2023]).sort(["team", "week", "metric"])
    j = a.select("team", "week", "metric", "shrunk_value").join(
        b.select("team", "week", "metric", pl.col("shrunk_value").alias("_b")),
        on=["team", "week", "metric"], how="inner",
    )
    assert a.height == b.height
    assert float((j.get_column("shrunk_value") - j.get_column("_b")).abs().max()) < 1e-12


def test_no_market_or_score_columns_in_strength_frame():
    ml = build_team_metrics_weekly([2025])
    banned = {"spread_line", "total_line", "moneyline", "vegas_wp", "result",
              "home_score", "away_score", "odds", "points_for", "points_against"}
    assert not banned.intersection(ml.columns)


def test_poisoned_future_game_does_not_change_earlier_weeks():
    """A fabricated week-99 game must not alter any week<=18 season-to-date value."""
    import matchup.strength.team_metrics as tm

    base = build_team_metrics_weekly([2024]).filter(pl.col("week").is_between(1, 18))
    real_batch = tm.game_metrics_batch

    def poisoned(family, seasons):
        df = real_batch(family, seasons)
        if df.is_empty() or 2024 not in seasons:
            return df
        row = df.filter(pl.col("season") == 2024).head(1)
        if row.is_empty():
            return df
        poison = row.with_columns(
            pl.lit(99).alias("week"),
            pl.lit(datetime(2026, 12, 1, tzinfo=UTC)).alias("data_asof"),
        )
        return pl.concat([df, poison], how="diagonal_relaxed")

    tm.game_metrics_batch.cache_clear()
    from unittest import mock
    with mock.patch.object(tm, "game_metrics_batch", poisoned):
        pois = build_team_metrics_weekly([2024]).filter(pl.col("week").is_between(1, 18))
    tm.game_metrics_batch.cache_clear()

    j = base.select("team", "week", "metric", "raw_value").join(
        pois.select("team", "week", "metric", pl.col("raw_value").alias("_p")),
        on=["team", "week", "metric"], how="inner",
    )
    assert base.height == j.height
    assert float((j.get_column("raw_value") - j.get_column("_p")).abs().max()) < 1e-12


def test_latest_completed_week_current_season_degrades_gracefully():
    from matchup.weekly.run import current_season

    w = latest_completed_week(current_season())
    assert w >= 0  # 0 before Week 1, never negative or crashing


@pytest.mark.slow
def test_weekly_run_end_to_end():
    from matchup.weekly.run import run_weekly_research

    out = run_weekly_research(refresh_research=True, ingest=False)
    assert out["n_teams_in_snapshot"] in (0, 30, 31, 32)
    assert out["pit_checks_all_passed"] is True
    assert set(out["research_method"]) >= {"association", "chronological", "stability"}
