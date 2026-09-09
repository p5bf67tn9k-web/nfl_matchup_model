"""Phase 3 -- predictive PERSISTENCE validation of the descriptive measurements.

Tests whether an as-of measurement carries out-of-sample information about the
SAME unit's FUTURE performance, beyond simple baselines. This is NOT a test of
matchup value (see reports/phase3_report.md -> "What Phase 3 does NOT establish").

Nothing here builds ratings, weights, opponent adjustment, matchup interactions,
expected performance, expected score, or any market-data feature.
"""
from matchup.validation.config import load_phase3_config
from matchup.validation.observations import build_observations
from matchup.validation.run import run_phase3

__all__ = ["build_observations", "load_phase3_config", "run_phase3"]
