"""Regression-to-the-mean shrinkage (Phase 4, Stage A).

    shrunk = league_mean + w * (raw - league_mean)     w = n / (n + k)

`k` is ONE parameter per metric, chosen strictly walk-forward: for each OOS
season S, `k` minimises pooled RMSE on observations with target season < S, is
frozen, then applied to S. Never per team / player / position / season; never
nonlinear; never tuned on the 2019-2025 evaluation period.
"""
from matchup.shrinkage.shrink import (
    apply_shrinkage_walkforward,
    select_k,
    shrink,
)

__all__ = ["apply_shrinkage_walkforward", "select_k", "shrink"]
