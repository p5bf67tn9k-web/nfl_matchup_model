"""Phase 4 orchestration.

Stage A (shrinkage): does  shrunk = mu + n/(n+k)*(raw-mu)  beat the RAW feature
out of sample, with k chosen strictly walk-forward?

Stage B (opponent adjustment): after A, does a chronological ridge opponent
adjustment add incremental information?

The baseline chain (season_to_date window, primary weeks 5-18, horizons 2 & 4):
  league_mean -> prior_season -> raw_trailing3 -> raw -> shrunk -> oppadj_raw -> oppadj_shrunk
season_to_date is the a-priori "use all season-to-date data" window; other
windows are reported as sensitivity, not used for status.
"""
from __future__ import annotations

import json
from datetime import UTC, datetime

import numpy as np
import polars as pl

from matchup.config import REPO_ROOT
from matchup.metrics.families import FAMILY_SPECS
from matchup.opponent_adjustment import select_alpha, walk_forward_strengths
from matchup.shrinkage import apply_shrinkage_walkforward, shrink
from matchup.validation.config import load_phase3_config
from matchup.validation.observations import build_observations
from matchup.validation.phase4_config import load_phase4_config, resolve_candidates
from matchup.validation.scoring import cluster_bootstrap, score_cell

OUT = REPO_ROOT / "outputs" / "phase4"
_ENTITY_TYPE = {
    "qb": "player", "rb": "player", "wr": "player", "team_offense": "team",
    "team_defense": "team", "pass_protection": "team", "pass_rush": "team",
    "special_teams": "team",
}
_ANCHOR_WINDOW = "season_to_date"


def _phase4_obs_cfg(cfg4: dict) -> dict:
    c = json.loads(json.dumps(load_phase3_config()))  # deep copy
    c["seasons"]["eval_start"] = cfg4["observation_history"]["build_target_seasons"][0]
    c["seasons"]["eval_end"] = cfg4["observation_history"]["build_target_seasons"][1]
    c["seasons"]["history_available_from"] = cfg4["observation_history"]["game_metrics_from"]
    return c


def _cluster_ids(df: pl.DataFrame) -> np.ndarray:
    key = (df.get_column("entity_id").cast(str) + "|" + df.get_column("season").cast(str)).to_list()
    lut: dict[str, int] = {}
    return np.array([lut.setdefault(k, len(lut)) for k in key])


def _arrays(cell: pl.DataFrame, feature_col: str) -> dict:
    return {
        "feature": cell.get_column(feature_col).to_numpy(),
        "target": cell.get_column("target_value").to_numpy(),
        "bl_league": cell.get_column("baseline_league").to_numpy(),
        "bl_prior": cell.get_column("baseline_prior").fill_null(np.nan).to_numpy(),
        "bl_raw_t3": cell.get_column("baseline_raw_t3").fill_null(np.nan).to_numpy(),
        "entities": cell.get_column("entity_id").to_numpy(),
        "seasons": cell.get_column("season").to_numpy(),
        "opp": cell.get_column("feat_n_games").to_numpy().astype(float),
    }


def _skill(rmse_a: float, rmse_b: float) -> float:
    return 1 - rmse_a / rmse_b if rmse_b and rmse_b > 0 else float("nan")


def _score_variant(cell: pl.DataFrame, feature_col: str, ref_col: str, *,
                   n_iter: int, seed: int) -> dict:
    a = _arrays(cell, feature_col)
    base = score_cell(**a)
    ref = cell.get_column(ref_col).to_numpy()
    feat = a["feature"]
    tgt = a["target"]
    ok = np.isfinite(feat) & np.isfinite(ref) & np.isfinite(tgt)
    rmse_feat = float(np.sqrt(np.mean((feat[ok] - tgt[ok]) ** 2)))
    rmse_ref = float(np.sqrt(np.mean((ref[ok] - tgt[ok]) ** 2)))
    skill_vs_ref = _skill(rmse_feat, rmse_ref)
    # bootstrap the incremental skill vs the reference layer
    ci = cluster_bootstrap(feat[ok], tgt[ok], ref[ok], np.full(ok.sum(), np.nan),
                           clusters=_cluster_ids(cell.filter(pl.Series(ok))),
                           n_iter=n_iter, seed=seed)
    return {
        **base,
        "feature_col": feature_col, "reference_col": ref_col,
        "rmse_feature": rmse_feat, "rmse_reference": rmse_ref,
        "skill_vs_reference": skill_vs_ref,
        "skill_vs_reference_ci_lo": ci["skill_vs_league_ci_lo"],
        "skill_vs_reference_ci_hi": ci["skill_vs_league_ci_hi"],
    }


def _adds_value(h2: dict | None, h4: dict | None, rules: dict) -> tuple[str, str]:
    def verdict(c):
        if c is None:
            return "no_cell"
        if c["n"] < rules["insufficient_data_min_n"]:
            return "insufficient"
        s, lo = c["skill_vs_reference"], c["skill_vs_reference_ci_lo"]
        if lo is not None and np.isfinite(lo) and lo > 0 and s >= rules["economic_floor_skill"]:
            return "pass"
        if lo is not None and np.isfinite(lo) and (lo <= 0 or s < 0):
            return "fail"
        return "ambiguous"

    v2, v4 = verdict(h2), verdict(h4)
    ev = (f"H2: skill_vs_ref={_f(h2, 'skill_vs_reference')}[{_f(h2, 'skill_vs_reference_ci_lo')}] n={_f(h2, 'n')} | "
          f"H4: skill_vs_ref={_f(h4, 'skill_vs_reference')}[{_f(h4, 'skill_vs_reference_ci_lo')}] n={_f(h4, 'n')}")
    if v2 == "no_cell" and v4 == "no_cell":
        return "UNVALIDATED", "not evaluable"
    if {v2, v4} <= {"insufficient", "no_cell"}:
        return "INSUFFICIENT_DATA", ev
    if v2 == "pass" and v4 == "pass":
        return "ADDS_VALUE", ev
    if {v2, v4} <= {"fail", "insufficient", "no_cell"} and "fail" in (v2, v4):
        return "NO_INCREMENTAL_VALUE", ev
    return "UNVALIDATED", "ambiguous: " + ev


def _f(c, k):
    if not c or c.get(k) is None or (isinstance(c.get(k), float) and not np.isfinite(c[k])):
        return "na"
    v = c[k]
    return f"{v:.3f}" if isinstance(v, float) else str(v)


# --------------------------------------------------------------------------- #
def run_phase4(*, bootstrap_iters: int | None = None) -> dict:
    cfg4 = load_phase4_config()
    n_iter = bootstrap_iters or cfg4["inherits_from_phase3"] and 1000
    n_iter = bootstrap_iters or 1000
    seed = 20260908
    OUT.mkdir(parents=True, exist_ok=True)

    cand = resolve_candidates(cfg4)
    cand.write_csv(OUT / "candidate_universe.csv")

    obs_cfg = _phase4_obs_cfg(cfg4)
    oos = range(cfg4["oos_evaluation_seasons"][0], cfg4["oos_evaluation_seasons"][1] + 1)
    plo, phi = obs_cfg["primary_analysis_weeks"]
    prim_h = cfg4["status_taxonomy"] and obs_cfg["status_rules"]["primary_horizons"]
    k_grid = cfg4["shrinkage"]["k_grid"]

    shr_rows, chain_rows, status_rows, klog_all, alog_all = [], [], [], [], []
    oa_families = set(cfg4["opponent_adjustment"]["applicable_families"])

    by_family: dict[str, list[str]] = {}
    for r in cand.iter_rows(named=True):
        by_family.setdefault(r["family"], []).append(r["metric"].split(".", 1)[1]
                                                     if "." in r["metric"] else r["metric"])

    for family, metrics in by_family.items():
        if family not in FAMILY_SPECS:
            continue  # NGS handled separately
        obs, _ = build_observations(family, obs_cfg)
        obs = obs.filter(pl.col("metric").is_in(metrics))
        if obs.is_empty():
            continue

        # ---- Stage A: shrinkage --------------------------------------
        obs_s, klog = apply_shrinkage_walkforward(
            obs, k_grid=k_grid, fallback_k=cfg4["shrinkage"]["fallback_k"],
            min_train_obs=cfg4["shrinkage"]["fallback_when_train_obs_below"],
            oos_seasons=oos, primary_weeks=(plo, phi), primary_horizons=prim_h,
        )
        for e in klog:
            e["metric"] = f"{family}.{e['metric']}"
        klog_all.extend(klog)
        obs_s = obs_s.with_columns(pl.col("feature_value").alias("raw_feature"))

        # ---- Stage B: opponent adjustment --------------------------
        do_oa = family in oa_families
        if do_oa:
            obs_s = _attach_opponent_adjustment(
                obs_s, family, metrics, cfg4, oos, (plo, phi), alog_all,
            )

        # ---- score the chain + assign status ----------------------
        for metric in metrics:
            m = obs_s.filter((pl.col("metric") == metric) & (pl.col("window") == _ANCHOR_WINDOW)
                             & (pl.col("week") >= plo) & (pl.col("week") <= phi))
            if m.is_empty():
                continue
            per_h: dict[str, dict[int, dict]] = {"shrunk": {}, "oppadj_raw": {}, "oppadj_shrunk": {}}
            for h in prim_h:
                cell = m.filter(pl.col("horizon") == h)
                if cell.height < 30:
                    continue
                # full chain point estimates
                for col in ("baseline_league", "baseline_prior", "baseline_raw_t3",
                            "raw_feature", "shrunk_feature",
                            *(["oppadj_raw", "oppadj_shrunk"] if do_oa else [])):
                    if col not in cell.columns:
                        continue
                    cc = cell.filter(pl.col(col).is_finite() if cell.schema[col] == pl.Float64 else pl.col(col).is_not_null())
                    if cc.height < 30:
                        continue
                    sc = score_cell(**_arrays(cc, col))
                    chain_rows.append({
                        "family": family, "metric": metric, "horizon": h, "step": col,
                        "n": sc["n"], "rmse": sc["rmse"], "mae": sc["mae"], "bias": sc["bias"],
                        "spearman": sc["spearman"],
                        "skill_vs_league": sc["skill_vs_league"],
                        "skill_vs_prior_season": sc["skill_vs_prior_season"],
                    })
                # Stage A verdict cell: shrunk vs raw
                per_h["shrunk"][h] = _score_variant(cell, "shrunk_feature", "raw_feature",
                                                    n_iter=n_iter, seed=seed)
                if do_oa and "oppadj_raw" in cell.columns:
                    cc = cell.filter(pl.col("oppadj_raw").is_finite())
                    if cc.height >= 30:
                        # Reference for Stage B = the SHRUNK feature (the layer immediately
                        # before opponent adjustment in the chain). Fixed, not selected on
                        # OOS data. Phase 4.1 audit fix: the original code chose the better
                        # of {raw, shrunk} using the OOS primary-cell skill (post-hoc
                        # selection); it changed 1 of 78 verdicts and none of the
                        # conclusions -- see reports/phase4_1_audit.md.
                        ref = "shrunk_feature"
                        per_h["oppadj_raw"][h] = _score_variant(cc, "oppadj_raw", ref,
                                                                n_iter=n_iter, seed=seed)
                        if "oppadj_shrunk" in cc.columns:
                            per_h["oppadj_shrunk"][h] = _score_variant(
                                cc.filter(pl.col("oppadj_shrunk").is_finite()),
                                "oppadj_shrunk", ref, n_iter=n_iter, seed=seed)

            for step in ("shrunk", "oppadj_raw", "oppadj_shrunk"):
                for h, c in per_h[step].items():
                    shr_rows.append({"family": family, "metric": metric, "stage": step, "horizon": h, **{
                        kk: c[kk] for kk in ("n", "spearman", "skill_vs_reference",
                                             "skill_vs_reference_ci_lo", "skill_vs_reference_ci_hi",
                                             "skill_vs_league", "skill_vs_prior_season",
                                             "reference_col")}})

            a_status, a_ev = _adds_value(per_h["shrunk"].get(2), per_h["shrunk"].get(4),
                                         cfg4["status_rules"])
            a_status = a_status.replace("ADDS_VALUE", "SHRINKAGE_ADDS_VALUE")
            if do_oa:
                cand_oa = per_h["oppadj_shrunk"] if per_h["oppadj_shrunk"] else per_h["oppadj_raw"]
                b_status, b_ev = _adds_value(cand_oa.get(2), cand_oa.get(4), cfg4["status_rules"])
                b_status = b_status.replace("ADDS_VALUE", "OPPONENT_ADJUSTMENT_ADDS_VALUE")
            else:
                b_status, b_ev = "NOT_APPLICABLE", "not in the per-game pipeline"

            combined = _combine(a_status, b_status)
            status_rows.append({
                "family": family, "metric": f"{family}.{metric}",
                "shrinkage_status": a_status, "shrinkage_evidence": a_ev,
                "opponent_adjustment_status": b_status, "opponent_adjustment_evidence": b_ev,
                "combined": combined,
            })

    # ---- NGS candidates (Stage A only) --------------------------------
    for m_full in _NGS_METRIC_COL:
        row, klog = _ngs_stage_a(m_full, cfg4, n_iter, seed)
        klog_all.append(klog)
        if not row:
            continue
        shr_rows.append({**row, "stage": "shrunk", "horizon": 4})
        s, lo = row["skill_vs_reference"], row["skill_vs_reference_ci_lo"]
        ok = (row["n"] >= cfg4["status_rules"]["insufficient_data_min_n"]
              and lo is not None and np.isfinite(lo) and lo > 0
              and s >= cfg4["status_rules"]["economic_floor_skill"])
        a_status = "SHRINKAGE_ADDS_VALUE" if ok else (
            "INSUFFICIENT_DATA" if row["n"] < cfg4["status_rules"]["insufficient_data_min_n"]
            else "NO_INCREMENTAL_VALUE")
        status_rows.append({
            "family": row["family"], "metric": m_full,
            "shrinkage_status": a_status,
            "shrinkage_evidence": f"season-to-season: skill_shrunk_vs_prior={s:.3f}[{lo}] n={row['n']}",
            "opponent_adjustment_status": "NOT_APPLICABLE",
            "opponent_adjustment_evidence": "style trait; not in the per-game pipeline",
            "combined": "SHRINKAGE_ONLY" if a_status == "SHRINKAGE_ADDS_VALUE" else "NEITHER",
        })

    # ---- negative controls ------------------------------------------
    negctrl = _negative_controls(cfg4, n_iter, seed)

    _write(cand, chain_rows, shr_rows, status_rows, klog_all, alog_all, negctrl, cfg4)
    counts = dict(pl.DataFrame(status_rows, infer_schema_length=None)
                  .group_by("combined").len().iter_rows()) if status_rows else {}
    return {"n_candidates": cand.height, "n_status_rows": len(status_rows),
            "combined_counts": counts}


_NGS_METRIC_COL = {
    "ngs_passing.avg_time_to_throw": ("ngs_passing", "avg_time_to_throw"),
    "ngs_receiving.avg_separation": ("ngs_receiving", "avg_separation"),
}


def _ngs_stage_a(metric_full: str, cfg4: dict, n_iter: int, seed: int) -> tuple[dict, dict]:
    """NGS Stage A only (opponent adjustment N/A for style traits). Season-to-season:
    feature = player's prior-season weekly mean; target = this-season mean; shrink
    toward the 3-completed-season league mean, k walk-forward. The 'raw feature' IS
    the prior-season value, so this tests: does shrinking the prior season beat it?"""
    from matchup.store import load_source

    src, col = _NGS_METRIC_COL[metric_full]
    raw = load_source(src, seasons=list(range(2015, 2026))).filter(pl.col("week") > 0)
    ps = (raw.group_by(["player_gsis_id", "season"])
          .agg(pl.col(col).mean().alias("v"), pl.len().alias("wk"))
          .filter(pl.col("wk") >= 4))
    # one row per (player, OOS season S): feature = S-1 value, target = S value
    pairs = (
        ps.select("player_gsis_id", (pl.col("season") + 1).alias("season"),
                  pl.col("v").alias("feature_value"), pl.col("wk").alias("feat_n_games"))
        .join(ps.select("player_gsis_id", "season", pl.col("v").alias("target_value")),
              on=["player_gsis_id", "season"], how="inner")
    )
    lm = {s: (ps.filter(pl.col("season").is_in([s - 3, s - 2, s - 1])).get_column("v").mean())
          for s in range(2019, 2026)}
    pairs = pairs.with_columns(
        pl.col("season").replace_strict(lm, default=None).alias("baseline_league")
    ).filter(pl.col("season").is_in(list(range(2019, 2026))) & pl.col("baseline_league").is_not_null())

    kl: list[dict] = []
    frames = []
    for s in range(2019, 2026):
        tr, te = pairs.filter(pl.col("season") < s), pairs.filter(pl.col("season") == s)
        if te.is_empty():
            continue
        if tr.height < 100:
            k = float(cfg4["shrinkage"]["fallback_k"])
        else:
            curve = {}
            for kk in cfg4["shrinkage"]["k_grid"]:
                sv = shrink(tr.get_column("feature_value").to_numpy(), tr.get_column("baseline_league").to_numpy(),
                            tr.get_column("feat_n_games").to_numpy().astype(float), kk)
                curve[kk] = float(np.sqrt(np.mean((sv - tr.get_column("target_value").to_numpy()) ** 2)))
            k = float(min(curve, key=curve.get))
        sv = shrink(te.get_column("feature_value").to_numpy(), te.get_column("baseline_league").to_numpy(),
                    te.get_column("feat_n_games").to_numpy().astype(float), k)
        frames.append(te.with_columns(pl.Series("shrunk", sv), pl.lit(k).alias("k")))
        kl.append({"oos_season": s, "k": k, "n_train": tr.height})
    if not frames:
        return {}, {"metric": metric_full, "folds": kl}
    allr = pl.concat(frames)
    f = allr.get_column("shrunk").to_numpy()
    r = allr.get_column("feature_value").to_numpy()   # raw prior season
    t = allr.get_column("target_value").to_numpy()
    lmv = allr.get_column("baseline_league").to_numpy()
    ci = cluster_bootstrap(f, t, r, np.full(len(f), np.nan),
                           clusters=allr.get_column("season").to_numpy(), n_iter=n_iter, seed=seed)
    rmse_f = float(np.sqrt(np.mean((f - t) ** 2)))
    rmse_r = float(np.sqrt(np.mean((r - t) ** 2)))
    rmse_l = float(np.sqrt(np.mean((lmv - t) ** 2)))
    return ({
        "family": src, "metric": metric_full.split(".")[1], "stage": "shrunk",
        "horizon": "season_to_season", "n": len(f),
        "skill_vs_reference": _skill(rmse_f, rmse_r),
        "skill_vs_reference_ci_lo": ci["skill_vs_league_ci_lo"],
        "skill_vs_reference_ci_hi": ci["skill_vs_league_ci_hi"],
        "skill_vs_league": _skill(rmse_f, rmse_l), "reference_col": "prior_season_raw",
    }, {"metric": metric_full, "folds": kl})


_NC_METRICS = {
    "team_offense": "epa_per_play", "team_defense": "epa_per_play",
    "qb": "epa_per_dropback", "wr": "yards_per_target", "rb": "rush_epa_per_att",
    "pass_protection": "sack_rate_allowed",
}


def _negative_controls(cfg4: dict, n_iter: int, seed: int) -> list[dict]:
    """(1) Phase 3 placebo on the SHRUNK feature -- permuting it within season must
    not produce skill vs the league mean. (2) Randomised opponent labels in the
    ridge -- the opponent-adjusted feature's skill must not exceed the real one."""
    from matchup.validation.negative_control import negative_control_cell

    rng = np.random.default_rng(seed)
    obs_cfg = _phase4_obs_cfg(cfg4)
    plo, phi = obs_cfg["primary_analysis_weeks"]
    oos = list(range(cfg4["oos_evaluation_seasons"][0], cfg4["oos_evaluation_seasons"][1] + 1))
    rows: list[dict] = []

    for family, metric in _NC_METRICS.items():
        obs, _ = build_observations(family, obs_cfg)
        obs = obs.filter((pl.col("metric") == metric) & (pl.col("window") == _ANCHOR_WINDOW)
                         & (pl.col("week") >= plo) & (pl.col("week") <= phi) & (pl.col("horizon") == 4))
        if obs.is_empty():
            continue
        obs_s, _ = apply_shrinkage_walkforward(
            obs, k_grid=cfg4["shrinkage"]["k_grid"], fallback_k=cfg4["shrinkage"]["fallback_k"],
            min_train_obs=cfg4["shrinkage"]["fallback_when_train_obs_below"],
            oos_seasons=range(oos[0], oos[-1] + 1), primary_weeks=(plo, phi), primary_horizons=[4])
        cell = obs_s.rename({"shrunk_feature": "feature_value_shrunk"}).with_columns(
            pl.col("feature_value_shrunk").alias("feature_value"))
        nc = negative_control_cell(cell, seed=seed, n_permutations=20)
        rows.append({"control": "phase3_placebo_on_shrunk", "family": family, "metric": metric,
                     "n": nc["n"], "placebo_skill_vs_league_mean": nc["placebo_skill_vs_league_mean"],
                     "placebo_spearman_mean": nc["placebo_spearman_mean"]})

        if family in cfg4["opponent_adjustment"]["applicable_families"]:
            real = _oa_strength_skill(family, metric, obs_s, oos, permute=False, seed=seed)
            perm = _oa_strength_skill(family, metric, obs_s, oos, permute=True, seed=int(rng.integers(1e6)))
            rows.append({"control": "randomized_opponent_labels", "family": family, "metric": metric,
                         "n": real["n"], "real_oppadj_skill_vs_shrunk": real["skill"],
                         "randomized_oppadj_skill_vs_shrunk": perm["skill"],
                         "expectation": "randomized <= real (opponent structure adds nothing real)"})
    return rows


def _oa_strength_skill(family, metric, obs_s, oos, *, permute, seed) -> dict:
    from matchup.opponent_adjustment import walk_forward_strengths

    strengths = walk_forward_strengths(
        family, metric, seasons=list(oos), fit_trailing_seasons=2, min_fit_games=200,
        alpha=30.0, permute_opponents=permute, seed=seed,
    )
    oa = {(ss, ww, e): v for (ss, ww), d in strengths.items() for e, v in d.items()}
    dev = np.array([oa.get((int(r["season"]), int(r["week"]), r["entity_id"]), np.nan)
                    for r in obs_s.iter_rows(named=True)])
    lm = obs_s.get_column("baseline_league").to_numpy()
    shr = obs_s.get_column("shrunk_feature").to_numpy()
    tgt = obs_s.get_column("target_value").to_numpy()
    pred = lm + dev
    ok = np.isfinite(pred) & np.isfinite(shr) & np.isfinite(tgt)
    r_oa = float(np.sqrt(np.mean((pred[ok] - tgt[ok]) ** 2)))
    r_sh = float(np.sqrt(np.mean((shr[ok] - tgt[ok]) ** 2)))
    return {"n": int(ok.sum()), "skill": 1 - r_oa / r_sh if r_sh > 0 else float("nan")}


def _combine(a: str, b: str) -> str:
    a_ok = a == "SHRINKAGE_ADDS_VALUE"
    b_ok = b == "OPPONENT_ADJUSTMENT_ADDS_VALUE"
    if a_ok and b_ok:
        return "BOTH_ADD_VALUE"
    if a_ok:
        return "SHRINKAGE_ONLY"
    if b_ok:
        return "OPPONENT_ADJUSTMENT_ONLY"
    if "INSUFFICIENT_DATA" in (a, b):
        return "INSUFFICIENT_DATA"
    return "NEITHER"


def _attach_opponent_adjustment(obs_s, family, metrics, cfg4, oos, primary_weeks, alog_all):
    """DISCLOSED DEVIATION: alpha is selected ONCE per (family, metric) on the
    pre-2019 training seasons and frozen for the whole 2019-2025 evaluation,
    rather than re-selected per OOS season -- for tractability. It is still chosen
    strictly from data before the evaluation period (spec sections 19-20)."""
    oacfg = cfg4["opponent_adjustment"]
    eval_lo = cfg4["oos_evaluation_seasons"][0]
    hist_lo = cfg4["observation_history"]["build_target_seasons"][0]
    trail = 2
    frames = []
    for metric in metrics:
        alpha, curve = select_alpha(
            family, metric, train_seasons=list(range(hist_lo, eval_lo)),
            alpha_grid=oacfg["alpha_grid"], fit_trailing_seasons=trail,
            min_fit_games=oacfg["min_fit_games"], primary_weeks=primary_weeks,
        )
        alog_all.append({"family": family, "metric": metric, "alpha": float(alpha),
                         "selected_on_seasons": [hist_lo, eval_lo - 1],
                         "alpha_curve": {str(k): round(v, 6) for k, v in curve.items()}})
        strengths = walk_forward_strengths(
            family, metric, seasons=list(oos), fit_trailing_seasons=trail,
            min_fit_games=oacfg["min_fit_games"], alpha=alpha,
        )
        oa_map = {(ss, ww, e): v for (ss, ww), d in strengths.items() for e, v in d.items()}
        sub = obs_s.filter(pl.col("metric") == metric)
        # the ridge strength is a CENTRED deviation from league average -> put it
        # back on the metric's scale by adding the league mean, so it is a
        # prediction directly comparable to target_value.
        dev = [oa_map.get((int(r["season"]), int(r["week"]), r["entity_id"]))
               for r in sub.iter_rows(named=True)]
        sub = sub.with_columns(pl.Series("_oa_dev", dev, dtype=pl.Float64))
        sub = sub.with_columns(
            (pl.col("baseline_league") + pl.col("_oa_dev")).alias("oppadj_raw"),
            (pl.col("baseline_league")
             + pl.col("_oa_dev") * (pl.col("feat_n_games") / (pl.col("feat_n_games") + pl.col("shrinkage_k"))))
            .alias("oppadj_shrunk"),
        ).drop("_oa_dev")
        frames.append(sub)
    return pl.concat(frames, how="diagonal_relaxed") if frames else obs_s


def _write(cand, chain_rows, shr_rows, status_rows, klog, alog, negctrl, cfg4):
    OUT.mkdir(parents=True, exist_ok=True)
    if chain_rows:
        pl.DataFrame(chain_rows, infer_schema_length=None).write_csv(OUT / "baseline_chain.csv")
    if shr_rows:
        df = pl.DataFrame(shr_rows, infer_schema_length=None)
        df.filter(pl.col("stage") == "shrunk").write_csv(OUT / "shrinkage_results.csv")
        df.filter(pl.col("stage") != "shrunk").write_csv(OUT / "opponent_adjustment_results.csv")
    if status_rows:
        pl.DataFrame(status_rows, infer_schema_length=None).sort("metric").write_csv(
            OUT / "metric_phase4_status.csv")
        (REPO_ROOT / "config" / "metrics_phase4_status.yaml").write_text(
            "# Generated by Phase 4. Layer-specific results; a metric may carry more than one.\n"
            "# 'SHRINKAGE_ADDS_VALUE' / 'OPPONENT_ADJUSTMENT_ADDS_VALUE' mean the layer improves\n"
            "# out-of-sample point prediction of future SAME-UNIT performance -- NOT that the\n"
            "# metric improves matchup prediction (a separate, later question).\n"
            + "\n".join(
                f"{r['metric']}: {{shrinkage: {r['shrinkage_status']}, "
                f"opponent_adjustment: {r['opponent_adjustment_status']}, combined: {r['combined']}, "
                f"shrinkage_evidence: \"{str(r['shrinkage_evidence']).replace(chr(34), chr(39))}\", "
                f"opponent_adjustment_evidence: \"{str(r['opponent_adjustment_evidence']).replace(chr(34), chr(39))}\"}}"
                for r in sorted(status_rows, key=lambda x: x["metric"])
            ) + "\n"
        )
    if negctrl:
        pl.DataFrame(negctrl, infer_schema_length=None).write_csv(OUT / "negative_control.csv")
    # hyperparameter stability
    if klog:
        pl.DataFrame(
            [{"metric": e["metric"], "oos_season": f.get("oos_season"), "k": f.get("k"),
              "n_train": f.get("n_train")}
             for e in klog if "folds" in e for f in e["folds"]]
            + [{"metric": e["metric"], "oos_season": e["oos_season"], "k": e["k"],
                "n_train": e["n_train"]}
               for e in klog if "oos_season" in e],
            infer_schema_length=None,
        ).write_csv(OUT / "hyperparameter_stability.csv")
    (OUT / "shrinkage_k_log.json").write_text(json.dumps(klog, indent=2, default=str))
    (OUT / "opponent_adjustment_alpha_log.json").write_text(json.dumps(alog, indent=2, default=str))
    (OUT / "run_meta.json").write_text(json.dumps({
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"), "config": cfg4,
    }, indent=2, default=str))
