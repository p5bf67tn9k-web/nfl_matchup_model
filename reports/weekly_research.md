# Weekly Research — 2026 (preseason)

> These indices are **transparent research indices**, not ratings, probabilities, or predictions of game outcomes. Each is an equal-weight mean of its member metrics' oriented, shrunk z-scores (reference-SD units). The member metrics are shown alongside every index. This project does not model game winners, scores, or spreads.

Generated 2026-09-09T00:28:43+00:00. Latest completed regular-season week detected: **0** — running in preseason-baseline mode.

No games have been played yet. The tables below are the **preseason baseline**: each team's prior full regular season, shrunk toward the 3-season league reference. They update automatically once Week 1 completes.

## Biggest offense movers (week over week)
**Risers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| LA | 1.526 | 0.000 | 1 | 0 |
| NE | 1.107 | 0.000 | 2 | 0 |
| BUF | 1.096 | 0.000 | 3 | 0 |
| GB | 0.878 | 0.000 | 4 | 0 |
| DAL | 0.835 | 0.000 | 5 | 0 |
| SF | 0.692 | 0.000 | 6 | 0 |

**Fallers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| CLE | -1.571 | 0.000 | 32 | 0 |
| LV | -1.338 | 0.000 | 31 | 0 |
| TEN | -1.122 | 0.000 | 30 | 0 |
| NYJ | -0.806 | 0.000 | 29 | 0 |
| MIN | -0.394 | 0.000 | 28 | 0 |
| NO | -0.389 | 0.000 | 27 | 0 |

## Biggest defense movers (week over week)
**Risers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| HOU | 0.931 | 0.000 | 1 | 0 |
| SEA | 0.738 | 0.000 | 2 | 0 |
| DEN | 0.716 | 0.000 | 3 | 0 |
| MIN | 0.621 | 0.000 | 4 | 0 |
| CLE | 0.594 | 0.000 | 5 | 0 |
| LAC | 0.571 | 0.000 | 6 | 0 |

**Fallers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| WAS | -1.045 | 0.000 | 32 | 0 |
| DAL | -0.973 | 0.000 | 31 | 0 |
| ARI | -0.901 | 0.000 | 30 | 0 |
| CIN | -0.874 | 0.000 | 29 | 0 |
| NYJ | -0.863 | 0.000 | 28 | 0 |
| MIA | -0.721 | 0.000 | 27 | 0 |

## Biggest metric changes vs preseason baseline
| team | metric | shrunk_value | delta_shrunk_vs_preseason | percentile | confidence |
| --- | --- | --- | --- | --- | --- |
| ARI | pass_protection.qb_hit_rate_allowed | 0.1641 | 0.0000 | 0.2581 | prior_season_only |
| ARI | pass_protection.sack_rate_allowed | 0.0751 | 0.0000 | 0.2258 | prior_season_only |
| ARI | pass_rush.qb_hit_rate_generated | 0.1272 | 0.0000 | 0.0968 | prior_season_only |
| ARI | pass_rush.sack_rate_generated | 0.0564 | 0.0000 | 0.1290 | prior_season_only |
| ARI | special_teams.st_epa_per_play | 0.0214 | 0.0000 | 0.0968 | prior_season_only |
| ARI | team_defense.early_down_epa_per_play | 0.0657 | 0.0000 | 0.0645 | prior_season_only |
| ARI | team_defense.epa_per_play | 0.0484 | 0.0000 | 0.1935 | prior_season_only |
| ARI | team_defense.explosive_rush_rate | 0.1124 | 0.0000 | 0.0968 | prior_season_only |
| ARI | team_defense.pass_epa_per_dropback | 0.1027 | 0.0000 | 0.1935 | prior_season_only |
| ARI | team_defense.pass_success_rate | 0.4875 | 0.0000 | 0.0323 | prior_season_only |
| ARI | team_defense.rush_epa_per_play | -0.0551 | 0.0000 | 0.3226 | prior_season_only |
| ARI | team_defense.rush_success_rate | 0.4170 | 0.0000 | 0.2903 | prior_season_only |
| ARI | team_defense.success_rate | 0.4641 | 0.0000 | 0.0000 | prior_season_only |
| ARI | team_offense.early_down_epa_per_play | -0.0095 | 0.0000 | 0.3226 | prior_season_only |
| ARI | team_offense.epa_per_play | -0.0094 | 0.0000 | 0.2903 | prior_season_only |

## Which factors have the strongest evidence (historical, 2016-2025)
From `outputs/research/factor_summary.csv`. **association** = same-season descriptive correlation; **chronological** = walk-forward (metric now -> outcome over next 4 games), with a cluster-bootstrap 95% CI; **stability** = sign-consistency of the association across 10 seasons. A large correlation alone is not called 'important'. Factors in a group are redundant -- treat each group as one line of evidence.

### Scoring (points scored) — group leaders
| group | factor | association_pearson | chronological_pearson | chronological_pearson_ci_lo | chronological_pearson_ci_hi | stability_frac_same_sign | evidence_tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| offense_efficiency | team_offense.epa_per_play | 0.892 | 0.401 | 0.324 | 0.470 | 1.000 | strong + temporally consistent |
| offense_explosiveness | team_offense.explosive_pass_rate | 0.619 | 0.315 | 0.224 | 0.397 | 1.000 | strong + temporally consistent |
| protection | pass_protection.sack_rate_allowed | -0.506 | -0.235 | -0.319 | -0.143 | 1.000 | moderate + temporally consistent |
| offense_style | team_offense.proe | 0.277 | 0.052 | -0.044 | 0.152 | 0.900 | weak / insufficient evidence |

### Points prevention (points allowed) — group leaders
| group | factor | association_pearson | chronological_pearson | chronological_pearson_ci_lo | chronological_pearson_ci_hi | stability_frac_same_sign | evidence_tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| defense_efficiency | team_defense.epa_per_play | 0.804 | 0.173 | 0.086 | 0.257 | 1.000 | moderate + temporally consistent |
| pass_rush | pass_rush.qb_hit_rate_generated | -0.357 | -0.135 | -0.212 | -0.053 | 1.000 | weak but statistically detectable chronologically |
| defense_explosiveness | team_defense.explosive_rush_rate | 0.342 | 0.127 | 0.041 | 0.214 | 1.000 | weak but statistically detectable chronologically |

### Winning — group leaders
| group | factor | association_pearson | chronological_pearson | chronological_pearson_ci_lo | chronological_pearson_ci_hi | stability_frac_same_sign | evidence_tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| offense_efficiency | team_offense.pass_epa_per_dropback | 0.717 | 0.289 | 0.205 | 0.365 | 1.000 | moderate + temporally consistent |
| protection | pass_protection.sack_rate_allowed | -0.463 | -0.222 | -0.309 | -0.128 | 1.000 | moderate + temporally consistent |
| offense_explosiveness | team_offense.explosive_pass_rate | 0.446 | 0.218 | 0.127 | 0.304 | 1.000 | moderate + temporally consistent |
| defense_efficiency | team_defense.epa_per_play | -0.519 | -0.185 | -0.267 | -0.095 | 1.000 | moderate + temporally consistent |
| defense_explosiveness | team_defense.explosive_rush_rate | -0.206 | -0.170 | -0.261 | -0.075 | 0.900 | moderate + temporally consistent |
| pass_rush | pass_rush.qb_hit_rate_generated | 0.291 | 0.116 | 0.026 | 0.209 | 0.900 | weak but statistically detectable chronologically |

## Caveats
- Indices are relative to a 3-season league reference, not absolute quality.
- Early-season indices are shrunk heavily toward the reference and flagged low/medium confidence; treat Week 1-4 movement cautiously.
- `association` correlations are descriptive -- not causal and not predictive.
- The Phase 5 matchup-interaction experiment found no reliable incremental signal; any matchup comparisons here are descriptive only.

