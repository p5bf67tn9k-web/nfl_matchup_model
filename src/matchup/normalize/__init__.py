"""League-relative normalization.

Production rule (decision DG, locked): normalize against the **three most recent
COMPLETED seasons** as of the prediction date. Never the current incomplete
season, never a future season, never future games of the current season. The
reference seasons and sample size are logged on every normalized row.
"""
from matchup.normalize.normalize import (
    build_reference_distribution,
    normalize_value,
    normalize_windowed,
)
from matchup.normalize.reference import completed_seasons_asof
from matchup.normalize.transforms import league_relative, percentile_rank, zscore

__all__ = [
    "build_reference_distribution",
    "completed_seasons_asof",
    "league_relative",
    "normalize_value",
    "normalize_windowed",
    "percentile_rank",
    "zscore",
]
