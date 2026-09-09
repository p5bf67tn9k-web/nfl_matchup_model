"""The 2026 weekly research workflow.

One command (`matchup weekly-research`) refreshes the team-strength snapshot for
the latest completed week, diffs it against the previous week and the preseason
baseline, points at the historical factor research, and writes machine-readable
outputs plus three markdown reports. Degrades gracefully before Week 1.
"""
from __future__ import annotations

from matchup.weekly.run import run_weekly_research

__all__ = ["run_weekly_research"]
