# League Overview — 2026 (preseason baseline (no games played))

> These indices are **transparent research indices**, not ratings, probabilities, or predictions of game outcomes. Each is an equal-weight mean of its member metrics' oriented, shrunk z-scores (reference-SD units). The member metrics are shown alongside every index. This project does not model game winners, scores, or spreads.

Generated 2026-09-09T00:28:43+00:00. Source tables: `outputs/rankings/team_rankings_weekly.csv`, `outputs/team_strength/team_metrics_weekly.parquet`, `outputs/weekly/weekly_metric_detail.csv`.

## Index construction
```
Every domain index = arithmetic mean of its member metrics' oriented, shrunk z-scores.
  z_shrunk(metric) = (shrunk_value - ref_mean) / ref_sd
  shrunk_value     = ref_mean + n_games/(n_games + k) * (raw_value - ref_mean)
  oriented         = +z_shrunk if higher-is-better, -z_shrunk if lower-is-better
  ref_mean/ref_sd  = mean/SD of team-season values over the 3 completed prior seasons
                     (min-opportunity filtered)
  k                = frozen Phase 4 walk-forward shrinkage constant per metric (config/strength.yaml)
Units are reference standard deviations. The index is NOT points, NOT a probability, NOT a
definitive rating. The member metrics are always shown alongside it.
```

## Offensive Strength Index (`offense_overall`)
Member metrics: `team_offense.epa_per_play`, `team_offense.success_rate`, `team_offense.early_down_epa_per_play`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LA | 1.526 | 0.000 | 0.000 | 3 | prior_season_only |
| 2 | NE | 1.107 | 0.000 | 0.000 | 3 | prior_season_only |
| 3 | BUF | 1.096 | 0.000 | 0.000 | 3 | prior_season_only |
| 4 | GB | 0.878 | 0.000 | 0.000 | 3 | prior_season_only |
| 5 | DAL | 0.835 | 0.000 | 0.000 | 3 | prior_season_only |
| 6 | SF | 0.692 | 0.000 | 0.000 | 3 | prior_season_only |
| 7 | IND | 0.613 | 0.000 | 0.000 | 3 | prior_season_only |
| 8 | CHI | 0.575 | 0.000 | 0.000 | 3 | prior_season_only |
| 9 | DET | 0.532 | 0.000 | 0.000 | 3 | prior_season_only |
| 10 | SEA | 0.464 | 0.000 | 0.000 | 3 | prior_season_only |
| 11 | WAS | 0.426 | 0.000 | 0.000 | 3 | prior_season_only |
| 12 | BAL | 0.264 | 0.000 | 0.000 | 3 | prior_season_only |
| 13 | KC | 0.258 | 0.000 | 0.000 | 3 | prior_season_only |
| 14 | ATL | 0.254 | 0.000 | 0.000 | 3 | prior_season_only |
| 15 | JAX | 0.240 | 0.000 | 0.000 | 3 | prior_season_only |
| 16 | DEN | 0.163 | 0.000 | 0.000 | 3 | prior_season_only |
| 17 | CIN | 0.147 | 0.000 | 0.000 | 3 | prior_season_only |
| 18 | PIT | 0.120 | 0.000 | 0.000 | 3 | prior_season_only |
| 19 | PHI | 0.059 | 0.000 | 0.000 | 3 | prior_season_only |
| 20 | TB | 0.040 | 0.000 | 0.000 | 3 | prior_season_only |
| 21 | NYG | 0.034 | 0.000 | 0.000 | 3 | prior_season_only |
| 22 | MIA | -0.105 | 0.000 | 0.000 | 3 | prior_season_only |
| 23 | ARI | -0.107 | 0.000 | 0.000 | 3 | prior_season_only |
| 24 | LAC | -0.165 | 0.000 | 0.000 | 3 | prior_season_only |
| 25 | CAR | -0.180 | 0.000 | 0.000 | 3 | prior_season_only |
| 26 | HOU | -0.197 | 0.000 | 0.000 | 3 | prior_season_only |
| 27 | NO | -0.389 | 0.000 | 0.000 | 3 | prior_season_only |
| 28 | MIN | -0.394 | 0.000 | 0.000 | 3 | prior_season_only |
| 29 | NYJ | -0.806 | 0.000 | 0.000 | 3 | prior_season_only |
| 30 | TEN | -1.122 | 0.000 | 0.000 | 3 | prior_season_only |
| 31 | LV | -1.338 | 0.000 | 0.000 | 3 | prior_season_only |
| 32 | CLE | -1.571 | 0.000 | 0.000 | 3 | prior_season_only |

## Passing-Offense Strength Index (`passing_offense`)
Member metrics: `team_offense.pass_epa_per_dropback`, `team_offense.pass_success_rate`, `team_offense.explosive_pass_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | NE | 1.316 | 0.000 | 0.000 | 3 | prior_season_only |
| 2 | LA | 1.095 | 0.000 | 0.000 | 3 | prior_season_only |
| 3 | GB | 0.929 | 0.000 | 0.000 | 3 | prior_season_only |
| 4 | SEA | 0.823 | 0.000 | 0.000 | 3 | prior_season_only |
| 5 | BUF | 0.790 | 0.000 | 0.000 | 3 | prior_season_only |
| 6 | DET | 0.674 | 0.000 | 0.000 | 3 | prior_season_only |
| 7 | SF | 0.670 | 0.000 | 0.000 | 3 | prior_season_only |
| 8 | DAL | 0.416 | 0.000 | 0.000 | 3 | prior_season_only |
| 9 | JAX | 0.294 | 0.000 | 0.000 | 3 | prior_season_only |
| 10 | CHI | 0.283 | 0.000 | 0.000 | 3 | prior_season_only |
| 11 | IND | 0.152 | 0.000 | 0.000 | 3 | prior_season_only |
| 12 | BAL | 0.108 | 0.000 | 0.000 | 3 | prior_season_only |
| 13 | KC | 0.092 | 0.000 | 0.000 | 3 | prior_season_only |
| 14 | WAS | 0.063 | 0.000 | 0.000 | 3 | prior_season_only |
| 15 | TB | 0.020 | 0.000 | 0.000 | 3 | prior_season_only |
| 16 | DEN | 0.015 | 0.000 | 0.000 | 3 | prior_season_only |
| 17 | HOU | -0.006 | 0.000 | 0.000 | 3 | prior_season_only |
| 18 | PHI | -0.009 | 0.000 | 0.000 | 3 | prior_season_only |
| 19 | ATL | -0.026 | 0.000 | 0.000 | 3 | prior_season_only |
| 20 | NYG | -0.072 | 0.000 | 0.000 | 3 | prior_season_only |
| 21 | MIA | -0.150 | 0.000 | 0.000 | 3 | prior_season_only |
| 22 | ARI | -0.152 | 0.000 | 0.000 | 3 | prior_season_only |
| 23 | PIT | -0.165 | 0.000 | 0.000 | 3 | prior_season_only |
| 24 | CIN | -0.180 | 0.000 | 0.000 | 3 | prior_season_only |
| 25 | LAC | -0.182 | 0.000 | 0.000 | 3 | prior_season_only |
| 26 | CAR | -0.232 | 0.000 | 0.000 | 3 | prior_season_only |
| 27 | NO | -0.431 | 0.000 | 0.000 | 3 | prior_season_only |
| 28 | MIN | -0.622 | 0.000 | 0.000 | 3 | prior_season_only |
| 29 | LV | -0.740 | 0.000 | 0.000 | 3 | prior_season_only |
| 30 | NYJ | -0.966 | 0.000 | 0.000 | 3 | prior_season_only |
| 31 | TEN | -1.012 | 0.000 | 0.000 | 3 | prior_season_only |
| 32 | CLE | -1.322 | 0.000 | 0.000 | 3 | prior_season_only |

## Rushing-Offense Strength Index (`rushing_offense`)
Member metrics: `team_offense.rush_epa_per_play`, `team_offense.rush_success_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LA | 1.115 | 0.000 | 0.000 | 2 | prior_season_only |
| 2 | BUF | 0.907 | 0.000 | 0.000 | 2 | prior_season_only |
| 3 | IND | 0.820 | 0.000 | 0.000 | 2 | prior_season_only |
| 4 | CHI | 0.765 | 0.000 | 0.000 | 2 | prior_season_only |
| 5 | CIN | 0.724 | 0.000 | 0.000 | 2 | prior_season_only |
| 6 | PIT | 0.569 | 0.000 | 0.000 | 2 | prior_season_only |
| 7 | DAL | 0.548 | 0.000 | 0.000 | 2 | prior_season_only |
| 8 | BAL | 0.545 | 0.000 | 0.000 | 2 | prior_season_only |
| 9 | WAS | 0.352 | 0.000 | 0.000 | 2 | prior_season_only |
| 10 | MIN | 0.340 | 0.000 | 0.000 | 2 | prior_season_only |
| 11 | SF | 0.294 | 0.000 | 0.000 | 2 | prior_season_only |
| 12 | GB | 0.270 | 0.000 | 0.000 | 2 | prior_season_only |
| 13 | DEN | 0.213 | 0.000 | 0.000 | 2 | prior_season_only |
| 14 | MIA | 0.201 | 0.000 | 0.000 | 2 | prior_season_only |
| 15 | NYG | 0.176 | 0.000 | 0.000 | 2 | prior_season_only |
| 16 | PHI | 0.173 | 0.000 | 0.000 | 2 | prior_season_only |
| 17 | CAR | 0.140 | 0.000 | 0.000 | 2 | prior_season_only |
| 18 | ATL | 0.132 | 0.000 | 0.000 | 2 | prior_season_only |
| 19 | KC | 0.128 | 0.000 | 0.000 | 2 | prior_season_only |
| 20 | DET | 0.016 | 0.000 | 0.000 | 2 | prior_season_only |
| 21 | SEA | -0.008 | 0.000 | 0.000 | 2 | prior_season_only |
| 22 | NYJ | -0.020 | 0.000 | 0.000 | 2 | prior_season_only |
| 23 | TB | -0.022 | 0.000 | 0.000 | 2 | prior_season_only |
| 24 | JAX | -0.032 | 0.000 | 0.000 | 2 | prior_season_only |
| 25 | LAC | -0.071 | 0.000 | 0.000 | 2 | prior_season_only |
| 26 | NE | -0.180 | 0.000 | 0.000 | 2 | prior_season_only |
| 27 | TEN | -0.317 | 0.000 | 0.000 | 2 | prior_season_only |
| 28 | ARI | -0.460 | 0.000 | 0.000 | 2 | prior_season_only |
| 29 | NO | -0.518 | 0.000 | 0.000 | 2 | prior_season_only |
| 30 | HOU | -0.574 | 0.000 | 0.000 | 2 | prior_season_only |
| 31 | CLE | -0.583 | 0.000 | 0.000 | 2 | prior_season_only |
| 32 | LV | -1.441 | 0.000 | 0.000 | 2 | prior_season_only |

## Pass-Protection Strength Index (`pass_protection`)
Member metrics: `pass_protection.sack_rate_allowed`, `pass_protection.qb_hit_rate_allowed`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | DEN | 1.004 | 0.000 | 0.000 | 2 | prior_season_only |
| 2 | CHI | 0.942 | 0.000 | 0.000 | 2 | prior_season_only |
| 3 | LA | 0.759 | 0.000 | 0.000 | 2 | prior_season_only |
| 4 | TB | 0.718 | 0.000 | 0.000 | 2 | prior_season_only |
| 5 | PIT | 0.652 | 0.000 | 0.000 | 2 | prior_season_only |
| 6 | ATL | 0.600 | 0.000 | 0.000 | 2 | prior_season_only |
| 7 | HOU | 0.576 | 0.000 | 0.000 | 2 | prior_season_only |
| 8 | PHI | 0.569 | 0.000 | 0.000 | 2 | prior_season_only |
| 9 | SEA | 0.562 | 0.000 | 0.000 | 2 | prior_season_only |
| 10 | SF | 0.560 | 0.000 | 0.000 | 2 | prior_season_only |
| 11 | DAL | 0.420 | 0.000 | 0.000 | 2 | prior_season_only |
| 12 | IND | 0.410 | 0.000 | 0.000 | 2 | prior_season_only |
| 13 | CIN | 0.248 | 0.000 | 0.000 | 2 | prior_season_only |
| 14 | GB | 0.233 | 0.000 | 0.000 | 2 | prior_season_only |
| 15 | BUF | 0.223 | 0.000 | 0.000 | 2 | prior_season_only |
| 16 | JAX | 0.217 | 0.000 | 0.000 | 2 | prior_season_only |
| 17 | MIA | 0.136 | 0.000 | 0.000 | 2 | prior_season_only |
| 18 | NO | 0.113 | 0.000 | 0.000 | 2 | prior_season_only |
| 19 | WAS | 0.103 | 0.000 | 0.000 | 2 | prior_season_only |
| 20 | CAR | 0.085 | 0.000 | 0.000 | 2 | prior_season_only |
| 21 | NE | -0.217 | 0.000 | 0.000 | 2 | prior_season_only |
| 22 | KC | -0.379 | 0.000 | 0.000 | 2 | prior_season_only |
| 23 | DET | -0.404 | 0.000 | 0.000 | 2 | prior_season_only |
| 24 | ARI | -0.524 | 0.000 | 0.000 | 2 | prior_season_only |
| 25 | NYG | -0.549 | 0.000 | 0.000 | 2 | prior_season_only |
| 26 | TEN | -0.630 | 0.000 | 0.000 | 2 | prior_season_only |
| 27 | BAL | -0.639 | 0.000 | 0.000 | 2 | prior_season_only |
| 28 | CLE | -0.915 | 0.000 | 0.000 | 2 | prior_season_only |
| 29 | LAC | -0.977 | 0.000 | 0.000 | 2 | prior_season_only |
| 30 | NYJ | -1.060 | 0.000 | 0.000 | 2 | prior_season_only |
| 31 | LV | -1.192 | 0.000 | 0.000 | 2 | prior_season_only |
| 32 | MIN | -1.414 | 0.000 | 0.000 | 2 | prior_season_only |

## Defensive Strength Index (`defense_overall`)
Member metrics: `team_defense.epa_per_play`, `team_defense.success_rate`, `team_defense.early_down_epa_per_play`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | HOU | 0.931 | 0.000 | 0.000 | 3 | prior_season_only |
| 2 | SEA | 0.738 | 0.000 | 0.000 | 3 | prior_season_only |
| 3 | DEN | 0.716 | 0.000 | 0.000 | 3 | prior_season_only |
| 4 | MIN | 0.621 | 0.000 | 0.000 | 3 | prior_season_only |
| 5 | CLE | 0.594 | 0.000 | 0.000 | 3 | prior_season_only |
| 6 | LAC | 0.571 | 0.000 | 0.000 | 3 | prior_season_only |
| 7 | JAX | 0.466 | 0.000 | 0.000 | 3 | prior_season_only |
| 8 | LA | 0.463 | 0.000 | 0.000 | 3 | prior_season_only |
| 9 | NO | 0.396 | 0.000 | 0.000 | 3 | prior_season_only |
| 10 | PHI | 0.295 | 0.000 | 0.000 | 3 | prior_season_only |
| 11 | BUF | 0.201 | 0.000 | 0.000 | 3 | prior_season_only |
| 12 | DET | 0.152 | 0.000 | 0.000 | 3 | prior_season_only |
| 13 | PIT | 0.072 | 0.000 | 0.000 | 3 | prior_season_only |
| 14 | NE | 0.025 | 0.000 | 0.000 | 3 | prior_season_only |
| 15 | KC | 0.024 | 0.000 | 0.000 | 3 | prior_season_only |
| 16 | LV | -0.070 | 0.000 | 0.000 | 3 | prior_season_only |
| 17 | CAR | -0.136 | 0.000 | 0.000 | 3 | prior_season_only |
| 18 | ATL | -0.151 | 0.000 | 0.000 | 3 | prior_season_only |
| 19 | IND | -0.158 | 0.000 | 0.000 | 3 | prior_season_only |
| 20 | BAL | -0.177 | 0.000 | 0.000 | 3 | prior_season_only |
| 21 | TB | -0.244 | 0.000 | 0.000 | 3 | prior_season_only |
| 22 | GB | -0.299 | 0.000 | 0.000 | 3 | prior_season_only |
| 23 | CHI | -0.491 | 0.000 | 0.000 | 3 | prior_season_only |
| 24 | TEN | -0.608 | 0.000 | 0.000 | 3 | prior_season_only |
| 25 | NYG | -0.658 | 0.000 | 0.000 | 3 | prior_season_only |
| 26 | SF | -0.680 | 0.000 | 0.000 | 3 | prior_season_only |
| 27 | MIA | -0.721 | 0.000 | 0.000 | 3 | prior_season_only |
| 28 | NYJ | -0.863 | 0.000 | 0.000 | 3 | prior_season_only |
| 29 | CIN | -0.874 | 0.000 | 0.000 | 3 | prior_season_only |
| 30 | ARI | -0.901 | 0.000 | 0.000 | 3 | prior_season_only |
| 31 | DAL | -0.973 | 0.000 | 0.000 | 3 | prior_season_only |
| 32 | WAS | -1.045 | 0.000 | 0.000 | 3 | prior_season_only |

## Pass-Defense Strength Index (`passing_defense`)
Member metrics: `team_defense.pass_epa_per_dropback`, `team_defense.pass_success_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | HOU | 0.977 | 0.000 | 0.000 | 2 | prior_season_only |
| 2 | DEN | 0.977 | 0.000 | 0.000 | 2 | prior_season_only |
| 3 | MIN | 0.876 | 0.000 | 0.000 | 2 | prior_season_only |
| 4 | SEA | 0.632 | 0.000 | 0.000 | 2 | prior_season_only |
| 5 | CLE | 0.623 | 0.000 | 0.000 | 2 | prior_season_only |
| 6 | PHI | 0.593 | 0.000 | 0.000 | 2 | prior_season_only |
| 7 | JAX | 0.576 | 0.000 | 0.000 | 2 | prior_season_only |
| 8 | BUF | 0.561 | 0.000 | 0.000 | 2 | prior_season_only |
| 9 | LAC | 0.501 | 0.000 | 0.000 | 2 | prior_season_only |
| 10 | LA | 0.354 | 0.000 | 0.000 | 2 | prior_season_only |
| 11 | DET | 0.332 | 0.000 | 0.000 | 2 | prior_season_only |
| 12 | NO | 0.301 | 0.000 | 0.000 | 2 | prior_season_only |
| 13 | NE | 0.218 | 0.000 | 0.000 | 2 | prior_season_only |
| 14 | ATL | 0.099 | 0.000 | 0.000 | 2 | prior_season_only |
| 15 | PIT | -0.030 | 0.000 | 0.000 | 2 | prior_season_only |
| 16 | KC | -0.044 | 0.000 | 0.000 | 2 | prior_season_only |
| 17 | GB | -0.083 | 0.000 | 0.000 | 2 | prior_season_only |
| 18 | NYG | -0.109 | 0.000 | 0.000 | 2 | prior_season_only |
| 19 | BAL | -0.209 | 0.000 | 0.000 | 2 | prior_season_only |
| 20 | IND | -0.212 | 0.000 | 0.000 | 2 | prior_season_only |
| 21 | CHI | -0.277 | 0.000 | 0.000 | 2 | prior_season_only |
| 22 | CAR | -0.404 | 0.000 | 0.000 | 2 | prior_season_only |
| 23 | LV | -0.412 | 0.000 | 0.000 | 2 | prior_season_only |
| 24 | TB | -0.483 | 0.000 | 0.000 | 2 | prior_season_only |
| 25 | SF | -0.612 | 0.000 | 0.000 | 2 | prior_season_only |
| 26 | TEN | -0.699 | 0.000 | 0.000 | 2 | prior_season_only |
| 27 | CIN | -0.767 | 0.000 | 0.000 | 2 | prior_season_only |
| 28 | WAS | -0.870 | 0.000 | 0.000 | 2 | prior_season_only |
| 29 | ARI | -0.879 | 0.000 | 0.000 | 2 | prior_season_only |
| 30 | MIA | -0.941 | 0.000 | 0.000 | 2 | prior_season_only |
| 31 | NYJ | -0.951 | 0.000 | 0.000 | 2 | prior_season_only |
| 32 | DAL | -0.999 | 0.000 | 0.000 | 2 | prior_season_only |

## Run-Defense Strength Index (`rushing_defense`)
Member metrics: `team_defense.rush_epa_per_play`, `team_defense.rush_success_rate`, `team_defense.explosive_rush_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SEA | 1.028 | 0.000 | 0.000 | 3 | prior_season_only |
| 2 | HOU | 0.663 | 0.000 | 0.000 | 3 | prior_season_only |
| 3 | DEN | 0.626 | 0.000 | 0.000 | 3 | prior_season_only |
| 4 | JAX | 0.484 | 0.000 | 0.000 | 3 | prior_season_only |
| 5 | TB | 0.383 | 0.000 | 0.000 | 3 | prior_season_only |
| 6 | LA | 0.367 | 0.000 | 0.000 | 3 | prior_season_only |
| 7 | NO | 0.366 | 0.000 | 0.000 | 3 | prior_season_only |
| 8 | KC | 0.327 | 0.000 | 0.000 | 3 | prior_season_only |
| 9 | CLE | 0.220 | 0.000 | 0.000 | 3 | prior_season_only |
| 10 | LAC | 0.103 | 0.000 | 0.000 | 3 | prior_season_only |
| 11 | BAL | 0.092 | 0.000 | 0.000 | 3 | prior_season_only |
| 12 | IND | 0.082 | 0.000 | 0.000 | 3 | prior_season_only |
| 13 | TEN | 0.051 | 0.000 | 0.000 | 3 | prior_season_only |
| 14 | LV | 0.030 | 0.000 | 0.000 | 3 | prior_season_only |
| 15 | MIN | 0.023 | 0.000 | 0.000 | 3 | prior_season_only |
| 16 | PHI | 0.012 | 0.000 | 0.000 | 3 | prior_season_only |
| 17 | CAR | -0.025 | 0.000 | 0.000 | 3 | prior_season_only |
| 18 | NE | -0.046 | 0.000 | 0.000 | 3 | prior_season_only |
| 19 | GB | -0.061 | 0.000 | 0.000 | 3 | prior_season_only |
| 20 | PIT | -0.074 | 0.000 | 0.000 | 3 | prior_season_only |
| 21 | SF | -0.196 | 0.000 | 0.000 | 3 | prior_season_only |
| 22 | ATL | -0.201 | 0.000 | 0.000 | 3 | prior_season_only |
| 23 | DET | -0.256 | 0.000 | 0.000 | 3 | prior_season_only |
| 24 | NYJ | -0.277 | 0.000 | 0.000 | 3 | prior_season_only |
| 25 | MIA | -0.351 | 0.000 | 0.000 | 3 | prior_season_only |
| 26 | CHI | -0.421 | 0.000 | 0.000 | 3 | prior_season_only |
| 27 | ARI | -0.461 | 0.000 | 0.000 | 3 | prior_season_only |
| 28 | CIN | -0.634 | 0.000 | 0.000 | 3 | prior_season_only |
| 29 | WAS | -0.656 | 0.000 | 0.000 | 3 | prior_season_only |
| 30 | BUF | -0.777 | 0.000 | 0.000 | 3 | prior_season_only |
| 31 | DAL | -0.858 | 0.000 | 0.000 | 3 | prior_season_only |
| 32 | NYG | -1.356 | 0.000 | 0.000 | 3 | prior_season_only |

## Pass-Rush Strength Index (`pass_rush`)
Member metrics: `pass_rush.qb_hit_rate_generated`, `pass_rush.sack_rate_generated`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | DEN | 1.509 | 0.000 | 0.000 | 2 | prior_season_only |
| 2 | CLE | 1.073 | 0.000 | 0.000 | 2 | prior_season_only |
| 3 | MIN | 1.026 | 0.000 | 0.000 | 2 | prior_season_only |
| 4 | ATL | 0.570 | 0.000 | 0.000 | 2 | prior_season_only |
| 5 | LA | 0.459 | 0.000 | 0.000 | 2 | prior_season_only |
| 6 | DET | 0.382 | 0.000 | 0.000 | 2 | prior_season_only |
| 7 | LAC | 0.310 | 0.000 | 0.000 | 2 | prior_season_only |
| 8 | NO | 0.262 | 0.000 | 0.000 | 2 | prior_season_only |
| 9 | PIT | 0.250 | 0.000 | 0.000 | 2 | prior_season_only |
| 10 | BUF | 0.242 | 0.000 | 0.000 | 2 | prior_season_only |
| 11 | PHI | 0.230 | 0.000 | 0.000 | 2 | prior_season_only |
| 12 | HOU | 0.226 | 0.000 | 0.000 | 2 | prior_season_only |
| 13 | SEA | 0.220 | 0.000 | 0.000 | 2 | prior_season_only |
| 14 | TEN | 0.213 | 0.000 | 0.000 | 2 | prior_season_only |
| 15 | KC | 0.132 | 0.000 | 0.000 | 2 | prior_season_only |
| 16 | GB | 0.039 | 0.000 | 0.000 | 2 | prior_season_only |
| 17 | WAS | 0.034 | 0.000 | 0.000 | 2 | prior_season_only |
| 18 | DAL | 0.004 | 0.000 | 0.000 | 2 | prior_season_only |
| 19 | NYG | -0.012 | 0.000 | 0.000 | 2 | prior_season_only |
| 20 | NE | -0.130 | 0.000 | 0.000 | 2 | prior_season_only |
| 21 | LV | -0.152 | 0.000 | 0.000 | 2 | prior_season_only |
| 22 | MIA | -0.191 | 0.000 | 0.000 | 2 | prior_season_only |
| 23 | CHI | -0.257 | 0.000 | 0.000 | 2 | prior_season_only |
| 24 | TB | -0.295 | 0.000 | 0.000 | 2 | prior_season_only |
| 25 | IND | -0.324 | 0.000 | 0.000 | 2 | prior_season_only |
| 26 | CIN | -0.363 | 0.000 | 0.000 | 2 | prior_season_only |
| 27 | BAL | -0.576 | 0.000 | 0.000 | 2 | prior_season_only |
| 28 | JAX | -0.622 | 0.000 | 0.000 | 2 | prior_season_only |
| 29 | ARI | -0.764 | 0.000 | 0.000 | 2 | prior_season_only |
| 30 | CAR | -0.841 | 0.000 | 0.000 | 2 | prior_season_only |
| 31 | NYJ | -0.958 | 0.000 | 0.000 | 2 | prior_season_only |
| 32 | SF | -1.371 | 0.000 | 0.000 | 2 | prior_season_only |

## Special-Teams Strength Index (`special_teams`)
Member metrics: `special_teams.st_epa_per_play`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | NYJ | 1.446 | 0.000 | 0.000 | 1 | prior_season_only |
| 2 | SF | 0.800 | 0.000 | 0.000 | 1 | prior_season_only |
| 3 | MIA | 0.771 | 0.000 | 0.000 | 1 | prior_season_only |
| 4 | JAX | 0.744 | 0.000 | 0.000 | 1 | prior_season_only |
| 5 | CIN | 0.718 | 0.000 | 0.000 | 1 | prior_season_only |
| 6 | DAL | 0.667 | 0.000 | 0.000 | 1 | prior_season_only |
| 7 | IND | 0.661 | 0.000 | 0.000 | 1 | prior_season_only |
| 8 | SEA | 0.642 | 0.000 | 0.000 | 1 | prior_season_only |
| 9 | BAL | 0.419 | 0.000 | 0.000 | 1 | prior_season_only |
| 10 | PIT | 0.405 | 0.000 | 0.000 | 1 | prior_season_only |
| 11 | DET | 0.398 | 0.000 | 0.000 | 1 | prior_season_only |
| 12 | HOU | 0.368 | 0.000 | 0.000 | 1 | prior_season_only |
| 13 | TEN | 0.362 | 0.000 | 0.000 | 1 | prior_season_only |
| 14 | MIN | 0.320 | 0.000 | 0.000 | 1 | prior_season_only |
| 15 | WAS | 0.313 | 0.000 | 0.000 | 1 | prior_season_only |
| 16 | CAR | 0.311 | 0.000 | 0.000 | 1 | prior_season_only |
| 17 | BUF | 0.205 | 0.000 | 0.000 | 1 | prior_season_only |
| 18 | GB | 0.177 | 0.000 | 0.000 | 1 | prior_season_only |
| 19 | KC | 0.170 | 0.000 | 0.000 | 1 | prior_season_only |
| 20 | LAC | 0.152 | 0.000 | 0.000 | 1 | prior_season_only |
| 21 | CHI | 0.015 | 0.000 | 0.000 | 1 | prior_season_only |
| 22 | DEN | -0.028 | 0.000 | 0.000 | 1 | prior_season_only |
| 23 | NE | -0.069 | 0.000 | 0.000 | 1 | prior_season_only |
| 24 | LV | -0.142 | 0.000 | 0.000 | 1 | prior_season_only |
| 25 | PHI | -0.168 | 0.000 | 0.000 | 1 | prior_season_only |
| 26 | TB | -0.204 | 0.000 | 0.000 | 1 | prior_season_only |
| 27 | NYG | -0.222 | 0.000 | 0.000 | 1 | prior_season_only |
| 28 | ATL | -0.253 | 0.000 | 0.000 | 1 | prior_season_only |
| 29 | ARI | -0.440 | 0.000 | 0.000 | 1 | prior_season_only |
| 30 | LA | -0.455 | 0.000 | 0.000 | 1 | prior_season_only |
| 31 | CLE | -0.635 | 0.000 | 0.000 | 1 | prior_season_only |
| 32 | NO | -0.962 | 0.000 | 0.000 | 1 | prior_season_only |

