"""Render a publication-quality matchup card (PNG + PDF) from the existing
team-strength research model's outputs.

    python scripts/create_matchup_card.py --away NE --home SEA --season 2026 --week 1

This module only draws what data.py assembles. It performs no strength
calculations of its own. See data.py's module docstring for exactly which
existing output column backs every number on the card.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from matchup.config import REPO_ROOT
from matchup.strength.config import DOMAINS
from matchup.visualization import styles as sty
from matchup.visualization.data import (
    MatchupCardData,
    TeamProfile,
    UnitComparison,
    compute_matchup_comparisons,
    identify_key_battles,
    load_matchup_card_data,
    team_identity_statements,
)

DEFAULT_OUTPUT_DIR = REPO_ROOT / "outputs" / "matchups"

_DISCLAIMER = (
    "Strength indices are league-relative research measures, not ratings, probabilities, "
    "or predictions. Values are based only on information available through the selected week. "
    "This is not a game prediction, spread, or win-probability model."
)


# --------------------------------------------------------------------------- #
# small drawing helpers
# --------------------------------------------------------------------------- #
def _section_title(ax, x: float, y: float, text: str) -> None:
    ax.text(x, y, text, fontsize=13, fontweight="bold", color=sty.INK, va="top", ha="left",
             family=sty.FONT_FAMILY)


def _hline(ax, y: float, x0: float = 0.0, x1: float = 1.0, color: str = sty.GRIDLINE, lw: float = 1.0) -> None:
    ax.plot([x0, x1], [y, y], color=color, lw=lw, transform=ax.transAxes, clip_on=False)


def _new_axes(fig, rect: tuple[float, float, float, float]):
    ax = fig.add_axes(rect)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return ax


# --------------------------------------------------------------------------- #
# header
# --------------------------------------------------------------------------- #
def _draw_header(ax, data: MatchupCardData, away_s: sty.TeamStyle, home_s: sty.TeamStyle) -> None:
    m = data.meta

    ax.add_patch(FancyBboxPatch((0.0, 0.0), 1.0, 1.0, boxstyle="square,pad=0",
                                 linewidth=0, facecolor=sty.INK, transform=ax.transAxes, zorder=0))
    ax.text(0.03, 0.85, "NFL MATCHUP RESEARCH", fontsize=12, fontweight="bold",
            color="#FFFFFF", va="top", ha="left", family=sty.FONT_FAMILY)
    week_label = f"Week {m.requested_week}" if m.requested_week > 0 else "Preseason"
    ax.text(0.97, 0.85, f"{m.season} · {week_label}", fontsize=12, color="#C9CBD4",
            va="top", ha="right", family=sty.FONT_FAMILY)

    matchup_txt = f"{sty.team_display_name(data.away.team).upper()}  at  {sty.team_display_name(data.home.team).upper()}"
    ax.text(0.03, 0.53, matchup_txt, fontsize=21, fontweight="bold", color="#FFFFFF",
            va="center", ha="left", family=sty.FONT_FAMILY)

    # `location` in the schedule table denotes site type ("Home"/"Neutral"), not a
    # place -- only surface it when the game is at a neutral site.
    venue_txt = m.stadium or "Venue: N/A"
    if m.location and m.location.lower() not in ("home", ""):
        venue_txt = f"{venue_txt} (Neutral Site)"
    date_txt = m.gameday or ""
    sub = " · ".join([t for t in (venue_txt, date_txt) if t])
    ax.text(0.03, 0.27, sub, fontsize=10, color="#9EA1AE", va="center", ha="left",
            family=sty.FONT_FAMILY)

    if data.away.overall_confidence or data.home.overall_confidence:
        conf_txt = (f"Data confidence -- away: {sty.fmt_confidence(data.away.overall_confidence)}  "
                    f"·  home: {sty.fmt_confidence(data.home.overall_confidence)}")
        ax.text(0.03, 0.15, conf_txt, fontsize=8, color="#7B7E8A", va="center", ha="left",
                family=sty.FONT_FAMILY)

    if m.is_baseline_display:
        badge = "PRESEASON BASELINE"
    else:
        badge = f"THROUGH WEEK {m.displayed_through_week}"
    ax.text(0.97, 0.12, badge, fontsize=9.5, fontweight="bold", color=sty.INK, va="center",
            ha="right", family=sty.FONT_FAMILY,
            bbox={"boxstyle": "round,pad=0.35", "facecolor": "#FFB612", "edgecolor": "none"})

    ax.add_patch(plt.Rectangle((0.0, 0.0), 0.5, 0.06, transform=ax.transAxes,
                                facecolor=away_s.primary, edgecolor="none"))
    ax.add_patch(plt.Rectangle((0.5, 0.0), 0.5, 0.06, transform=ax.transAxes,
                                facecolor=home_s.primary, edgecolor="none"))


# --------------------------------------------------------------------------- #
# Section 1: team strength profile (all 9 domains)
# --------------------------------------------------------------------------- #
def _draw_strength_profile(
    ax, data: MatchupCardData, away_s: sty.TeamStyle, home_s: sty.TeamStyle
) -> None:
    away, home = data.away, data.home
    scale = sty.BAR_SCALE_ABS
    yax = ax.get_yaxis_transform()  # x in axes fraction, y in data coords -- scale-independent margins

    ax.set_xlim(-scale, scale)
    domains = list(DOMAINS.keys())
    n = len(domains)
    ax.set_ylim(-0.6, n - 0.4)
    ax.axvline(0, color=sty.ZERO_LINE, lw=1.2, zorder=1)

    for i, dom_id in enumerate(domains):
        y = n - 1 - i
        dv_away, dv_home = away.domain(dom_id), home.domain(dom_id)

        ax.text(-0.02, y, DOMAINS[dom_id]["label"], fontsize=9.3, fontweight="bold",
                color=sty.INK, va="center", ha="right", transform=yax, family=sty.FONT_FAMILY)

        for dv, style, offset in ((dv_away, away_s, 0.19), (dv_home, home_s, -0.19)):
            yy = y + offset
            if dv.index_value is None:
                ax.barh(yy, 0.02, height=0.3, left=-0.01, color=sty.GRIDLINE, zorder=2)
                txt = sty.NA
            else:
                v = max(-scale, min(scale, dv.index_value))
                ax.barh(yy, v, height=0.3, left=0, color=style.primary,
                        edgecolor="none", zorder=2, align="center")
                txt = (f"{sty.fmt_index(dv.index_value)}  ·  {sty.fmt_rank(dv.rank, dv.n_teams)}"
                       f"  ·  {sty.fmt_percentile(dv.percentile)}")
                if dv.confidence:
                    dot_color = sty.CONFIDENCE_COLORS.get(dv.confidence, sty.SUBINK)
                    ax.scatter([1.015], [yy], s=12, color=dot_color, zorder=3,
                               transform=yax, clip_on=False)
            ax.text(1.03, yy, txt, fontsize=6.9, color=sty.SUBINK,
                    va="center", ha="left", transform=yax, family=sty.FONT_FAMILY)

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


# --------------------------------------------------------------------------- #
# Section 2: matchup comparisons (6 offense-vs-defense pairs)
# --------------------------------------------------------------------------- #
# |gap| that fills the advantage meter to its edge. Display-only clip -- the
# printed gap number is always the exact value.
GAP_METER_SCALE = 2.0

# column anchors for the Section 2 ledger, in axes fraction (x-axis is 0..1).
_S2_X_LABEL = 0.0
_S2_X_OFFENSE = 0.505
_S2_X_DEFENSE = 0.605
_S2_X_METER_C = 0.755
_S2_METER_HW = 0.075
_S2_X_EDGE_TXT = _S2_X_METER_C + _S2_METER_HW + 0.018


def _draw_comparisons(
    ax, data: MatchupCardData, comparisons: list[UnitComparison],
    away_s: sty.TeamStyle, home_s: sty.TeamStyle,
) -> None:
    """Section 2 as a compact ledger. One row per offense-vs-defense unit pair:
    both unit index values, a centered advantage meter that fills toward the
    favored unit, and the favored team + exact gap. No free-floating bars."""
    team_style = {"away": away_s, "home": home_s}
    n = len(comparisons)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, n + 1)  # top row is the column header
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # -- column header ----------------------------------------------------- #
    hy = n + 0.5
    for x, txt, ha in (
        (_S2_X_LABEL, "MATCHUP", "left"),
        (_S2_X_OFFENSE, "OFFENSE", "center"),
        (_S2_X_DEFENSE, "DEFENSE", "center"),
        (_S2_X_METER_C, "ADVANTAGE", "center"),
    ):
        ax.text(x, hy, txt, fontsize=7.2, fontweight="bold", color=sty.SUBINK,
                va="center", ha=ha, family=sty.FONT_FAMILY, zorder=5)
    ax.plot([-0.01, 1.0], [n + 0.06, n + 0.06], color=sty.GRIDLINE, lw=1.0,
            clip_on=False, zorder=1)

    for i, c in enumerate(comparisons):
        y = n - 1 - i + 0.5  # row centre
        a_s, b_s = team_style[c.unit_a_team], team_style[c.unit_b_team]

        if i % 2 == 0:
            ax.add_patch(plt.Rectangle((-0.01, y - 0.5), 1.02, 1.0, facecolor=sty.PANEL_BG,
                                        edgecolor="none", zorder=0))

        # matchup label (two lines: pairing, then which team fields each unit)
        ax.text(_S2_X_LABEL, y + 0.16, c.label, fontsize=8.1, fontweight="bold", color=sty.INK,
                va="center", ha="left", family=sty.FONT_FAMILY, zorder=5)
        ax.text(_S2_X_LABEL, y - 0.17, f"{a_s.abbr} offense  vs  {b_s.abbr} defense",
                fontsize=6.8, color=sty.SUBINK, va="center", ha="left",
                family=sty.FONT_FAMILY, zorder=5)

        if c.gap is None:
            for x in (_S2_X_OFFENSE, _S2_X_DEFENSE):
                ax.text(x, y, sty.NA, fontsize=8.6, color=sty.SUBINK, va="center", ha="center",
                        family=sty.FONT_FAMILY, zorder=5)
            ax.text(_S2_X_METER_C, y, "insufficient data", fontsize=7.0, style="italic",
                    color=sty.SUBINK, va="center", ha="center", family=sty.FONT_FAMILY, zorder=5)
            continue

        # unit index values
        ax.text(_S2_X_OFFENSE, y, sty.fmt_index(c.unit_a_value), fontsize=9.4, color=sty.INK,
                va="center", ha="center", family=sty.FONT_FAMILY, zorder=5)
        ax.text(_S2_X_DEFENSE, y, sty.fmt_index(c.unit_b_value), fontsize=9.4, color=sty.INK,
                va="center", ha="center", family=sty.FONT_FAMILY, zorder=5)

        # advantage meter: track, then a fill growing from centre toward the
        # favored unit (right = offense edge, left = defense edge)
        favored_a = c.gap >= 0
        favored_s = a_s if favored_a else b_s
        color = favored_s.primary
        frac = max(-1.0, min(1.0, c.gap / GAP_METER_SCALE))
        w = frac * _S2_METER_HW

        ax.add_patch(FancyBboxPatch(
            (_S2_X_METER_C - _S2_METER_HW, y - 0.10), 2 * _S2_METER_HW, 0.20,
            boxstyle="round,pad=0,rounding_size=0.015", linewidth=0,
            facecolor=sty.GRIDLINE, zorder=2))
        if abs(w) > 1e-4:
            ax.add_patch(FancyBboxPatch(
                (min(_S2_X_METER_C, _S2_X_METER_C + w), y - 0.10), max(abs(w), 0.004), 0.20,
                boxstyle="round,pad=0,rounding_size=0.015", linewidth=0,
                facecolor=color, zorder=3))
        ax.plot([_S2_X_METER_C, _S2_X_METER_C], [y - 0.13, y + 0.13],
                color=sty.INK, lw=1.0, zorder=4)

        ax.text(_S2_X_EDGE_TXT, y, f"{favored_s.abbr}  +{abs(c.gap):.2f}",
                fontsize=8.4, fontweight="bold", color=color, va="center", ha="left",
                family=sty.FONT_FAMILY, zorder=5)


# --------------------------------------------------------------------------- #
# Section 3: key matchup battles
# --------------------------------------------------------------------------- #
def _draw_key_battles(
    ax, data: MatchupCardData, battles: list[UnitComparison],
    away_s: sty.TeamStyle, home_s: sty.TeamStyle,
) -> None:
    team_style = {"away": away_s, "home": home_s}
    n = max(len(battles), 1)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, n)

    if not battles:
        ax.text(0.5, n / 2, "No measurable offense-vs-defense gaps available for this snapshot.",
                fontsize=9.5, color=sty.SUBINK, va="center", ha="center", family=sty.FONT_FAMILY)
        ax.set_xticks([]); ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
        return

    for i, c in enumerate(battles):
        y0 = n - 1 - i
        style_a, style_b = team_style[c.unit_a_team], team_style[c.unit_b_team]
        ax.add_patch(FancyBboxPatch((0.01, y0 + 0.06), 0.98, 0.86,
                                     boxstyle="round,pad=0.01,rounding_size=0.02",
                                     linewidth=0.8, edgecolor=sty.GRIDLINE, facecolor=sty.PANEL_BG))
        cy = y0 + 0.49
        ax.text(0.05, cy + 0.22, f"{style_a.name.upper()}", fontsize=9.5, fontweight="bold",
                color=style_a.primary, va="center", ha="left", family=sty.FONT_FAMILY)
        ax.text(0.05, cy + 0.02, DOMAINS[c.unit_a_domain]["label"], fontsize=8, color=sty.SUBINK,
                va="center", ha="left", family=sty.FONT_FAMILY)
        ax.text(0.05, cy - 0.22, sty.fmt_index(c.unit_a_value), fontsize=12, fontweight="bold",
                color=sty.INK, va="center", ha="left", family=sty.FONT_FAMILY)

        ax.text(0.5, cy, "vs", fontsize=10, color=sty.SUBINK, va="center", ha="center",
                style="italic", family=sty.FONT_FAMILY)

        ax.text(0.95, cy + 0.22, f"{style_b.name.upper()}", fontsize=9.5, fontweight="bold",
                color=style_b.primary, va="center", ha="right", family=sty.FONT_FAMILY)
        ax.text(0.95, cy + 0.02, DOMAINS[c.unit_b_domain]["label"], fontsize=8, color=sty.SUBINK,
                va="center", ha="right", family=sty.FONT_FAMILY)
        ax.text(0.95, cy - 0.22, sty.fmt_index(c.unit_b_value), fontsize=12, fontweight="bold",
                color=sty.INK, va="center", ha="right", family=sty.FONT_FAMILY)

        gap_txt = f"RELATIVE GAP: {abs(c.gap):.2f}" if c.gap is not None else "RELATIVE GAP: N/A"
        ax.text(0.5, y0 + 0.14, gap_txt, fontsize=8, fontweight="bold", color=sty.INK,
                va="center", ha="center", family=sty.FONT_FAMILY)

    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


# --------------------------------------------------------------------------- #
# Section 4: team identities
# --------------------------------------------------------------------------- #
def _draw_identity(ax, profile: TeamProfile, style: sty.TeamStyle) -> None:
    ax.add_patch(plt.Rectangle((0.0, 0.92), 1.0, 0.08, transform=ax.transAxes,
                                facecolor=style.primary, edgecolor="none"))
    ax.text(0.04, 0.955, style.name.upper(), fontsize=10.5, fontweight="bold", color="#FFFFFF",
            va="center", ha="left", family=sty.FONT_FAMILY)

    stmts = team_identity_statements(profile)
    y = 0.82
    if not stmts:
        ax.text(0.04, y, "No domain data available for this team/week.", fontsize=8.6,
                color=sty.SUBINK, va="top", ha="left", family=sty.FONT_FAMILY)
    for s in stmts[:5]:
        ax.text(0.04, y, f"• {s}", fontsize=8.6, color=sty.INK, va="top", ha="left",
                family=sty.FONT_FAMILY, wrap=True)
        y -= 0.155

    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.add_patch(plt.Rectangle((0.0, 0.0), 1.0, 1.0, transform=ax.transAxes, fill=False,
                                edgecolor=sty.GRIDLINE, linewidth=1.0))


# --------------------------------------------------------------------------- #
# Section 5: model context / footer
# --------------------------------------------------------------------------- #
def _draw_footer(ax, data: MatchupCardData) -> None:
    m = data.meta
    label = (f"Model baseline entering Week {m.requested_week}" if m.is_baseline_display
              else f"Model data through Week {m.displayed_through_week}, {m.season}")
    ax.text(0.0, 0.86, label, fontsize=9.5, fontweight="bold", color=sty.INK, va="top", ha="left",
            family=sty.FONT_FAMILY)
    ax.text(0.0, 0.62, _DISCLAIMER, fontsize=7.4, color=sty.SUBINK, va="top", ha="left",
            family=sty.FONT_FAMILY, wrap=True)
    src_note = (
        f"Domain indices, ranks, and confidence are read directly from the model's existing "
        f"outputs (data source: {m.data_source}); this report performs no independent strength "
        f"calculation. Nine domains, equal-weight means of shrunk z-scores -- see "
        f"config/strength.yaml."
    )
    ax.text(0.0, 0.26, src_note, fontsize=6.8, color=sty.SUBINK, va="top", ha="left",
            family=sty.FONT_FAMILY, wrap=True)
    if m.generated_at:
        ax.text(1.0, 0.02, f"Generated {m.generated_at}", fontsize=6.6, color=sty.SUBINK,
                va="bottom", ha="right", family=sty.FONT_FAMILY)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    for spine in ax.spines.values():
        spine.set_visible(False)


# --------------------------------------------------------------------------- #
# figure assembly
# --------------------------------------------------------------------------- #
def build_figure(data: MatchupCardData):
    away_s, home_s = sty.display_team_pair(data.away.team, data.home.team)
    comparisons = compute_matchup_comparisons(data)
    battles = identify_key_battles(comparisons)

    n_domains = len(DOMAINS)
    n_comp = len(comparisons)
    n_battles = max(len(battles), 1)

    header_h = 1.40
    sec1_title_h, sec1_row_h = 0.55, 0.42
    sec2_title_h, sec2_row_h = 0.55, 0.48
    sec3_title_h, sec3_row_h = 0.40, 0.62
    sec4_title_h, sec4_h = 0.40, 2.0
    footer_h = 1.15
    margins = 0.9

    sec1_h = sec1_title_h + n_domains * sec1_row_h
    sec2_h = sec2_title_h + (n_comp + 1) * sec2_row_h  # +1 for the ledger header row
    sec3_h = sec3_title_h + n_battles * sec3_row_h

    total_h = margins + header_h + sec1_h + sec2_h + sec3_h + sec4_title_h + sec4_h + footer_h
    width = 12.0

    fig = plt.figure(figsize=(width, total_h), dpi=200, facecolor=sty.BG)

    left, right = 0.09, 0.96
    y = total_h - margins / 2

    y -= header_h
    ax_header = fig.add_axes([left - 0.02, y / total_h, (right - left) + 0.04, header_h / total_h])
    ax_header.set_xlim(0, 1); ax_header.set_ylim(0, 1)
    ax_header.set_xticks([]); ax_header.set_yticks([])
    for spine in ax_header.spines.values():
        spine.set_visible(False)
    _draw_header(ax_header, data, away_s, home_s)

    y -= sec1_title_h
    ax_t1 = fig.add_axes([left, y / total_h, right - left, sec1_title_h / total_h])
    ax_t1.axis("off")
    ax_t1.set_xlim(0, 1); ax_t1.set_ylim(0, 1)
    _section_title(ax_t1, 0.0, 0.95, "SECTION 1 — TEAM STRENGTH PROFILE (9 DOMAINS)")
    ax_t1.text(0.0, 0.32, "index value (reference-SD units, league-relative)  ·  bar length clipped at ±"
               f"{sty.BAR_SCALE_ABS:g}  ·  value · rank · percentile · confidence",
               fontsize=7.2, color=sty.SUBINK, family=sty.FONT_FAMILY, va="top")

    y -= n_domains * sec1_row_h
    ax_s1 = fig.add_axes([left + 0.22, y / total_h, right - left - 0.46, (n_domains * sec1_row_h) / total_h])
    _draw_strength_profile(ax_s1, data, away_s, home_s)

    y -= sec2_title_h
    ax_t2 = fig.add_axes([left, y / total_h, right - left, sec2_title_h / total_h])
    ax_t2.axis("off")
    ax_t2.set_xlim(0, 1); ax_t2.set_ylim(0, 1)
    _section_title(ax_t2, 0.0, 0.95, "SECTION 2 — MATCHUP COMPARISON")
    ax_t2.text(0.0, 0.32, "one row per offense-vs-defense unit pair  ·  ADVANTAGE meter fills toward the "
               "favored unit (right = offense, left = defense); label shows the favored team and exact gap",
               fontsize=7.2, color=sty.SUBINK, family=sty.FONT_FAMILY, va="top")

    y -= (n_comp + 1) * sec2_row_h
    ax_s2 = fig.add_axes([left, y / total_h, right - left, ((n_comp + 1) * sec2_row_h) / total_h])
    _draw_comparisons(ax_s2, data, comparisons, away_s, home_s)

    y -= sec3_title_h
    ax_t3 = fig.add_axes([left, y / total_h, right - left, sec3_title_h / total_h])
    ax_t3.axis("off")
    ax_t3.set_xlim(0, 1); ax_t3.set_ylim(0, 1)
    _section_title(ax_t3, 0.0, 0.95, "SECTION 3 — KEY MATCHUP BATTLES")

    y -= n_battles * sec3_row_h
    ax_s3 = fig.add_axes([left, y / total_h, right - left, (n_battles * sec3_row_h) / total_h])
    _draw_key_battles(ax_s3, data, battles, away_s, home_s)

    y -= sec4_title_h
    ax_t4 = fig.add_axes([left, y / total_h, right - left, sec4_title_h / total_h])
    ax_t4.axis("off")
    ax_t4.set_xlim(0, 1); ax_t4.set_ylim(0, 1)
    _section_title(ax_t4, 0.0, 0.95, "SECTION 4 — TEAM IDENTITIES")

    y -= sec4_h
    gap = 0.02
    col_w = (right - left - gap) / 2
    ax_id_away = fig.add_axes([left, y / total_h, col_w, sec4_h / total_h])
    ax_id_home = fig.add_axes([left + col_w + gap, y / total_h, col_w, sec4_h / total_h])
    _draw_identity(ax_id_away, data.away, away_s)
    _draw_identity(ax_id_home, data.home, home_s)

    y -= footer_h
    ax_footer = fig.add_axes([left, y / total_h, right - left, footer_h / total_h])
    _hline(ax_footer, 0.98)
    _draw_footer(ax_footer, data)

    return fig


# --------------------------------------------------------------------------- #
# public API
# --------------------------------------------------------------------------- #
def create_matchup_card(
    away: str, home: str, season: int, week: int,
    *, output_dir: Path | None = None,
) -> tuple[Path, Path]:
    """Build and save a matchup card as PNG + PDF.

    Returns (png_path, pdf_path). Raises data.MatchupDataError if required
    model outputs are missing or the requested teams/week can't be resolved.
    """
    data = load_matchup_card_data(away, home, season, week)
    fig = build_figure(data)

    out_dir = output_dir or DEFAULT_OUTPUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{season}_week{week}_{data.away.team}_{data.home.team}"
    png_path = out_dir / f"{stem}.png"
    pdf_path = out_dir / f"{stem}.pdf"

    fig.savefig(png_path, facecolor=fig.get_facecolor(), bbox_inches=None)
    fig.savefig(pdf_path, facecolor=fig.get_facecolor(), bbox_inches=None)
    plt.close(fig)
    return png_path, pdf_path
