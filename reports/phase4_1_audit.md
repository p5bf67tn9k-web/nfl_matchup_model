# Phase 4.1 Report — Phase 4 Audit & Protocol Reconciliation

**Project:** `nfl_matchup_model`
**Run date:** 2026-09-08
**Scope:** audit and sensitivity only. **No** matchup interactions, ratings, composites, expected
performance, expected score, game prediction, betting logic, or market features were built. Nothing
here searches for a better result; the question is whether the Phase 4 result is methodologically
sound and matches the approved protocol.

Artefacts: `outputs/phase4/audit_candidate_universe.csv`, `ridge_sanity.csv`,
`shrinkage_n_sensitivity.csv`, `shrinkage_k_sensitivity.csv`, `stage_b_reference_audit.csv`,
`audit_excluded_metrics_shrinkage.csv`, `phase4_audit_summary.json`.

---

## 1. Executive verdict

| audit item | finding |
|---|---|
| Candidate universe | **Matches the approved protocol.** No metric that qualifies under the approved 4-part rule was excluded. The frozen config's rule statement is a *reformulation*, provably equivalent on this data. |
| Ridge sanity | **Weakly identified overall; metric-dependent.** The *median* opponent-coefficient variance in the real ridge is only ~3% above the random-permutation null. Per family: **team defense** has a clear real opponent signal (opponent-coef sd 69% above the null, 73% of fitted variance); **QB, WR, pass protection, team offense** are ~10–20% above the null (small real signal); **RB** is *at or below* the null (opponent effects unidentifiable — a back faces each defense ~once). In every case, adjusting the feature for these (mostly weak) opponent effects does not improve future-performance prediction. |
| Opportunity-count `n` sensitivity | **Robust.** Switching from game-count `n` to an opportunity-count proxy changes the qualitative conclusion for **0 of 40** metric×horizon cells. Game-count `n` is if anything marginally better. |
| `k` sensitivity | **Robust.** The OOS-RMSE-vs-`k` curves are flat-bottomed; every representative metric's shrinkage advantage holds across `k ∈ {4, 8, 12}` (noisy metrics want `k ≥ 12`). No conclusion depends on a narrow `k`. |
| Stage-B reference | **One implementation defect found.** The original code selected the reference as the better of `{raw, shrunk}` using the **OOS primary-cell skill** — a post-hoc selection. **Fixed** (fixed reference = `shrunk_feature`) and re-run: **1 of 78** verdicts changed (a ≈0 vs ≈0 cell), **no conclusion** changed. |
| Leakage | **Green.** All 114 tests pass (108 prior + 6 new audit tests). No new leakage path uncovered; the Stage-B defect was an evaluation-yardstick issue, not a feature leak. |
| **Recommendation** | **`APPROVE_PHASE_4`** |

---

## 2. Candidate-universe reconciliation (`audit_candidate_universe.csv`)

**Approved Phase 4 universe** (4-part rule): (1) Phase 3 `VALIDATED_PERSISTENCE`, (2) Phase 3
`RANK_PERSISTENT` with sufficient data, (3) Phase 3 `UNVALIDATED` with meaningful one-horizon
evidence, (4) the two named NGS metrics.

**Implemented rule** (frozen `phase4_validation.yaml`): `RANK_PERSISTENT` with `primary_n_h4 ≥ 300`,
plus the two NGS metrics. **42 metrics.**

**Reconciliation:**
* Rule (1): all 3 `VALIDATED_PERSISTENCE` are `RANK_PERSISTENT` → in.
* Rule (2): the 40 `RANK_PERSISTENT` metrics. The `primary_n_h4 ≥ 300` clause is **inert** — the
  smallest `primary_n_h4` among them is 1466.
* Rule (3): every Phase 3 `UNVALIDATED` metric (9 of them) is also `RANK_PERSISTENT` → already
  captured by (2). None has positive `skill_vs_league` at either horizon anyway.
* Rule (4): the 2 NGS → in.

**Excluded (8):** exactly the 8 Phase 3 `NOT_RANK_PERSISTENT` metrics
(`qb.interception_rate`, `special_teams.fg_pct`, `pass_rush.sack_rate_generated`,
`rb.explosive_rush_rate`, `wr.epa_per_target`, `team_defense.explosive_pass_rate`,
`team_defense.rush_epa_per_play`, `team_offense.explosive_rush_rate`). All have **negative**
`skill_vs_league` at **both** horizons in Phase 3 (−0.04 to −0.13) and `skill_vs_prior_season ≈ 0`.
None satisfies "meaningful evidence at one horizon" under any reasonable reading — they are
rank-noise with negative point-prediction skill.

**Additional-candidate check (`audit_excluded_metrics_shrinkage.csv`):** Stage-A shrinkage was run
on all 8 excluded metrics as an audit. **All 8 benefit from shrinkage** (`skill_shrunk_vs_raw` H4
= +0.12 to +0.20); 6 of 8 even edge past the league mean after shrinkage (+0.007 to +0.022). Adding
them would only produce more `SHRINKAGE_ADDS_VALUE` verdicts and would reinforce — not change — the
Phase 4 story.

**Verdict:** the implemented universe = the approved universe. The narrower phrasing is a
**disclosed reformulation** (equivalent set on this data), not a substantive narrowing. **No
broader candidate set needs to be run before Phase 5.**

---

## 3. Ridge sanity (`ridge_sanity.csv`)

Fitted deterministically at a mid-season cutoff (week 10, 2023; trailing-2-season data), real vs
permuted opponent labels, at the frozen per-family alpha:

| family (metric) | alpha | opponent coef sd (real / permuted) | fitted-var frac opponent (real / permuted) | verdict |
|---|---|---|---|---|
| team_defense (`epa_per_play`) | 30 | **0.038 / 0.022** (real +69%) | **0.73 / 0.49** | **real, identifiable** — EPA allowed is opponent-offense-driven |
| pass_protection (`sack_rate_allowed`) | 30 | 0.0046 / 0.0038 (+20%) | 0.20 / 0.14 | small real signal |
| wr (`yards_per_target`) | 30 | 0.290 / 0.248 (+17%) | 0.12 / 0.09 | small real signal |
| qb (`epa_per_dropback`) | 30 | 0.069 / 0.060 (+15%) | 0.47 / 0.39 | small real signal |
| team_offense (`epa_per_play`) | 3 | 0.034 / 0.031 (+11%) | 0.25 / 0.21 | small real signal |
| rb (`rush_epa_per_att`) | 30 | 0.056 / **0.064** (−13%) | 0.32 / 0.37 | **unidentifiable** — real ≤ null |

**Answer to the A-vs-B question (spec §2):** predominantly **A, with the strength varying by
family**:
* **team defense**: opponent effects are clearly real (opponent-coef sd 69% above the null, 73% of
  fitted variance) and genuinely estimable — the ridge is working — they are simply **non-predictive
  as a feature transform** for future same-unit performance.
* **QB, WR, pass protection, team offense**: a small real opponent signal (10–20% above the null),
  still non-predictive.
* **RB**: opponent effects are **not identifiable** — a back faces each defense ~once, so real
  variance is at or below the permutation null; those "opponent coefficients" are fitted noise.

So the `NO_INCREMENTAL_VALUE` verdict stands, and the *median* opponent structure the ridge fits is
only marginally above noise — but for team defense specifically it is real, which the Phase 4 report
now reflects (§4, updated).

The ridge diagnostics are otherwise healthy: intercepts ≈ the metric mean, small home coefficients
(`epa_per_play` +0.009 offense / −0.008 defense; `yards_per_target` +0.17 yd), entity-coefficient
variance dominant where expected (offense 74% of fitted variance; defense 24%), residual variance
below raw metric variance, in-sample R² 0.06–0.14.

---

## 4. Opportunity-count sensitivity (`shrinkage_n_sensitivity.csv`) — AUDIT ONLY

The frozen Phase 4 uses `n` = games in the feature window. This audit re-ran Stage-A shrinkage with
`n` = opportunity count expressed in game-equivalents (`feat_opp_n / C_family`, `C_family` = the
league-average opportunities per game for that denominator, a fixed constant), **same k grid, same
walk-forward selection**.

| | game `n` | opportunity `n` |
|---|---|---|
| metric×horizon cells where the qualitative conclusion changes | — | **0 of 40** |
| median H4 `skill_shrunk_vs_raw` | ≈ +0.11 | ≈ +0.10 |
| largest disagreement | `rb.rush_success_rate` game +0.134 vs opp +0.115 (−0.019); `wr.yards_per_reception` +0.085 vs +0.093 (+0.009) | |

Opportunity `n` is *slightly worse* for a handful of metrics whose plays-per-game varies a lot
(`rb.rush_success_rate`, `wr.adot`) and marginally better for a few. **The major shrinkage finding
is robust to a more information-sensitive sample-size measure.** Not adopted — a sensitivity check,
not a new status system.

---

## 5. `k` sensitivity (`shrinkage_k_sensitivity.csv`) — AUDIT ONLY

Fixed `k` applied walk-forward (no selection), OOS RMSE pooled over primary weeks / horizons 2 & 4:

| metric (noise class) | OOS RMSE @ H4 by k `{1,2,4,8,12,16}` | raw | league |
|---|---|---|---|
| `qb.epa_per_dropback` (moderate) | .173 .167 **.162** .160 .161 .162 | .184 | .178 |
| `team_offense.epa_per_play` (persistent) | .109 .107 **.105** .106 .107 .108 | .113 | .122 |
| `team_defense.epa_per_play` (moderate) | .116 .113 .109 .107 .106 **.106** | .121 | .110 |
| `team_offense.proe` (persistent) | .0469 .0464 **.0463** .0471 .0481 .0489 | .0482 | .0558 |
| `rb.fumble_lost_rate` (noisy) | .0125 .0119 .0112 .0105 .0102 **.0101** | .0134 | .0099 |
| `special_teams.st_epa_per_play` (noisy) | .154 .151 .147 .145 **.1445** .145 | .160 | .151 |

Every curve is **flat-bottomed** — the difference between the best and second-best `k` is < 1.5% of
RMSE. The shrunk feature beats `raw` at every `k` in the grid, and beats the league mean at every
`k` for the persistent metrics. **No conclusion depends on a narrow `k`.** (`proe`'s advantage over
`raw` is tiny at every `k`, consistent with its `NO_INCREMENTAL_VALUE` shrinkage status.)

---

## 6. Stage-B reference audit (`stage_b_reference_audit.csv`)

**Defect found.** The original `phase4.py` chose the Stage-B reference as:

```python
ref = "shrunk_feature" if per_h["shrunk"][h]["skill_vs_reference"] > 0 else "raw_feature"
```

where `skill_shrunk_vs_raw` is computed on the **OOS 2019–2025 primary cell**. This is a **post-hoc
reference selection** — the yardstick for opponent adjustment is chosen by looking at an OOS result.
It does not leak a *feature* (it selects the *comparison baseline*), but it violates the intent of a
frozen protocol.

**Fix applied.** `phase4.py` now uses the fixed reference `shrunk_feature` (the chain layer
immediately before opponent adjustment). Config updated. Phase 4 re-run.

**Impact.** Comparing the original (OOS-selected) verdicts against a fixed `shrunk_feature`
reference: **77 of 78** (metric, horizon) verdicts are identical. The single exception is
`rb.rush_epa_per_att` H4 — original `skill_vs_reference` +0.0018, fixed −0.0002 (both ≈ 0,
`NO_INCREMENTAL_VALUE` either way). Under the fixed reference, mean `skill_oppadj_vs_shrunk` at H4
= **−0.028** (max +0.011). **Opponent adjustment still adds no value; no Phase 4 conclusion
changes.**

The frozen `outputs/phase4/` files now carry the fixed-reference numbers; the audit CSV documents
the before/after.

---

## 7. Leakage status

**All 114 tests green** (108 prior + 6 new audit tests in `tests/unit/test_phase4_audit.py`):
`shrink()` accepts an alternative `n` column; forced-fallback gives a fixed `k`; the Stage-B
reference is a constant string (not OOS-selected — regression test for the §6 fix); the audit
candidate universe has no "approved-but-not-implemented" metric; the excluded set is exactly the 8
`NOT_RANK_PERSISTENT` metrics.

Existing leakage tests **not weakened**. No new leakage path was uncovered — confirmed:
`k` selection reads only target seasons < S; opportunity counts are computed from the same
feature-window rows as the game count; ridge fits contain only games with `data_asof < kickoff`;
randomised opponent labels are a within-fit permutation with no external data; no market/result
column is reachable; the Phase-4 future-row poison tests are unchanged and pass.

---

## 8. Protocol deviations (consolidated)

| # | deviation | disclosed in | material? |
|---|---|---|---|
| P4-A | ridge `alpha` selected once per (family, metric) on 2016–2018, not per OOS season | `phase4_validation.yaml`, Phase 4 report §1 | no (opponent adjustment adds nothing at any alpha) |
| P4-B | observation history extended to 2016–2018 for `k`/`alpha` training; evaluation stays 2019–2025 | `phase4_validation.yaml`, Phase 4 report §1 | no |
| P4-C | `oppadj_raw = league_mean + centred_strength` (scale fix) | Phase 4 report §1 | no |
| **P4.1-D** | **Stage-B reference was OOS-selected (post-hoc); now fixed to `shrunk_feature`** | **this report §6; config updated** | **no — 1/78 verdicts, 0 conclusions** |
| P4.1-E | candidate-universe rule *phrased* as `RANK_PERSISTENT + n≥300 + NGS` rather than the approved 4-part prose | this report §2 | no — provably the same set |

---

## 9. What changes to the Phase 4 conclusions

**Nothing substantive.**

* Stage A — **39 of 42 → `SHRINKAGE_ADDS_VALUE`** — unchanged, and now shown robust to `k` and to
  the `n` definition.
* Stage B — **0 of 39 → `OPPONENT_ADJUSTMENT_ADDS_VALUE`** — unchanged under the corrected fixed
  reference. The audit **refines the mechanism**: opponent effects are clearly real for team defense
  but non-predictive as a feature transform; small-but-real for QB/WR/protection/team-offense; and
  unidentifiable for RB (a back faces each defense ~once).
* Combined — **39 `SHRINKAGE_ONLY`, 3 `NEITHER`** — unchanged.

**Report edits made** (not silent): Phase 4 report §0 gets an audit banner; §4 replaces the
"schedule information" narrative with an explicit observed-result / hypothesis / untested-claim
split and a pointer to §3 here; §10 replaces "Shrinkage is not optional" with "Regression-to-the-mean
shrinkage is the current preferred calibration layer for the Phase 4 candidate metrics" and adds an
explicit statement that `SHRINKAGE_ADDS_VALUE` does not imply matchup value, game-prediction value,
final-model inclusion, or causation.

---

## 10. Recommendation

# `APPROVE_PHASE_4`

Rationale:
* The candidate universe matches the approved protocol; the 8 excluded metrics genuinely fail the
  approved rules and would not change the story.
* The shrinkage result is robust to `k`, to the sample-size definition, and survives the negative
  controls (Phase 4 §5).
* The opponent-adjustment null is confirmed under a corrected, non-post-hoc reference; the audit
  strengthens the interpretation by identifying *why* it is null (two mechanisms).
* The one implementation defect (post-hoc Stage-B reference) is fixed and shown immaterial.
* Overstated language has been softened.

No Phase 5 work should begin until this audit is explicitly reviewed. The Phase 5 question remains
distinct: *do the shrunk (not opponent-adjusted) measurements of two opposing units, combined in an
interaction model, predict game-level outcomes better than simple baselines?*

---

## 11. STOP

Phase 4.1 is complete. Awaiting explicit approval. Do not proceed to Phase 5.
