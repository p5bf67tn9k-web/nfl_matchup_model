"""Phase 4.1 audit tests."""
from __future__ import annotations

import inspect

import numpy as np
import polars as pl
import pytest

import matchup.validation.phase4 as p4
from matchup.shrinkage.shrink import apply_shrinkage_walkforward, select_k


def test_shrink_accepts_alternative_n_column():
    df = pl.DataFrame({
        "feature_value": np.linspace(-0.3, 0.3, 200),
        "baseline_league": np.zeros(200),
        "target_value": np.linspace(-0.1, 0.1, 200),
        "feat_n_games": np.full(200, 8.0),
        "feat_opp_n": np.full(200, 260.0),
    })
    _, _, curve_g = select_k(df, [1, 4, 16], fallback_k=8, min_train_obs=10, n_col="feat_n_games")
    _, _, curve_o = select_k(df, [1, 4, 16], fallback_k=8, min_train_obs=10, n_col="feat_opp_n")
    # with n=260 the weight is ~1 for any k in the grid -> curves are near-flat
    assert max(curve_o.values()) - min(curve_o.values()) < max(curve_g.values()) - min(curve_g.values())


def test_apply_shrinkage_walkforward_n_col_kw_exists():
    sig = inspect.signature(apply_shrinkage_walkforward)
    assert "n_col" in sig.parameters


def test_force_fallback_k_gives_fixed_k():
    df = pl.DataFrame({"feature_value": [0.1] * 50, "baseline_league": [0.0] * 50,
                       "target_value": [0.05] * 50, "feat_n_games": [8.0] * 50})
    k, fb, _ = select_k(df, [1, 2, 4], fallback_k=12, min_train_obs=10**9)
    assert fb and k == 12


def test_stage_b_reference_is_fixed_not_selected():
    """Phase 4.1 fix: the opponent-adjustment reference must be the constant
    'shrunk_feature', not chosen from OOS skill."""
    src = inspect.getsource(p4.run_phase4)
    assert 'ref = "shrunk_feature"' in src
    assert 'if per_h["shrunk"][h]["skill_vs_reference"] > 0' not in src


@pytest.mark.network
def test_audit_candidate_universe_matches_approved():
    from matchup.validation.phase4_audit import audit_candidate_universe

    acu = audit_candidate_universe()
    # no metric that qualifies under the approved 4-part rule is missing from the implementation
    missing = acu.filter(pl.col("reason").str.contains("SHOULD RE-RUN"))
    assert missing.height == 0, missing.get_column("metric").to_list()


@pytest.mark.network
def test_audit_excluded_metrics_are_the_8_not_rank_persistent():
    from matchup.validation.phase4_audit import excluded_metrics_shrinkage_check

    exc = excluded_metrics_shrinkage_check()
    st3 = pl.read_csv("outputs/phase3/metric_status.csv")
    nrp = set(st3.filter(pl.col("rank_persistence") == "NOT_RANK_PERSISTENT").get_column("metric").to_list())
    assert set(exc.get_column("metric").unique().to_list()) == nrp
