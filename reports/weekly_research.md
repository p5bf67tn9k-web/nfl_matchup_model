# Weekly Research — 2026 Week 1

> These indices are **transparent research indices**, not ratings, probabilities, or predictions of game outcomes. Each is an equal-weight mean of its member metrics' oriented, shrunk z-scores (reference-SD units). The member metrics are shown alongside every index. This project does not model game winners, scores, or spreads.

Generated 2026-09-16T01:32:02+00:00. Latest completed regular-season week detected: **1**

## Biggest offense movers (week over week)
**Risers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| CLE | -0.129 | 1.442 | 22 | 10 |
| LV | -0.120 | 1.217 | 19 | 12 |
| NYJ | 0.229 | 1.035 | 7 | 22 |
| TEN | -0.121 | 1.001 | 20 | 10 |
| NYG | 0.558 | 0.524 | 2 | 19 |
| NO | 0.020 | 0.410 | 15 | 12 |

**Fallers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| LA | -0.146 | -1.672 | 23 | -22 |
| NE | -0.172 | -1.279 | 25 | -23 |
| GB | -0.127 | -1.005 | 21 | -17 |
| BUF | 0.229 | -0.868 | 8 | -5 |
| IND | -0.198 | -0.811 | 26 | -19 |
| ATL | -0.406 | -0.660 | 32 | -18 |

## Biggest defense movers (week over week)
**Risers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| WAS | 0.132 | 1.177 | 6 | 26 |
| ARI | 0.095 | 0.996 | 10 | 20 |
| NYJ | 0.088 | 0.951 | 12 | 16 |
| CIN | -0.025 | 0.850 | 20 | 9 |
| MIA | 0.080 | 0.801 | 13 | 14 |
| SF | 0.103 | 0.783 | 9 | 17 |

**Fallers**
| team | index_value | delta_vs_prev_week | rank_of_league | rank_change_vs_prev_week |
| --- | --- | --- | --- | --- |
| HOU | -0.163 | -1.094 | 27 | -26 |
| CLE | -0.307 | -0.902 | 32 | -27 |
| LAC | -0.117 | -0.688 | 23 | -17 |
| DEN | 0.030 | -0.686 | 15 | -12 |
| LA | -0.218 | -0.681 | 29 | -21 |
| SEA | 0.104 | -0.635 | 8 | -6 |

## Biggest metric changes vs preseason baseline
| team | metric | shrunk_value | delta_shrunk_vs_preseason | percentile | confidence |
| --- | --- | --- | --- | --- | --- |
| NE | team_offense.pass_epa_per_dropback | 0.0346 | -0.1823 | 0.5484 | low |
| LA | team_offense.pass_epa_per_dropback | -0.0117 | -0.1733 | 0.0968 | low |
| CLE | team_offense.pass_epa_per_dropback | 0.0023 | 0.1624 | 0.1935 | low |
| GB | team_offense.pass_epa_per_dropback | 0.0208 | -0.1609 | 0.3226 | low |
| NYJ | team_offense.pass_epa_per_dropback | 0.0663 | 0.1571 | 0.8387 | low |
| NYJ | team_defense.pass_epa_per_dropback | 0.0267 | -0.1389 | 0.7097 | low |
| TEN | team_offense.pass_epa_per_dropback | 0.0135 | 0.1372 | 0.2903 | low |
| LV | team_offense.pass_epa_per_dropback | 0.0282 | 0.1311 | 0.4194 | low |
| MIN | team_offense.pass_epa_per_dropback | 0.0321 | 0.1283 | 0.5161 | low |
| LV | team_offense.epa_per_play | -0.0033 | 0.1273 | 0.3871 | low |
| LA | team_offense.epa_per_play | -0.0252 | -0.1265 | 0.1290 | low |
| LA | team_offense.early_down_epa_per_play | -0.0168 | -0.1235 | 0.3226 | low |
| NYJ | special_teams.st_epa_per_play | 0.0758 | -0.1207 | 0.7742 | low |
| CLE | team_defense.pass_epa_per_dropback | 0.0806 | 0.1195 | 0.0000 | low |
| HOU | team_defense.pass_epa_per_dropback | 0.0668 | 0.1165 | 0.0645 | low |

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

