"""Chronological ridge opponent adjustment (Phase 4, Stage B).

Per (entity, game) unit-metric observation:

    metric ~ entity one-hot + opponent one-hot + home        (ridge)

The opponent-adjusted strength of an entity is (intercept + entity coefficient),
i.e. its expected metric against a league-average opponent on a neutral field,
centred to mean 0 across entities in the fit.

The ridge is fit strictly on completed games before the target kickoff (trailing
2 seasons). ``alpha`` is one per family, chosen walk-forward on earlier target
seasons only. Opponent adjustment is a HYPOTHESIS -- it may help some metrics,
hurt others, or do nothing.
"""
from matchup.opponent_adjustment.ridge_adjust import (
    game_unit_rows,
    select_alpha,
    walk_forward_strengths,
)

__all__ = ["game_unit_rows", "select_alpha", "walk_forward_strengths"]
