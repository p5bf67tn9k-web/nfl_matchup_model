"""Factor research: which already-implemented football metrics show the
strongest, most stable evidence of association with -- and chronological
predictive information about -- scoring, points prevention, and winning.

Nothing here predicts individual game winners or scores. Correlation is never
reported as causation, and a large correlation alone never earns the label
"important".
"""
from __future__ import annotations

from matchup.research.factors import run_factor_analysis

__all__ = ["run_factor_analysis"]
