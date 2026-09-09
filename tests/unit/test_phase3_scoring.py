"""Unit tests for Phase 3 scoring, status logic, and the negative control."""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.validation.negative_control import negative_control_cell
from matchup.validation.scoring import cluster_bootstrap, score_cell
from matchup.validation.status import assign_rank_persistence, assign_status


def _synthetic(n=2000, signal=0.6, seed=1):
    rng = np.random.default_rng(seed)
    entities = rng.integers(0, 120, n)
    seasons = rng.integers(2019, 2026, n)
    latent = rng.normal(0, 1, n)
    feature = latent + rng.normal(0, 0.4, n)
    target = signal * latent + rng.normal(0, np.sqrt(1 - signal**2), n)
    league = np.full(n, target.mean())
    prior = latent + rng.normal(0, 0.5, n)
    raw_t3 = feature + rng.normal(0, 0.3, n)
    return feature, target, league, prior, raw_t3, entities, seasons


def test_score_cell_detects_signal_and_baseline_wins():
    f, t, lg, pr, c, e, s = _synthetic(signal=0.6)
    sc = score_cell(f, t, lg, pr, c, entities=e, seasons=s, opp=np.full(len(f), 100.0))
    assert sc["spearman"] > 0.2
    assert sc["n_entities"] > 50
    # a pure-noise feature is worse than the league-mean constant on RMSE
    f_noise = np.random.default_rng(0).permutation(f)
    sc_n = score_cell(f_noise, t, lg, pr, c, entities=e, seasons=s, opp=np.full(len(f), 100.0))
    assert sc_n["skill_vs_league"] < sc["skill_vs_league"]


def test_cluster_bootstrap_ci_brackets_point_estimate():
    f, t, lg, pr, c, e, s = _synthetic(signal=0.5)
    clusters = e * 10 + (s - 2019)
    sc = score_cell(f, t, lg, pr, c, entities=e, seasons=s, opp=np.full(len(f), 100.0))
    ci = cluster_bootstrap(f, t, lg, pr, clusters=clusters, n_iter=300, seed=7)
    assert ci["spearman_ci_lo"] <= sc["spearman"] <= ci["spearman_ci_hi"]
    assert ci["spearman_ci_lo"] > 0  # real signal


def test_negative_control_shows_no_positive_skill():
    f, t, lg, _pr, _c, _e, s = _synthetic(signal=0.7)
    cell = pl.DataFrame({"feature_value": f, "target_value": t, "baseline_league": lg, "season": s})
    nc = negative_control_cell(cell, seed=3, n_permutations=25, min_per_season=15)
    assert abs(nc["placebo_spearman_mean"]) < 0.06
    assert nc["placebo_skill_vs_league_mean"] <= 0.02  # permuted feature never gains skill


def _cell(n, skill_l, skill_l_lo, skill_p, skill_p_lo, sp, sp_lo):
    return {"n": n, "window": "season_to_date",
            "skill_vs_league": skill_l, "skill_vs_league_ci_lo": skill_l_lo, "skill_vs_league_ci_hi": skill_l + 0.05,
            "skill_vs_prior_season": skill_p, "skill_vs_prior_season_ci_lo": skill_p_lo, "skill_vs_prior_season_ci_hi": skill_p + 0.05,
            "spearman": sp, "spearman_ci_lo": sp_lo, "spearman_ci_hi": sp + 0.05}


RULES = {"insufficient_data_min_n": 300,
         "economic_floor": {"min_skill_vs_league": 0.03, "min_abs_spearman": 0.15}}


def test_status_validated_when_both_horizons_clear_the_bar():
    good = _cell(2000, 0.08, 0.04, 0.06, 0.02, 0.35, 0.30)
    st, _ = assign_status({2: good, 4: good}, RULES)
    assert st == "VALIDATED_PERSISTENCE"


def test_status_unvalidated_when_only_one_horizon_clears():
    good = _cell(2000, 0.08, 0.04, 0.06, 0.02, 0.35, 0.30)
    weak = _cell(2000, 0.01, -0.02, 0.00, -0.03, 0.05, 0.00)
    st, _ = assign_status({2: good, 4: weak}, RULES)
    assert st == "UNVALIDATED"


def test_status_no_incremental_when_both_fail():
    bad = _cell(2000, -0.05, -0.09, -0.02, -0.05, 0.10, 0.05)
    st, _ = assign_status({2: bad, 4: bad}, RULES)
    assert st == "NO_INCREMENTAL_PERSISTENCE"


def test_status_insufficient_data():
    tiny = _cell(50, 0.5, 0.4, 0.4, 0.3, 0.5, 0.4)
    st, _ = assign_status({2: tiny, 4: tiny}, RULES)
    assert st == "INSUFFICIENT_DATA"


def test_rank_persistence_independent_of_rmse_skill():
    # strong rank persistence, negative RMSE skill (the QB-EPA pattern)
    rank_ok_rmse_bad = _cell(2000, -0.04, -0.07, -0.02, -0.05, 0.38, 0.31)
    rk, _ = assign_rank_persistence({2: rank_ok_rmse_bad, 4: rank_ok_rmse_bad}, RULES)
    assert rk == "RANK_PERSISTENT"
    st, _ = assign_status({2: rank_ok_rmse_bad, 4: rank_ok_rmse_bad}, RULES)
    assert st == "NO_INCREMENTAL_PERSISTENCE"
