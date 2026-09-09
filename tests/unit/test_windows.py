"""Windowing correctness: game sequence not week arithmetic; bye / season /
playoff boundaries."""
from __future__ import annotations

import polars as pl
import pytest

from matchup.metrics.build import game_metrics_from_asof
from matchup.metrics.windows import window_metric
from matchup.pointintime.asof import AsOf
from matchup.pointintime.calendar import build_game_calendar

pytestmark = [pytest.mark.network]


def _kick(team, season, week):
    return (
        build_game_calendar()
        .filter((pl.col("season") == season) & (pl.col("week") == week)
                & ((pl.col("home_team") == team) | (pl.col("away_team") == team)))
        .get_column("kickoff_utc").item()
    )


@pytest.fixture(scope="module")
def kc_wk10_qb():
    kick = _kick("KC", 2024, 10)
    ao = AsOf(asof_utc=kick)
    return game_metrics_from_asof(ao, "qb"), kick


def test_trailing_3_spans_the_bye(kc_wk10_qb):
    gm, kick = kc_wk10_qb
    # KC bye = week 6, target = week 10 -> last 3 games before are weeks 5, 7, 8
    r = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                      target_week=10, target_kickoff=kick, window="trailing_3")
    assert r["n_games"].item() == 3
    # verify against the raw game rows for Mahomes before the target
    mah = gm.filter(pl.col("entity_id") == "00-0033873")
    weeks = sorted(mah.filter(pl.col("season") == 2024).get_column("week").to_list())
    assert weeks == [1, 2, 3, 4, 5, 7, 8, 9]  # week 6 bye, week 10 excluded
    # trailing-3 components == sum of the last 3 game rows
    cal = build_game_calendar().select("game_id", "kickoff_utc")
    last3 = (
        mah.join(cal, on="game_id").filter(pl.col("kickoff_utc") < kick)
        .sort("kickoff_utc").tail(3)
    )
    assert r["dropbacks"].item() == last3.get_column("dropbacks").sum()


def test_season_to_date_only_target_season(kc_wk10_qb):
    gm, kick = kc_wk10_qb
    r = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                      target_week=10, target_kickoff=kick, window="season_to_date")
    assert r["n_games"].item() == 8  # weeks 1-5, 7-9
    assert r["target_season"].item() == 2024


def test_prior_season_is_full_prior_year_incl_playoffs(kc_wk10_qb):
    gm, kick = kc_wk10_qb
    r = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                      target_week=10, target_kickoff=kick, window="prior_season")
    mah_2023 = gm.filter((pl.col("entity_id") == "00-0033873") & (pl.col("season") == 2023))
    assert r["n_games"].item() == mah_2023.height
    # 2023: KC won the Super Bowl -> Mahomes played postseason games (week > 18)
    assert (mah_2023.get_column("week") > 18).any()


def test_window_carries_provenance(kc_wk10_qb):
    gm, kick = kc_wk10_qb
    r = window_metric("qb", gm, entity_id="00-0033873", target_season=2024,
                      target_week=10, target_kickoff=kick, window="trailing_5")
    d = r.to_dicts()[0]
    assert d["window"] == "trailing_5"
    assert d["n_opportunities"] == d["dropbacks"]
    assert d["pit_source"] == "pbp" and d["pit_status"] == "LIVE_SAFE"
    assert d["earliest_valid_season"] == 1999
    assert d["data_asof"] < kick
    assert d["cpoe_attempt_count"] is not None


def test_empty_window_returns_no_rows(kc_wk10_qb):
    gm, kick = kc_wk10_qb
    # a QB with no prior games -> empty
    r = window_metric("qb", gm, entity_id="00-9999999", target_season=2024,
                      target_week=10, target_kickoff=kick, window="trailing_3")
    assert r.is_empty()


def test_team_window_spans_bye_with_full_schedule():
    kick = _kick("KC", 2024, 10)
    ao = AsOf(asof_utc=kick)
    gm = game_metrics_from_asof(ao, "team_offense")
    r = window_metric("team_offense", gm, entity_id="KC", target_season=2024,
                      target_week=10, target_kickoff=kick, window="season_to_date")
    assert r["n_games"].item() == 8  # KC played 8 games weeks 1-9 (bye wk 6)
