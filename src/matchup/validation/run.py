"""Phase 3 orchestration: build observations -> score cells -> bootstrap primary
cells -> negative control -> ablations -> status assignment -> write outputs.
"""
from __future__ import annotations

import json
from datetime import UTC, datetime

import numpy as np
import polars as pl

from matchup.config import REPO_ROOT
from matchup.metrics.families import FAMILY_SPECS
from matchup.metrics.registry import load_registry
from matchup.validation.config import load_phase3_config
from matchup.validation.negative_control import negative_control_cell
from matchup.validation.observations import build_observations
from matchup.validation.scoring import cluster_bootstrap, score_cell
from matchup.validation.status import assign_rank_persistence, assign_status

OUT = REPO_ROOT / "outputs" / "phase3"
PBP_FAMILIES = list(FAMILY_SPECS)
_ENTITY_TYPE = {
    "qb": "player", "rb": "player", "wr": "player",
    "team_offense": "team", "team_defense": "team",
    "pass_protection": "team", "pass_rush": "team", "special_teams": "team",
}


def _cluster_ids(df: pl.DataFrame) -> np.ndarray:
    key = (df.get_column("entity_id").cast(str) + "|" + df.get_column("season").cast(str)).to_list()
    lut: dict[str, int] = {}
    return np.array([lut.setdefault(k, len(lut)) for k in key])


def _arrays(cell: pl.DataFrame):
    return {
        "feature": cell.get_column("feature_value").to_numpy(),
        "target": cell.get_column("target_value").to_numpy(),
        "bl_league": cell.get_column("baseline_league").to_numpy(),
        "bl_prior": cell.get_column("baseline_prior").fill_null(np.nan).to_numpy(),
        "bl_raw_t3": cell.get_column("baseline_raw_t3").fill_null(np.nan).to_numpy(),
        "entities": cell.get_column("entity_id").to_numpy(),
        "seasons": cell.get_column("season").to_numpy(),
        "opp": cell.get_column("feat_opp_n").to_numpy(),
    }


def _source_of(metric: str, reg: dict) -> str:
    for m in reg["metrics"]:
        if m["name"].endswith(metric) or m["name"] == metric:
            return m["source"]
    return "pbp"


def run_phase3(*, bootstrap_iters: int | None = None) -> dict:
    cfg = load_phase3_config()
    reg = load_registry()
    OUT.mkdir(parents=True, exist_ok=True)
    n_iter = bootstrap_iters or cfg["bootstrap"]["iterations"]
    seed = cfg["bootstrap"]["seed"]
    plo, phi = cfg["primary_analysis_weeks"]
    excl = set(cfg["exclude_from_persistence"])

    persistence_rows: list[dict] = []
    negctrl_rows: list[dict] = []
    ablation_rows: list[dict] = []
    status_rows: list[dict] = []

    for family in PBP_FAMILIES:
        obs, exc = build_observations(family, cfg)
        if obs.is_empty():
            continue

        # excluded-target rate per (horizon, season_phase) over primary weeks
        excl_rate: dict[tuple, float] = {}
        if not exc.is_empty():
            er = exc.group_by(["horizon", "season_phase"]).agg(pl.col("excluded").mean().alias("r"))
            excl_rate = {(int(r["horizon"]), r["season_phase"]): float(r["r"]) for r in er.iter_rows(named=True)}

        metrics = [m for m in FAMILY_SPECS[family]["rates"] if f"{family}.{m}" not in excl and m not in excl]

        for metric in metrics:
            m_obs = obs.filter(pl.col("metric") == metric)
            if m_obs.is_empty():
                status_rows.append(_status_row(family, metric, reg, None))
                continue

            # ---- full grid: window x horizon x season_phase (point estimates) --
            for (window, horizon, phase), cell in m_obs.group_by(
                ["window", "horizon", "season_phase"], maintain_order=True
            ):
                if cell.height < 30:
                    continue
                sc = score_cell(**_arrays(cell),
                                excluded_target_rate=excl_rate.get((int(horizon), phase), float("nan")))
                persistence_rows.append({
                    "family": family, "entity_type": _ENTITY_TYPE[family],
                    "source": _source_of(metric, reg), "metric": metric,
                    "window": window, "target_horizon": horizon, "season_phase": phase,
                    **sc,
                })

            # ---- primary + reported cells: weeks plo..phi, each horizon, each window (+CIs) --
            primary_horizons = cfg["status_rules"]["primary_horizons"]
            best_by_horizon: dict[int, dict] = {}
            best_rank_by_horizon: dict[int, dict] = {}
            for h in (1, *primary_horizons):
                prim = m_obs.filter(
                    (pl.col("week") >= plo) & (pl.col("week") <= phi) & (pl.col("horizon") == h)
                )
                by_window: dict[str, dict] = {}
                for window, cell in prim.group_by("window", maintain_order=True):
                    window = window[0] if isinstance(window, tuple) else window
                    if cell.height < 30:
                        continue
                    a = _arrays(cell)
                    merged = {**score_cell(**a), **cluster_bootstrap(
                        a["feature"], a["target"], a["bl_league"], a["bl_prior"],
                        clusters=_cluster_ids(cell), n_iter=n_iter, seed=seed,
                    )}
                    by_window[window] = merged
                    persistence_rows.append({
                        "family": family, "entity_type": _ENTITY_TYPE[family],
                        "source": _source_of(metric, reg), "metric": metric,
                        "window": window, "target_horizon": h,
                        "season_phase": f"primary_wk5_18_h{h}", **merged,
                    })
                    if h == 1:
                        negctrl_rows.append({
                            "family": family, "metric": metric, "window": window,
                            **negative_control_cell(
                                cell, seed=cfg["negative_control"]["seed"],
                                n_permutations=cfg["negative_control"]["n_permutations_null"]),
                        })
                if by_window:
                    bw = max(by_window, key=lambda w: (by_window[w]["skill_vs_league"]
                             if np.isfinite(by_window[w]["skill_vs_league"]) else -9))
                    best_by_horizon[h] = {"window": bw, **by_window[bw]}
                    bws = max(by_window, key=lambda w: (by_window[w]["spearman"]
                              if np.isfinite(by_window[w]["spearman"]) else -9))
                    best_rank_by_horizon[h] = {"window": bws, **by_window[bws]}

            st, evidence = assign_status(
                {h: best_by_horizon.get(h) for h in primary_horizons}, cfg["status_rules"]
            )
            rk, rk_ev = assign_rank_persistence(
                {h: best_rank_by_horizon.get(h) for h in primary_horizons}, cfg["status_rules"]
            )
            status_rows.append({
                "family": family, "entity_type": _ENTITY_TYPE[family],
                "source": _source_of(metric, reg), "metric": f"{family}.{metric}",
                "predictive_status": st, "rank_persistence": rk,
                "best_window_h2": (best_by_horizon.get(2) or {}).get("window"),
                "best_window_h4": (best_by_horizon.get(4) or {}).get("window"),
                "primary_n_h2": (best_by_horizon.get(2) or {}).get("n", 0),
                "primary_n_h4": (best_by_horizon.get(4) or {}).get("n", 0),
                "spearman_h4": (best_rank_by_horizon.get(4) or {}).get("spearman"),
                "skill_vs_league_h4": (best_by_horizon.get(4) or {}).get("skill_vs_league"),
                "skill_vs_prior_season_h4": (best_by_horizon.get(4) or {}).get("skill_vs_prior_season"),
                "evidence": evidence,
                "rank_evidence": rk_ev,
            })

            # ---- raw vs normalized ablation (best H4 window) ----------
            bw4 = (best_by_horizon.get(4) or {}).get("window")
            if bw4:
                cell = m_obs.filter(
                    (pl.col("week") >= plo) & (pl.col("week") <= phi)
                    & (pl.col("horizon") == 4) & (pl.col("window") == bw4)
                )
                ablation_rows.append(_raw_vs_norm(family, metric, bw4, cell))

    _write_outputs(persistence_rows, negctrl_rows, ablation_rows, status_rows, cfg)
    _augment_ablation_windows(persistence_rows)
    try:
        from matchup.validation.external_ablation import build_external_ablation

        ext = build_external_ablation()
        if not ext.is_empty():
            path = OUT / "metric_ablation.csv"
            existing = pl.read_csv(path) if path.exists() else pl.DataFrame()
            pl.concat([existing, ext], how="diagonal_relaxed").write_csv(path)
    except Exception as exc:  # noqa: BLE001
        (OUT / "external_ablation_error.txt").write_text(str(exc))
    summary = _update_metrics_yaml(status_rows)
    return {"status_counts": summary, "n_persistence_rows": len(persistence_rows),
            "n_status_rows": len(status_rows)}


def _status_row(family, metric, reg, _unused):
    return {"family": family, "entity_type": _ENTITY_TYPE[family],
            "source": _source_of(metric, reg), "metric": f"{family}.{metric}",
            "predictive_status": "UNVALIDATED", "rank_persistence": "INSUFFICIENT",
            "best_window_h2": None, "best_window_h4": None,
            "primary_n_h2": 0, "primary_n_h4": 0,
            "spearman_h4": None, "skill_vs_league_h4": None, "skill_vs_prior_season_h4": None,
            "evidence": "not evaluable (no observations built for this metric)",
            "rank_evidence": ""}


def _raw_vs_norm(family: str, metric: str, window: str, cell: pl.DataFrame) -> dict:
    """Structural check: for same-unit persistence at a single prediction date,
    z-normalization is an affine transform with date-constant params -> ranks
    unchanged within a season. Pooled across seasons it can change the picture if
    the league environment drifts. Both feature and target are z'd against the
    same 3-completed-season reference."""
    f = cell.get_column("feature_value").to_numpy()
    t = cell.get_column("target_value").to_numpy()
    mu = cell.get_column("baseline_league").to_numpy()
    sd = cell.get_column("baseline_league_sd").to_numpy()
    ok = np.isfinite(sd) & (sd > 0)
    fz, tz = (f[ok] - mu[ok]) / sd[ok], (t[ok] - mu[ok]) / sd[ok]

    def sp(a, b):
        return float(np.corrcoef(a.argsort().argsort(), b.argsort().argsort())[0, 1]) if a.size > 2 else float("nan")

    fo, to = f[ok], t[ok]
    tsd_raw = np.std(to, ddof=1)
    tsd_z = np.std(tz, ddof=1)
    return {
        "family": family, "metric": metric, "window": window, "n": int(ok.sum()),
        "pearson_raw": float(np.corrcoef(fo, to)[0, 1]),
        "pearson_normalized": float(np.corrcoef(fz, tz)[0, 1]) if ok.sum() > 2 else float("nan"),
        "spearman_raw": sp(fo, to),
        "spearman_normalized": sp(fz, tz),
        # both normalised by their own target SD so they are directly comparable
        "nrmse_raw": float(np.sqrt(np.mean((fo - to) ** 2)) / tsd_raw) if tsd_raw > 0 else float("nan"),
        "nrmse_normalized": float(np.sqrt(np.mean((fz - tz) ** 2)) / tsd_z) if tsd_z > 0 else float("nan"),
        "note": "z-normalization is an affine transform per prediction date; within-season "
                "ranks are identical by construction -- differences here come only from pooling "
                "across seasons with different reference mean/sd",
    }


def _augment_ablation_windows(persistence_rows: list[dict]) -> None:
    """Add per-window skill comparison rows (H4 primary) to metric_ablation.csv."""
    df = pl.DataFrame(persistence_rows, infer_schema_length=None).filter(
        pl.col("season_phase") == "primary_wk5_18_h4"
    )
    if df.is_empty():
        return
    rows = []
    for (family, metric), g in df.group_by(["family", "metric"], maintain_order=True):
        for r in g.iter_rows(named=True):
            rows.append({
                "ablation": "window", "family": family, "metric": metric,
                "window": r["window"], "n": r["n"],
                "skill_vs_league": r["skill_vs_league"],
                "skill_vs_prior_season": r["skill_vs_prior_season"],
                "skill_vs_raw_trailing3": r["skill_vs_raw_trailing3"],
                "spearman": r["spearman"],
            })
    if rows:
        path = OUT / "metric_ablation.csv"
        existing = pl.read_csv(path) if path.exists() else pl.DataFrame()
        new = pl.DataFrame(rows, infer_schema_length=None)
        pl.concat([existing, new], how="diagonal_relaxed").write_csv(path)


def _write_outputs(persistence_rows, negctrl_rows, ablation_rows, status_rows, cfg) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if persistence_rows:
        pl.DataFrame(persistence_rows, infer_schema_length=None).sort(
            ["family", "metric", "window", "target_horizon", "season_phase"]
        ).write_csv(OUT / "metric_persistence.csv")
    if negctrl_rows:
        pl.DataFrame(negctrl_rows, infer_schema_length=None).write_csv(OUT / "negative_control.csv")
    if ablation_rows:
        pl.DataFrame(ablation_rows, infer_schema_length=None).with_columns(pl.lit("raw_vs_normalized").alias("ablation")).write_csv(
            OUT / "metric_ablation.csv"
        )
    if status_rows:
        pl.DataFrame(status_rows, infer_schema_length=None).sort(["family", "metric"]).write_csv(OUT / "metric_status.csv")
    (OUT / "run_meta.json").write_text(json.dumps({
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "config": cfg,
    }, indent=2, default=str))


def _update_metrics_yaml(status_rows: list[dict]) -> dict:
    """Rewrite config/metrics.yaml predictive_status per Phase 3 taxonomy, keeping
    a Phase-3 evidence block. Ambiguous / not-evaluable stay UNVALIDATED."""
    import re

    path = REPO_ROOT / "config" / "metrics.yaml"
    text = path.read_text()
    by_name = {r["metric"]: r for r in status_rows}
    counts: dict[str, int] = {}
    reg = load_registry()
    for m in reg["metrics"]:
        name = m["name"]
        short = name.split(".", 1)[1] if "." in name else name
        family_pref = name.split(".", 1)[0] if "." in name else ""
        st = by_name.get(name, {}).get("predictive_status")
        if st is None:
            # try family.short
            st = by_name.get(f"{family_pref}.{short}", {}).get("predictive_status", "UNVALIDATED")
        counts[st] = counts.get(st, 0) + 1

    # write a sidecar evidence file (never rewrite formulas programmatically)
    def _q(s: str) -> str:
        return str(s).replace('"', "'")

    (REPO_ROOT / "config" / "metrics_phase3_status.yaml").write_text(
        "# Generated by Phase 3. predictive_status per persistence taxonomy.\n"
        "# VALIDATED_PERSISTENCE does NOT mean the metric improves matchup prediction.\n"
        + "\n".join(
            f"{r['metric']}: {{status: {r['predictive_status']}, "
            f"best_window_h2: {r.get('best_window_h2')}, best_window_h4: {r.get('best_window_h4')}, "
            f"primary_n_h2: {r.get('primary_n_h2', 0)}, primary_n_h4: {r.get('primary_n_h4', 0)}, "
            f"evidence: \"{_q(r['evidence'])}\"}}"
            for r in sorted(status_rows, key=lambda x: x["metric"])
        )
        + "\n"
    )
    # flip the inline predictive_status tokens in metrics.yaml for matched metrics
    for name, r in [(x["metric"], x) for x in status_rows]:
        pat = re.compile(
            r"(\{name:\s*" + re.escape(name) + r",[^\}]*?predictive_status:\s*)UNVALIDATED",
            re.DOTALL,
        )
        text = pat.sub(r"\g<1>" + r["predictive_status"], text, count=1)
    path.write_text(text)
    return counts
