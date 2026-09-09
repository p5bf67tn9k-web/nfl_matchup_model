"""Enforcement of the point-in-time status contract.

A source may only enter a prediction feature frame if its status is LIVE_SAFE
(or HISTORICAL_SAFE, and only in explicit backtest mode). POST_SEASON_ONLY,
REFERENCE_ONLY, and UNKNOWN are hard-blocked.
"""
from __future__ import annotations

from matchup.config import PITStatus, load_publish_lag


class PointInTimeViolation(RuntimeError):
    """Raised when a non-admissible source is requested for a feature frame."""


def status_of(source: str) -> PITStatus:
    return load_publish_lag().get(source).point_in_time_status


def feature_frame_admissible(source: str, *, mode: str = "live") -> bool:
    """Is ``source`` allowed into a feature frame in the given mode?

    mode="live"     -> only LIVE_SAFE
    mode="backtest" -> LIVE_SAFE or HISTORICAL_SAFE
    """
    st = status_of(source)
    if mode == "live":
        return st is PITStatus.LIVE_SAFE
    if mode == "backtest":
        return st in (PITStatus.LIVE_SAFE, PITStatus.HISTORICAL_SAFE)
    raise ValueError(f"unknown mode {mode!r}")


def assert_admissible(source: str, *, mode: str = "live") -> None:
    if not feature_frame_admissible(source, mode=mode):
        raise PointInTimeViolation(
            f"source {source!r} has point-in-time status "
            f"{status_of(source).value} and cannot enter a {mode} feature frame"
        )
