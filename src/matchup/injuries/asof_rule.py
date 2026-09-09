"""Conservative injury as-of fallback rule (decision DB).

When ``date_modified`` is present (historical, 2010-2024) it is the PRIMARY as-of
filter: a row is knowable iff ``date_modified < kickoff_utc``.

When ``date_modified`` is absent (2025+ / live), this fallback applies:

    game weekday Thu / Fri / Sat  ->  cutoff = kickoff_utc - 24h
    game weekday Sun / Mon / Tue / Wed  ->  cutoff = 23:59:59 America/New_York
                                            of the Saturday BEFORE kickoff

with a hard floor of ``kickoff_utc - 1h`` so the cutoff is always strictly pre-game.

The whole (season, week, team) injury report is then treated as knowable at that
cutoff. This is deliberately cautious (prefer false exclusion / staleness over
false inclusion). Its real cost is measured by
``matchup.injuries.validation`` on 2022-2024.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import polars as pl

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

_EARLY_WEEK_DOW = {7, 1, 2, 3}  # Sun, Mon, Tue, Wed  (polars weekday: Mon=1..Sun=7)
_LATE_WEEK_DOW = {4, 5, 6}      # Thu, Fri, Sat


def injury_asof_cutoff(kickoff_utc: datetime) -> datetime:
    """Scalar version. ``kickoff_utc`` must be timezone-aware."""
    if kickoff_utc.tzinfo is None:
        raise ValueError("kickoff_utc must be timezone-aware")
    kick_utc = kickoff_utc.astimezone(UTC)
    kick_et = kick_utc.astimezone(ET)
    dow = kick_et.isoweekday()  # Mon=1 .. Sun=7

    if dow in _LATE_WEEK_DOW:
        cutoff = kick_utc - timedelta(hours=24)
    else:
        offset_days = (dow % 7) + 1  # Sun->1, Mon->2, Tue->3, Wed->4
        sat_date = (kick_et - timedelta(days=offset_days)).date()
        cutoff_et = datetime(
            sat_date.year, sat_date.month, sat_date.day, 23, 59, 59, tzinfo=ET
        )
        cutoff = cutoff_et.astimezone(UTC)

    floor = kick_utc - timedelta(hours=1)
    return min(cutoff, floor)


def injury_asof_cutoff_expr(kickoff_col: str = "kickoff_utc") -> pl.Expr:
    """Vectorised equivalent, producing a UTC datetime column ``injury_asof_cutoff``."""
    kick = pl.col(kickoff_col).dt.convert_time_zone("UTC")
    kick_et = kick.dt.convert_time_zone("America/New_York")
    dow = kick_et.dt.weekday()  # Mon=1 .. Sun=7

    late = kick - pl.duration(hours=24)

    offset_days = (dow % 7) + 1
    sat_et_midnight = (kick_et.dt.date() - pl.duration(days=offset_days)).cast(pl.Datetime)
    sat_et = (
        (sat_et_midnight + pl.duration(hours=23, minutes=59, seconds=59))
        .dt.replace_time_zone("America/New_York", ambiguous="earliest")
        .dt.convert_time_zone("UTC")
    )

    cutoff = pl.when(dow.is_in([4, 5, 6])).then(late).otherwise(sat_et)
    floor = kick - pl.duration(hours=1)
    return pl.min_horizontal(cutoff, floor).alias("injury_asof_cutoff")


# --------------------------------------------------------------------------- #
# availability status resolution (documented conflict handling)
# --------------------------------------------------------------------------- #
_OUT_PRACTICE = {"Out (Definitely Will Not Play)"}
_DNP = {"Did Not Participate In Practice"}
_LIMITED = {"Limited Participation in Practice"}
_FULL = {"Full Participation in Practice"}


def resolve_availability_status(
    report_status: str | None,
    practice_status: str | None,
    roster_status: str | None,
) -> str:
    """Collapse the (report_status, practice_status, roster_status) triple into one
    ordinal availability label. Conflict handling is explicit and documented here.

    Precedence (most authoritative first):
      1. report_status == "Out"                       -> OUT
      2. roster_status in {RES, PUP, NON, CUT, ...}   -> OUT            (not on active roster)
      3. report_status == "Doubtful"                  -> DOUBTFUL
      4. practice_status == "Out (Definitely..."      -> OUT
      5. report_status == "Questionable"              -> QUESTIONABLE
      6. practice_status DNP  (no game designation)   -> UNKNOWN_LEAN_OUT
      7. practice_status Limited                      -> PROBABLE_LIMITED
      8. report_status == "Probable"                  -> PROBABLE
      9. practice_status Full / everything else       -> ASSUME_AVAILABLE
     10. all three null                               -> UNKNOWN

    NOTE: report_status == null is UNKNOWN, never "healthy". A null report_status with
    a Full practice is ASSUME_AVAILABLE only because the player still appeared on a
    practice report; a player absent from the injury table entirely is handled upstream.
    """
    rs = (report_status or "").strip()
    ps = (practice_status or "").strip()
    ros = (roster_status or "").strip().upper()

    inactive_roster = ros in {"RES", "PUP", "NON", "CUT", "EXE", "IR", "SUS", "RET"}

    if rs == "Out":
        return "OUT"
    if inactive_roster:
        return "OUT"
    if rs == "Doubtful":
        return "DOUBTFUL"
    if ps in _OUT_PRACTICE:
        return "OUT"
    if rs == "Questionable":
        return "QUESTIONABLE"
    if ps in _DNP:
        return "UNKNOWN_LEAN_OUT"
    if ps in _LIMITED:
        return "PROBABLE_LIMITED"
    if rs == "Probable":
        return "PROBABLE"
    if ps in _FULL or rs or ps:
        return "ASSUME_AVAILABLE"
    return "UNKNOWN"
