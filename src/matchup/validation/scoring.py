"""Scoring + cluster bootstrap for persistence cells.

A "cell" is a set of observation rows sharing (family, metric, window, horizon,
[season_phase]). The feature_value IS the point prediction of target_value (raw
units): persistence = "the unit will perform about as it just did".
"""
from __future__ import annotations

import numpy as np

_SCORE_KEYS = [
    "n", "n_entities", "n_seasons", "opportunity_n_median", "target_mean", "target_sd",
    "rmse", "mae", "bias", "spearman", "pearson",
    "rmse_league", "rmse_prior_season", "rmse_raw_trailing3",
    "skill_vs_league", "skill_vs_prior_season", "skill_vs_raw_trailing3",
    "n_prior_season", "excluded_target_rate",
]


def _rmse(pred: np.ndarray, actual: np.ndarray) -> float:
    return float(np.sqrt(np.mean((pred - actual) ** 2)))


def _spearman(a: np.ndarray, b: np.ndarray) -> float:
    if a.size < 3:
        return float("nan")
    ar = a.argsort().argsort().astype(float)
    br = b.argsort().argsort().astype(float)
    return float(np.corrcoef(ar, br)[0, 1])


def score_cell(
    feature: np.ndarray,
    target: np.ndarray,
    bl_league: np.ndarray,
    bl_prior: np.ndarray,
    bl_raw_t3: np.ndarray,
    *,
    entities: np.ndarray,
    seasons: np.ndarray,
    opp: np.ndarray,
    excluded_target_rate: float = float("nan"),
) -> dict:
    rmse = _rmse(feature, target)
    rmse_l = _rmse(bl_league, target)

    have_c = np.isfinite(bl_raw_t3)
    if have_c.sum() >= 10:
        rmse_c = _rmse(bl_raw_t3[have_c], target[have_c])
        rmse_c_feat = _rmse(feature[have_c], target[have_c])
        skill_c = 1 - rmse_c_feat / rmse_c if rmse_c > 0 else float("nan")
    else:
        rmse_c = skill_c = float("nan")

    have_prior = np.isfinite(bl_prior)
    if have_prior.sum() >= 10:
        rmse_p = _rmse(bl_prior[have_prior], target[have_prior])
        rmse_p_feat = _rmse(feature[have_prior], target[have_prior])
        skill_p = 1 - rmse_p_feat / rmse_p if rmse_p > 0 else float("nan")
    else:
        rmse_p = skill_p = float("nan")

    return {
        "n": int(feature.size),
        "n_entities": int(np.unique(entities).size),
        "n_seasons": int(np.unique(seasons).size),
        "opportunity_n_median": float(np.median(opp)) if opp.size else float("nan"),
        "target_mean": float(np.mean(target)),
        "target_sd": float(np.std(target, ddof=1)) if target.size > 1 else float("nan"),
        "rmse": rmse, "mae": float(np.mean(np.abs(feature - target))),
        "bias": float(np.mean(feature - target)),
        "spearman": _spearman(feature, target),
        "pearson": float(np.corrcoef(feature, target)[0, 1]) if feature.size > 2 else float("nan"),
        "rmse_league": rmse_l, "rmse_prior_season": rmse_p, "rmse_raw_trailing3": rmse_c,
        "skill_vs_league": 1 - rmse / rmse_l if rmse_l > 0 else float("nan"),
        "skill_vs_prior_season": skill_p,
        "skill_vs_raw_trailing3": skill_c,
        "n_prior_season": int(have_prior.sum()),
        "excluded_target_rate": excluded_target_rate,
    }


def _wrmse2(resid_sq: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Vectorised weighted RMSE per bootstrap row of ``w`` (shape n_iter x n)."""
    return np.sqrt((w * resid_sq).sum(1) / w.sum(1))


def _wcorr(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Vectorised weighted Pearson correlation, per row of ``w``."""
    sw = w.sum(1)
    mx = (w * x).sum(1) / sw
    my = (w * y).sum(1) / sw
    cov = (w * (x - mx[:, None]) * (y - my[:, None])).sum(1) / sw
    vx = (w * (x - mx[:, None]) ** 2).sum(1) / sw
    vy = (w * (y - my[:, None]) ** 2).sum(1) / sw
    denom = np.sqrt(vx * vy)
    out = np.full_like(sw, np.nan)
    ok = denom > 0
    out[ok] = cov[ok] / denom[ok]
    return out


def cluster_bootstrap(
    feature: np.ndarray,
    target: np.ndarray,
    bl_league: np.ndarray,
    bl_prior: np.ndarray,
    *,
    clusters: np.ndarray,          # integer cluster id per row (entity_id x season)
    n_iter: int,
    seed: int,
    level: float = 0.95,
) -> dict:
    """Percentile CIs for skill_vs_league, skill_vs_prior_season, spearman.

    Multiplier (Bayesian) cluster bootstrap: each CLUSTER gets an Exponential(1)
    weight per resample, broadcast to its rows. This respects that a unit-season's
    rows are correlated (not IID) and is fully vectorised. The spearman CI uses a
    weighted Pearson of the fixed rank vectors -- a standard fast approximation.
    """
    rng = np.random.default_rng(seed)
    _, cidx = np.unique(clusters, return_inverse=True)
    n_clusters = cidx.max() + 1
    W_cluster = rng.exponential(1.0, size=(n_iter, n_clusters))
    w = W_cluster[:, cidx]                      # (n_iter, n)

    resid_f = (feature - target) ** 2
    resid_l = (bl_league - target) ** 2
    rf = _wrmse2(resid_f, w)
    rl = _wrmse2(resid_l, w)
    sk_l = np.where(rl > 0, 1 - rf / rl, np.nan)

    rank_f = feature.argsort().argsort().astype(float)
    rank_t = target.argsort().argsort().astype(float)
    sp = _wcorr(rank_f, rank_t, w)

    have_prior = np.isfinite(bl_prior)
    if have_prior.sum() >= 10:
        wp = w[:, have_prior]
        rp = _wrmse2((bl_prior[have_prior] - target[have_prior]) ** 2, wp)
        rpf = _wrmse2((feature[have_prior] - target[have_prior]) ** 2, wp)
        sk_p = np.where(rp > 0, 1 - rpf / rp, np.nan)
    else:
        sk_p = np.full(n_iter, np.nan)

    lo, hi = (1 - level) / 2 * 100, (1 + level) / 2 * 100

    def ci(v):
        v = v[np.isfinite(v)]
        if v.size < 20:
            return (float("nan"), float("nan"))
        return (float(np.percentile(v, lo)), float(np.percentile(v, hi)))

    l_lo, l_hi = ci(sk_l)
    p_lo, p_hi = ci(sk_p)
    s_lo, s_hi = ci(sp)
    return {
        "skill_vs_league_ci_lo": l_lo, "skill_vs_league_ci_hi": l_hi,
        "skill_vs_prior_season_ci_lo": p_lo, "skill_vs_prior_season_ci_hi": p_hi,
        "spearman_ci_lo": s_lo, "spearman_ci_hi": s_hi,
        "bootstrap_iterations": n_iter, "bootstrap_method": "multiplier_cluster_exponential",
    }
