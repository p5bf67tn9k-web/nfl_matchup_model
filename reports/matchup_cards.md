# Matchup cards — presentation layer

This is a **presentation/reporting layer** on top of the existing team-strength research
system. It draws the model's existing outputs as a publication-quality graphic for any two
teams; it does not compute strength, does not define new metrics, and does not add betting
logic, spreads, win probabilities, or game-winner predictions. See
[`final_methodology.md`](final_methodology.md) and [`../config/strength.yaml`](../config/strength.yaml)
for the actual research methodology this layer visualizes.

## How to generate a card

```bash
make weekly-research   # first, if you haven't already -- builds the outputs this reads
python scripts/create_matchup_card.py --away NE --home SEA --season 2026 --week 1
```

```
usage: create_matchup_card.py --away AWAY --home HOME --season SEASON --week WEEK [--output-dir DIR]
```

`--away`/`--home` are team abbreviations (e.g. `NE`, `SEA`); `--season`/`--week` select which
snapshot to render. If the requested week hasn't been played yet, the card automatically falls
back to the latest available data and labels itself a **preseason/baseline display** rather than
failing or fabricating a week that doesn't exist yet.

## Where output files go

```
outputs/matchups/{season}_week{week}_{AWAY}_{HOME}.png
outputs/matchups/{season}_week{week}_{AWAY}_{HOME}.pdf
```

e.g. `outputs/matchups/2026_week1_NE_SEA.png` / `.pdf`. Both are portrait-oriented, sized for a
single Substack image embed.

## What every section means

**Header** — matchup, season/week, venue (from the schedule table's `stadium`/`gameday` columns
only -- never betting columns), and a badge stating whether this is a preseason baseline or data
through a specific completed week.

**Section 1 — Team Strength Profile.** All **nine existing domains** from
`config/strength.yaml` (`offense_overall`, `passing_offense`, `rushing_offense`,
`pass_protection`, `defense_overall`, `passing_defense`, `rushing_defense`, `pass_rush`,
`special_teams`), side by side for both teams. Each row shows the team's existing domain
`index_value` (a reference-standard-deviation unit, equal-weight mean of the domain's member
metrics' oriented, shrunk z-scores — see `strength/team_strength.py`), its existing
`rank_of_league`, a percentile, and a confidence dot. The percentile is the **one derived value**
in this whole layer: it's the existing rank run through the identical rank→percentile mapping
`strength/team_strength.py` already applies to metrics (`(n_teams - rank) / (n_teams - 1)`) — a
documented, deterministic transform of an existing number, not an independent statistic. There is
deliberately **no overall team rating** here, matching the model's own design.

**Section 2 — Matchup Comparison.** The six football-relevant offense-vs-defense domain pairs
(away passing offense vs. home passing defense, away rushing offense vs. home rushing defense,
away pass protection vs. home pass rush, and the mirror image for the home team). The bar is the
plain difference between two *existing* domain index values (`unit_a − unit_b`); positive favors
the offensive unit's team. This is descriptive arithmetic on values the model already publishes,
not a new interaction metric — consistent with the Phase 5 finding
(`STOP_NO_RELIABLE_MATCHUP_SIGNAL`) that an opponent-interaction term adds no reliable predictive
value. Nothing on this card is presented as a prediction.

**Section 3 — Key Matchup Battles.** The 3–5 largest measurable `|gap|` values from Section 2,
called out with both teams' domain values and the relative gap. Comparisons missing a value on
either side are excluded here, never treated as zero.

**Section 4 — Team Identities.** Short, templated bullets built only from fields the model
already publishes for that team: its `top_strength_domain`/`top_weakness_domain` (and index
values), plus any other domain where the team ranks top-5 or bottom-5 league-wide. No narrative
invention — every sentence traces to an existing column.

**Section 5 — Model Context / footer.** States whether this is a preseason baseline or
in-season data, which existing output file backed the numbers (`data_source`), and the standard
disclaimer: *"Strength indices are league-relative research measures, not ratings, probabilities,
or predictions. Values are based only on information available through the selected week."*

## How this relates to the underlying research model

Every number on the card is read from one of:

- `outputs/weekly/weekly_summary.json` — season / through-week / mode
- `outputs/weekly/weekly_team_snapshot.csv` — record, top strength/weakness, confidence
- `outputs/weekly/weekly_changes.csv` — per-(team, domain) index value, rank, confidence
- `outputs/rankings/team_rankings_weekly.csv` — historical fallback for a week that is no
  longer the current snapshot (index value + rank only; confidence/record show as `N/A`)
- `data/processed/schedules/season=YYYY/data.parquet` — venue/date only; betting columns in
  that table (`spread_line`, `moneyline`, `total_line`, `result`, ...) are never read

If a required value isn't available for the requested team/week, the card shows `N/A` rather
than substituting or inventing a number. See `src/matchup/visualization/data.py`'s module
docstring for the exact source column behind every field.

## Code layout

```
src/matchup/visualization/
  data.py          # loads existing outputs; assembles per-team domain profiles,
                    # the 6 offense-vs-defense comparisons, and key-battle ordering
  styles.py         # team display names/colors, palette, formatting (N/A, ranks, percentiles)
  matchup_card.py   # renders the 5 sections to a matplotlib figure -> PNG + PDF

scripts/create_matchup_card.py   # CLI entry point
tests/test_matchup_card.py       # team selection, domain retrieval, gap ordering,
                                  # missing-data -> N/A, determinism, render smoke test
```
