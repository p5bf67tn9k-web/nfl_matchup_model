"""Unit tests for Phase 4 shrinkage + opponent-adjustment primitives."""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.opponent_adjustment.ridge_adjust import _Design
from matchup.shrinkage.shrink import select_k, shrink


def test_shrink_formula():
    raw = np.array([0.30, -0.20, 0.05])
    mu = np.array([0.02, 0.02, 0.02])
    n = np.array([8.0, 8.0, 8.0])
    k = 8.0
    w = 0.5
    got = shrink(raw, mu, n, k)
    exp = mu + w * (raw - mu)
    assert np.allclose(got, exp)
    # n -> inf : shrunk -> raw ; n -> 0 : shrunk -> mu
    assert np.allclose(shrink(raw, mu, np.full(3, 1e9), k), raw, atol=1e-4)
    assert np.allclose(shrink(raw, mu, np.zeros(3), k), mu)


def test_select_k_picks_grid_minimum():
    # construct data where the true shrink is w=0.5 -> k should be near n
    rng = np.random.default_rng(0)
    n_obs = 4000
    latent = rng.normal(0, 0.1, n_obs)
    mu = np.full(n_obs, 0.0)
    raw = latent + rng.normal(0, 0.1, n_obs)          # noisy signal
    target = latent + rng.normal(0, 0.1, n_obs)
    df = pl.DataFrame({
        "feature_value": raw, "baseline_league": mu, "target_value": target,
        "feat_n_games": np.full(n_obs, 8.0),
    })
    k, fb, curve = select_k(df, [1, 2, 4, 8, 12, 16], fallback_k=8, min_train_obs=500)
    assert not fb
    assert k in (4, 8, 12)              # w ~ 0.5 given equal noise -> k ~ n = 8
    assert curve[k] == min(curve.values())


def test_select_k_fallback_when_thin():
    df = pl.DataFrame({"feature_value": [0.1] * 10, "baseline_league": [0.0] * 10,
                       "target_value": [0.1] * 10, "feat_n_games": [8.0] * 10})
    k, fb, _ = select_k(df, [1, 2, 4], fallback_k=8, min_train_obs=500)
    assert fb and k == 8


def test_ridge_design_recovers_effects():
    # synthetic: 6 teams, each plays every other twice; y = off[t] - def[o] + home*0.1 + noise
    rng = np.random.default_rng(1)
    teams = list("ABCDEF")
    off = {t: v for t, v in zip(teams, [0.3, 0.1, 0.0, -0.1, -0.1, -0.2], strict=True)}
    rows = []
    for a in teams:
        for b in teams:
            if a == b:
                continue
            for home in (0, 1):
                y = off[a] - off[b] + 0.1 * home + rng.normal(0, 0.02)
                rows.append({"entity_id": a, "opponent": b, "home": home, "y": y})
    d = _Design(pl.DataFrame(rows))
    s = d.strengths(alpha=1.0)
    # recovered strengths should rank-correlate ~perfectly with true offense
    true = np.array([off[t] for t in teams])
    est = np.array([s[t] for t in teams])
    assert np.corrcoef(true, est)[0, 1] > 0.98


def test_ridge_design_permute_opponents_destroys_structure():
    rng = np.random.default_rng(2)
    teams = list("ABCDEF")
    off = {t: v for t, v in zip(teams, [0.3, 0.1, 0.0, -0.1, -0.1, -0.2], strict=True)}
    rows = [
        {"entity_id": a, "opponent": b, "home": h,
         "y": off[a] - off[b] + 0.1 * h + rng.normal(0, 0.02)}
        for a in teams for b in teams if a != b for h in (0, 1)
    ]
    df = pl.DataFrame(rows)
    real = _Design(df).strengths(1.0)
    perm = _Design(df, permute_opponents=True, seed=3).strengths(1.0)
    true = np.array([off[t] for t in teams])
    r_real = np.corrcoef(true, [real[t] for t in teams])[0, 1]
    r_perm = np.corrcoef(true, [perm[t] for t in teams])[0, 1]
    assert r_real > 0.95
    assert r_perm < r_real  # permuting opponent labels weakens recovery
