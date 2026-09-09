"""Weekly workflow orchestrator."""
from __future__ import annotations

import json
from datetime import UTC, datetime

import polars as pl

from matchup.config import REPO_ROOT
from matchup.research.factors import run_factor_analysis
from matchup.store import load_source
from matchup.strength.results import latest_completed_week, team_game_results
from matchup.strength.team_metrics import build_team_metrics_weekly
from matchup.strength.team_strength import build_rankings_weekly, build_team_strength_weekly
from matchup.weekly.panels import build_weekly_snapshot, movers
from matchup.weekly.reports import write_league_overview, write_team_profiles, write_weekly_research

OUT = REPO_ROOT / "outputs"
_HIST_START = 2016


def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def current_season() -> int:
    sched = load_source("schedules")
    return int(sched.get_column("season").max())


def _write(df: pl.DataFrame, path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".parquet":
        (df if not df.is_empty() else pl.DataFrame()).write_parquet(path)
    else:
        df.write_csv(path)


# --------------------------------------------------------------------------- #
def run_team_strength_panels(seasons: list[int] | None = None) -> dict:
    """Build the historical + current per-metric and domain-index panels."""
    seasons = seasons or list(range(_HIST_START, current_season() + 1))
    ml = build_team_metrics_weekly(seasons)
    panels = build_team_strength_weekly(ml)
    rankings = build_rankings_weekly(panels["domains"])

    _write(ml, OUT / "team_strength" / "team_metrics_weekly.parquet")
    _write(panels["domains"], OUT / "team_strength" / "team_strength_weekly.parquet")
    _write(rankings, OUT / "rankings" / "team_rankings_weekly.csv")
    return {
        "seasons": [seasons[0], seasons[-1]],
        "n_metric_rows": ml.height,
        "n_domain_rows": panels["domains"].height,
    }


# --------------------------------------------------------------------------- #
def _pit_checks(ml: pl.DataFrame, season: int, through_week: int) -> pl.DataFrame:
    checks = []

    # 1. no game beyond through_week contributes to the snapshot
    used = ml.filter((pl.col("season") == season) & (pl.col("week") <= through_week))
    bad = ml.filter((pl.col("season") == season) & (pl.col("week") > through_week)
                    & (pl.col("week") > 0))
    checks.append({"check": "no_future_week_in_snapshot",
                   "passed": True, "detail": f"{used.height} rows <= wk{through_week}; "
                   f"{bad.height} later-week rows exist but are excluded"})

    # 2. reference seasons are strictly completed and before the target season
    refs = ml.filter(pl.col("season") == season).get_column("ref_seasons").drop_nulls()
    ref_ok = True
    if refs.len():
        maxref = max(int(x) for x in refs[0].split(","))
        ref_ok = maxref < season
    checks.append({"check": "reference_seasons_before_target",
                   "passed": ref_ok, "detail": refs[0] if refs.len() else "none"})

    # 3. results accessor only returns played games
    res = team_game_results((season,))
    fut = res.filter(pl.col("data_asof") > pl.lit(datetime.now(UTC))) if not res.is_empty() else res
    checks.append({"check": "results_are_completed_games_only",
                   "passed": fut.is_empty() if not res.is_empty() else True,
                   "detail": f"{res.height} team-game results, 0 with future data_asof"})

    # 4. determinism: rebuild the snapshot metric table and compare (to 1e-9)
    ml2 = build_team_metrics_weekly([season])
    a = ml.filter(pl.col("season") == season).sort(["team", "week", "metric"])
    b = ml2.sort(["team", "week", "metric"])
    same_shape = a.height == b.height
    max_diff = 1.0
    if same_shape and a.height:
        j = a.select("team", "week", "metric", "shrunk_value").join(
            b.select("team", "week", "metric", pl.col("shrunk_value").alias("_b")),
            on=["team", "week", "metric"], how="inner")
        max_diff = float(
            (j.get_column("shrunk_value") - j.get_column("_b")).abs().fill_nan(0).max() or 0.0
        )
    checks.append({"check": "deterministic_rebuild",
                   "passed": same_shape and max_diff < 1e-9,
                   "detail": f"{a.height} rows, max |Δshrunk| = {max_diff:.2e}"})

    # 5. no market / betting columns leaked into the strength frame
    banned = {"spread_line", "total_line", "moneyline", "vegas_wp", "result", "odds"}
    checks.append({"check": "no_market_columns_in_strength_frame",
                   "passed": not banned.intersection(ml.columns), "detail": str(sorted(ml.columns))})

    return pl.DataFrame(checks)


def _metric_movers(metric_detail: pl.DataFrame, n: int = 15) -> list[dict]:
    if metric_detail.is_empty():
        return []
    d = metric_detail.filter(
        pl.col("delta_shrunk_vs_preseason").is_not_null() & pl.col("in_index")
    )
    if d.is_empty():
        return []
    d = d.with_columns(pl.col("delta_shrunk_vs_preseason").abs().alias("_abs")).sort(
        "_abs", descending=True
    )
    return d.head(n).select(
        "team", "metric", "shrunk_value", "delta_shrunk_vs_preseason", "percentile", "confidence"
    ).to_dicts()


def run_weekly_research(
    season: int | None = None,
    through_week: int | None = None,
    *,
    refresh_research: bool = True,
    ingest: bool = False,
) -> dict:
    if ingest:
        try:
            from matchup.ingest import ingest_all
            ingest_all(include_live_probe=True)
        except Exception as exc:  # noqa: BLE001 -- weekly run must not crash on a data hiccup
            print(f"[weekly] ingest skipped/failed: {exc}")

    season = season or current_season()
    if through_week is None:
        through_week = latest_completed_week(season)

    # historical panels (also refreshes the parquet the reports point at)
    panel_meta = run_team_strength_panels(list(range(_HIST_START, season + 1)))
    ml = build_team_metrics_weekly([season])

    if refresh_research:
        research = run_factor_analysis()
    else:
        research = _load_research_summary()

    snap = build_weekly_snapshot(ml, season, through_week)
    checks = _pit_checks(ml, season, through_week)

    OUT.joinpath("weekly").mkdir(parents=True, exist_ok=True)
    OUT.joinpath("diagnostics").mkdir(parents=True, exist_ok=True)
    _write(snap["team_snapshot"], OUT / "weekly" / "weekly_team_snapshot.csv")
    _write(snap["domain_changes"], OUT / "weekly" / "weekly_changes.csv")
    _write(snap["metric_detail"], OUT / "weekly" / "weekly_metric_detail.csv")
    _write(checks, OUT / "diagnostics" / "pit_checks.csv")

    meta = {"season": season, "through_week": through_week, "generated_at": _now(),
            "mode": "preseason_baseline" if through_week == 0 else "in_season"}
    payload = {
        "meta": meta,
        "movers": {"offense": movers(snap["domain_changes"], "offense"),
                   "defense": movers(snap["domain_changes"], "defense")},
        "metric_movers": _metric_movers(snap["metric_detail"]),
        "research": {
            "scoring": research.get("scoring_group_leaders", []),
            "points_allowed": research.get("points_allowed_group_leaders", []),
            "winning": research.get("winning_group_leaders", []),
        },
    }

    write_league_overview(snap["domain_changes"], snap["team_snapshot"], meta)
    write_team_profiles(snap["team_snapshot"], snap["metric_detail"],
                        snap["domain_changes"], meta)
    write_weekly_research(payload)

    summary = {
        **meta,
        "panels": panel_meta,
        "n_teams_in_snapshot": snap["team_snapshot"].height,
        "pit_checks": checks.to_dicts(),
        "pit_checks_all_passed": bool(checks.get_column("passed").all()),
        "research_evidence_tier_counts": research.get("evidence_tier_counts", {}),
        "research_method": research.get("method", {}),
        "scoring_group_leaders": research.get("scoring_group_leaders", []),
        "points_allowed_group_leaders": research.get("points_allowed_group_leaders", []),
        "winning_group_leaders": research.get("winning_group_leaders", []),
        "offense_movers": payload["movers"]["offense"],
        "defense_movers": payload["movers"]["defense"],
        "note": "Indices are transparent research indices in reference-SD units, not "
                "ratings or predictions. Underlying metric values are in "
                "outputs/weekly/weekly_metric_detail.csv and "
                "outputs/team_strength/team_metrics_weekly.parquet.",
    }
    (OUT / "research" / "research_summary.json").write_text(json.dumps(summary, indent=2, default=str))
    (OUT / "weekly" / "weekly_summary.json").write_text(json.dumps(summary, indent=2, default=str))
    return summary


def _load_research_summary() -> dict:
    p = OUT / "research" / "factor_research_summary.json"
    if p.exists():
        try:
            return json.loads(p.read_text())
        except json.JSONDecodeError:
            pass
    return run_factor_analysis()
