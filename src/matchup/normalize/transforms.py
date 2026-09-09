"""Pure normalization transforms. No I/O, no as-of logic."""
from __future__ import annotations

import numpy as np


def zscore(value: float, ref: np.ndarray) -> float | None:
    ref = ref[~np.isnan(ref)]
    if ref.size < 2:
        return None
    sd = ref.std(ddof=1)
    if sd == 0 or np.isnan(sd):
        return None
    return float((value - ref.mean()) / sd)


def percentile_rank(value: float, ref: np.ndarray) -> float | None:
    """Fraction of the reference distribution at or below ``value`` (0..1)."""
    ref = ref[~np.isnan(ref)]
    if ref.size < 1:
        return None
    return float((ref <= value).mean())


def league_relative(value: float, ref: np.ndarray, *, mode: str = "diff") -> float | None:
    """mode='diff' -> value - ref_mean (default; safe for metrics that cross zero,
    e.g. EPA). mode='ratio' -> value / ref_mean (only for strictly-positive metrics)."""
    ref = ref[~np.isnan(ref)]
    if ref.size < 1:
        return None
    m = ref.mean()
    if mode == "ratio":
        return None if m == 0 else float(value / m)
    return float(value - m)
