# 2026 Research Guide — how to read the weekly outputs

This is the practical companion to
[`reports/final_methodology.md`](final_methodology.md). It explains what each
weekly output file contains and how to interpret it.

---

## The one weekly command

```bash
make weekly-research
```

Runs in ~1 minute. Before Week 1 it produces a **preseason baseline**; from Week 1
on it produces the **through-Week-W** snapshot for the latest completed week. To
regenerate an earlier week: `... weekly-research --week 3`.

---

## What you get

### Reports (`reports/`)

| File | Use it to… |
|---|---|
| `league_overview.md` | Rank all 32 teams on each of the nine strength indices; see the index formula; see the results context table. |
| `team_profiles.md` | For one team: its nine domain indices with league rank and week/preseason deltas, **and** the full underlying metric table (raw value, league reference mean/SD, sample size, shrunk value, percentile, confidence, Phase 3 status). |
| `weekly_research.md` | What moved this week (biggest offense/defense risers & fallers), biggest metric changes vs preseason, and the historical factor-evidence leaders for scoring / points-allowed / winning, with caveats. |

### Machine-readable (`outputs/`)

| File | Grain | Key columns |
|---|---|---|
| `team_strength/team_metrics_weekly.parquet` | team × season × week × metric | `raw_value, ref_mean, ref_sd, n_games, n_opportunities, k, shrunk_value, z_shrunk, oriented_z_shrunk, in_index, phase3_status` |
| `team_strength/team_strength_weekly.parquet` | team × season × week × domain | `index_value, rank_of_league, delta_vs_prev_week, delta_vs_preseason, n_metrics_used, min_confidence` |
| `rankings/team_rankings_weekly.csv` | team × season × week | each domain's `index_value` and `rank_of_league` as columns |
| `weekly/weekly_team_snapshot.csv` | team (current week) | record, points for/against/diff, all nine indices + ranks, `top_strength_domain`, `top_weakness_domain`, `overall_confidence` |
| `weekly/weekly_changes.csv` | team × domain (current week) | `index_value, rank_of_league, delta_vs_prev_week, rank_change_vs_prev_week, delta_vs_preseason` |
| `weekly/weekly_metric_detail.csv` | team × metric (current week) | the full per-metric numbers + `delta_shrunk_vs_prev_week`, `delta_shrunk_vs_preseason` |
| `research/scoring_factor_analysis.csv` | factor × outcome | association / chronological / stability columns + `evidence_tier` |
| `research/defense_factor_analysis.csv` | factor × outcome (points allowed) | same |
| `research/winning_factor_analysis.csv` | factor × outcome (win / win% / point diff) | same |
| `research/factor_summary.csv` | all of the above combined | `+ group, rank_in_group, group_leader, redundancy_note` |
| `research/research_summary.json` | one object | the week's headline: mode, movers, factor group leaders, PIT check results |
| `diagnostics/pit_checks.csv` | one row per canary | `check, passed, detail` |

---

## How to read a strength index

- **Scale**: reference standard deviations. `+1.0` ≈ one SD better than the
  2023–2025 league average team on that dimension. `0` ≈ average. It is **not**
  points and **not** a probability.
- **Direction**: higher is always better (metrics are oriented before averaging).
- **Rank**: 1 = best in the league that week.
- **Always check the members**: `n_metrics_used` vs `n_metrics_defined` in the
  domain table, then the per-metric rows in `weekly_metric_detail.csv` /
  `team_profiles.md`. The index never replaces the underlying numbers.
- **Confidence**: `prior_season_only` (preseason) → `low` (< 3 games) → `medium`
  (3–5) → `high` (≥ 6). Treat Week 1–4 indices as directional only.

## How to read the factor tables

Three numbers per factor, per outcome:

- **association_pearson** — same-season descriptive correlation. Big (0.6–0.9 for
  the efficiency metrics). *This is not a prediction.*
- **chronological_pearson** (+ CI) — the walk-forward correlation: the metric now
  vs the next 4 games' outcome. Always smaller than the association (typically
  0.15–0.40). The CI is cluster-bootstrapped; if it clears 0 the relationship is
  detectable.
- **stability_frac_same_sign** — fraction of the 10 seasons where the association
  had the same sign. ≥ 0.8 means the relationship is not driven by one odd year.

`evidence_tier` combines these (effect size → CI → stability). It never says
"important". `group_leader = true` marks the representative of a redundant group;
read the group, not the individual metric.

**Headline pattern (2016–2025):** offensive efficiency and explosiveness carry
the most chronological information about scoring, point differential, and
winning; defensive metrics associate strongly within a season but carry
noticeably less forward-looking information — the offense/defense asymmetry seen
in every earlier phase.

## Preseason vs in-season

| | Preseason (Week 0) | In-season (Week W ≥ 1) |
|---|---|---|
| Metric source | prior full season, shrunk | weeks 1..W season-to-date, shrunk |
| Confidence | `prior_season_only` | `low` → `high` as games accumulate |
| `delta_vs_prev_week` | 0 (no prior week) | real |
| `delta_vs_preseason` | 0 | movement from the baseline |

## When something looks wrong

1. Check `outputs/diagnostics/pit_checks.csv` — all five canaries should be
   `passed = true`.
2. Check `research_summary.json` → `mode` and `through_week` match reality.
3. Re-run: `make weekly-research`. The pipeline is deterministic; a rebuild
   should reproduce every shrunk value to ~1e-12.
4. If 2026 data has not landed yet, the system stays in preseason mode — that is
   expected, not a bug.
