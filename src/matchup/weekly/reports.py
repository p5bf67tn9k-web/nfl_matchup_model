"""Markdown report writers for the weekly workflow.

The reports summarise what changed but never replace the underlying numbers:
every generated report links to (and samples from) the machine-readable tables,
and the per-team profile prints the actual metric values.
"""
from __future__ import annotations

import math

import polars as pl

from matchup.config import REPO_ROOT
from matchup.strength.config import DOMAINS
from matchup.strength.team_strength import index_formula_text

REPORTS = REPO_ROOT / "reports"

_DISCLAIMER = (
    "> These indices are **transparent research indices**, not ratings, "
    "probabilities, or predictions of game outcomes. Each is an equal-weight mean "
    "of its member metrics' oriented, shrunk z-scores (reference-SD units). The "
    "member metrics are shown alongside every index. This project does not model "
    "game winners, scores, or spreads."
)
_SOURCE_TABLES = (
    "Source tables: `outputs/rankings/team_rankings_weekly.csv`, "
    "`outputs/team_strength/team_metrics_weekly.parquet`, "
    "`outputs/weekly/weekly_metric_detail.csv`."
)
_PROFILE_INTRO = (
    "Every profile shows the domain indices AND the underlying per-metric numbers "
    "(raw value, league reference mean/SD, sample size, shrunk value, percentile, "
    "confidence). Full detail: `outputs/team_strength/team_metrics_weekly.parquet`."
)
_PRESEASON_NOTE = (
    "No games have been played yet. The tables below are the **preseason "
    "baseline**: each team's prior full regular season, shrunk toward the 3-season "
    "league reference. They update automatically once Week 1 completes."
)
_FACTOR_INTRO = (
    "From `outputs/research/factor_summary.csv`. **association** = same-season "
    "descriptive correlation; **chronological** = walk-forward (metric now -> "
    "outcome over next 4 games), with a cluster-bootstrap 95% CI; **stability** = "
    "sign-consistency of the association across 10 seasons. A large correlation "
    "alone is not called 'important'. Factors in a group are redundant -- treat "
    "each group as one line of evidence."
)
_CAVEATS = [
    "- Indices are relative to a 3-season league reference, not absolute quality.",
    ("- Early-season indices are shrunk heavily toward the reference and flagged "
     "low/medium confidence; treat Week 1-4 movement cautiously."),
    "- `association` correlations are descriptive -- not causal and not predictive.",
    ("- The Phase 5 matchup-interaction experiment found no reliable incremental "
     "signal; any matchup comparisons here are descriptive only."),
]


def _fmt(x, nd=3) -> str:
    if x is None:
        return "—"
    try:
        if isinstance(x, float) and math.isnan(x):
            return "—"
        return f"{x:.{nd}f}" if isinstance(x, float) else str(x)
    except (TypeError, ValueError):
        return str(x)


def _table(df: pl.DataFrame, cols: list[str], *, nd: int = 3, limit: int | None = None) -> str:
    df = df.select([c for c in cols if c in df.columns])
    if limit:
        df = df.head(limit)
    head = "| " + " | ".join(df.columns) + " |"
    sep = "| " + " | ".join("---" for _ in df.columns) + " |"
    lines = [head, sep]
    for row in df.iter_rows(named=True):
        lines.append("| " + " | ".join(_fmt(row[c], nd) for c in df.columns) + " |")
    return "\n".join(lines)


def write_league_overview(
    domains: pl.DataFrame, team_snapshot: pl.DataFrame, meta: dict
) -> str:
    s, w = meta["season"], meta["through_week"]
    when = "preseason baseline (no games played)" if w == 0 else f"through Week {w}"
    parts = [
        f"# League Overview — {s} ({when})",
        "",
        _DISCLAIMER,
        "",
        f"Generated {meta['generated_at']}. {_SOURCE_TABLES}",
        "",
        "## Index construction",
        "```",
        index_formula_text(),
        "```",
        "",
    ]
    for dom, spec in DOMAINS.items():
        d = domains.filter(pl.col("domain") == dom).sort("rank_of_league")
        if d.is_empty():
            continue
        parts.append(f"## {spec['label']} (`{dom}`)")
        parts.append(f"Member metrics: {', '.join('`' + m + '`' for m in spec['metrics'])}")
        parts.append("")
        parts.append(_table(
            d.with_columns(pl.col("rank_of_league").alias("rank")),
            ["rank", "team", "index_value", "delta_vs_prev_week", "delta_vs_preseason",
             "n_metrics_used", "min_confidence"],
        ))
        parts.append("")
    if not team_snapshot.is_empty() and w > 0:
        parts.append("## Results context")
        parts.append(_table(
            team_snapshot.sort("point_diff", descending=True, nulls_last=True),
            ["team", "wins", "losses", "ties", "points_for", "points_against", "point_diff",
             "offense_overall_index", "defense_overall_index"], nd=2,
        ))
    body = "\n".join(parts) + "\n"
    (REPORTS / "league_overview.md").write_text(body)
    return body


def write_team_profiles(
    team_snapshot: pl.DataFrame, metric_detail: pl.DataFrame,
    domain_changes: pl.DataFrame, meta: dict
) -> str:
    s, w = meta["season"], meta["through_week"]
    when = "preseason baseline" if w == 0 else f"through Week {w}"
    parts = [
        f"# Team Profiles — {s} ({when})",
        "",
        _DISCLAIMER,
        "",
        _PROFILE_INTRO,
        "",
    ]
    teams = sorted(team_snapshot.get_column("team").to_list()) if not team_snapshot.is_empty() else []
    for team in teams:
        ts = team_snapshot.filter(pl.col("team") == team).to_dicts()[0]
        parts.append(f"## {team}")
        rec = (f"{ts.get('wins') or 0}-{ts.get('losses') or 0}-{ts.get('ties') or 0}"
               if w > 0 else "no games yet")
        parts.append(
            f"Record: {rec} · Points for/against: "
            f"{_fmt(ts.get('points_for'), 0)}/{_fmt(ts.get('points_against'), 0)} · "
            f"Point differential: {_fmt(ts.get('point_diff'), 0)} · "
            f"Data confidence: {ts.get('overall_confidence')}"
        )
        parts.append(
            f"Strongest area: **{ts.get('top_strength_domain')}** "
            f"({_fmt(ts.get('top_strength_index'))}) · "
            f"Weakest area: **{ts.get('top_weakness_domain')}** "
            f"({_fmt(ts.get('top_weakness_index'))})"
        )
        parts.append("")
        dc = domain_changes.filter(pl.col("team") == team).sort(["side", "domain"])
        parts.append("### Domain indices")
        parts.append(_table(dc, [
            "domain", "label", "index_value", "rank_of_league", "delta_vs_prev_week",
            "delta_vs_preseason", "min_confidence",
        ]))
        parts.append("")
        parts.append("### Underlying metrics")
        md = metric_detail.filter(pl.col("team") == team).sort(["family", "metric"])
        parts.append(_table(md, [
            "metric", "raw_value", "ref_mean", "ref_sd", "n_games", "n_opportunities",
            "shrunk_value", "z_shrunk", "oriented_z_shrunk", "rank_of_league", "percentile",
            "confidence", "phase3_status", "delta_shrunk_vs_prev_week",
        ], nd=4))
        parts.append("")
    body = "\n".join(parts) + "\n"
    (REPORTS / "team_profiles.md").write_text(body)
    return body


def write_weekly_research(payload: dict) -> str:
    m = payload["meta"]
    s, w = m["season"], m["through_week"]
    parts = [
        f"# Weekly Research — {s} Week {w}" if w > 0 else f"# Weekly Research — {s} (preseason)",
        "",
        _DISCLAIMER,
        "",
        f"Generated {m['generated_at']}. "
        f"Latest completed regular-season week detected: **{w}**"
        + ("" if w > 0 else " — running in preseason-baseline mode.")
        + "\n",
    ]
    if w == 0:
        parts += [_PRESEASON_NOTE, ""]
    for side in ("offense", "defense"):
        mv = payload["movers"][side]
        parts.append(f"## Biggest {side} movers (week over week)")
        if not mv["risers"] and not mv["fallers"]:
            parts.append("_No previous week to compare against yet._\n")
            continue
        parts.append("**Risers**")
        parts.append(_table(pl.DataFrame(mv["risers"]) if mv["risers"] else pl.DataFrame(),
                            ["team", "index_value", "delta_vs_prev_week", "rank_of_league",
                             "rank_change_vs_prev_week"]))
        parts.append("\n**Fallers**")
        parts.append(_table(pl.DataFrame(mv["fallers"]) if mv["fallers"] else pl.DataFrame(),
                            ["team", "index_value", "delta_vs_prev_week", "rank_of_league",
                             "rank_change_vs_prev_week"]))
        parts.append("")

    parts.append("## Biggest metric changes vs preseason baseline")
    bm = payload.get("metric_movers", [])
    parts.append(_table(pl.DataFrame(bm) if bm else pl.DataFrame(),
                        ["team", "metric", "shrunk_value", "delta_shrunk_vs_preseason",
                         "percentile", "confidence"], nd=4))
    parts.append("")

    parts.append("## Which factors have the strongest evidence (historical, 2016-2025)")
    parts.append(_FACTOR_INTRO)
    for label, key in (("Scoring (points scored)", "scoring"),
                       ("Points prevention (points allowed)", "points_allowed"),
                       ("Winning", "winning")):
        rows = payload["research"].get(key, [])
        parts.append(f"\n### {label} — group leaders")
        parts.append(_table(pl.DataFrame(rows) if rows else pl.DataFrame(),
                            ["group", "factor", "association_pearson", "chronological_pearson",
                             "chronological_pearson_ci_lo", "chronological_pearson_ci_hi",
                             "stability_frac_same_sign", "evidence_tier"]))
    parts.append("")
    parts.append("## Caveats")
    parts += [*_CAVEATS, ""]
    body = "\n".join(parts) + "\n"
    (REPORTS / "weekly_research.md").write_text(body)
    return body
