# nfl_matchup_model

An **independent, auditable NFL team-strength research system**.

> For every team, every week: unit-level strength on nine football dimensions, with every raw
> metric, league reference, sample size and confidence kept visible — plus a factor study of which
> statistics have the strongest, most temporally stable evidence for scoring, points allowed, and
> winning.

It does **not** predict game winners, scores, or spreads, has **no** betting logic, and uses **no**
market data. It does not collapse everything into one black-box rating: the domain indices are
explicit equal-weight means of oriented, shrunk z-scores, and the member metrics are always shown.

**Start here:** [`reports/final_methodology.md`](reports/final_methodology.md) ·
[`reports/2026_research_guide.md`](reports/2026_research_guide.md)

```bash
make weekly-research        # THE weekly command: rebuild strength + research + reports (~1 min)
```

## Research validation record (Phases 0–5)

* [`reports/phase0_report.md`](reports/phase0_report.md) — data-source audit, discrepancies, leakage risks.
* [`reports/phase1_report.md`](reports/phase1_report.md) — canonical Parquet layer, the as-of engine,
  injury fallback validation, ID crosswalk.
* [`reports/phase2_report.md`](reports/phase2_report.md) — 58 descriptive metrics, windowing,
  normalization, reliability & redundancy diagnostics.
* [`reports/phase3_report.md`](reports/phase3_report.md) — walk-forward **persistence** validation:
  rank persistence is near-universal, but only team-offense metrics beat simple baselines on RMSE.
* [`reports/phase4_report.md`](reports/phase4_report.md) — **shrinkage** (`w = n/(n+k)`, `k`
  walk-forward) and **chronological ridge opponent adjustment**. Pre-registered in
  `config/phase4_validation.yaml`; results in `outputs/phase4/`.
* [`reports/phase4_1_audit.md`](reports/phase4_1_audit.md) — audit of Phase 4: candidate-universe
  reconciliation, ridge sanity, `k`/`n` sensitivity, one Stage-B defect found & fixed. Verdict:
  `APPROVE_PHASE_4`.
* [`reports/phase5_report.md`](reports/phase5_report.md) — walk-forward **matchup-interaction**
  validation: does `A × B` (Team A's shrunk unit measure interacted with the opponent unit's shrunk
  measure) beat the additive `A + B`? Pre-registered in `config/phase5_validation.yaml`; results in
  `outputs/phase5/`. Verdict: **`STOP_NO_RELIABLE_MATCHUP_SIGNAL`**.
* [`reports/data_dictionary.md`](reports/data_dictionary.md) — generated from config + manifests.

These phases validated the **measurement layer** the research system is built on. Phases 3–5 found:
regression-to-the-mean **shrinkage adds out-of-sample value for 39 of 42 candidate metrics** (it
explains the Phase 3 gap between rank persistence and RMSE skill); **opponent-adjusting the unit
feature adds nothing** (0 of 39); and in Phase 5, across 9 pre-registered unit-vs-unit matchups,
**the opponent measurement adds no reliable value to predicting a unit's own future performance —
neither additively nor as an interaction term** (all 9 → `UNIT_ONLY`; interaction skill point
estimates within ±0.002 of zero, 0 of 18 tests FDR-significant). None of this establishes
game-prediction value. The final system therefore reports **transparent team-strength indices +
factor evidence**, not game predictions.

## The research system

```bash
make team-strength       # team-strength panels 2016-current -> outputs/team_strength/
make factor-analysis     # scoring / points-allowed / winning factor study -> outputs/research/
make weekly-research     # the weekly workflow (ingest + strength + research + 3 reports)
make final-build         # all of the above + lint + tests
```

Generated each run: `reports/league_overview.md`, `reports/team_profiles.md`,
`reports/weekly_research.md`; `outputs/{team_strength,rankings,weekly,research,diagnostics}/`.
Config: [`config/strength.yaml`](config/strength.yaml) (metrics, domains, shrinkage `k`, no learned
weights). Before Week 1 of a season the workflow runs in **preseason-baseline mode** and updates
automatically as games are played.

## Setup

```bash
/opt/homebrew/bin/python3.12 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
```

## Run the pipeline

```bash
make ingest              # materialise data/processed/ (idempotent, cache-backed)
make validate-injuries   # injury as-of fallback validation -> outputs/phase1/
make crosswalk           # ID crosswalk coverage -> outputs/phase1/
make data-dictionary     # regenerate reports/data_dictionary.md
make phase2-diagnostics  # regenerate outputs/phase2/*.csv (registry, coverage, reliability, redundancy)
make phase3-validation   # run the persistence validation study -> outputs/phase3/ (~1 min)
make phase4-validation   # run the shrinkage & opponent-adjustment study -> outputs/phase4/ (~3 min)
make phase4-audit        # Phase 4.1 audit / sensitivity analyses -> outputs/phase4/audit_*.csv
make phase5-validation   # run the matchup-interaction validation study -> outputs/phase5/ (~1 min)
make test                # 150 tests (needs the nflverse cache populated by `make ingest`)
```

Point-in-time access from code:

```python
from matchup.pointintime.asof import AsOf, team_state_asof
st = team_state_asof("KC", 2024, 7)          # leak-checked frames + coverage metadata
ao = AsOf(asof_utc=st["target_kickoff_utc"])
ao.pbp("KC"); ao.ngs("passing", "KC"); ao.injuries("KC")
```

## Data

All data via [`nflreadpy`](https://nflreadpy.nflverse.com/) (nflverse). Raw pulls are cached under
`data/raw/nflreadpy_cache/` (gitignored). Canonical parquet will live in `data/processed/`.

### Attribution

nflverse data is licensed **CC-BY-SA 4.0**. Advanced stats are courtesy of **Pro Football Reference**
(2018+). FTN charting / 2023+ participation data are courtesy of **FTN Data via nflverse** (excluded
from the MVP). Full attribution is reproduced in generated reports.
