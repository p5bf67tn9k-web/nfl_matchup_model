"""Unit tests for the factor-research statistics."""
from __future__ import annotations

import numpy as np

from matchup.research.factors import _cluster_boot_ci, _evidence_tier, _pearson, _spearman


def test_pearson_spearman_basic():
    x = np.arange(50.0)
    y = 2 * x + np.random.default_rng(0).normal(0, 1, 50)
    assert _pearson(x, y) > 0.98
    assert _spearman(x, y) > 0.98
    assert np.isnan(_pearson(np.ones(50), y))          # zero variance -> nan
    assert np.isnan(_pearson(np.arange(3.0), np.arange(3.0)))  # too few


def test_cluster_boot_ci_contains_truth_and_excludes_zero_for_strong_signal():
    rng = np.random.default_rng(1)
    n = 800
    clusters = np.repeat(np.arange(80), 10)
    x = rng.normal(0, 1, n)
    y = 0.5 * x + rng.normal(0, 1, n)
    lo, hi = _cluster_boot_ci(x, y, clusters, n_iter=500, seed=1)
    assert lo > 0 and hi < 1
    assert lo < np.corrcoef(x, y)[0, 1] < hi

    # pure noise -> CI should straddle 0
    y0 = rng.normal(0, 1, n)
    lo0, hi0 = _cluster_boot_ci(x, y0, clusters, n_iter=500, seed=2)
    assert lo0 < 0 < hi0


def test_evidence_tier_rules():
    # strong, CI clears zero, temporally consistent
    assert _evidence_tier(0.42, 0.35, 0.49, 1.0, 1500, 0.9) == "strong + temporally consistent"
    # moderate + consistent
    assert _evidence_tier(0.20, 0.12, 0.28, 0.9, 1500, 0.6).startswith("moderate")
    # detectable but tiny
    assert _evidence_tier(0.08, 0.03, 0.13, 0.9, 1500, 0.3) == \
        "weak but statistically detectable chronologically"
    # no chronological signal, but strong stable association
    assert _evidence_tier(0.02, -0.05, 0.09, 0.9, 1500, 0.55) == \
        "descriptive association only (no chronological signal)"
    # nothing
    assert _evidence_tier(0.01, -0.2, 0.2, 0.4, 100, 0.1) == "weak / insufficient evidence"


def test_evidence_tier_never_says_important():
    rng = np.random.default_rng(0)
    for _ in range(200):
        t = _evidence_tier(
            rng.uniform(-1, 1), rng.uniform(-1, 0.2), rng.uniform(-0.2, 1),
            rng.uniform(0, 1), int(rng.integers(0, 3000)), rng.uniform(-1, 1),
        )
        assert "important" not in t.lower()
