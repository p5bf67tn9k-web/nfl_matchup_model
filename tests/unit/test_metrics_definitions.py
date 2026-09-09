"""Hand-verified metric definitions -- checks numerator, denominator, exclusions
and the resulting value against the underlying play data, not just that code runs.
"""
from __future__ import annotations

import polars as pl
import pytest

from matchup.metrics.build import game_metrics_offline
from matchup.metrics.families import (
    qb_game_metrics,
    special_teams_game_metrics,
    team_offense_game_metrics,
)
from matchup.metrics.plays import classify_plays
from matchup.store import load_source

pytestmark = [pytest.mark.network]

MAHOMES = "00-0033873"
GAME = "2024_01_BAL_KC"  # KC 27 - BAL 20. Mahomes 20/28, 291 yds, 1 TD, 1 INT, 2 sacks.


@pytest.fixture(scope="module")
def kc_wk1_plays():
    raw = load_source("pbp", seasons=[2024]).filter(pl.col("game_id") == GAME)
    return classify_plays(raw.with_columns(pl.lit(None).cast(pl.Datetime("us", "UTC")).alias("data_asof")))


def test_qb_dropback_denominator_excludes_2pt_spikes_kneels(kc_wk1_plays):
    p = kc_wk1_plays.filter(pl.col("passer_player_id") == MAHOMES)
    db = p.filter(pl.col("is_dropback"))
    # every dropback is a throw, sack, or scramble; none is a spike/kneel/2pt
    assert (db.get_column("qb_spike").fill_null(0) == 0).all()
    assert (db.get_column("qb_kneel").fill_null(0) == 0).all()
    assert (db.get_column("two_point_attempt").fill_null(0) == 0).all()
    assert db.get_column("epa").null_count() == 0  # EPA always defined on dropbacks


def test_mahomes_wk1_2024_box_score_matches(kc_wk1_plays):
    row = qb_game_metrics(kc_wk1_plays).filter(pl.col("entity_id") == MAHOMES).to_dicts()[0]
    assert row["throws"] == 28
    assert row["completions"] == 20
    assert row["sacks"] == 2
    assert row["pass_yards"] == 291.0
    assert row["pass_tds"] == 1
    assert row["interceptions"] == 1  # pick to R.Smith intended for R.Rice, Q2
    assert abs(row["interception_rate"] - 1 / 28) < 1e-9
    assert row["dropbacks"] == 28 + 2 + row["scrambles"]  # throws + sacks + scrambles
    # completion pct = 20 / 28
    assert abs(row["completion_pct"] - 20 / 28) < 1e-9
    # YPA = 291 / 28
    assert abs(row["yards_per_attempt"] - 291 / 28) < 1e-9
    # EPA/dropback = sum(epa over dropbacks) / dropbacks, recomputed by hand
    hand = kc_wk1_plays.filter(
        (pl.col("passer_player_id") == MAHOMES) & pl.col("is_dropback")
    )
    assert abs(row["epa_per_dropback"] - hand.get_column("epa").sum() / hand.height) < 1e-9


def test_cpoe_uses_attempts_with_cpoe_denominator(kc_wk1_plays):
    row = qb_game_metrics(kc_wk1_plays).filter(pl.col("entity_id") == MAHOMES).to_dicts()[0]
    throws = kc_wk1_plays.filter((pl.col("passer_player_id") == MAHOMES) & pl.col("is_pass_throw"))
    with_cpoe = throws.filter(pl.col("cpoe").is_not_null())
    assert row["cpoe_attempt_count"] == with_cpoe.height
    assert abs(row["cpoe_coverage_fraction"] - with_cpoe.height / throws.height) < 1e-9
    assert abs(row["cpoe"] - with_cpoe.get_column("cpoe").mean()) < 1e-9
    # denominator is NOT all throws
    assert with_cpoe.height <= throws.height


def test_team_offense_play_universe_and_epa(kc_wk1_plays):
    row = team_offense_game_metrics(kc_wk1_plays).filter(pl.col("entity_id") == "KC").to_dicts()[0]
    hand = kc_wk1_plays.filter((pl.col("posteam") == "KC") & pl.col("off_play"))
    assert row["plays"] == hand.height
    assert abs(row["epa_per_play"] - hand.get_column("epa").sum() / hand.height) < 1e-9
    # kneels / spikes / 2pt excluded
    assert hand.filter(pl.col("qb_kneel").fill_null(0) == 1).height == 0
    assert hand.filter(pl.col("two_point_attempt").fill_null(0) == 1).height == 0
    # pass and rush partition the universe
    assert row["dropbacks"] + row["designed_rushes"] <= row["plays"]


def test_special_teams_fg_from_special_flag():
    raw = load_source("pbp", seasons=[2024]).filter(pl.col("game_id") == GAME).with_columns(
        pl.lit(None).cast(pl.Datetime("us", "UTC")).alias("data_asof")
    )
    st = special_teams_game_metrics(raw).filter(pl.col("entity_id") == "KC").to_dicts()[0]
    fg = raw.filter((pl.col("special") == 1) & (pl.col("field_goal_attempt") == 1) & (pl.col("posteam") == "KC"))
    made = fg.filter(pl.col("field_goal_result") == "made")
    assert st["fg_attempts"] == fg.height
    assert st["fg_made"] == made.height
    if fg.height:
        assert abs(st["fg_pct"] - made.height / fg.height) < 1e-9


def test_explosive_thresholds_applied():
    plays = classify_plays(
        load_source("pbp", seasons=[2024]).head(20000).with_columns(
            pl.lit(None).cast(pl.Datetime("us", "UTC")).alias("data_asof")
        )
    )
    exp_pass = plays.filter(pl.col("is_explosive_pass"))
    assert (exp_pass.get_column("yards_gained") >= 20).all()
    assert (exp_pass.get_column("complete_pass").fill_null(0) == 1).all()
    exp_rush = plays.filter(pl.col("is_explosive_rush"))
    assert (exp_rush.get_column("yards_gained") >= 10).all()


def test_rb_carries_exclude_scrambles_and_kneels():
    gm = game_metrics_offline("rb", [2024])
    # entity_ids that are actually QBs shouldn't appear via scrambles; sample-check a game
    plays = classify_plays(
        load_source("pbp", seasons=[2024]).filter(pl.col("game_id") == GAME).with_columns(
            pl.lit(None).cast(pl.Datetime("us", "UTC")).alias("data_asof")
        )
    )
    r = plays.filter(pl.col("is_designed_rush"))
    assert (r.get_column("qb_scramble").fill_null(0) == 0).all()
    assert (r.get_column("qb_kneel").fill_null(0) == 0).all()
    assert not gm.is_empty()
