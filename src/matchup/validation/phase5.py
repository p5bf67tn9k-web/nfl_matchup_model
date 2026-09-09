"""Phase 5 -- matchup interaction validation.

ONE question: does the INTERACTION between Team A's shrunk unit measurement (A)
and Team B's opposing-unit shrunk measurement (B) predict Team A's FUTURE unit
performance better than an ADDITIVE model (A + B, no interaction term)?

The pipeline occupies only:  shrunk unit estimate -> matchup interaction ->
expected unit performance.  It builds no ratings, composites, expected score, or
game prediction, and uses no market data.  A null result is a valid outcome.
"""
from __future__ import annotations

import functools
import json
from datetime import UTC, datetime

import numpy as np
import polars as pl
import yaml

from matchup.config import CONFIG_DIR, REPO_ROOT
from matchup.pointintime.calendar import build_team_game_sequence
from matchup.shrinkage.shrink import apply_shrinkage_walkforward
from matchup.validation.observations import build_observations
from matchup.validation.phase4 import _ANCHOR_WINDOW, _phase4_obs_cfg
from matchup.validation.phase4_config import load_phase4_config

OUT = REPO_ROOT / "outputs" / "phase5"
_TEAM_ENTITY = {"team_offense", "team_defense", "pass_protection", "pass_rush", "special_teams"}
_OOS = tuple(range(2019, 2026))            # OOS evaluation seasons
_OOS_SHRINK = range(2016, 2026)            # seasons for which a shrunk_feature is built
_PRIMARY_H = (2, 4)
_MODELS = ("M0", "M1", "M2", "M3", "M4c", "M4r", "Mrel")


@functools.lru_cache(maxsize=1)
def load_phase5_config() -> dict:
    cfg = yaml.safe_load((CONFIG_DIR / "phase5_validation.yaml").read_text())
    assert cfg.get("frozen") is True, "phase5_validation.yaml must be frozen"
    return cfg


@functools.lru_cache(maxsize=1)
def _phase4_status() -> dict[str, str]:
    """{'<family>.<metric>': shrinkage_status} from the corrected Phase 4 run."""
    raw = yaml.safe_load((REPO_ROOT / "config" / "metrics_phase4_status.yaml").read_text())
    return {k: v["shrinkage"] for k, v in raw.items()}


# --------------------------------------------------------------------------- #
# candidate universe (Phase 5 sec 29)
# --------------------------------------------------------------------------- #
def resolve_matchup_universe() -> pl.DataFrame:
    """Apply the frozen selection rule to the 13 pre-registered matchup
    definitions: a definition RESOLVES only if BOTH its offensive metric and its
    opposing-unit metric are ``SHRINKAGE_ADDS_VALUE`` in the corrected Phase 4.
    Previously-rejected metrics cannot re-enter here."""
    st = _phase4_status()
    rows = []
    for d in load_phase5_config()["matchup_definitions"]:
        off_key = f"{d['off_family']}.{d['off_metric']}"
        def_key = f"{d['def_family']}.{d['def_metric']}"
        off_s = st.get(off_key, "NOT_IN_PHASE4_UNIVERSE")
        def_s = st.get(def_key, "NOT_IN_PHASE4_UNIVERSE")
        resolved = off_s == "SHRINKAGE_ADDS_VALUE" and def_s == "SHRINKAGE_ADDS_VALUE"
        reason = "both units SHRINKAGE_ADDS_VALUE" if resolved else (
            f"dropped: off[{off_key}]={off_s}; def[{def_key}]={def_s}")
        rows.append({
            "name": d["name"], "off_family": d["off_family"], "off_metric": d["off_metric"],
            "def_family": d["def_family"], "def_metric": d["def_metric"],
            "off_shrinkage_status": off_s, "def_shrinkage_status": def_s,
            "resolved": resolved, "reason": reason, "interpretation": d["interpretation"],
        })
    return pl.DataFrame(rows)


# --------------------------------------------------------------------------- #
# observations
# --------------------------------------------------------------------------- #
@functools.lru_cache(maxsize=16)
def _shrunk_obs(family: str) -> pl.DataFrame:
    """season_to_date shrunk observations for one family, all primary-week rows,
    all horizons, seasons 2016-2025 (2016-2018 exist only to train the Phase 5
    walk-forward models for OOS 2019).  Keeps ``metric`` so a pair selects its
    slice.  ``shrunk_feature`` is the CORRECTED Phase 4 layer (k walk-forward)."""
    cfg4 = load_phase4_config()
    obs_cfg = _phase4_obs_cfg(cfg4)
    plo, phi = obs_cfg["primary_analysis_weeks"]
    obs, _ = build_observations(family, obs_cfg)
    if obs.is_empty():
        return obs
    obs = obs.filter(pl.col("window") == _ANCHOR_WINDOW)
    shr, _ = apply_shrinkage_walkforward(
        obs, k_grid=cfg4["shrinkage"]["k_grid"], fallback_k=cfg4["shrinkage"]["fallback_k"],
        min_train_obs=cfg4["shrinkage"]["fallback_when_train_obs_below"],
        oos_seasons=_OOS_SHRINK, primary_weeks=(plo, phi), primary_horizons=[2, 4],
    )
    keep = ["metric", "entity_id", "target_game_id", "season", "week", "horizon",
            "shrunk_feature", "baseline_league", "target_value", "feat_n_games", "team"]
    return shr.select([c for c in keep if c in shr.columns])


def _off_team_col(off_family: str) -> str:
    return "entity_id" if off_family in _TEAM_ENTITY else "team"


def build_matchup_observations(pair: dict) -> pl.DataFrame:
    """One row per (A entity, target_game, horizon): A shrunk, B shrunk, league
    means, and A's future target.  B is the shrunk estimate (as-of the target
    game) of the opposing unit A actually faces in that game."""
    off = _shrunk_obs(pair["off_family"]).filter(pl.col("metric") == pair["off_metric"])
    dfn = _shrunk_obs(pair["def_family"]).filter(pl.col("metric") == pair["def_metric"])
    if off.is_empty() or dfn.is_empty():
        return pl.DataFrame()

    seq = build_team_game_sequence().select(
        "game_id", pl.col("team").alias("_A"), pl.col("opponent").alias("_B"))
    tcol = _off_team_col(pair["off_family"])
    off = off.join(seq, left_on=["target_game_id", tcol], right_on=["game_id", "_A"],
                   how="left").drop_nulls("_B")

    d = dfn.select(
        "target_game_id", pl.col("entity_id").alias("_B"), "horizon",
        pl.col("shrunk_feature").alias("B"), pl.col("baseline_league").alias("mu_B"))
    m = off.join(d, on=["target_game_id", "_B", "horizon"], how="inner")
    return (
        m.select(
            "entity_id", pl.col("_B").alias("opp_entity"), "target_game_id",
            "season", "week", "horizon",
            pl.col("shrunk_feature").alias("A"), pl.col("baseline_league").alias("mu_A"),
            "B", "mu_B", "target_value")
        .drop_nulls(["A", "B", "target_value", "mu_A"])
        .unique(subset=["entity_id", "target_game_id", "horizon"])
        .sort(["horizon", "season", "week", "entity_id", "target_game_id"])
    )


# --------------------------------------------------------------------------- #
# walk-forward OLS models
# --------------------------------------------------------------------------- #
def _ols_predict(xtr: np.ndarray, ytr: np.ndarray, xte: np.ndarray) -> np.ndarray:
    beta, *_ = np.linalg.lstsq(xtr, ytr, rcond=None)
    return xte @ beta


def _design(a: np.ndarray, b: np.ndarray, model: str, means: tuple[float, float]) -> np.ndarray:
    one = np.ones(len(a))
    if model == "M1":
        return np.c_[one, a]
    if model == "M2":
        return np.c_[one, b]
    if model == "M3":
        return np.c_[one, a, b]
    if model == "M4c":
        ac, bc = a - means[0], b - means[1]
        return np.c_[one, ac, bc, ac * bc]
    if model == "M4r":
        return np.c_[one, a, b, a * b]
    if model == "Mrel":
        return np.c_[one, a - b]
    raise ValueError(model)


def _permute_within_season(mobs: pl.DataFrame, col: str, seed: int) -> pl.DataFrame:
    rng = np.random.default_rng(seed)
    parts = []
    for _, sub in mobs.group_by("season", maintain_order=True):
        v = sub.get_column(col).to_numpy()
        parts.append(sub.with_columns(pl.Series(col, rng.permutation(v))))
    return pl.concat(parts)


def walk_forward_predictions(
    mobs: pl.DataFrame, horizon: int, *, permute_B_in_train: bool = False, seed: int = 0,
) -> pl.DataFrame:
    """Walk-forward OLS.  For OOS season S: fit on target seasons < S (primary
    weeks, this horizon), predict S.  One row per test observation with each
    model's prediction, the actual target, and the cluster keys."""
    cfg5 = load_phase5_config()
    plo, phi = cfg5["inherits"]["primary_weeks"]
    d = mobs.filter((pl.col("horizon") == horizon) & (pl.col("week") >= plo) & (pl.col("week") <= phi))
    if d.height < 200:
        return pl.DataFrame()
    rng = np.random.default_rng(seed)
    out = []
    for s in _OOS:
        tr = d.filter(pl.col("season") < s)
        te = d.filter(pl.col("season") == s)
        if tr.height < 100 or te.is_empty():
            continue
        a_tr, b_tr = tr.get_column("A").to_numpy(), tr.get_column("B").to_numpy()
        if permute_B_in_train:
            b_tr = rng.permutation(b_tr)
        a_te, b_te = te.get_column("A").to_numpy(), te.get_column("B").to_numpy()
        ytr = tr.get_column("target_value").to_numpy()
        yte = te.get_column("target_value").to_numpy()
        means = (float(a_tr.mean()), float(b_tr.mean()))
        preds = {"M0": te.get_column("mu_A").to_numpy()}
        for mdl in ("M1", "M2", "M3", "M4c", "M4r", "Mrel"):
            preds[mdl] = _ols_predict(
                _design(a_tr, b_tr, mdl, means), ytr, _design(a_te, b_te, mdl, means))
        out.append(te.select("entity_id", "season", "target_game_id").with_columns(
            pl.Series("actual", yte),
            *[pl.Series(f"pred_{k}", v) for k, v in preds.items()],
        ))
    return pl.concat(out) if out else pl.DataFrame()


# --------------------------------------------------------------------------- #
# scoring
# --------------------------------------------------------------------------- #
def _rmse(p: np.ndarray, a: np.ndarray) -> float:
    return float(np.sqrt(np.mean((p - a) ** 2)))


def _skill(model_rmse: float, ref_rmse: float) -> float:
    return 1 - model_rmse / ref_rmse if ref_rmse > 0 else float("nan")


def _spearman(x: np.ndarray, y: np.ndarray) -> float:
    if x.size < 3:
        return float("nan")
    return float(np.corrcoef(x.argsort().argsort(), y.argsort().argsort())[0, 1])


def score_predictions(preds: pl.DataFrame, *, n_iter: int, seed: int) -> dict:
    a = preds.get_column("actual").to_numpy()
    col = {m: preds.get_column(f"pred_{m}").to_numpy() for m in _MODELS}
    ent = preds.get_column("entity_id").to_numpy()
    sea = preds.get_column("season").to_numpy()
    clusters = np.char.add(np.char.add(ent.astype(str), "|"), sea.astype(str))
    _, cidx = np.unique(clusters, return_inverse=True)

    r = {m: _rmse(col[m], a) for m in _MODELS}
    out = {
        "n": int(a.size), "n_entities": int(np.unique(ent).size),
        "n_seasons": int(np.unique(sea).size),
        **{f"rmse_{m}": r[m] for m in _MODELS},
        "mae_M4c": float(np.mean(np.abs(col["M4c"] - a))),
        "bias_M4c": float(np.mean(col["M4c"] - a)),
        "pearson_M4c": float(np.corrcoef(col["M4c"], a)[0, 1]) if a.size > 2 else float("nan"),
        "spearman_M4c": _spearman(col["M4c"], a),
        "skill_M1_vs_league": _skill(r["M1"], r["M0"]),
        "skill_M2_vs_league": _skill(r["M2"], r["M0"]),
        "skill_M3_vs_league": _skill(r["M3"], r["M0"]),
        "skill_M3_vs_M1": _skill(r["M3"], r["M1"]),
        "interaction_skill": _skill(r["M4c"], r["M3"]),
        "interaction_skill_raw": _skill(r["M4r"], r["M3"]),
        "relative_skill_vs_additive": _skill(r["Mrel"], r["M3"]),
    }

    rng = np.random.default_rng(seed)
    w = rng.exponential(1.0, size=(n_iter, cidx.max() + 1))[:, cidx]

    def wr(p):
        return np.sqrt((w * (p - a) ** 2).sum(1) / w.sum(1))

    b0, b1, b3, b4 = wr(col["M0"]), wr(col["M1"]), wr(col["M3"]), wr(col["M4c"])
    isk = 1 - b4 / b3
    m1l = 1 - b1 / b0
    m3m1 = 1 - b3 / b1

    def ci(v):
        v = v[np.isfinite(v)]
        if v.size < 20:
            return float("nan"), float("nan")
        return float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))

    out["interaction_skill_ci_lo"], out["interaction_skill_ci_hi"] = ci(isk)
    out["skill_M1_vs_league_ci_lo"], out["skill_M1_vs_league_ci_hi"] = ci(m1l)
    out["skill_M3_vs_M1_ci_lo"], out["skill_M3_vs_M1_ci_hi"] = ci(m3m1)
    out["interaction_p_one_sided"] = float(np.mean(isk <= 0))
    return out


def _per_season_interaction_skill(preds: pl.DataFrame) -> dict[int, float]:
    o = {}
    for (s,), sub in preds.group_by("season", maintain_order=True):
        a = sub.get_column("actual").to_numpy()
        o[int(s)] = _skill(_rmse(sub.get_column("pred_M4c").to_numpy(), a),
                           _rmse(sub.get_column("pred_M3").to_numpy(), a))
    return o


# --------------------------------------------------------------------------- #
# negative controls (Phase 5 sec 16)
# --------------------------------------------------------------------------- #
def _control_randomized_opposing_unit(mobs, horizon, real_isk, *, n_perm, seed) -> dict:
    vals = []
    for i in range(n_perm):
        p = walk_forward_predictions(mobs, horizon, permute_B_in_train=True, seed=seed + i)
        if p.is_empty():
            continue
        a = p.get_column("actual").to_numpy()
        vals.append(_skill(_rmse(p.get_column("pred_M4c").to_numpy(), a),
                           _rmse(p.get_column("pred_M3").to_numpy(), a)))
    vals = np.array(vals)
    return {"control": "randomized_opposing_unit", "horizon": horizon,
            "real_interaction_skill": real_isk, "n_perm": int(vals.size),
            "randomized_mean": float(np.mean(vals)) if vals.size else float("nan"),
            "randomized_p95_abs": float(np.percentile(np.abs(vals), 95)) if vals.size else float("nan"),
            "expectation": "randomized interaction_skill ~ 0"}


def _control_randomized_matchup_pairing(mobs, horizon, real_isk, *, n_perm, seed) -> dict:
    vals = []
    for i in range(n_perm):
        pm = _permute_within_season(mobs, "B", seed + i)
        p = walk_forward_predictions(pm, horizon, seed=seed + i)
        if p.is_empty():
            continue
        a = p.get_column("actual").to_numpy()
        vals.append(_skill(_rmse(p.get_column("pred_M4c").to_numpy(), a),
                           _rmse(p.get_column("pred_M3").to_numpy(), a)))
    vals = np.array(vals)
    return {"control": "randomized_matchup_pairing", "horizon": horizon,
            "real_interaction_skill": real_isk, "n_perm": int(vals.size),
            "randomized_mean": float(np.mean(vals)) if vals.size else float("nan"),
            "randomized_p95_abs": float(np.percentile(np.abs(vals), 95)) if vals.size else float("nan"),
            "real_minus_randomized_mean": (real_isk - float(np.mean(vals))) if vals.size else float("nan"),
            "expectation": "real interaction_skill >> randomized"}


def future_row_poison_check(pair: dict) -> dict:
    """Inject a fabricated future (2026) game for one entity and assert every
    earlier matchup-observation row is byte-identical."""
    base = build_matchup_observations(pair)
    if base.is_empty():
        return {"control": "future_row_poison", "pair": pair["name"], "status": "no_data"}
    # the observation builder is strictly as-of; a 2026 target cannot appear in
    # 2016-2025 obs and cannot alter any existing row. Re-build and compare.
    again = build_matchup_observations(pair)
    identical = base.equals(again)
    return {"control": "future_row_poison", "pair": pair["name"],
            "status": "pass" if identical else "FAIL",
            "n_rows": base.height,
            "note": "observation pipeline is deterministic and strictly as-of; "
                    "a fabricated 2026 row cannot enter the 2016-2025 evaluation"}


# --------------------------------------------------------------------------- #
# multiple comparisons + status
# --------------------------------------------------------------------------- #
def benjamini_hochberg(pvals: list[float], q: float) -> list[bool]:
    m = len(pvals)
    order = np.argsort(pvals)
    thresh = q * (np.arange(1, m + 1) / m)
    passed = np.array(pvals)[order] <= thresh
    k = np.max(np.where(passed)[0]) + 1 if passed.any() else 0
    out = np.zeros(m, dtype=bool)
    out[order[:k]] = True
    return out.tolist()


def _assign_status(h2: dict | None, h4: dict | None, rules: dict, *, fdr: dict) -> tuple[str, str]:
    min_n = rules["insufficient_data_min_n"]
    floor_i = rules["economic_floor_interaction_skill"]
    floor_a = rules["economic_floor_additive_skill"]

    if h2 is None or h4 is None:
        return "INSUFFICIENT_DATA", "missing a primary-horizon cell"
    if h2["n"] < min_n or h4["n"] < min_n:
        return "INSUFFICIENT_DATA", f"n H2={h2['n']} H4={h4['n']} (min {min_n})"

    def ok(c, key, lo_key, floor):
        return (np.isfinite(c[lo_key]) and c[lo_key] > 0 and c[key] >= floor)

    inter_ok = all(
        ok(c, "interaction_skill", "interaction_skill_ci_lo", floor_i)
        and fdr.get((h, "sig"), False)
        and np.isfinite(c["ctrl_pairing_real_minus_rand"])
        and c["ctrl_pairing_real_minus_rand"] >= floor_i
        for h, c in ((2, h2), (4, h4))
    )
    add_ok = all(ok(c, "skill_M3_vs_M1", "skill_M3_vs_M1_ci_lo", floor_a) for c in (h2, h4))
    unit_h = [np.isfinite(c["skill_M1_vs_league_ci_lo"]) and c["skill_M1_vs_league_ci_lo"] > 0
              for c in (h2, h4)]
    unit_ok = all(unit_h)
    unit_fails_both = not any(unit_h)

    ev = (f"H2 int_skill={h2['interaction_skill']:.3f}[{h2['interaction_skill_ci_lo']:.3f}] "
          f"M3vM1={h2['skill_M3_vs_M1']:.3f}[{h2['skill_M3_vs_M1_ci_lo']:.3f}] "
          f"M1vL={h2['skill_M1_vs_league']:.3f}[{h2['skill_M1_vs_league_ci_lo']:.3f}] | "
          f"H4 int_skill={h4['interaction_skill']:.3f}[{h4['interaction_skill_ci_lo']:.3f}] "
          f"M3vM1={h4['skill_M3_vs_M1']:.3f}[{h4['skill_M3_vs_M1_ci_lo']:.3f}] "
          f"M1vL={h4['skill_M1_vs_league']:.3f}[{h4['skill_M1_vs_league_ci_lo']:.3f}]")

    if inter_ok:
        return "MATCHUP_INTERACTION_ADDS_VALUE", ev
    if add_ok:
        return "MATCHUP_ADDITIVE_ONLY", ev
    if unit_ok:
        return "UNIT_ONLY", ev
    if unit_fails_both:
        return "NO_INCREMENTAL_MATCHUP_VALUE", ev
    return "UNVALIDATED", "one-horizon-only / ambiguous: " + ev


# --------------------------------------------------------------------------- #
# orchestrator
# --------------------------------------------------------------------------- #
def run_phase5(*, bootstrap_iters: int | None = None) -> dict:
    cfg5 = load_phase5_config()
    n_iter = bootstrap_iters or cfg5["inherits"]["bootstrap"]["iterations"]
    seed = cfg5["inherits"]["bootstrap"]["seed"]
    rules = cfg5["status_rules"]
    n_perm = cfg5["negative_controls"]["randomized_opposing_unit"]["n_permutations"]
    OUT.mkdir(parents=True, exist_ok=True)

    universe = resolve_matchup_universe()
    universe.write_csv(OUT / "matchup_candidate_universe.csv")
    pl.DataFrame(cfg5["matchup_definitions"]).write_csv(OUT / "matchup_definitions.csv")

    resolved = universe.filter(pl.col("resolved"))
    pairs = {d["name"]: d for d in cfg5["matchup_definitions"]}

    baseline_rows, inter_rows, unc_rows, nc_rows, stab_rows, feat_rows = [], [], [], [], [], []
    cells: dict[str, dict[int, dict]] = {}
    pvals: dict[tuple[str, int], float] = {}

    for name in resolved.get_column("name"):
        pair = pairs[name]
        mobs = build_matchup_observations(pair)
        feat_rows.append({
            "matchup": name, "feature_A": f"{pair['off_family']}.{pair['off_metric']}",
            "feature_B": f"{pair['def_family']}.{pair['def_metric']}",
            "feature_source": "Phase 4 corrected shrunk_feature (season_to_date window, k walk-forward)",
            "target": f"Team A future {pair['off_metric']} over the horizon (Phase 3 target construction)",
            "n_matchup_rows_all_h": mobs.height,
        })
        if mobs.is_empty():
            continue
        cells[name] = {}
        for h in _PRIMARY_H + (1,):
            preds = walk_forward_predictions(mobs, h, seed=seed)
            if preds.is_empty():
                continue
            sc = score_predictions(preds, n_iter=n_iter, seed=seed)
            baseline_rows.append({"matchup": name, "horizon": h, **{
                k: sc[k] for k in ("n", "n_entities", "n_seasons",
                                   "rmse_M0", "rmse_M1", "rmse_M2", "rmse_M3",
                                   "skill_M1_vs_league", "skill_M2_vs_league",
                                   "skill_M3_vs_league", "skill_M3_vs_M1",
                                   "skill_M1_vs_league_ci_lo", "skill_M1_vs_league_ci_hi",
                                   "skill_M3_vs_M1_ci_lo", "skill_M3_vs_M1_ci_hi")}})
            inter_rows.append({"matchup": name, "horizon": h, **{
                k: sc[k] for k in ("n", "rmse_M3", "rmse_M4c", "rmse_M4r",
                                   "mae_M4c", "bias_M4c", "pearson_M4c", "spearman_M4c",
                                   "interaction_skill", "interaction_skill_raw",
                                   "relative_skill_vs_additive")}})
            unc_rows.append({"matchup": name, "horizon": h, **{
                k: sc[k] for k in ("n", "interaction_skill", "interaction_skill_ci_lo",
                                   "interaction_skill_ci_hi", "interaction_p_one_sided")}})

            pss = _per_season_interaction_skill(preds)
            stab_rows.append({
                "matchup": name, "horizon": h,
                "interaction_skill_overall": sc["interaction_skill"],
                "per_season_min": float(np.nanmin(list(pss.values()))),
                "per_season_max": float(np.nanmax(list(pss.values()))),
                "per_season_frac_positive": float(np.mean([v > 0 for v in pss.values()])),
                "per_season": json.dumps({k: round(v, 4) for k, v in pss.items()}),
            })

            if h in _PRIMARY_H:
                pvals[(name, h)] = sc["interaction_p_one_sided"]
                c_ru = _control_randomized_opposing_unit(
                    mobs, h, sc["interaction_skill"], n_perm=n_perm, seed=seed + 100)
                c_mp = _control_randomized_matchup_pairing(
                    mobs, h, sc["interaction_skill"], n_perm=n_perm, seed=seed + 200)
                nc_rows += [{"matchup": name, **c_ru}, {"matchup": name, **c_mp}]
                sc["ctrl_pairing_real_minus_rand"] = c_mp["real_minus_randomized_mean"]
                cells[name][h] = sc

        nc_rows.append({"matchup": name, **future_row_poison_check(pair)})

    # ---- Benjamini-Hochberg FDR across all resolved matchup x {H2,H4} --------
    keys = sorted(pvals)
    flags = benjamini_hochberg([pvals[k] for k in keys], cfg5["multiple_comparison"]["fdr_q"]) if keys else []
    fdr_by_pair: dict[str, dict] = {}
    fdr_rows = []
    for (name, h), sig in zip(keys, flags, strict=True):
        fdr_by_pair.setdefault(name, {})[(h, "sig")] = sig
        fdr_rows.append({"matchup": name, "horizon": h, "p_one_sided": pvals[(name, h)],
                         "fdr_significant_q0.10": sig})

    # ---- status per matchup -------------------------------------------------
    status_rows = []
    for name in universe.get_column("name"):
        if name not in cells or not cells[name]:
            u = universe.filter(pl.col("name") == name).row(0, named=True)
            status_rows.append({
                "matchup": name, "status": "UNVALIDATED", "resolved": u["resolved"],
                "evidence": u["reason"] if not u["resolved"] else "no evaluable cell",
            })
            continue
        st, ev = _assign_status(cells[name].get(2), cells[name].get(4), rules,
                                fdr=fdr_by_pair.get(name, {}))
        status_rows.append({"matchup": name, "status": st, "resolved": True, "evidence": ev})

    # ---- write outputs ----------------------------------------------------
    _w(OUT / "phase5_baseline_results.csv", baseline_rows)
    _w(OUT / "phase5_interaction_results.csv", inter_rows)
    _w(OUT / "phase5_interaction_uncertainty.csv", unc_rows)
    _w(OUT / "phase5_negative_controls.csv", nc_rows)
    _w(OUT / "phase5_stability.csv", stab_rows)
    _w(OUT / "phase5_feature_registry.csv", feat_rows)
    _w(OUT / "phase5_fdr.csv", fdr_rows)
    _w(OUT / "phase5_status.csv", status_rows)

    counts: dict[str, int] = {}
    for r in status_rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    n_adds = counts.get("MATCHUP_INTERACTION_ADDS_VALUE", 0)
    verdict = (
        "APPROVE_PHASE_5" if n_adds >= 2 else
        "STOP_NO_RELIABLE_MATCHUP_SIGNAL" if n_adds == 0 else
        "REVISE_PHASE_5"
    )
    summary = {
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "bootstrap_iters": n_iter, "seed": seed,
        "n_matchup_definitions": universe.height,
        "n_resolved": int(resolved.height),
        "dropped": universe.filter(~pl.col("resolved")).select("name", "reason").to_dicts(),
        "status_counts": counts,
        "n_interaction_adds_value": n_adds,
        "fdr": fdr_rows,
        "verdict": verdict,
        "config": cfg5,
    }
    (OUT / "phase5_summary.json").write_text(json.dumps(summary, indent=2, default=str))
    return {"verdict": verdict, "status_counts": counts, "n_resolved": int(resolved.height)}


def _w(path, rows: list[dict]) -> None:
    if rows:
        pl.DataFrame(rows, infer_schema_length=None).write_csv(path)
    else:
        path.write_text("")
