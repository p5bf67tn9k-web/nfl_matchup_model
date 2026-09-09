"""Shrinkage formula + walk-forward k selection."""
from __future__ import annotations

import numpy as np
import polars as pl


def shrink(raw: np.ndarray, league_mean: np.ndarray, n: np.ndarray, k: float) -> np.ndarray:
    """shrunk = mu + w*(raw - mu), w = n/(n+k)."""
    w = n / (n + k)
    return league_mean + w * (raw - league_mean)


def _pooled_rmse(df: pl.DataFrame, k: float, n_col: str = "feat_n_games") -> float:
    s = shrink(
        df.get_column("feature_value").to_numpy(),
        df.get_column("baseline_league").to_numpy(),
        df.get_column(n_col).to_numpy().astype(float),
        k,
    )
    t = df.get_column("target_value").to_numpy()
    return float(np.sqrt(np.mean((s - t) ** 2)))


def select_k(
    train: pl.DataFrame,
    k_grid: list[float],
    *,
    fallback_k: float,
    min_train_obs: int,
    n_col: str = "feat_n_games",
) -> tuple[float, bool, dict[float, float]]:
    """Pick k minimising pooled RMSE over ``train`` (already restricted to the
    primary weeks / horizons). Returns (k, used_fallback, {k: rmse})."""
    if train.height < min_train_obs:
        return fallback_k, True, {}
    curve = {float(k): _pooled_rmse(train, k, n_col) for k in k_grid}
    best = min(curve, key=curve.get)
    return best, False, curve


def apply_shrinkage_walkforward(
    obs: pl.DataFrame,
    *,
    k_grid: list[float],
    fallback_k: float,
    min_train_obs: int,
    oos_seasons: range,
    primary_weeks: tuple[int, int],
    primary_horizons: list[int],
    n_col: str = "feat_n_games",
) -> tuple[pl.DataFrame, list[dict]]:
    """Add a ``shrunk_feature`` column to ``obs`` (all windows/horizons/weeks),
    using a k chosen per OOS season from strictly earlier target seasons.

    Returns (obs_with_shrunk, per_(metric, season) k log).
    """
    plo, phi = primary_weeks
    train_mask = (
        (pl.col("week") >= plo) & (pl.col("week") <= phi)
        & pl.col("horizon").is_in(primary_horizons)
    )
    out_frames: list[pl.DataFrame] = []
    klog: list[dict] = []
    for metric, m_obs in obs.group_by("metric", maintain_order=True):
        metric = metric[0] if isinstance(metric, tuple) else metric
        for s in oos_seasons:
            train = m_obs.filter((pl.col("season") < s) & train_mask)
            k, fb, curve = select_k(train, k_grid, fallback_k=fallback_k,
                                    min_train_obs=min_train_obs, n_col=n_col)
            season_obs = m_obs.filter(pl.col("season") == s)
            if season_obs.is_empty():
                continue
            shr = shrink(
                season_obs.get_column("feature_value").to_numpy(),
                season_obs.get_column("baseline_league").to_numpy(),
                season_obs.get_column(n_col).to_numpy().astype(float),
                k,
            )
            out_frames.append(season_obs.with_columns(
                pl.Series("shrunk_feature", shr),
                pl.lit(k).alias("shrinkage_k"),
                pl.lit(fb).alias("shrinkage_k_fallback"),
            ))
            klog.append({
                "metric": metric, "oos_season": int(s), "k": float(k),
                "used_fallback": fb, "n_train": train.height,
                "k_curve": {str(kk): round(v, 6) for kk, v in curve.items()},
            })
    if not out_frames:
        return obs.with_columns(pl.lit(None, dtype=pl.Float64).alias("shrunk_feature")), klog
    return pl.concat(out_frames, how="diagonal_relaxed"), klog
