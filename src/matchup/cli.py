"""Phase 1 CLI.

    python -m matchup.cli ingest [--no-live-probe]
    python -m matchup.cli calendar [--seasons 2024]
    python -m matchup.cli crosswalk
    python -m matchup.cli validate-injuries
    python -m matchup.cli team-state --team KC --season 2024 --week 7
    python -m matchup.cli data-dictionary
    python -m matchup.cli phase1-report
"""
from __future__ import annotations

import argparse
import json

import polars as pl


def _cmd_ingest(args: argparse.Namespace) -> None:
    from matchup.ingest import ingest_all

    res = ingest_all(include_live_probe=not args.no_live_probe)
    for s, r in res.items():
        print(f"{s:16s} written={r.partitions_written} "
              f"unavailable={r.partitions_unavailable} rows={r.total_rows} errors={r.errors}")


def _cmd_calendar(args: argparse.Namespace) -> None:
    from matchup.pointintime.calendar import build_game_calendar

    cal = build_game_calendar(args.seasons or None)
    if args.seasons:
        cal = cal.filter(pl.col("season").is_in(args.seasons))
    with pl.Config(tbl_rows=30, tbl_cols=-1):
        print(cal.head(30))
    print(f"\n{cal.height} games; kickoff_time_estimated={cal.get_column('kickoff_time_estimated').sum()}")


def _cmd_crosswalk(_: argparse.Namespace) -> None:
    from matchup.config import REPO_ROOT
    from matchup.ids.crosswalk import crosswalk_coverage_report

    rep = crosswalk_coverage_report()
    out = REPO_ROOT / "outputs" / "phase1" / "id_crosswalk_coverage.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    rep.write_csv(out)
    over = rep.filter(pl.col("unmatched_share") > 0.03)
    print(f"wrote {out}")
    print(f"unit-seasons over 3% unmatched: {over.height}")
    if over.height:
        print(over)


def _cmd_validate_injuries(_: argparse.Namespace) -> None:
    from matchup.injuries.validation import run_validation

    s = run_validation()
    print(json.dumps({k: v for k, v in s.items()
                      if k not in ("false_inclusion_examples", "cutoff_staleness_examples",
                                   "per_season")},
                     indent=2, default=str))
    print("PASS" if s["passes_acceptance"] else "FAIL — acceptance criterion not met")


def _cmd_team_state(args: argparse.Namespace) -> None:
    from matchup.pointintime.asof import team_state_asof

    st = team_state_asof(args.team, args.season, args.week, mode=args.mode)
    print(f"target {st['target_game_id']} kickoff {st['target_kickoff_utc']}")
    for k, v in st.items():
        if isinstance(v, pl.DataFrame):
            da = v.get_column("data_asof").max() if "data_asof" in v.columns and v.height else "-"
            print(f"  {k:16s} rows={v.height:>7}  max(data_asof)={da}")


def _cmd_data_dictionary(_: argparse.Namespace) -> None:
    from matchup.reporting import write_data_dictionary

    p = write_data_dictionary()
    print(f"wrote {p}")


def _cmd_phase2_diagnostics(_: argparse.Namespace) -> None:
    from matchup.config import REPO_ROOT
    from matchup.diagnostics import build_redundancy_report, build_reliability_report
    from matchup.metrics.registry import coverage_table, registered_metrics

    out = REPO_ROOT / "outputs" / "phase2"
    out.mkdir(parents=True, exist_ok=True)
    registered_metrics().write_csv(out / "metric_registry.csv")
    coverage_table().write_csv(out / "metric_coverage.csv")
    build_reliability_report().write_csv(out / "metric_reliability.csv")
    build_redundancy_report().write_csv(out / "metric_redundancy.csv")
    print(f"wrote metric_registry / metric_coverage / metric_reliability / metric_redundancy to {out}")


def _cmd_phase3(args: argparse.Namespace) -> None:
    from matchup.validation import run_phase3

    print(json.dumps(run_phase3(bootstrap_iters=args.bootstrap_iters), indent=2, default=str))


def _cmd_phase4(args: argparse.Namespace) -> None:
    from matchup.validation.phase4 import run_phase4

    print(json.dumps(run_phase4(bootstrap_iters=args.bootstrap_iters), indent=2, default=str))


def _cmd_phase4_audit(args: argparse.Namespace) -> None:
    from matchup.validation.phase4_audit import run_audit

    print(json.dumps(run_audit(bootstrap_iters=args.bootstrap_iters), indent=2, default=str))


def _cmd_phase5(args: argparse.Namespace) -> None:
    from matchup.validation.phase5 import run_phase5

    print(json.dumps(run_phase5(bootstrap_iters=args.bootstrap_iters), indent=2, default=str))


def _cmd_team_strength(args: argparse.Namespace) -> None:
    from matchup.weekly.run import run_team_strength_panels

    seasons = list(range(args.start, args.end + 1)) if args.start and args.end else None
    print(json.dumps(run_team_strength_panels(seasons), indent=2, default=str))


def _cmd_factor_analysis(_: argparse.Namespace) -> None:
    from matchup.research.factors import run_factor_analysis

    print(json.dumps(run_factor_analysis(), indent=2, default=str))


def _cmd_weekly_research(args: argparse.Namespace) -> None:
    from matchup.weekly.run import run_weekly_research

    out = run_weekly_research(
        season=args.season, through_week=args.week,
        refresh_research=not args.no_refresh_research, ingest=args.ingest,
    )
    print(json.dumps(out, indent=2, default=str))


def _cmd_metric(args: argparse.Namespace) -> None:
    from matchup.metrics.build import game_metrics_from_asof, offline_provider
    from matchup.metrics.windows import WINDOWS, window_metric
    from matchup.normalize.normalize import normalize_windowed
    from matchup.pointintime.asof import AsOf
    from matchup.pointintime.calendar import build_game_calendar

    cal = build_game_calendar()
    row = cal.filter(
        (pl.col("season") == args.season) & (pl.col("week") == args.week)
        & ((pl.col("home_team") == args.team) | (pl.col("away_team") == args.team))
    )
    kick = row.get_column("kickoff_utc").item()
    gm = game_metrics_from_asof(AsOf(asof_utc=kick), args.family)
    for w in WINDOWS:
        r = window_metric(args.family, gm, entity_id=args.entity, target_season=args.season,
                          target_week=args.week, target_kickoff=kick, window=w)
        if r.is_empty():
            print(f"{w}: (no games)")
            continue
        if args.normalize_metric:
            r = normalize_windowed(r, args.family, args.normalize_metric, asof_utc=kick,
                                   ref_game_metrics_provider=offline_provider(args.family))
        print(f"\n== {w} ==")
        for k, v in r.to_dicts()[0].items():
            print(f"  {k}: {v}")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="matchup")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("ingest")
    s.add_argument("--no-live-probe", action="store_true")
    s.set_defaults(func=_cmd_ingest)

    s = sub.add_parser("calendar")
    s.add_argument("--seasons", type=int, nargs="*")
    s.set_defaults(func=_cmd_calendar)

    s = sub.add_parser("crosswalk")
    s.set_defaults(func=_cmd_crosswalk)

    s = sub.add_parser("validate-injuries")
    s.set_defaults(func=_cmd_validate_injuries)

    s = sub.add_parser("team-state")
    s.add_argument("--team", required=True)
    s.add_argument("--season", type=int, required=True)
    s.add_argument("--week", type=int, required=True)
    s.add_argument("--mode", default="backtest", choices=["backtest", "live"])
    s.set_defaults(func=_cmd_team_state)

    s = sub.add_parser("data-dictionary")
    s.set_defaults(func=_cmd_data_dictionary)

    s = sub.add_parser("phase2-diagnostics", help="regenerate outputs/phase2/*.csv")
    s.set_defaults(func=_cmd_phase2_diagnostics)

    s = sub.add_parser("phase3", help="run the persistence validation study -> outputs/phase3/")
    s.add_argument("--bootstrap-iters", type=int, default=1000)
    s.set_defaults(func=_cmd_phase3)

    s = sub.add_parser("phase4", help="run the shrinkage & opponent-adjustment study -> outputs/phase4/")
    s.add_argument("--bootstrap-iters", type=int, default=1000)
    s.set_defaults(func=_cmd_phase4)

    s = sub.add_parser("phase4-audit", help="Phase 4.1 audit -> outputs/phase4/audit_*.csv")
    s.add_argument("--bootstrap-iters", type=int, default=400)
    s.set_defaults(func=_cmd_phase4_audit)

    s = sub.add_parser("phase5", help="run the matchup-interaction validation study -> outputs/phase5/")
    s.add_argument("--bootstrap-iters", type=int, default=1000)
    s.set_defaults(func=_cmd_phase5)

    s = sub.add_parser("team-strength", help="build team-strength panels -> outputs/team_strength/")
    s.add_argument("--start", type=int, default=None)
    s.add_argument("--end", type=int, default=None)
    s.set_defaults(func=_cmd_team_strength)

    s = sub.add_parser("factor-analysis", help="run the factor research -> outputs/research/")
    s.set_defaults(func=_cmd_factor_analysis)

    s = sub.add_parser("weekly-research", help="the weekly 2026 workflow -> outputs/ + reports/")
    s.add_argument("--season", type=int, default=None)
    s.add_argument("--week", type=int, default=None, help="through-week override; default = latest completed")
    s.add_argument("--no-refresh-research", action="store_true", help="reuse cached factor research")
    s.add_argument("--ingest", action="store_true", help="run the nflverse ingest/live-probe first")
    s.set_defaults(func=_cmd_weekly_research)

    s = sub.add_parser("metric", help="print windowed (+optionally normalized) metric for one entity")
    s.add_argument("--family", required=True)
    s.add_argument("--entity", required=True, help="gsis_id or team abbr")
    s.add_argument("--team", required=True, help="team whose game defines the target kickoff")
    s.add_argument("--season", type=int, required=True)
    s.add_argument("--week", type=int, required=True)
    s.add_argument("--normalize-metric", default=None)
    s.set_defaults(func=_cmd_metric)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
