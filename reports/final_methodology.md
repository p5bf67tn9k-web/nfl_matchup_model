# Final Methodology — NFL Team-Strength Research System

_Last updated 2026-09-09. Companion: [`reports/2026_research_guide.md`](2026_research_guide.md)._

---

## 1. What the project does

It is a **transparent, auditable research system** that, for every NFL team and
every week of the season, measures **unit-level strength** on nine football
dimensions and lets a person inspect every number behind each measurement. It
also runs a **factor study**: which already-implemented football statistics show
the strongest and most temporally stable evidence of association with — and
chronological predictive information about — **scoring, points prevention, and
winning**.

Concretely it produces, each week:

- offensive and defensive strength (and seven sub-unit indices) for all 32 teams,
- the raw metric values, league reference, sample size and confidence behind each,
- the change from the previous week and from the preseason baseline,
- W-L record, points for / against / differential,
- a factor-evidence table (association vs chronological vs stability),
- three markdown reports and a machine-readable summary.

## 2. What it does NOT do

- It does **not** predict game winners, final scores, point spreads, or win
  probabilities.
- It has **no** betting logic and uses **no** market data (spreads, totals,
  moneylines, odds). Those columns are stripped by the point-in-time engine and a
  test asserts they never reach a strength or research frame.
- It does **not** produce a single black-box "overall team rating". The domain
  indices are explicit arithmetic; the underlying metrics are always shown.
- It does **not** model matchups. The Phase 5 experiment concluded
  `STOP_NO_RELIABLE_MATCHUP_SIGNAL` — the tested representation of matchup
  strength gave no reliable incremental information for the tested target. That
  conclusion stands. Matchup comparisons may be shown descriptively; they are not
  a model target.
- It introduces **no new data sources** and **no new metrics** beyond those
  already validated in Phases 1–4.

## 3. Data sources

Single source: **nflverse** via `nflreadpy` 0.1.5 (CC-BY-SA). Canonical
season-partitioned Parquet under `data/processed/`, built by `matchup.cli
ingest`. Seasons: pbp / schedules / rosters / injuries 2013+, NGS 2016+, PFR
2018+. The 2026 season is a live probe — the system runs in **preseason-baseline
mode** until Week 1 games are played, then updates automatically.

Game **results** (final scores, wins) are read by a dedicated accessor
(`matchup.strength.results.team_game_results`) that returns only completed games
and is never joined into a feature frame — it is the research **dependent
variable** and the snapshot **record**, nothing else.

## 4. Metric definitions

Unchanged from Phase 2. The 26 team-level rates used here are defined in
`config/metrics.yaml` (exact numerator / denominator / eligibility / exclusions)
and implemented in `matchup.metrics.families`. Directionality
(`higher_better` / `lower_better` / `neutral`) is taken from that config.
`config/strength.yaml` lists exactly which metrics feed which domain index and
which are display-only.

Metrics feeding indices, by domain:

| Domain | Index name | Member metrics |
|---|---|---|
| `offense_overall` | Offensive Strength Index | epa_per_play, success_rate, early_down_epa_per_play |
| `passing_offense` | Passing-Offense Strength Index | pass_epa_per_dropback, pass_success_rate, explosive_pass_rate |
| `rushing_offense` | Rushing-Offense Strength Index | rush_epa_per_play, rush_success_rate |
| `pass_protection` | Pass-Protection Strength Index | sack_rate_allowed, qb_hit_rate_allowed |
| `defense_overall` | Defensive Strength Index | def epa_per_play, success_rate, early_down_epa_per_play (allowed) |
| `passing_defense` | Pass-Defense Strength Index | def pass_epa_per_dropback, pass_success_rate (allowed) |
| `rushing_defense` | Run-Defense Strength Index | def rush_epa_per_play, rush_success_rate, explosive_rush_rate (allowed) |
| `pass_rush` | Pass-Rush Strength Index | qb_hit_rate_generated, sack_rate_generated |
| `special_teams` | Special-Teams Strength Index | st_epa_per_play |

Display-only (shown on team profiles, not in any index): `proe`,
`explosive_rush_rate` (offense), `rush_stuffed_rate_approx`,
`explosive_pass_rate` (defense), `fg_pct`. These are Phase 3
`NOT_RANK_PERSISTENT` or neutral-direction.

## 5. Team-strength methodology

For a team **through week W** of a season (regular season only, weeks ≤ W):

1. **Season-to-date raw value** — sum the metric's raw components over the team's
   games in weeks 1..W, recompute the rate from the sums (never average
   per-game rates).
2. **Shrink** toward the historical league mean:
   `shrunk = ref_mean + n_games/(n_games + k) · (raw − ref_mean)`
   with `k` the frozen Phase 4 walk-forward-selected constant for that metric
   (`config/strength.yaml`, median over the 2019–2025 evaluation seasons).
3. **Express as a z-score** vs the historical reference:
   `z_shrunk = (shrunk − ref_mean) / ref_sd`.
4. **Orient**: `oriented_z = +z_shrunk` if higher-is-better, `−z_shrunk` if
   lower-is-better (so higher oriented z = better on every metric).
5. **Cross-sectional rank / percentile** among the 32 teams at the same week.
6. **Domain index** = arithmetic mean of the domain's member `oriented_z` values.

The index is in **reference-standard-deviation units**. It is a *transparent
research index*, **not** points, **not** a probability, **not** a calibrated
rating. Every member metric (raw value, ref mean/SD, n, shrunk value, percentile,
confidence) is carried in `outputs/team_strength/team_metrics_weekly.parquet` and
printed in `reports/team_profiles.md`. No weights are learned; every domain uses
equal weights, stated in config.

**Preseason baseline (week 0)** = the team's prior full regular season value,
shrunk toward the current season's 3-season reference. Flagged
`prior_season_only` confidence.

## 6. Shrinkage methodology

Regression-to-the-mean shrinkage `w = n/(n+k)` was validated in Phase 4
(`SHRINKAGE_ADDS_VALUE` for 39 of 42 candidate metrics; it closed the Phase 3 gap
between rank persistence and RMSE skill). `k` is **not** re-fit here — the frozen
Phase 4 per-metric constants are reused verbatim. Early-season values are
therefore pulled strongly toward the league reference (e.g. after 1 game with
k = 8, the raw value gets weight 1/9), which is the intended behaviour and is
surfaced through the confidence flag.

## 7. Historical baselines

The reference distribution for season S is the set of **team-season values over
the 3 completed seasons before S's Week 1** (`completed_seasons_asof`, the same
rule as Phase 2/3 normalization), filtered to teams meeting the Phase 2
minimum-opportunity bar. `ref_mean` and `ref_sd` are the mean and sample SD of
that distribution. For 2026 the reference is 2023–2025.

## 8. Weekly methodology

`matchup.cli weekly-research` (see §15):

1. optionally ingest / live-probe nflverse (failures are caught, not fatal);
2. detect the current season and the latest completed regular-season week
   (`latest_completed_week`); 0 → preseason mode;
3. rebuild the historical + current per-metric and domain panels;
4. refresh the factor research (or reuse the cached summary);
5. take the **current**, **previous-week**, and **preseason** snapshots and diff
   the domain indices and the per-metric shrunk values;
6. write the machine-readable outputs and the three reports;
7. run point-in-time canary checks and write `outputs/diagnostics/pit_checks.csv`;
8. write `outputs/research/research_summary.json`.

## 9. Scoring analysis

`outputs/research/scoring_factor_analysis.csv`. Candidate offensive factors
(seven efficiency metrics, two explosiveness metrics, PROE, two protection
metrics) vs **points scored**, under three lenses (§12). Observed on 2016–2025:

- **Offensive EPA/play** — association r ≈ 0.89, chronological r ≈ 0.40 [0.32,
  0.47], same sign in all 10 seasons → *strong + temporally consistent*.
- **Explosive-pass rate** — association r ≈ 0.62, chronological r ≈ 0.32 →
  *strong + temporally consistent*.
- **Sack rate allowed** — association r ≈ −0.51, chronological r ≈ −0.23 →
  *moderate + temporally consistent*.
- **PROE** — association r ≈ 0.28, chronological r ≈ 0.05 (CI includes 0) →
  *weak / insufficient*.

## 10. Defensive (points-allowed) analysis

`outputs/research/defense_factor_analysis.csv`. Candidate defensive factors vs
**points allowed**:

- **Defensive EPA/play allowed** — association r ≈ 0.80, but chronological
  r ≈ 0.17 [0.09, 0.26] → *moderate + temporally consistent*, and clearly
  weaker forward-looking than the offensive equivalent.
- **Pass-rush QB-hit rate** — association r ≈ −0.36, chronological r ≈ −0.13 →
  *weak but statistically detectable*.
- **Explosive-rush rate allowed** — association r ≈ 0.34, chronological r ≈ 0.13
  → *weak but statistically detectable*.

The gap between the association and chronological columns is the central result:
**a defense's points-allowed relationship is much more "what already happened"
than "what will happen next"**, consistent with Phase 3's finding that defensive
metrics rank-persist but do not beat baselines on forward RMSE.

## 11. Winning analysis

`outputs/research/winning_factor_analysis.csv`. All factor groups vs **win**,
**rolling win %**, and **point differential**:

- Offensive passing efficiency and explosiveness carry the most chronological
  information about winning (r ≈ 0.22–0.29).
- Pass protection (sack / hit rate allowed) is a *moderate + temporally
  consistent* negative correlate of winning.
- Defensive EPA/play allowed is a *moderate + temporally consistent* negative
  correlate (r ≈ −0.19) — again weaker forward-looking than the offensive side.
- No single factor is labelled "most important". Within a factor group the
  metrics are redundant (§12) and count as one line of evidence.

## 12. The three research lenses (association / chronological / stability)

| Lens | What it measures | How | Interpretation |
|---|---|---|---|
| **association** | Same-season, descriptive | Season-level Pearson & Spearman of the team-season metric vs the team-season outcome, 2016–2025 | "Teams that did more of X also scored/allowed/won more **that season**." Not predictive, not causal. |
| **chronological** | Predictive-looking | Walk-forward: shrunk season-to-date metric through week W (W = 3..14, seasons 2019–2025) vs the team's mean outcome over its **next 4 games**; Pearson/Spearman with a cluster bootstrap 95% CI (cluster = team × season, 2000 iterations) | "Knowing X now carries information about the next month of games." Still a correlation, not a guarantee. |
| **stability** | Temporal consistency | The association correlation computed **separately per season**; report the mean, SD, and fraction of seasons with the same sign | Guards against a relationship that is really one or two unusual seasons. |

**Evidence tier** (transparent rule, `config` thresholds, never "important"):
effect size first (|chronological r| ≥ 0.30 strong, ≥ 0.15 moderate, else weak),
then whether the chronological CI clears zero with n ≥ 300, then whether the
association is same-sign in ≥ 80 % of seasons. A large correlation with no
chronological signal is `descriptive association only`.

## 13. Redundancy

The Phase 2 redundancy report showed several metrics are near-duplicates (e.g.
the various EPA rates). The factor table therefore groups metrics
(`offense_efficiency`, `offense_explosiveness`, `protection`,
`defense_efficiency`, …), ranks factors **within** each group, and flags the
`group_leader`. The reports and summary present **group leaders only** and state
explicitly: *factors within a group are correlated — count the group as one line
of evidence.* This is also why the domain indices are not a sum of all metrics.

## 14. Point-in-time methodology

- Every feature is season-to-date **through week W** — it uses only that team's
  games in weeks ≤ W. A poisoned-future-game test asserts a fabricated week-99
  game changes no earlier value.
- The historical reference for season S uses only seasons completed before S's
  Week 1.
- `game_metrics_batch` stamps each game with `data_asof = kickoff + duration +
  publish lag`; windowing filters on it. Verified by the inherited Phase 3/4
  leakage suite.
- The results accessor returns only games that have kicked off; a test asserts
  no returned game has a future `data_asof` and that 2026 is empty pre-Week-1.
- No market columns anywhere — enforced by test.
- `outputs/diagnostics/pit_checks.csv` records five canaries each run.

## 15. Limitations — what can and cannot be concluded

**Can:**
- Rank teams on each of nine football dimensions, relative to a 3-season league
  reference, with sample size and confidence attached.
- See how a team's indices and underlying metrics have moved week to week and vs
  preseason.
- See which football statistics have the strongest, most temporally consistent
  **association** with scoring / points-allowed / winning, and which additionally
  carry **chronological** (forward-looking) information.

**Cannot:**
- Predict a specific game's winner, score, or margin — not attempted, not
  supported.
- Claim causation. Every relationship in the factor tables is a correlation.
- Treat the domain index as an absolute or calibrated quantity — it is a
  z-score-scale research index.
- Assume the early-season (Week 1–4) indices are precise — they are shrunk hard
  and flagged low/medium confidence.
- Conclude anything about matchups beyond the Phase 5 null result.

## 16. How to run the weekly process

```bash
make weekly-research        # ingest + rebuild strength + refresh research + reports (~1 min)
# or, without re-ingesting:
PYTHONPATH=src .venv/bin/python -m matchup.cli weekly-research
# force a specific through-week (e.g. re-run Week 3 later):
PYTHONPATH=src .venv/bin/python -m matchup.cli weekly-research --week 3
```

Supporting commands: `make team-strength` (panels only), `make factor-analysis`
(research only), `make final-build` (everything + lint + tests).

Outputs land in `outputs/team_strength/`, `outputs/rankings/`, `outputs/weekly/`,
`outputs/research/`, `outputs/diagnostics/`; reports in
`reports/league_overview.md`, `reports/team_profiles.md`,
`reports/weekly_research.md`.
