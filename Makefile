PY := PYTHONPATH=src .venv/bin/python

.PHONY: ingest calendar crosswalk validate-injuries data-dictionary test test-fast lint phase1 \
        phase2-diagnostics phase3-validation phase4-validation phase4-audit phase5-validation \
        phase2 phase3 phase4 phase5 team-strength factor-analysis weekly-research final-build

ingest:            ## materialise the canonical parquet layer (idempotent, cache-backed)
	$(PY) -m matchup.cli ingest

crosswalk:         ## write outputs/phase1/id_crosswalk_coverage.csv
	$(PY) -m matchup.cli crosswalk

validate-injuries: ## run the injury as-of fallback validation (2022-2024)
	$(PY) -m matchup.cli validate-injuries

data-dictionary:   ## regenerate reports/data_dictionary.md from config + manifests
	$(PY) -m matchup.cli data-dictionary

phase2-diagnostics: ## regenerate outputs/phase2/*.csv (registry, coverage, reliability, redundancy)
	$(PY) -m matchup.cli phase2-diagnostics

phase3-validation: ## run the persistence validation study -> outputs/phase3/ (~1 min)
	$(PY) -m matchup.cli phase3

phase4-validation: ## run the shrinkage & opponent-adjustment study -> outputs/phase4/ (~3 min)
	$(PY) -m matchup.cli phase4

phase4-audit: ## Phase 4.1 audit / sensitivity analyses -> outputs/phase4/audit_*.csv (~2 min)
	$(PY) -m matchup.cli phase4-audit

phase5-validation: ## run the matchup-interaction validation study -> outputs/phase5/ (~1 min)
	$(PY) -m matchup.cli phase5

team-strength: ## build team-strength panels 2016-current -> outputs/team_strength/ (~15 s)
	$(PY) -m matchup.cli team-strength

factor-analysis: ## factor research (scoring / points-allowed / winning) -> outputs/research/ (~15 s)
	$(PY) -m matchup.cli factor-analysis

weekly-research: ## THE weekly 2026 command: refresh strength + research + reports (~45 s)
	$(PY) -m matchup.cli weekly-research --ingest

final-build: team-strength factor-analysis weekly-research lint test  ## full research system + checks

phase1: ingest crosswalk validate-injuries data-dictionary test  ## full Phase 1 pipeline

phase2: phase2-diagnostics test  ## Phase 2 diagnostics + tests

phase3: phase3-validation test  ## Phase 3 persistence validation + tests

phase4: phase4-validation test  ## Phase 4 shrinkage & opponent-adjustment + tests

phase5: phase5-validation test  ## Phase 5 matchup-interaction validation + tests

test:              ## full test suite (needs the nflverse cache populated)
	$(PY) -m pytest -q

test-fast:         ## skip network-marked tests
	$(PY) -m pytest -q -m "not network"

lint:
	.venv/bin/ruff check src tests scripts
