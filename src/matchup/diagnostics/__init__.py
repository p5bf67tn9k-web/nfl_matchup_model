"""Descriptive diagnostics: metric reliability and redundancy.

NEITHER establishes predictive value. Reliability = "does the metric measure the
same thing consistently". Redundancy = "how much do metrics overlap in the
measurement space". Predictive value is a Phase 3+ walk-forward question.

Any diagnostic that looks at future observations (e.g. season-to-date vs
rest-of-season) is RETROSPECTIVE ONLY and is flagged ``is_retrospective=True``.
It must never feed production features, normalization, selection, or weights.
"""
from matchup.diagnostics.redundancy import build_redundancy_report
from matchup.diagnostics.reliability import build_reliability_report

__all__ = ["build_redundancy_report", "build_reliability_report"]
