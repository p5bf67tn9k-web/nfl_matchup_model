"""Unit tests for point-in-time primitives with hand-verifiable cases."""
from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

import polars as pl
import pytest

from matchup.injuries.asof_rule import injury_asof_cutoff, resolve_availability_status
from matchup.pointintime.availability import source_available_at
from matchup.pointintime.calendar import kickoff_expr

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")


# --------------------------------------------------------------------------- #
# kickoff parsing: gametime is ET -> UTC
# --------------------------------------------------------------------------- #
def test_kickoff_expr_converts_eastern_to_utc():
    df = pl.DataFrame(
        {
            "gameday": ["2024-09-08", "2024-01-15", None],
            "gametime": ["13:00", "20:15", "16:30"],
        }
    ).with_columns(kickoff_expr())
    got = df.get_column("kickoff_utc").to_list()
    # Sept -> EDT (-4): 13:00 ET == 17:00 UTC
    assert got[0] == datetime(2024, 9, 8, 17, 0, tzinfo=UTC)
    # Jan -> EST (-5): 20:15 ET == 01:15 UTC next day
    assert got[1] == datetime(2024, 1, 16, 1, 15, tzinfo=UTC)


def test_kickoff_expr_uses_fallback_when_gametime_null():
    df = pl.DataFrame({"gameday": ["2019-09-08"], "gametime": [None]}).with_columns(
        kickoff_expr()
    )
    # fallback 13:00 ET, Sept EDT -> 17:00 UTC
    assert df.get_column("kickoff_utc").item() == datetime(2019, 9, 8, 17, 0, tzinfo=UTC)


# --------------------------------------------------------------------------- #
# injury as-of fallback rule -- hand cases
# --------------------------------------------------------------------------- #
def test_injury_cutoff_sunday_game_is_preceding_saturday_2359_et():
    # Sun 2024-11-10, 13:00 ET kickoff  ->  cutoff Sat 2024-11-09 23:59:59 ET
    kick = datetime(2024, 11, 10, 13, 0, tzinfo=ET).astimezone(UTC)
    cutoff = injury_asof_cutoff(kick)
    cutoff_et = cutoff.astimezone(ET)
    assert (cutoff_et.year, cutoff_et.month, cutoff_et.day) == (2024, 11, 9)
    assert (cutoff_et.hour, cutoff_et.minute) == (23, 59)


def test_injury_cutoff_monday_game_is_that_weeks_saturday():
    # Mon 2024-11-11 20:15 ET -> Saturday 2024-11-09 23:59:59 ET (2 days prior)
    kick = datetime(2024, 11, 11, 20, 15, tzinfo=ET).astimezone(UTC)
    cutoff = injury_asof_cutoff(kick).astimezone(ET)
    assert (cutoff.month, cutoff.day) == (11, 9)


def test_injury_cutoff_thursday_game_is_kickoff_minus_24h():
    kick = datetime(2024, 11, 7, 20, 15, tzinfo=ET).astimezone(UTC)
    cutoff = injury_asof_cutoff(kick)
    assert cutoff == kick - __import__("datetime").timedelta(hours=24)


def test_injury_cutoff_saturday_game_is_kickoff_minus_24h():
    # late-season Saturday game -> treated like Thu/Fri (kickoff - 24h), not "this Saturday 23:59"
    kick = datetime(2024, 12, 21, 13, 0, tzinfo=ET).astimezone(UTC)
    cutoff = injury_asof_cutoff(kick)
    assert cutoff == kick - __import__("datetime").timedelta(hours=24)


def test_injury_cutoff_wednesday_opener():
    # 2026 season opener is a Wednesday
    kick = datetime(2026, 9, 9, 20, 20, tzinfo=ET).astimezone(UTC)
    cutoff = injury_asof_cutoff(kick).astimezone(ET)
    # preceding Saturday = 2026-09-05
    assert (cutoff.month, cutoff.day) == (9, 5)


def test_injury_cutoff_always_strictly_before_kickoff():
    for wd in range(1, 8):
        kick = datetime(2024, 1, 1 + wd, 13, 0, tzinfo=ET).astimezone(UTC)
        assert injury_asof_cutoff(kick) < kick


# --------------------------------------------------------------------------- #
# publish-lag availability
# --------------------------------------------------------------------------- #
def test_source_available_at_adds_duration_and_lag():
    kick = datetime(2024, 9, 8, 17, 0, tzinfo=UTC)
    # 4h game + 3 day PFR lag
    got = source_available_at(kick, lag_days=3)
    assert got == datetime(2024, 9, 11, 21, 0, tzinfo=UTC)
    # 1 day pbp lag
    assert source_available_at(kick, lag_days=1) == datetime(2024, 9, 9, 21, 0, tzinfo=UTC)


# --------------------------------------------------------------------------- #
# availability status resolution -- documented conflict handling
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize(
    ("report", "practice", "roster", "expected"),
    [
        ("Out", "Did Not Participate In Practice", "ACT", "OUT"),
        (None, None, "RES", "OUT"),
        ("Doubtful", "Limited Participation in Practice", "ACT", "DOUBTFUL"),
        ("Questionable", "Limited Participation in Practice", "ACT", "QUESTIONABLE"),
        (None, "Did Not Participate In Practice", "ACT", "UNKNOWN_LEAN_OUT"),
        (None, "Limited Participation in Practice", "ACT", "PROBABLE_LIMITED"),
        (None, "Full Participation in Practice", "ACT", "ASSUME_AVAILABLE"),
        (None, None, None, "UNKNOWN"),
        (None, "\n    ", "ACT", "UNKNOWN"),  # dirty whitespace practice value
    ],
)
def test_resolve_availability_status(report, practice, roster, expected):
    assert resolve_availability_status(report, practice, roster) == expected


def test_null_report_status_is_never_healthy():
    # a null report_status must not by itself imply availability
    assert resolve_availability_status(None, None, None) == "UNKNOWN"
