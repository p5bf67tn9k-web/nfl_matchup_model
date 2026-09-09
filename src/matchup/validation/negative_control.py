"""Negative control / placebo (spec section 13).

Permute the feature vector across observations WITHIN the same eval season,
breaking the entity->future link while preserving the feature's marginal
distribution and the season structure. A permuted feature should show ~0 skill
and correlation CIs that include 0.
"""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.validation.scoring import _rmse, _spearman


def negative_control_cell(
    cell: pl.DataFrame, *, seed: int, n_permutations: int, min_per_season: int = 15
) -> dict:
    """cell = observation rows for one (family, metric, window, horizon).

    Permutes the feature WITHIN each eval season. Seasons with fewer than
    ``min_per_season`` observations are pooled into one 'small' bucket so the
    permutation cannot degenerate into the identity for sparse seasons.
    """
    feat = cell.get_column("feature_value").to_numpy()
    targ = cell.get_column("target_value").to_numpy()
    seas = cell.get_column("season").to_numpy().astype(object)
    counts = {s: int((seas == s).sum()) for s in np.unique(seas)}
    seas = np.array([s if counts[s] >= min_per_season else "small" for s in seas], dtype=object)
    big_buckets = sum(1 for b in np.unique(seas) if int((seas == b).sum()) >= min_per_season)
    if feat.size < 200 or big_buckets < 3:
        return {"n": int(feat.size), "skipped": "insufficient per-season observations to permute",
                "placebo_skill_vs_league_mean": float("nan"),
                "placebo_skill_vs_league_p95_abs": float("nan"),
                "placebo_spearman_mean": float("nan"),
                "placebo_spearman_p95_abs": float("nan"), "n_permutations": 0}
    rng = np.random.default_rng(seed)

    # centre feature and target within season so the placebo cannot retain spurious
    # correlation from between-season league drift (within-season permutation alone
    # leaves the season means intact). The real metrics are compared to a baseline
    # that already absorbs the season level, so this is the like-for-like placebo.
    feat_c = feat.astype(float).copy()
    targ_c = targ.astype(float).copy()
    for s in np.unique(seas):
        m = seas == s
        feat_c[m] -= feat_c[m].mean()
        targ_c[m] -= targ_c[m].mean()
    rmse_l = _rmse(np.zeros_like(targ_c), targ_c)  # season-centred league baseline

    skills, spears = [], []
    for _ in range(n_permutations):
        perm = feat_c.copy()
        for s in np.unique(seas):
            m = seas == s
            perm[m] = rng.permutation(feat_c[m])
        r = _rmse(perm, targ_c)
        skills.append(1 - r / rmse_l if rmse_l > 0 else np.nan)
        spears.append(_spearman(perm, targ_c))
    skills = np.array(skills, float)
    spears = np.array(spears, float)
    return {
        "n": int(feat.size),
        "placebo_skill_vs_league_mean": float(np.nanmean(skills)),
        "placebo_skill_vs_league_p95_abs": float(np.nanpercentile(np.abs(skills), 95)),
        "placebo_spearman_mean": float(np.nanmean(spears)),
        "placebo_spearman_p95_abs": float(np.nanpercentile(np.abs(spears), 95)),
        "n_permutations": n_permutations,
    }
