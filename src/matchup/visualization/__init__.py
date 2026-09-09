"""Presentation layer on top of the existing team-strength research model.

This package reads the model's existing outputs (outputs/weekly/*,
outputs/rankings/*) and existing config (config/strength.yaml -- the nine
domains and their member metrics) and renders them as a publication-quality
matchup card. It does not compute team strength, does not define new metrics,
and does not add betting logic. See matchup_card.create_matchup_card.
"""
from __future__ import annotations

from matchup.visualization.matchup_card import create_matchup_card

__all__ = ["create_matchup_card"]
