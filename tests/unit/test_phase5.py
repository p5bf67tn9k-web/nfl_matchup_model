"""Unit tests for Phase 5 matchup-interaction primitives (synthetic, no network)."""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.validation.phase5 import (
    _design,
    _permute_within_season,
    benjamini_hochberg,
    load_phase5_config,
    resolve_matchup_universe,
    score_predictions,
    walk_forward_predictions,
)


def _synth_mobs(*, beta_a=2.0, beta_b=1.0, beta_ab=0.0, noise=0.05, seed=0) -> pl.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for season in range(2016, 2026):
        for i in range(300):
            a = float(rng.normal(0, 0.1))
            b = float(rng.normal(0, 0.1))
            y = beta_a * a + beta_b * b + beta_ab * a * b + rng.normal(0, noise)
            rows.append({
                "entity_id": f"E{i % 30}", "opp_entity": f"O{i % 30}",
                "target_game_id": f"{season}_{i}", "season": season,
                "week": 5 + (i % 14), "horizon": 2,
                "A": a, "mu_A": 0.0, "B": b, "mu_B": 0.0, "target_value": y,
            })
    return pl.DataFrame(rows)


def test_config_frozen():
    assert load_phase5_config()["frozen"] is True


def test_candidate_universe_only_double_shrinkage_metrics_resolve():
    u = resolve_matchup_universe()
    for r in u.iter_rows(named=True):
        if r["resolved"]:
            assert r["off_shrinkage_status"] == "SHRINKAGE_ADDS_VALUE"
            assert r["def_shrinkage_status"] == "SHRINKAGE_ADDS_VALUE"
        else:
            assert "SHRINKAGE_ADDS_VALUE" not in (
                r["off_shrinkage_status"], r["def_shrinkage_status"]
            ) or "NOT_IN_PHASE4_UNIVERSE" in (r["off_shrinkage_status"], r["def_shrinkage_status"])
    # at least a couple resolve, and the count is stable/​known
    assert u.filter(pl.col("resolved")).height == 9


def test_design_matrices():
    a = np.array([0.1, 0.2, 0.3])
    b = np.array([-0.1, 0.0, 0.2])
    assert _design(a, b, "M1", (0.0, 0.0)).shape == (3, 2)
    assert _design(a, b, "M3", (0.0, 0.0)).shape == (3, 3)
    m4c = _design(a, b, "M4c", (0.2, 0.0))
    assert m4c.shape == (3, 4)
    # centered interaction column == (A - meanA) * (B - meanB)
    assert np.allclose(m4c[:, 3], (a - 0.2) * (b - 0.0))
    assert np.allclose(_design(a, b, "Mrel", (0.0, 0.0))[:, 1], a - b)


def test_interaction_skill_recovered_when_interaction_is_real():
    mobs = _synth_mobs(beta_ab=8.0, noise=0.03, seed=1)
    preds = walk_forward_predictions(mobs, 2, seed=1)
    sc = score_predictions(preds, n_iter=200, seed=1)
    assert sc["interaction_skill"] > 0.05
    assert sc["interaction_skill_ci_lo"] > 0
    assert sc["interaction_p_one_sided"] < 0.05


def test_interaction_skill_near_zero_when_model_is_additive():
    mobs = _synth_mobs(beta_ab=0.0, noise=0.05, seed=2)
    preds = walk_forward_predictions(mobs, 2, seed=2)
    sc = score_predictions(preds, n_iter=200, seed=2)
    assert abs(sc["interaction_skill"]) < 0.01
    # additive term itself carries the real B signal
    assert sc["skill_M3_vs_M1"] > 0


def test_score_predictions_skill_identity():
    mobs = _synth_mobs(beta_ab=3.0, seed=3)
    preds = walk_forward_predictions(mobs, 2, seed=3)
    sc = score_predictions(preds, n_iter=50, seed=3)
    assert np.isclose(sc["interaction_skill"], 1 - sc["rmse_M4c"] / sc["rmse_M3"])


def test_randomized_pairing_destroys_interaction_skill():
    mobs = _synth_mobs(beta_ab=8.0, noise=0.03, seed=4)
    real = score_predictions(walk_forward_predictions(mobs, 2, seed=4), n_iter=50, seed=4)
    permuted = _permute_within_season(mobs, "B", 4)
    rnd = score_predictions(walk_forward_predictions(permuted, 2, seed=4), n_iter=50, seed=4)
    assert real["interaction_skill"] - rnd["interaction_skill"] > 0.03


def test_permute_within_season_preserves_marginals():
    mobs = _synth_mobs(seed=5)
    p = _permute_within_season(mobs, "B", 5)
    for s in range(2016, 2026):
        a = sorted(mobs.filter(pl.col("season") == s).get_column("B").to_list())
        b = sorted(p.filter(pl.col("season") == s).get_column("B").to_list())
        assert a == b


def test_benjamini_hochberg():
    # 1 clearly significant, rest null
    p = [0.001, 0.20, 0.40, 0.60, 0.80]
    flags = benjamini_hochberg(p, 0.10)
    assert flags[0] is True
    assert not any(flags[1:])
    # all null -> none pass
    assert not any(benjamini_hochberg([0.5, 0.6, 0.7], 0.10))
    # all tiny -> all pass
    assert all(benjamini_hochberg([1e-6, 2e-6, 3e-6], 0.10))


def test_walk_forward_is_chronological():
    """A poisoned far-future season must not change predictions for earlier seasons."""
    mobs = _synth_mobs(beta_ab=4.0, seed=6)
    base = walk_forward_predictions(mobs, 2, seed=6)
    poison = mobs.filter(pl.col("season") == 2025).with_columns(
        (pl.col("target_value") + 999.0).alias("target_value"),
        (pl.col("A") * -5 + 3).alias("A"),
    )
    # extra 2025 rows can only affect the 2025 test fold (it is the last), never earlier
    mobs2 = pl.concat([mobs.filter(pl.col("season") < 2025), poison])
    got = walk_forward_predictions(mobs2, 2, seed=6)
    for s in range(2019, 2025):
        b = base.filter(pl.col("season") == s).sort("target_game_id")
        g = got.filter(pl.col("season") == s).sort("target_game_id")
        assert np.allclose(b.get_column("pred_M4c").to_numpy(), g.get_column("pred_M4c").to_numpy())
