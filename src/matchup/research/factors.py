"""Candidate-factor research against scoring / points-allowed / winning outcomes.

Three clearly-separated lenses per (factor, outcome):

  1. association   -- contemporaneous, SEASON level. Descriptive: "teams that do
     more of X also tend to score/allow/win more IN THE SAME SEASON". Big
     correlations here are expected and are NOT predictions.
  2. chronological -- walk-forward, GAME level. Feature = a team's season-to-date
     shrunk metric through week W; outcome = that team's realised outcome over
     the NEXT 4 games. Predictive-looking evidence with cluster-bootstrap CIs.
  3. stability     -- the season-level association computed separately per season
     2016-2025: mean, SD, and fraction of seasons with the same sign.

A factor is never called "important" for having the largest correlation. The
evidence tier combines chronological CI, effect size, temporal consistency,
sample size, and (via factor groups) redundancy.
"""
from __future__ import annotations

import numpy as np
import polars as pl

from matchup.config import REPO_ROOT
from matchup.metrics.build import game_metrics_offline
from matchup.metrics.windows import entity_season_aggregate
from matchup.normalize.reference import min_opportunities_for
from matchup.strength.config import load_strength_config, orient_sign
from matchup.strength.results import team_game_results
from matchup.strength.team_metrics import build_team_metrics_weekly

OUT = REPO_ROOT / "outputs" / "research"

_ASSOC_SEASONS = list(range(2016, 2026))
_OFF_OUTCOMES = ["points_scored", "point_differential", "win", "rolling_win_pct_4"]
_DEF_OUTCOMES = ["points_allowed", "point_differential", "win", "rolling_win_pct_4"]
_ST_OUTCOMES = ["point_differential", "win", "rolling_win_pct_4"]


# --------------------------------------------------------------------------- #
# panels
# --------------------------------------------------------------------------- #
def _season_outcomes() -> pl.DataFrame:
    res = team_game_results(tuple(_ASSOC_SEASONS)).filter(pl.col("game_type") == "REG")
    return (
        res.group_by(["season", "team"])
        .agg(
            pl.len().alias("games"),
            pl.col("points_for").sum().alias("points_scored"),
            pl.col("points_against").sum().alias("points_allowed"),
            pl.col("point_diff").sum().alias("point_differential"),
            pl.col("won").mean().alias("win"),
        )
        .with_columns(pl.col("win").alias("rolling_win_pct_4"))  # season-level proxy
    )


def _season_factor_values(metrics: list[str]) -> pl.DataFrame:
    """team-season raw value of each metric, min-opportunity filtered."""
    by_fam: dict[str, list[str]] = {}
    for m in metrics:
        fam, bare = m.split(".", 1)
        by_fam.setdefault(fam, []).append(bare)
    frames = []
    for fam, bares in by_fam.items():
        gm = game_metrics_offline(fam, _ASSOC_SEASONS)
        if gm.is_empty():
            continue
        gm = gm.filter(pl.col("week").is_between(1, 18))
        sl = entity_season_aggregate(fam, gm).filter(
            pl.col("n_opportunities") >= min_opportunities_for(fam)
        )
        have = [b for b in bares if b in sl.columns]
        long = sl.select(
            "season", pl.col("entity_id").alias("team"),
            *[pl.col(b).alias(f"{fam}.{b}") for b in have],
        ).unpivot(index=["season", "team"], variable_name="factor", value_name="factor_value")
        frames.append(long)
    return pl.concat(frames, how="diagonal_relaxed") if frames else pl.DataFrame()


def _chronological_panel(metrics: list[str], horizon: int) -> pl.DataFrame:
    """feature = shrunk season-to-date metric through week W (W in 3..14);
    outcome = mean points_for / points_against / point_diff / win over the next
    `horizon` REG games of the same season."""
    cfg = load_strength_config()["research"]
    lo, hi = cfg["walk_forward_seasons"]
    seasons = list(range(lo, hi + 1))
    ml = build_team_metrics_weekly(seasons).filter(
        pl.col("metric").is_in(metrics) & (pl.col("week") >= 3) & (pl.col("week") <= 14)
    )
    if ml.is_empty():
        return pl.DataFrame()
    feat = ml.select(
        "season", "team", "week", "metric",
        pl.col("shrunk_value").alias("feature_value"),
    )
    res = team_game_results(tuple(seasons)).filter(pl.col("game_type") == "REG").select(
        "season", "team", "week", "points_for", "points_against", "point_diff", "won"
    )
    # forward window: games with W < game_week <= W + horizon
    fw = feat.join(res, on=["season", "team"], how="inner", suffix="_g").filter(
        (pl.col("week_g") > pl.col("week")) & (pl.col("week_g") <= pl.col("week") + horizon)
    )
    agg = fw.group_by(["season", "team", "week", "metric", "feature_value"]).agg(
        pl.len().alias("n_fwd_games"),
        pl.col("points_for").mean().alias("points_scored"),
        pl.col("points_against").mean().alias("points_allowed"),
        pl.col("point_diff").mean().alias("point_differential"),
        pl.col("won").mean().alias("win"),
    ).filter(pl.col("n_fwd_games") >= horizon)
    return agg.with_columns(pl.col("win").alias("rolling_win_pct_4"))


# --------------------------------------------------------------------------- #
# stats helpers
# --------------------------------------------------------------------------- #
def _pearson(x: np.ndarray, y: np.ndarray) -> float:
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 5 or np.std(x[m]) == 0 or np.std(y[m]) == 0:
        return float("nan")
    return float(np.corrcoef(x[m], y[m])[0, 1])


def _spearman(x: np.ndarray, y: np.ndarray) -> float:
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 5:
        return float("nan")
    xr = x[m].argsort().argsort().astype(float)
    yr = y[m].argsort().argsort().astype(float)
    return _pearson(xr, yr)


def _cluster_boot_ci(x, y, clusters, *, n_iter, seed) -> tuple[float, float]:
    m = np.isfinite(x) & np.isfinite(y)
    x, y, clusters = x[m], y[m], clusters[m]
    if x.size < 20:
        return float("nan"), float("nan")
    uniq, inv = np.unique(clusters, return_inverse=True)
    rng = np.random.default_rng(seed)
    w = rng.exponential(1.0, size=(n_iter, uniq.size))[:, inv]
    sw = w.sum(1)
    mx = (w * x).sum(1) / sw
    my = (w * y).sum(1) / sw
    cov = (w * (x - mx[:, None]) * (y - my[:, None])).sum(1) / sw
    vx = (w * (x - mx[:, None]) ** 2).sum(1) / sw
    vy = (w * (y - my[:, None]) ** 2).sum(1) / sw
    denom = np.sqrt(vx * vy)
    r = np.where(denom > 0, cov / np.where(denom > 0, denom, 1), np.nan)
    r = r[np.isfinite(r)]
    if r.size < 20:
        return float("nan"), float("nan")
    return float(np.percentile(r, 2.5)), float(np.percentile(r, 97.5))


# --------------------------------------------------------------------------- #
def _outcomes_for(group: str) -> list[str]:
    if group.startswith("offense") or group == "protection":
        return _OFF_OUTCOMES
    if group.startswith("defense") or group == "pass_rush":
        return _DEF_OUTCOMES
    return _ST_OUTCOMES


def _analyse() -> pl.DataFrame:
    cfg = load_strength_config()["research"]
    groups: dict[str, list[str]] = cfg["factor_groups"]
    n_iter, seed = cfg["bootstrap_iters"], cfg["seed"]
    horizon = cfg["walk_forward_horizon"]

    all_metrics = sorted({m for ms in groups.values() for m in ms})
    sv = _season_factor_values(all_metrics)
    so = _season_outcomes()
    assoc = sv.join(so, on=["season", "team"], how="inner")
    chrono = _chronological_panel(all_metrics, horizon)

    rows = []
    for group, metrics in groups.items():
        for factor in metrics:
            fam = factor.split(".")[0]
            sign = orient_sign(factor) or 1
            for outcome in _outcomes_for(group):
                a = assoc.filter(pl.col("factor") == factor)
                ax = a.get_column("factor_value").to_numpy().astype(float)
                ay = a.get_column(outcome).to_numpy().astype(float)
                assoc_r = _pearson(ax, ay)
                assoc_rho = _spearman(ax, ay)

                # per-season stability of the association
                per = []
                for s in _ASSOC_SEASONS:
                    asub = a.filter(pl.col("season") == s)
                    per.append(_pearson(
                        asub.get_column("factor_value").to_numpy().astype(float),
                        asub.get_column(outcome).to_numpy().astype(float),
                    ))
                per = np.array([p for p in per if np.isfinite(p)])
                stab_mean = float(np.mean(per)) if per.size else float("nan")
                stab_sd = float(np.std(per, ddof=1)) if per.size >= 2 else float("nan")
                frac_sign = (
                    float(np.mean(np.sign(per) == np.sign(stab_mean))) if per.size else float("nan")
                )

                # chronological
                cr = crho = c_lo = c_hi = float("nan")
                n_pred = 0
                if not chrono.is_empty():
                    c = chrono.filter(pl.col("metric") == factor)
                    if not c.is_empty():
                        cx = c.get_column("feature_value").to_numpy().astype(float)
                        cy = c.get_column(outcome).to_numpy().astype(float)
                        cl = (c.get_column("season").cast(str) + "|" + c.get_column("team")).to_numpy()
                        cr, crho = _pearson(cx, cy), _spearman(cx, cy)
                        c_lo, c_hi = _cluster_boot_ci(cx, cy, cl, n_iter=n_iter, seed=seed)
                        n_pred = int(np.isfinite(cx).sum())

                tier = _evidence_tier(cr, c_lo, c_hi, frac_sign, n_pred, assoc_r)
                rows.append({
                    "group": group, "factor": factor, "family": fam, "outcome": outcome,
                    "orientation": "higher_metric_higher_outcome" if sign > 0 else "higher_metric_lower_outcome",
                    "association_pearson": assoc_r, "association_spearman": assoc_rho,
                    "association_r2": assoc_r ** 2 if np.isfinite(assoc_r) else float("nan"),
                    "n_association": len(a),
                    "stability_mean_r": stab_mean, "stability_sd_r": stab_sd,
                    "stability_frac_same_sign": frac_sign, "n_seasons": int(per.size),
                    "chronological_pearson": cr, "chronological_spearman": crho,
                    "chronological_pearson_ci_lo": c_lo, "chronological_pearson_ci_hi": c_hi,
                    "chronological_r2": cr ** 2 if np.isfinite(cr) else float("nan"),
                    "n_chronological": n_pred,
                    "evidence_tier": tier,
                })
    df = pl.DataFrame(rows)
    # redundancy: rank factors within (group, outcome) by |chronological pearson|
    df = df.with_columns(
        pl.col("chronological_pearson").abs().rank("min", descending=True)
        .over(["group", "outcome"]).alias("rank_in_group"),
    ).with_columns(
        (pl.col("rank_in_group") == 1).alias("group_leader"),
        pl.lit("factors within a group are correlated; count the group as ONE line of evidence")
        .alias("redundancy_note"),
    )
    return df.sort(["outcome", "group", "rank_in_group"])


def _evidence_tier(cr, lo, hi, frac_sign, n_pred, assoc_r) -> str:
    """Transparent bucketing. Effect size FIRST, then whether the chronological CI
    clears zero, then temporal consistency. Never returns "important"."""
    detectable = (
        np.isfinite(lo) and np.isfinite(hi) and (lo > 0 or hi < 0) and n_pred >= 300
    )
    stable = np.isfinite(frac_sign) and frac_sign >= 0.8
    a = abs(cr) if np.isfinite(cr) else 0.0
    if detectable and a >= 0.30:
        return "strong + temporally consistent" if stable else "strong but variable across seasons"
    if detectable and a >= 0.15:
        return "moderate + temporally consistent" if stable else "moderate but variable across seasons"
    if detectable:
        return "weak but statistically detectable chronologically"
    if np.isfinite(assoc_r) and abs(assoc_r) >= 0.30 and stable:
        return "descriptive association only (no chronological signal)"
    return "weak / insufficient evidence"


# --------------------------------------------------------------------------- #
def run_factor_analysis() -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    df = _analyse()

    scoring = df.filter(pl.col("outcome") == "points_scored")
    defense = df.filter(pl.col("outcome") == "points_allowed")
    winning = df.filter(pl.col("outcome").is_in(["win", "rolling_win_pct_4", "point_differential"]))

    scoring.write_csv(OUT / "scoring_factor_analysis.csv")
    defense.write_csv(OUT / "defense_factor_analysis.csv")
    winning.write_csv(OUT / "winning_factor_analysis.csv")
    df.write_csv(OUT / "factor_summary.csv")

    def _top(sub: pl.DataFrame, outcome: str) -> list[dict]:
        s = sub.filter((pl.col("outcome") == outcome) & pl.col("group_leader")).sort(
            pl.col("chronological_pearson").abs(), descending=True, nulls_last=True
        )
        return s.select(
            "group", "factor", "association_pearson", "chronological_pearson",
            "chronological_pearson_ci_lo", "chronological_pearson_ci_hi",
            "stability_frac_same_sign", "n_chronological", "evidence_tier",
        ).head(6).to_dicts()

    summary = {
        "method": {
            "association": "contemporaneous season-level Pearson/Spearman (descriptive)",
            "chronological": "walk-forward: shrunk season-to-date metric (wk 3-14) vs mean "
                             "outcome over next 4 REG games, 2019-2025, cluster bootstrap CI",
            "stability": "season-by-season association correlation, 2016-2025",
            "caveat": "correlation is not causation; a large correlation alone does not make a "
                      "factor 'important'; factors within a group are redundant",
        },
        "n_factor_outcome_rows": df.height,
        "evidence_tier_counts": dict(
            df.group_by("evidence_tier").len().sort("len", descending=True).iter_rows()
        ),
        "scoring_group_leaders": _top(df, "points_scored"),
        "points_allowed_group_leaders": _top(df, "points_allowed"),
        "winning_group_leaders": _top(df, "win"),
        "point_differential_group_leaders": _top(df, "point_differential"),
    }
    (OUT / "factor_research_summary.json").write_text(
        __import__("json").dumps(summary, indent=2, default=str)
    )
    return summary
