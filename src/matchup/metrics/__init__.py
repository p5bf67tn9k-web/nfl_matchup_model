"""Phase 2 — descriptive metrics.

Strictly a *measurement* layer. Nothing here decides whether a metric is
predictive: that is a Phase 3+ walk-forward question. Reliability, correlation,
and football intuition do NOT establish predictive value.

Pipeline
--------
    classify_plays(pbp)              -> enriched play frame with documented flags
    <family>_game_metrics(...)       -> one row per (entity, game): raw additive
                                        components + single-game rates + provenance
    window_metric(...)               -> trailing / expanding / prior-season aggregates
                                        over the entity's GAME SEQUENCE (never week math)
    normalize(...)                   -> z / percentile / league-relative vs the 3 most
                                        recent COMPLETED seasons as of the prediction date
"""
from matchup.metrics.plays import (
    EXPLOSIVE_PASS_YARDS,
    EXPLOSIVE_RUSH_YARDS,
    PLAY_FLAG_COLUMNS,
    classify_plays,
)
from matchup.metrics.windows import WINDOWS, window_metric

__all__ = [
    "EXPLOSIVE_PASS_YARDS",
    "EXPLOSIVE_RUSH_YARDS",
    "PLAY_FLAG_COLUMNS",
    "WINDOWS",
    "classify_plays",
    "window_metric",
]
