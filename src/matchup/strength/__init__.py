"""Transparent team-strength research layer (final build).

Turns the already-validated metric + shrinkage + normalization infrastructure
into per-team, per-week research indices with every underlying number kept
visible. Builds nothing that predicts game outcomes, spreads, or winners.
"""
from __future__ import annotations

from matchup.strength.config import DOMAINS, STRENGTH_METRICS, load_strength_config
from matchup.strength.results import team_game_results
from matchup.strength.team_metrics import build_team_metrics_weekly
from matchup.strength.team_strength import build_rankings_weekly, build_team_strength_weekly

__all__ = [
    "DOMAINS",
    "STRENGTH_METRICS",
    "build_rankings_weekly",
    "build_team_metrics_weekly",
    "build_team_strength_weekly",
    "load_strength_config",
    "team_game_results",
]
