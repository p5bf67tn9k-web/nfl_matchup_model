"""Visual constants for matchup cards: team display names/colors, palette,
typography, and small presentation-only formatting helpers.

Nothing in this module touches the strength model. Team colors/names are
public-knowledge branding facts used only for chart styling.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

NA = "N/A"

# --- team display metadata (name, primary color, secondary color) ----------
# Presentation-only. Not part of the research model.
TEAM_META: dict[str, tuple[str, str, str]] = {
    "ARI": ("Arizona Cardinals", "#97233F", "#000000"),
    "ATL": ("Atlanta Falcons", "#A71930", "#000000"),
    "BAL": ("Baltimore Ravens", "#241773", "#9E7C0C"),
    "BUF": ("Buffalo Bills", "#00338D", "#C60C30"),
    "CAR": ("Carolina Panthers", "#0085CA", "#101820"),
    "CHI": ("Chicago Bears", "#0B162A", "#C83803"),
    "CIN": ("Cincinnati Bengals", "#FB4F14", "#000000"),
    "CLE": ("Cleveland Browns", "#311D00", "#FF3C00"),
    "DAL": ("Dallas Cowboys", "#041E42", "#869397"),
    "DEN": ("Denver Broncos", "#FB4F14", "#002244"),
    "DET": ("Detroit Lions", "#0076B6", "#B0B7BC"),
    "GB":  ("Green Bay Packers", "#203731", "#FFB612"),
    "HOU": ("Houston Texans", "#03202F", "#A71930"),
    "IND": ("Indianapolis Colts", "#002C5F", "#A2AAAD"),
    "JAX": ("Jacksonville Jaguars", "#101820", "#D7A22A"),
    "KC":  ("Kansas City Chiefs", "#E31837", "#FFB81C"),
    "LA":  ("Los Angeles Rams", "#003594", "#FFA300"),
    "LAC": ("Los Angeles Chargers", "#0080C6", "#FFC20E"),
    "LV":  ("Las Vegas Raiders", "#000000", "#A5ACAF"),
    "MIA": ("Miami Dolphins", "#008E97", "#FC4C02"),
    "MIN": ("Minnesota Vikings", "#4F2683", "#FFC62F"),
    "NE":  ("New England Patriots", "#002244", "#C60C30"),
    "NO":  ("New Orleans Saints", "#D3BC8D", "#101820"),
    "NYG": ("New York Giants", "#0B2265", "#A71930"),
    "NYJ": ("New York Jets", "#125740", "#000000"),
    "PHI": ("Philadelphia Eagles", "#004C54", "#A5ACAF"),
    "PIT": ("Pittsburgh Steelers", "#FFB612", "#101820"),
    "SEA": ("Seattle Seahawks", "#002244", "#69BE28"),
    "SF":  ("San Francisco 49ers", "#AA0000", "#B3995D"),
    "TB":  ("Tampa Bay Buccaneers", "#D50A0A", "#34302B"),
    "TEN": ("Tennessee Titans", "#0C2340", "#4B92DB"),
    "WAS": ("Washington Commanders", "#5A1414", "#FFB612"),
}

_FALLBACK_COLOR = ("#3A3A3A", "#8A8A8A")


def team_display_name(abbr: str) -> str:
    meta = TEAM_META.get(abbr.upper())
    return meta[0] if meta else abbr.upper()


def team_colors(abbr: str) -> tuple[str, str]:
    meta = TEAM_META.get(abbr.upper())
    return (meta[1], meta[2]) if meta else _FALLBACK_COLOR


# --- palette / typography ---------------------------------------------------
BG = "#FFFFFF"
PANEL_BG = "#F7F7F9"
INK = "#111318"
SUBINK = "#5B5F6B"
GRIDLINE = "#E2E3E8"
ZERO_LINE = "#B9BBC4"
POSITIVE_TINT = "#DDE8DA"
NEGATIVE_TINT = "#F1DEDD"

CONFIDENCE_COLORS = {
    "high": "#1E7A34",
    "medium": "#B98900",
    "low": "#B5482A",
    "prior_season_only": "#6B6F7B",
    "none": "#B5482A",
}

FONT_FAMILY = "DejaVu Sans"  # matplotlib default, ships with every install

# domain index values are reference-SD z-scores; this is the fixed display
# range the strength bars are clipped/scaled to (a rendering choice, not a
# change to the underlying value).
BAR_SCALE_ABS = 2.5


@dataclass(frozen=True)
class TeamStyle:
    abbr: str
    name: str
    primary: str
    secondary: str


def team_style(abbr: str) -> TeamStyle:
    name = team_display_name(abbr)
    primary, secondary = team_colors(abbr)
    return TeamStyle(abbr=abbr.upper(), name=name, primary=primary, secondary=secondary)


def _hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _color_distance(a: str, b: str) -> float:
    ar, ag, ab = _hex_to_rgb(a)
    br, bg, bb = _hex_to_rgb(b)
    return math.sqrt((ar - br) ** 2 + (ag - bg) ** 2 + (ab - bb) ** 2)


_COLOR_CLASH_THRESHOLD = 90.0  # empirical: distinguishes near-identical navy/black pairs


def display_team_pair(away_abbr: str, home_abbr: str) -> tuple[TeamStyle, TeamStyle]:
    """away/home TeamStyle for chart rendering, with the home team's display
    color swapped to its secondary color if its primary is visually too close
    to the away team's primary (a real case: e.g. NE and SEA are both navy).
    Never changes team names/abbreviations, only which brand color is used to
    draw that team's bars/accents on this card."""
    away = team_style(away_abbr)
    home = team_style(home_abbr)
    if (_color_distance(away.primary, home.primary) < _COLOR_CLASH_THRESHOLD
            and _color_distance(away.primary, home.secondary) >= _COLOR_CLASH_THRESHOLD):
        home = TeamStyle(abbr=home.abbr, name=home.name, primary=home.secondary, secondary=home.primary)
    return away, home


# --- formatting helpers ------------------------------------------------------
def fmt_index(value: float | None) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return NA
    return f"{value:+.2f}"


def fmt_rank(rank: int | None, n_teams: int | None) -> str:
    if rank is None or n_teams is None:
        return NA
    return f"{rank}/{n_teams}"


def fmt_percentile(pct: float | None) -> str:
    if pct is None or (isinstance(pct, float) and math.isnan(pct)):
        return NA
    return f"{pct * 100:.0f}th pct"


def fmt_confidence(label: str | None) -> str:
    if not label:
        return NA
    return {
        "high": "High confidence",
        "medium": "Medium confidence",
        "low": "Low confidence",
        "prior_season_only": "Preseason baseline (prior season only)",
        "none": "No data",
    }.get(label, label)


def bar_fraction(value: float | None, scale_abs: float = BAR_SCALE_ABS) -> float | None:
    """Clip+scale an index value to [-1, 1] for bar rendering. Display-only."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    return max(-1.0, min(1.0, value / scale_abs))
