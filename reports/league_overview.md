# League Overview — 2026 (through Week 1)

> These indices are **transparent research indices**, not ratings, probabilities, or predictions of game outcomes. Each is an equal-weight mean of its member metrics' oriented, shrunk z-scores (reference-SD units). The member metrics are shown alongside every index. This project does not model game winners, scores, or spreads.

Generated 2026-09-16T01:32:02+00:00. Source tables: `outputs/rankings/team_rankings_weekly.csv`, `outputs/team_strength/team_metrics_weekly.parquet`, `outputs/weekly/weekly_metric_detail.csv`.

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
| 1 | JAX | 0.589 | 0.348 | 0.348 | 3 | low |
| 2 | NYG | 0.558 | 0.524 | 0.524 | 3 | low |
| 3 | CHI | 0.491 | -0.084 | -0.084 | 3 | low |
| 4 | SF | 0.437 | -0.254 | -0.254 | 3 | low |
| 5 | BAL | 0.278 | 0.013 | 0.013 | 3 | low |
| 6 | DAL | 0.233 | -0.602 | -0.602 | 3 | low |
| 7 | NYJ | 0.229 | 1.035 | 1.035 | 3 | low |
| 8 | BUF | 0.229 | -0.868 | -0.868 | 3 | low |
| 9 | ARI | 0.219 | 0.326 | 0.326 | 3 | low |
| 10 | CAR | 0.207 | 0.387 | 0.387 | 3 | low |
| 11 | HOU | 0.166 | 0.363 | 0.363 | 3 | low |
| 12 | CIN | 0.119 | -0.027 | -0.027 | 3 | low |
| 13 | TB | 0.111 | 0.071 | 0.071 | 3 | low |
| 14 | DET | 0.023 | -0.508 | -0.508 | 3 | low |
| 15 | NO | 0.020 | 0.410 | 0.410 | 3 | low |
| 16 | WAS | 0.006 | -0.420 | -0.420 | 3 | low |
| 17 | SEA | -0.049 | -0.513 | -0.513 | 3 | low |
| 18 | KC | -0.067 | -0.325 | -0.325 | 3 | low |
| 19 | LV | -0.120 | 1.217 | 1.217 | 3 | low |
| 20 | TEN | -0.121 | 1.001 | 1.001 | 3 | low |
| 21 | GB | -0.127 | -1.005 | -1.005 | 3 | low |
| 22 | CLE | -0.129 | 1.442 | 1.442 | 3 | low |
| 23 | LA | -0.146 | -1.672 | -1.672 | 3 | low |
| 24 | LAC | -0.162 | 0.003 | 0.003 | 3 | low |
| 25 | NE | -0.172 | -1.279 | -1.279 | 3 | low |
| 26 | IND | -0.198 | -0.811 | -0.811 | 3 | low |
| 27 | MIN | -0.225 | 0.168 | 0.168 | 3 | low |
| 28 | PHI | -0.275 | -0.334 | -0.334 | 3 | low |
| 29 | MIA | -0.295 | -0.190 | -0.190 | 3 | low |
| 30 | PIT | -0.362 | -0.483 | -0.483 | 3 | low |
| 31 | DEN | -0.373 | -0.536 | -0.536 | 3 | low |
| 32 | ATL | -0.406 | -0.660 | -0.660 | 3 | low |

## Passing-Offense Strength Index (`passing_offense`)
Member metrics: `team_offense.pass_epa_per_dropback`, `team_offense.pass_success_rate`, `team_offense.explosive_pass_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | JAX | 0.544 | 0.249 | 0.249 | 3 | low |
| 2 | CHI | 0.334 | 0.051 | 0.051 | 3 | low |
| 3 | NYG | 0.313 | 0.385 | 0.385 | 3 | low |
| 4 | BUF | 0.252 | -0.538 | -0.538 | 3 | low |
| 5 | BAL | 0.239 | 0.131 | 0.131 | 3 | low |
| 6 | NYJ | 0.217 | 1.183 | 1.183 | 3 | low |
| 7 | CAR | 0.154 | 0.387 | 0.387 | 3 | low |
| 8 | ARI | 0.143 | 0.295 | 0.295 | 3 | low |
| 9 | SEA | 0.117 | -0.706 | -0.706 | 3 | low |
| 10 | SF | 0.110 | -0.560 | -0.560 | 3 | low |
| 11 | HOU | 0.079 | 0.085 | 0.085 | 3 | low |
| 12 | CIN | 0.037 | 0.217 | 0.217 | 3 | low |
| 13 | NO | 0.024 | 0.455 | 0.455 | 3 | low |
| 14 | GB | 0.020 | -0.909 | -0.909 | 3 | low |
| 15 | DAL | 0.012 | -0.404 | -0.404 | 3 | low |
| 16 | PHI | 0.000 | 0.009 | 0.009 | 3 | low |
| 17 | NE | -0.014 | -1.330 | -1.330 | 3 | low |
| 18 | CLE | -0.039 | 1.283 | 1.283 | 3 | low |
| 19 | KC | -0.047 | -0.138 | -0.138 | 3 | low |
| 20 | WAS | -0.070 | -0.134 | -0.134 | 3 | low |
| 21 | MIA | -0.072 | 0.078 | 0.078 | 3 | low |
| 22 | TB | -0.078 | -0.098 | -0.098 | 3 | low |
| 23 | LV | -0.088 | 0.652 | 0.652 | 3 | low |
| 24 | DET | -0.100 | -0.773 | -0.773 | 3 | low |
| 25 | MIN | -0.123 | 0.498 | 0.498 | 3 | low |
| 26 | TEN | -0.125 | 0.887 | 0.887 | 3 | low |
| 27 | LAC | -0.135 | 0.047 | 0.047 | 3 | low |
| 28 | LA | -0.187 | -1.282 | -1.282 | 3 | low |
| 29 | PIT | -0.205 | -0.040 | -0.040 | 3 | low |
| 30 | IND | -0.221 | -0.373 | -0.373 | 3 | low |
| 31 | ATL | -0.273 | -0.247 | -0.247 | 3 | low |
| 32 | DEN | -0.277 | -0.292 | -0.292 | 3 | low |

## Rushing-Offense Strength Index (`rushing_offense`)
Member metrics: `team_offense.rush_epa_per_play`, `team_offense.rush_success_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SF | 0.222 | -0.073 | -0.073 | 2 | low |
| 2 | IND | 0.150 | -0.670 | -0.670 | 2 | low |
| 3 | TB | 0.148 | 0.170 | 0.170 | 2 | low |
| 4 | NYG | 0.139 | -0.038 | -0.038 | 2 | low |
| 5 | KC | 0.138 | 0.010 | 0.010 | 2 | low |
| 6 | JAX | 0.127 | 0.160 | 0.160 | 2 | low |
| 7 | BAL | 0.108 | -0.437 | -0.437 | 2 | low |
| 8 | DET | 0.103 | 0.086 | 0.086 | 2 | low |
| 9 | WAS | 0.096 | -0.257 | -0.257 | 2 | low |
| 10 | NYJ | 0.088 | 0.109 | 0.109 | 2 | low |
| 11 | CHI | 0.087 | -0.678 | -0.678 | 2 | low |
| 12 | HOU | 0.062 | 0.637 | 0.637 | 2 | low |
| 13 | CIN | 0.050 | -0.674 | -0.674 | 2 | low |
| 14 | LA | 0.046 | -1.069 | -1.069 | 2 | low |
| 15 | CAR | 0.044 | -0.096 | -0.096 | 2 | low |
| 16 | ATL | 0.025 | -0.107 | -0.107 | 2 | low |
| 17 | LV | 0.023 | 1.464 | 1.464 | 2 | low |
| 18 | ARI | 0.014 | 0.474 | 0.474 | 2 | low |
| 19 | CLE | 0.006 | 0.588 | 0.588 | 2 | low |
| 20 | DAL | 0.004 | -0.544 | -0.544 | 2 | low |
| 21 | TEN | -0.006 | 0.310 | 0.310 | 2 | low |
| 22 | NO | -0.094 | 0.424 | 0.424 | 2 | low |
| 23 | MIN | -0.096 | -0.436 | -0.436 | 2 | low |
| 24 | LAC | -0.135 | -0.063 | -0.063 | 2 | low |
| 25 | BUF | -0.156 | -1.062 | -1.062 | 2 | low |
| 26 | SEA | -0.159 | -0.151 | -0.151 | 2 | low |
| 27 | PHI | -0.171 | -0.344 | -0.344 | 2 | low |
| 28 | PIT | -0.189 | -0.758 | -0.758 | 2 | low |
| 29 | DEN | -0.191 | -0.404 | -0.404 | 2 | low |
| 30 | GB | -0.221 | -0.492 | -0.492 | 2 | low |
| 31 | NE | -0.322 | -0.142 | -0.142 | 2 | low |
| 32 | MIA | -0.324 | -0.526 | -0.526 | 2 | low |

## Pass-Protection Strength Index (`pass_protection`)
Member metrics: `pass_protection.sack_rate_allowed`, `pass_protection.qb_hit_rate_allowed`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | NYJ | 0.377 | 1.437 | 1.437 | 2 | low |
| 2 | SF | 0.348 | -0.212 | -0.212 | 2 | low |
| 3 | LV | 0.333 | 1.525 | 1.525 | 2 | low |
| 4 | DAL | 0.301 | -0.119 | -0.119 | 2 | low |
| 5 | WAS | 0.275 | 0.173 | 0.173 | 2 | low |
| 6 | CHI | 0.153 | -0.789 | -0.789 | 2 | low |
| 7 | ARI | 0.149 | 0.673 | 0.673 | 2 | low |
| 8 | CAR | 0.108 | 0.023 | 0.023 | 2 | low |
| 9 | JAX | 0.107 | -0.110 | -0.110 | 2 | low |
| 10 | BUF | 0.099 | -0.125 | -0.125 | 2 | low |
| 11 | CIN | 0.087 | -0.160 | -0.160 | 2 | low |
| 12 | PIT | 0.068 | -0.583 | -0.583 | 2 | low |
| 13 | BAL | 0.063 | 0.702 | 0.702 | 2 | low |
| 14 | DET | 0.039 | 0.443 | 0.443 | 2 | low |
| 15 | NE | 0.029 | 0.247 | 0.247 | 2 | low |
| 16 | NYG | 0.006 | 0.555 | 0.555 | 2 | low |
| 16 | KC | 0.006 | 0.386 | 0.386 | 2 | low |
| 18 | TEN | -0.003 | 0.627 | 0.627 | 2 | low |
| 19 | LAC | -0.005 | 0.972 | 0.972 | 2 | low |
| 20 | LA | -0.026 | -0.785 | -0.785 | 2 | low |
| 21 | NO | -0.042 | -0.156 | -0.156 | 2 | low |
| 22 | PHI | -0.084 | -0.653 | -0.653 | 2 | low |
| 23 | HOU | -0.132 | -0.708 | -0.708 | 2 | low |
| 24 | MIN | -0.136 | 1.277 | 1.277 | 2 | low |
| 25 | SEA | -0.154 | -0.715 | -0.715 | 2 | low |
| 26 | TB | -0.169 | -0.888 | -0.888 | 2 | low |
| 27 | DEN | -0.173 | -1.177 | -1.177 | 2 | low |
| 28 | IND | -0.181 | -0.591 | -0.591 | 2 | low |
| 29 | ATL | -0.339 | -0.939 | -0.939 | 2 | low |
| 30 | GB | -0.368 | -0.601 | -0.601 | 2 | low |
| 31 | MIA | -0.370 | -0.507 | -0.507 | 2 | low |
| 32 | CLE | -0.503 | 0.412 | 0.412 | 2 | low |

## Defensive Strength Index (`defense_overall`)
Member metrics: `team_defense.epa_per_play`, `team_defense.success_rate`, `team_defense.early_down_epa_per_play`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PIT | 0.241 | 0.170 | 0.170 | 3 | low |
| 2 | KC | 0.217 | 0.193 | 0.193 | 3 | low |
| 3 | ATL | 0.196 | 0.346 | 0.346 | 3 | low |
| 4 | LV | 0.155 | 0.225 | 0.225 | 3 | low |
| 5 | BAL | 0.133 | 0.309 | 0.309 | 3 | low |
| 6 | WAS | 0.132 | 1.177 | 1.177 | 3 | low |
| 7 | GB | 0.118 | 0.417 | 0.417 | 3 | low |
| 8 | SEA | 0.104 | -0.635 | -0.635 | 3 | low |
| 9 | SF | 0.103 | 0.783 | 0.783 | 3 | low |
| 10 | ARI | 0.095 | 0.996 | 0.996 | 3 | low |
| 11 | JAX | 0.090 | -0.376 | -0.376 | 3 | low |
| 12 | NYJ | 0.088 | 0.951 | 0.951 | 3 | low |
| 13 | MIA | 0.080 | 0.801 | 0.801 | 3 | low |
| 14 | MIN | 0.064 | -0.558 | -0.558 | 3 | low |
| 15 | DEN | 0.030 | -0.686 | -0.686 | 3 | low |
| 16 | NE | 0.009 | -0.016 | -0.016 | 3 | low |
| 17 | NO | -0.002 | -0.398 | -0.398 | 3 | low |
| 18 | PHI | -0.003 | -0.298 | -0.298 | 3 | low |
| 19 | DET | -0.007 | -0.159 | -0.159 | 3 | low |
| 20 | CIN | -0.025 | 0.850 | 0.850 | 3 | low |
| 21 | TB | -0.054 | 0.190 | 0.190 | 3 | low |
| 22 | BUF | -0.083 | -0.284 | -0.284 | 3 | low |
| 23 | LAC | -0.117 | -0.688 | -0.688 | 3 | low |
| 24 | CHI | -0.117 | 0.374 | 0.374 | 3 | low |
| 25 | TEN | -0.124 | 0.483 | 0.483 | 3 | low |
| 26 | NYG | -0.132 | 0.527 | 0.527 | 3 | low |
| 27 | HOU | -0.163 | -1.094 | -1.094 | 3 | low |
| 28 | IND | -0.166 | -0.008 | -0.008 | 3 | low |
| 29 | LA | -0.218 | -0.681 | -0.681 | 3 | low |
| 30 | CAR | -0.276 | -0.140 | -0.140 | 3 | low |
| 31 | DAL | -0.290 | 0.683 | 0.683 | 3 | low |
| 32 | CLE | -0.307 | -0.902 | -0.902 | 3 | low |

## Pass-Defense Strength Index (`passing_defense`)
Member metrics: `team_defense.pass_epa_per_dropback`, `team_defense.pass_success_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PIT | 0.333 | 0.363 | 0.363 | 2 | low |
| 2 | BAL | 0.213 | 0.423 | 0.423 | 2 | low |
| 3 | ATL | 0.208 | 0.109 | 0.109 | 2 | low |
| 4 | KC | 0.203 | 0.247 | 0.247 | 2 | low |
| 5 | SF | 0.188 | 0.800 | 0.800 | 2 | low |
| 6 | LV | 0.144 | 0.556 | 0.556 | 2 | low |
| 7 | ARI | 0.120 | 0.999 | 0.999 | 2 | low |
| 8 | GB | 0.078 | 0.161 | 0.161 | 2 | low |
| 9 | JAX | 0.069 | -0.507 | -0.507 | 2 | low |
| 10 | MIN | 0.067 | -0.809 | -0.809 | 2 | low |
| 11 | CIN | 0.059 | 0.826 | 0.826 | 2 | low |
| 12 | NO | 0.043 | -0.258 | -0.258 | 2 | low |
| 13 | NYJ | 0.043 | 0.993 | 0.993 | 2 | low |
| 14 | MIA | 0.040 | 0.981 | 0.981 | 2 | low |
| 15 | DEN | 0.030 | -0.947 | -0.947 | 2 | low |
| 16 | WAS | 0.015 | 0.884 | 0.884 | 2 | low |
| 17 | PHI | 0.013 | -0.580 | -0.580 | 2 | low |
| 18 | DET | -0.002 | -0.334 | -0.334 | 2 | low |
| 19 | TB | -0.033 | 0.451 | 0.451 | 2 | low |
| 20 | BUF | -0.062 | -0.622 | -0.622 | 2 | low |
| 21 | SEA | -0.074 | -0.706 | -0.706 | 2 | low |
| 22 | NE | -0.084 | -0.302 | -0.302 | 2 | low |
| 23 | NYG | -0.103 | 0.005 | 0.005 | 2 | low |
| 24 | CHI | -0.117 | 0.159 | 0.159 | 2 | low |
| 25 | TEN | -0.140 | 0.559 | 0.559 | 2 | low |
| 26 | LA | -0.172 | -0.527 | -0.527 | 2 | low |
| 27 | HOU | -0.176 | -1.153 | -1.153 | 2 | low |
| 28 | LAC | -0.180 | -0.681 | -0.681 | 2 | low |
| 29 | IND | -0.221 | -0.009 | -0.009 | 2 | low |
| 30 | CAR | -0.319 | 0.085 | 0.085 | 2 | low |
| 31 | DAL | -0.419 | 0.580 | 0.580 | 2 | low |
| 32 | CLE | -0.468 | -1.092 | -1.092 | 2 | low |

## Run-Defense Strength Index (`rushing_defense`)
Member metrics: `team_defense.rush_epa_per_play`, `team_defense.rush_success_rate`, `team_defense.explosive_rush_rate`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SEA | 0.295 | -0.733 | -0.733 | 3 | low |
| 2 | LV | 0.262 | 0.233 | 0.233 | 3 | low |
| 3 | MIN | 0.182 | 0.159 | 0.159 | 3 | low |
| 4 | ATL | 0.176 | 0.377 | 0.377 | 3 | low |
| 5 | KC | 0.164 | -0.163 | -0.163 | 3 | low |
| 6 | WAS | 0.159 | 0.815 | 0.815 | 3 | low |
| 7 | ARI | 0.149 | 0.610 | 0.610 | 3 | low |
| 8 | GB | 0.126 | 0.187 | 0.187 | 3 | low |
| 9 | NE | 0.114 | 0.160 | 0.160 | 3 | low |
| 10 | HOU | 0.110 | -0.553 | -0.553 | 3 | low |
| 11 | NYG | 0.098 | 1.454 | 1.454 | 3 | low |
| 12 | DET | 0.070 | 0.327 | 0.327 | 3 | low |
| 13 | JAX | 0.049 | -0.436 | -0.436 | 3 | low |
| 14 | LAC | 0.022 | -0.081 | -0.081 | 3 | low |
| 15 | SF | 0.010 | 0.206 | 0.206 | 3 | low |
| 16 | PIT | -0.003 | 0.071 | 0.071 | 3 | low |
| 17 | CHI | -0.012 | 0.408 | 0.408 | 3 | low |
| 18 | PHI | -0.029 | -0.041 | -0.041 | 3 | low |
| 19 | MIA | -0.031 | 0.320 | 0.320 | 3 | low |
| 20 | TEN | -0.039 | -0.090 | -0.090 | 3 | low |
| 21 | BUF | -0.044 | 0.734 | 0.734 | 3 | low |
| 22 | CIN | -0.068 | 0.566 | 0.566 | 3 | low |
| 23 | NYJ | -0.087 | 0.189 | 0.189 | 3 | low |
| 24 | CAR | -0.087 | -0.062 | -0.062 | 3 | low |
| 25 | TB | -0.099 | -0.482 | -0.482 | 3 | low |
| 26 | IND | -0.106 | -0.187 | -0.187 | 3 | low |
| 27 | DAL | -0.116 | 0.743 | 0.743 | 3 | low |
| 28 | DEN | -0.141 | -0.767 | -0.767 | 3 | low |
| 29 | CLE | -0.145 | -0.365 | -0.365 | 3 | low |
| 30 | NO | -0.150 | -0.515 | -0.515 | 3 | low |
| 31 | LA | -0.195 | -0.562 | -0.562 | 3 | low |
| 32 | BAL | -0.264 | -0.356 | -0.356 | 3 | low |

## Pass-Rush Strength Index (`pass_rush`)
Member metrics: `pass_rush.qb_hit_rate_generated`, `pass_rush.sack_rate_generated`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | JAX | 0.432 | 1.054 | 1.054 | 2 | low |
| 2 | LV | 0.316 | 0.467 | 0.467 | 2 | low |
| 3 | PIT | 0.303 | 0.054 | 0.054 | 2 | low |
| 4 | MIN | 0.286 | -0.739 | -0.739 | 2 | low |
| 5 | KC | 0.162 | 0.030 | 0.030 | 2 | low |
| 6 | CIN | 0.153 | 0.516 | 0.516 | 2 | low |
| 7 | BAL | 0.132 | 0.708 | 0.708 | 2 | low |
| 8 | GB | 0.122 | 0.083 | 0.083 | 2 | low |
| 9 | NE | 0.120 | 0.251 | 0.251 | 2 | low |
| 10 | BUF | 0.103 | -0.139 | -0.139 | 2 | low |
| 11 | WAS | 0.078 | 0.044 | 0.044 | 2 | low |
| 12 | DET | 0.042 | -0.340 | -0.340 | 2 | low |
| 13 | ARI | 0.017 | 0.781 | 0.781 | 2 | low |
| 14 | NYJ | 0.010 | 0.968 | 0.968 | 2 | low |
| 15 | DAL | -0.006 | -0.010 | -0.010 | 2 | low |
| 15 | DEN | -0.006 | -1.515 | -1.515 | 2 | low |
| 17 | SEA | -0.017 | -0.236 | -0.236 | 2 | low |
| 18 | SF | -0.017 | 1.354 | 1.354 | 2 | low |
| 19 | IND | -0.043 | 0.281 | 0.281 | 2 | low |
| 20 | NO | -0.051 | -0.313 | -0.313 | 2 | low |
| 21 | ATL | -0.060 | -0.630 | -0.630 | 2 | low |
| 22 | HOU | -0.073 | -0.299 | -0.299 | 2 | low |
| 23 | TB | -0.085 | 0.210 | 0.210 | 2 | low |
| 24 | CHI | -0.089 | 0.168 | 0.168 | 2 | low |
| 25 | CLE | -0.092 | -1.165 | -1.165 | 2 | low |
| 26 | CAR | -0.119 | 0.722 | 0.722 | 2 | low |
| 27 | LAC | -0.132 | -0.442 | -0.442 | 2 | low |
| 28 | PHI | -0.225 | -0.455 | -0.455 | 2 | low |
| 29 | NYG | -0.259 | -0.247 | -0.247 | 2 | low |
| 30 | MIA | -0.283 | -0.091 | -0.091 | 2 | low |
| 31 | LA | -0.294 | -0.753 | -0.753 | 2 | low |
| 32 | TEN | -0.316 | -0.528 | -0.528 | 2 | low |

## Special-Teams Strength Index (`special_teams`)
Member metrics: `special_teams.st_epa_per_play`

| rank | team | index_value | delta_vs_prev_week | delta_vs_preseason | n_metrics_used | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CLE | 0.280 | 0.915 | 0.915 | 1 | low |
| 2 | LV | 0.247 | 0.390 | 0.390 | 1 | low |
| 3 | CIN | 0.214 | -0.504 | -0.504 | 1 | low |
| 4 | TB | 0.214 | 0.418 | 0.418 | 1 | low |
| 5 | CHI | 0.188 | 0.173 | 0.173 | 1 | low |
| 6 | BAL | 0.164 | -0.255 | -0.255 | 1 | low |
| 7 | BUF | 0.161 | -0.044 | -0.044 | 1 | low |
| 8 | NYJ | 0.146 | -1.300 | -1.300 | 1 | low |
| 9 | KC | 0.136 | -0.034 | -0.034 | 1 | low |
| 10 | IND | 0.134 | -0.527 | -0.527 | 1 | low |
| 11 | JAX | 0.134 | -0.610 | -0.610 | 1 | low |
| 12 | DEN | 0.126 | 0.153 | 0.153 | 1 | low |
| 13 | HOU | 0.121 | -0.247 | -0.247 | 1 | low |
| 14 | GB | 0.108 | -0.069 | -0.069 | 1 | low |
| 15 | MIN | 0.089 | -0.231 | -0.231 | 1 | low |
| 16 | SEA | 0.037 | -0.604 | -0.604 | 1 | low |
| 17 | NE | 0.027 | 0.096 | 0.096 | 1 | low |
| 18 | NYG | 0.004 | 0.226 | 0.226 | 1 | low |
| 19 | PHI | 0.003 | 0.171 | 0.171 | 1 | low |
| 20 | PIT | -0.002 | -0.407 | -0.407 | 1 | low |
| 21 | WAS | -0.032 | -0.345 | -0.345 | 1 | low |
| 22 | LA | -0.035 | 0.421 | 0.421 | 1 | low |
| 23 | DET | -0.037 | -0.435 | -0.435 | 1 | low |
| 24 | CAR | -0.055 | -0.366 | -0.366 | 1 | low |
| 25 | SF | -0.082 | -0.882 | -0.882 | 1 | low |
| 26 | MIA | -0.093 | -0.864 | -0.864 | 1 | low |
| 27 | DAL | -0.111 | -0.778 | -0.778 | 1 | low |
| 28 | ATL | -0.129 | 0.124 | 0.124 | 1 | low |
| 29 | NO | -0.134 | 0.829 | 0.829 | 1 | low |
| 30 | ARI | -0.231 | 0.209 | 0.209 | 1 | low |
| 31 | TEN | -0.256 | -0.619 | -0.619 | 1 | low |
| 32 | LAC | -0.286 | -0.438 | -0.438 | 1 | low |

## Results context
| team | wins | losses | ties | points_for | points_against | point_diff |
| --- | --- | --- | --- | --- | --- | --- |
| JAX | 1 | 0 | 0 | 34 | 10 | 24 |
| CHI | 1 | 0 | 0 | 59 | 37 | 22 |
| KC | 1 | 0 | 0 | 31 | 10 | 21 |
| SF | 1 | 0 | 0 | 27 | 7 | 20 |
| BAL | 1 | 0 | 0 | 41 | 23 | 18 |
| MIN | 1 | 0 | 0 | 39 | 22 | 17 |
| LV | 1 | 0 | 0 | 27 | 13 | 14 |
| NYJ | 1 | 0 | 0 | 23 | 10 | 13 |
| ARI | 1 | 0 | 0 | 26 | 14 | 12 |
| NYG | 1 | 0 | 0 | 28 | 20 | 8 |
| PIT | 1 | 0 | 0 | 20 | 13 | 7 |
| CIN | 1 | 0 | 0 | 33 | 27 | 6 |
| BUF | 1 | 0 | 0 | 36 | 31 | 5 |
| SEA | 1 | 0 | 0 | 13 | 10 | 3 |
| PHI | 1 | 0 | 0 | 24 | 22 | 2 |
| DET | 1 | 0 | 0 | 31 | 30 | 1 |
| NO | 0 | 1 | 0 | 30 | 31 | -1 |
| WAS | 0 | 1 | 0 | 22 | 24 | -2 |
| NE | 0 | 1 | 0 | 10 | 13 | -3 |
| HOU | 0 | 1 | 0 | 31 | 36 | -5 |
| TB | 0 | 1 | 0 | 27 | 33 | -6 |
| ATL | 0 | 1 | 0 | 13 | 20 | -7 |
| DAL | 0 | 1 | 0 | 20 | 28 | -8 |
| LAC | 0 | 1 | 0 | 14 | 26 | -12 |
| TEN | 0 | 1 | 0 | 10 | 23 | -13 |
| MIA | 0 | 1 | 0 | 13 | 27 | -14 |
| GB | 0 | 1 | 0 | 22 | 39 | -17 |
| IND | 0 | 1 | 0 | 23 | 41 | -18 |
| LA | 0 | 1 | 0 | 7 | 27 | -20 |
| DEN | 0 | 1 | 0 | 10 | 31 | -21 |
| CAR | 0 | 1 | 0 | 37 | 59 | -22 |
| CLE | 0 | 1 | 0 | 10 | 34 | -24 |
