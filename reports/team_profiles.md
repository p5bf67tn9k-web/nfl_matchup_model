# Team Profiles — 2026 (preseason baseline)

> These indices are **transparent research indices**, not ratings, probabilities, or predictions of game outcomes. Each is an equal-weight mean of its member metrics' oriented, shrunk z-scores (reference-SD units). The member metrics are shown alongside every index. This project does not model game winners, scores, or spreads.

Every profile shows the domain indices AND the underlying per-metric numbers (raw value, league reference mean/SD, sample size, shrunk value, percentile, confidence). Full detail: `outputs/team_strength/team_metrics_weekly.parquet`.

## ARI
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **offense_overall** (-0.107) · Weakest area: **defense_overall** (-0.901)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.901 | 30 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.764 | 29 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.879 | 29 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.461 | 27 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.107 | 23 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.524 | 24 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.152 | 22 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.460 | 28 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.440 | 29 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1732 | 0.1450 | 0.0327 | 17 | 745 | 0.1641 | 0.5851 | -0.5851 | 24 | 0.2581 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2441 | 0.2045 | 0.0323 | 17 | 745 | 0.2249 | 0.6303 | -0.6303 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0792 | 0.0664 | 0.0188 | 17 | 745 | 0.0751 | 0.4631 | -0.4631 | 25 | 0.2258 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1113 | 0.1442 | 0.0234 | 17 | 620 | 0.1272 | -0.7239 | -0.7239 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0484 | 0.0660 | 0.0121 | 17 | 620 | 0.0564 | -0.8036 | -0.8036 | 28 | 0.1290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.7576 | 0.8507 | 0.0691 | 17 | 233 | 0.8027 | -0.6940 | -0.6940 | 30 | 0.0645 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | -0.0171 | 0.0622 | 0.0928 | 17 | 233 | 0.0214 | -0.4399 | -0.4399 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.1287 | -0.0013 | 0.0639 | 17 | 1102 | 0.0657 | 1.0482 | -1.0482 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0897 | 0.0046 | 0.0677 | 17 | 1102 | 0.0484 | 0.6468 | -0.6468 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0839 | 0.0797 | 0.0112 | 17 | 1102 | 0.0820 | 0.2047 | -0.2047 | 22 | 0.3226 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1242 | 0.1000 | 0.0206 | 17 | 1102 | 0.1124 | 0.6052 | -0.6052 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1654 | 0.0361 | 0.0949 | 17 | 1102 | 0.1027 | 0.7019 | -0.7019 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.5194 | 0.4536 | 0.0320 | 17 | 1102 | 0.4875 | 1.0566 | -1.0566 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0379 | -0.0760 | 0.0649 | 17 | 1102 | -0.0551 | 0.3221 | -0.3221 | 22 | 0.3226 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4312 | 0.4020 | 0.0330 | 17 | 1102 | 0.4170 | 0.4558 | -0.4558 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4882 | 0.4384 | 0.0255 | 17 | 1102 | 0.4641 | 1.0080 | -1.0080 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0115 | -0.0054 | 0.0784 | 17 | 1128 | -0.0095 | -0.0528 | -0.0528 | 22 | 0.3226 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0137 | -0.0001 | 0.0921 | 17 | 1128 | -0.0094 | -0.1006 | -0.1006 | 23 | 0.2903 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0658 | 0.0796 | 0.0177 | 17 | 1128 | 0.0725 | -0.4010 | -0.4010 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0735 | 0.0990 | 0.0195 | 17 | 1128 | 0.0859 | -0.6721 | -0.6721 | 30 | 0.0645 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0238 | 0.0308 | 0.1280 | 17 | 1128 | 0.0260 | -0.0372 | -0.0372 | 20 | 0.3871 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4510 | 0.4521 | 0.0418 | 17 | 1128 | 0.4514 | -0.0174 | -0.0174 | 18 | 0.4516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | 0.0036 | -0.0477 | 0.0349 | 17 | 1128 | -0.0062 | 1.1904 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.1423 | -0.0806 | 0.0754 | 17 | 1128 | -0.1124 | -0.4219 | -0.4219 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3676 | 0.4004 | 0.0385 | 17 | 1128 | 0.3812 | -0.4980 | -0.4980 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4300 | 0.4370 | 0.0337 | 17 | 1128 | 0.4313 | -0.1678 | -0.1678 | 24 | 0.2581 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## ATL
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_protection** (0.600) · Weakest area: **special_teams** (-0.253)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.151 | 18 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.570 | 4 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.099 | 14 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.201 | 22 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.254 | 14 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.600 | 6 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.026 | 19 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.132 | 18 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.253 | 28 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1252 | 0.1450 | 0.0327 | 17 | 583 | 0.1315 | -0.4111 | 0.4111 | 12 | 0.6452 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1866 | 0.2045 | 0.0323 | 17 | 583 | 0.1953 | -0.2864 | 0.2864 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0446 | 0.0664 | 0.0188 | 17 | 583 | 0.0516 | -0.7896 | 0.7896 | 5 | 0.8710 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1440 | 0.1442 | 0.0234 | 17 | 625 | 0.1441 | -0.0038 | -0.0038 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0912 | 0.0660 | 0.0121 | 17 | 625 | 0.0798 | 1.1445 | 1.1445 | 4 | 0.9032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8205 | 0.8507 | 0.0691 | 17 | 227 | 0.8352 | -0.2250 | -0.2250 | 24 | 0.2581 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0166 | 0.0622 | 0.0928 | 17 | 227 | 0.0387 | -0.2530 | -0.2530 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0166 | -0.0013 | 0.0639 | 17 | 1088 | 0.0079 | 0.1440 | -0.1440 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0083 | 0.0046 | 0.0677 | 17 | 1088 | 0.0065 | 0.0282 | -0.0282 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0784 | 0.0797 | 0.0112 | 17 | 1088 | 0.0790 | -0.0627 | 0.0627 | 18 | 0.4516 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0888 | 0.1000 | 0.0206 | 17 | 1088 | 0.0942 | -0.2794 | 0.2794 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0020 | 0.0361 | 0.0949 | 17 | 1088 | 0.0186 | -0.1850 | 0.1850 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4528 | 0.4536 | 0.0320 | 17 | 1088 | 0.4532 | -0.0135 | 0.0135 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0276 | -0.0760 | 0.0649 | 17 | 1088 | -0.0495 | 0.4083 | -0.4083 | 26 | 0.1935 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4322 | 0.4020 | 0.0330 | 17 | 1088 | 0.4176 | 0.4728 | -0.4728 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4522 | 0.4384 | 0.0255 | 17 | 1088 | 0.4455 | 0.2795 | -0.2795 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0678 | -0.0054 | 0.0784 | 17 | 1075 | 0.0444 | 0.6351 | 0.6351 | 8 | 0.7742 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0078 | -0.0001 | 0.0921 | 17 | 1075 | -0.0054 | -0.0569 | -0.0569 | 21 | 0.3548 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0806 | 0.0796 | 0.0177 | 17 | 1075 | 0.0801 | 0.0303 | 0.0303 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1128 | 0.0990 | 0.0195 | 17 | 1075 | 0.1061 | 0.3635 | 0.3635 | 8 | 0.7742 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0082 | 0.0308 | 0.1280 | 17 | 1075 | 0.0154 | -0.1199 | -0.1199 | 22 | 0.3226 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4528 | 0.4521 | 0.0418 | 17 | 1075 | 0.4526 | 0.0122 | 0.0122 | 15 | 0.5484 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0846 | -0.0477 | 0.0349 | 17 | 1075 | -0.0775 | -0.8560 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0731 | -0.0806 | 0.0754 | 17 | 1075 | -0.0768 | 0.0510 | 0.0510 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4143 | 0.4004 | 0.0385 | 17 | 1075 | 0.4085 | 0.2123 | 0.2123 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4447 | 0.4370 | 0.0337 | 17 | 1075 | 0.4432 | 0.1846 | 0.1846 | 16 | 0.5161 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## BAL
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_offense** (0.545) · Weakest area: **pass_protection** (-0.639)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.177 | 20 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.576 | 27 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.209 | 19 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.092 | 11 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.264 | 12 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.639 | 27 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.108 | 12 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.545 | 8 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.419 | 9 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1657 | 0.1450 | 0.0327 | 17 | 501 | 0.1591 | 0.4296 | -0.4296 | 22 | 0.3226 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1779 | 0.2045 | 0.0323 | 17 | 501 | 0.1908 | -0.4245 | 0.4245 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0898 | 0.0664 | 0.0188 | 17 | 501 | 0.0823 | 0.8478 | -0.8478 | 29 | 0.0968 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1387 | 0.1442 | 0.0234 | 17 | 692 | 0.1414 | -0.1199 | -0.1199 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0434 | 0.0660 | 0.0121 | 17 | 692 | 0.0536 | -1.0326 | -1.0326 | 31 | 0.0323 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8824 | 0.8507 | 0.0691 | 17 | 226 | 0.8670 | 0.2358 | 0.2358 | 12 | 0.6290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1377 | 0.0622 | 0.0928 | 17 | 226 | 0.1011 | 0.4189 | 0.4189 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0346 | -0.0013 | 0.0639 | 17 | 1114 | 0.0172 | 0.2896 | -0.2896 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0251 | 0.0046 | 0.0677 | 17 | 1114 | 0.0152 | 0.1559 | -0.1559 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0925 | 0.0797 | 0.0112 | 17 | 1114 | 0.0867 | 0.6258 | -0.6258 | 28 | 0.1290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1023 | 0.1000 | 0.0206 | 17 | 1114 | 0.1012 | 0.0587 | -0.0587 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0915 | 0.0361 | 0.0949 | 17 | 1114 | 0.0647 | 0.3008 | -0.3008 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4610 | 0.4536 | 0.0320 | 17 | 1114 | 0.4574 | 0.1181 | -0.1181 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1148 | -0.0760 | 0.0649 | 17 | 1114 | -0.0973 | -0.3272 | 0.3272 | 6 | 0.8387 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4015 | 0.4020 | 0.0330 | 17 | 1114 | 0.4017 | -0.0069 | 0.0069 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4425 | 0.4384 | 0.0255 | 17 | 1114 | 0.4405 | 0.0841 | -0.0841 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0307 | -0.0054 | 0.0784 | 17 | 992 | 0.0191 | 0.3126 | 0.3126 | 12 | 0.6452 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0369 | -0.0001 | 0.0921 | 17 | 992 | 0.0251 | 0.2737 | 0.2737 | 13 | 0.6129 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0858 | 0.0796 | 0.0177 | 17 | 992 | 0.0828 | 0.1817 | 0.1817 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1280 | 0.0990 | 0.0195 | 17 | 992 | 0.1139 | 0.7639 | 0.7639 | 2 | 0.9677 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0176 | 0.0308 | 0.1280 | 17 | 992 | 0.0218 | -0.0700 | -0.0700 | 21 | 0.3548 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4651 | 0.4521 | 0.0418 | 17 | 992 | 0.4609 | 0.2112 | 0.2112 | 12 | 0.6452 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.1111 | -0.0477 | 0.0349 | 17 | 992 | -0.0990 | -1.4716 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | 0.0382 | -0.0806 | 0.0754 | 17 | 992 | -0.0194 | 0.8121 | 0.8121 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4187 | 0.4004 | 0.0385 | 17 | 992 | 0.4111 | 0.2783 | 0.2783 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4456 | 0.4370 | 0.0337 | 17 | 992 | 0.4439 | 0.2065 | 0.2065 | 13 | 0.6129 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## BUF
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **offense_overall** (1.096) · Weakest area: **rushing_defense** (-0.777)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.201 | 11 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.242 | 10 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.561 | 8 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.777 | 30 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 1.096 | 3 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.223 | 15 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.790 | 5 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.907 | 2 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.205 | 17 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1199 | 0.1450 | 0.0327 | 17 | 584 | 0.1279 | -0.5223 | 0.5223 | 7 | 0.8065 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1588 | 0.2045 | 0.0323 | 17 | 584 | 0.1810 | -0.7289 | 0.7289 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0685 | 0.0664 | 0.0188 | 17 | 584 | 0.0678 | 0.0756 | -0.0756 | 19 | 0.4194 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1623 | 0.1442 | 0.0234 | 17 | 530 | 0.1535 | 0.3982 | 0.3982 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0679 | 0.0660 | 0.0121 | 17 | 530 | 0.0671 | 0.0854 | 0.0854 | 14 | 0.5806 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9048 | 0.8507 | 0.0691 | 17 | 204 | 0.8786 | 0.4028 | 0.4028 | 8 | 0.7742 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0992 | 0.0622 | 0.0928 | 17 | 204 | 0.0813 | 0.2049 | 0.2049 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0455 | -0.0013 | 0.0639 | 17 | 971 | -0.0241 | -0.3562 | 0.3562 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0068 | 0.0046 | 0.0677 | 17 | 971 | -0.0013 | -0.0867 | 0.0867 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0717 | 0.0797 | 0.0112 | 17 | 971 | 0.0753 | -0.3903 | 0.3903 | 10 | 0.7097 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1316 | 0.1000 | 0.0206 | 17 | 971 | 0.1162 | 0.7910 | -0.7910 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0674 | 0.0361 | 0.0949 | 17 | 971 | -0.0172 | -0.5622 | 0.5622 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4189 | 0.4536 | 0.0320 | 17 | 971 | 0.4357 | -0.5591 | 0.5591 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | 0.0491 | -0.0760 | 0.0649 | 17 | 971 | -0.0074 | 1.0562 | -1.0562 | 31 | 0.0323 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4330 | 0.4020 | 0.0330 | 17 | 971 | 0.4180 | 0.4849 | -0.4849 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4305 | 0.4384 | 0.0255 | 17 | 971 | 0.4343 | -0.1601 | 0.1601 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.1097 | -0.0054 | 0.0784 | 17 | 1097 | 0.0729 | 0.9986 | 0.9986 | 3 | 0.9355 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.1452 | -0.0001 | 0.0921 | 17 | 1097 | 0.0987 | 1.0729 | 1.0729 | 3 | 0.9355 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.1045 | 0.0796 | 0.0177 | 17 | 1097 | 0.0924 | 0.7227 | 0.7227 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1155 | 0.0990 | 0.0195 | 17 | 1097 | 0.1075 | 0.4338 | 0.4338 | 6 | 0.8387 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.2046 | 0.0308 | 0.1280 | 17 | 1097 | 0.1490 | 0.9238 | 0.9238 | 4 | 0.9032 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4966 | 0.4521 | 0.0418 | 17 | 1097 | 0.4823 | 0.7234 | 0.7234 | 6 | 0.8387 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0588 | -0.0477 | 0.0349 | 17 | 1097 | -0.0567 | -0.2577 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | 0.0386 | -0.0806 | 0.0754 | 17 | 1097 | -0.0192 | 0.8148 | 0.8148 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4660 | 0.4004 | 0.0385 | 17 | 1097 | 0.4388 | 0.9985 | 0.9985 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4877 | 0.4370 | 0.0337 | 17 | 1097 | 0.4780 | 1.2174 | 1.2174 | 2 | 0.9677 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## CAR
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **special_teams** (0.311) · Weakest area: **pass_rush** (-0.841)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.136 | 17 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.841 | 30 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.404 | 22 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.025 | 17 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.180 | 25 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.085 | 20 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.232 | 26 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.140 | 17 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.311 | 16 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1478 | 0.1450 | 0.0327 | 17 | 582 | 0.1469 | 0.0575 | -0.0575 | 21 | 0.3548 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1607 | 0.2045 | 0.0323 | 17 | 582 | 0.1819 | -0.6985 | 0.6985 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0601 | 0.0664 | 0.0188 | 17 | 582 | 0.0621 | -0.2269 | 0.2269 | 14 | 0.5806 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.0941 | 0.1442 | 0.0234 | 17 | 563 | 0.1184 | -1.1014 | -1.1014 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0533 | 0.0660 | 0.0121 | 17 | 563 | 0.0590 | -0.5806 | -0.5806 | 27 | 0.1613 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8276 | 0.8507 | 0.0691 | 17 | 206 | 0.8388 | -0.1723 | -0.1723 | 22 | 0.3226 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1183 | 0.0622 | 0.0928 | 17 | 206 | 0.0911 | 0.3109 | 0.3109 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0113 | -0.0013 | 0.0639 | 17 | 1039 | -0.0065 | -0.0809 | 0.0809 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0600 | 0.0046 | 0.0677 | 17 | 1039 | 0.0331 | 0.4214 | -0.4214 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0746 | 0.0797 | 0.0112 | 17 | 1039 | 0.0769 | -0.2485 | 0.2485 | 12 | 0.6452 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0911 | 0.1000 | 0.0206 | 17 | 1039 | 0.0954 | -0.2212 | 0.2212 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1187 | 0.0361 | 0.0949 | 17 | 1039 | 0.0787 | 0.4486 | -0.4486 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4760 | 0.4536 | 0.0320 | 17 | 1039 | 0.4652 | 0.3599 | -0.3599 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0248 | -0.0760 | 0.0649 | 17 | 1039 | -0.0479 | 0.4327 | -0.4327 | 27 | 0.1613 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3933 | 0.4020 | 0.0330 | 17 | 1039 | 0.3975 | -0.1350 | 0.1350 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4418 | 0.4384 | 0.0255 | 17 | 1039 | 0.4401 | 0.0683 | -0.0683 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0460 | -0.0054 | 0.0784 | 17 | 1035 | -0.0330 | -0.3521 | -0.3521 | 27 | 0.1613 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0247 | -0.0001 | 0.0921 | 17 | 1035 | -0.0168 | -0.1813 | -0.1813 | 26 | 0.1935 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0739 | 0.0796 | 0.0177 | 17 | 1035 | 0.0766 | -0.1653 | -0.1653 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0911 | 0.0990 | 0.0195 | 17 | 1035 | 0.0950 | -0.2080 | -0.2080 | 22 | 0.3226 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.0267 | 0.0308 | 0.1280 | 17 | 1035 | -0.0083 | -0.3055 | -0.3055 | 26 | 0.1935 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4381 | 0.4521 | 0.0418 | 17 | 1035 | 0.4426 | -0.2266 | -0.2266 | 25 | 0.2258 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0870 | -0.0477 | 0.0349 | 17 | 1035 | -0.0795 | -0.9125 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0720 | -0.0806 | 0.0754 | 17 | 1035 | -0.0762 | 0.0586 | 0.0586 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4149 | 0.4004 | 0.0385 | 17 | 1035 | 0.4089 | 0.2207 | 0.2207 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4367 | 0.4370 | 0.0337 | 17 | 1035 | 0.4368 | -0.0058 | -0.0058 | 18 | 0.4516 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## CHI
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_protection** (0.942) · Weakest area: **defense_overall** (-0.491)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.491 | 23 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.257 | 23 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.277 | 21 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.421 | 26 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.575 | 8 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.942 | 2 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.283 | 10 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.765 | 4 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.015 | 21 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1047 | 0.1450 | 0.0327 | 17 | 640 | 0.1176 | -0.8377 | 0.8377 | 4 | 0.9032 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1663 | 0.2045 | 0.0323 | 17 | 640 | 0.1848 | -0.6088 | 0.6088 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0375 | 0.0664 | 0.0188 | 17 | 640 | 0.0467 | -1.0466 | 1.0466 | 3 | 0.9355 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1351 | 0.1442 | 0.0234 | 17 | 592 | 0.1395 | -0.1990 | -0.1990 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0591 | 0.0660 | 0.0121 | 17 | 592 | 0.0622 | -0.3151 | -0.3151 | 21 | 0.3548 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8462 | 0.8507 | 0.0691 | 17 | 230 | 0.8484 | -0.0340 | -0.0340 | 18 | 0.4516 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0649 | 0.0622 | 0.0928 | 17 | 230 | 0.0636 | 0.0147 | 0.0147 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0706 | -0.0013 | 0.0639 | 17 | 1059 | 0.0357 | 0.5797 | -0.5797 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0348 | 0.0046 | 0.0677 | 17 | 1059 | 0.0201 | 0.2294 | -0.2294 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.1030 | 0.0797 | 0.0112 | 17 | 1059 | 0.0925 | 1.1418 | -1.1418 | 32 | 0.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1152 | 0.1000 | 0.0206 | 17 | 1059 | 0.1078 | 0.3815 | -0.3815 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0507 | 0.0361 | 0.0949 | 17 | 1059 | 0.0437 | 0.0794 | -0.0794 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4831 | 0.4536 | 0.0320 | 17 | 1059 | 0.4688 | 0.4738 | -0.4738 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0422 | -0.0760 | 0.0649 | 17 | 1059 | -0.0575 | 0.2852 | -0.2852 | 21 | 0.3548 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4401 | 0.4020 | 0.0330 | 17 | 1059 | 0.4216 | 0.5954 | -0.5954 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4712 | 0.4384 | 0.0255 | 17 | 1059 | 0.4553 | 0.6639 | -0.6639 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0741 | -0.0054 | 0.0784 | 17 | 1134 | 0.0487 | 0.6894 | 0.6894 | 6 | 0.8387 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0758 | -0.0001 | 0.0921 | 17 | 1134 | 0.0515 | 0.5605 | 0.5605 | 8 | 0.7742 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0938 | 0.0796 | 0.0177 | 17 | 1134 | 0.0869 | 0.4118 | 0.4118 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1160 | 0.0990 | 0.0195 | 17 | 1134 | 0.1078 | 0.4472 | 0.4472 | 5 | 0.8710 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.1196 | 0.0308 | 0.1280 | 17 | 1134 | 0.0912 | 0.4721 | 0.4721 | 8 | 0.7742 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4500 | 0.4521 | 0.0418 | 17 | 1134 | 0.4507 | -0.0338 | -0.0338 | 19 | 0.4194 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0654 | -0.0477 | 0.0349 | 17 | 1134 | -0.0621 | -0.4119 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | 0.0067 | -0.0806 | 0.0754 | 17 | 1134 | -0.0356 | 0.5970 | 0.5970 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4617 | 0.4004 | 0.0385 | 17 | 1134 | 0.4363 | 0.9335 | 0.9335 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4568 | 0.4370 | 0.0337 | 17 | 1134 | 0.4530 | 0.4759 | 0.4759 | 11 | 0.6774 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## CIN
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_offense** (0.724) · Weakest area: **defense_overall** (-0.874)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.874 | 29 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.363 | 26 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.767 | 27 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.634 | 28 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.147 | 17 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.248 | 13 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.180 | 24 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.724 | 5 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.718 | 5 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1456 | 0.1450 | 0.0327 | 17 | 687 | 0.1454 | 0.0117 | -0.0117 | 19 | 0.4194 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1378 | 0.2045 | 0.0323 | 17 | 687 | 0.1702 | -1.0621 | 1.0621 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0524 | 0.0664 | 0.0188 | 17 | 687 | 0.0569 | -0.5070 | 0.5070 | 10 | 0.7097 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1285 | 0.1442 | 0.0234 | 17 | 607 | 0.1361 | -0.3450 | -0.3450 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0577 | 0.0660 | 0.0121 | 17 | 607 | 0.0614 | -0.3816 | -0.3816 | 24 | 0.2581 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8929 | 0.8507 | 0.0691 | 17 | 236 | 0.8724 | 0.3140 | 0.3140 | 9 | 0.7419 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1916 | 0.0622 | 0.0928 | 17 | 236 | 0.1289 | 0.7178 | 0.7178 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.1195 | -0.0013 | 0.0639 | 17 | 1068 | 0.0609 | 0.9740 | -0.9740 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.1222 | 0.0046 | 0.0677 | 17 | 1068 | 0.0652 | 0.8946 | -0.8946 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0988 | 0.0797 | 0.0112 | 17 | 1068 | 0.0902 | 0.9368 | -0.9368 | 31 | 0.0323 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1181 | 0.1000 | 0.0206 | 17 | 1068 | 0.1093 | 0.4527 | -0.4527 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1788 | 0.0361 | 0.0949 | 17 | 1068 | 0.1096 | 0.7748 | -0.7748 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.5008 | 0.4536 | 0.0320 | 17 | 1068 | 0.4779 | 0.7586 | -0.7586 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | 0.0343 | -0.0760 | 0.0649 | 17 | 1068 | -0.0155 | 0.9311 | -0.9311 | 30 | 0.0645 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4352 | 0.4020 | 0.0330 | 17 | 1068 | 0.4191 | 0.5188 | -0.5188 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4757 | 0.4384 | 0.0255 | 17 | 1068 | 0.4576 | 0.7541 | -0.7541 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0406 | -0.0054 | 0.0784 | 17 | 1092 | -0.0293 | -0.3055 | -0.3055 | 25 | 0.2258 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0120 | -0.0001 | 0.0921 | 17 | 1092 | 0.0081 | 0.0896 | 0.0896 | 19 | 0.4194 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0684 | 0.0796 | 0.0177 | 17 | 1092 | 0.0738 | -0.3242 | -0.3242 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0919 | 0.0990 | 0.0195 | 17 | 1092 | 0.0953 | -0.1879 | -0.1879 | 21 | 0.3548 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.0206 | 0.0308 | 0.1280 | 17 | 1092 | -0.0042 | -0.2731 | -0.2731 | 25 | 0.2258 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4556 | 0.4521 | 0.0418 | 17 | 1092 | 0.4545 | 0.0573 | 0.0573 | 14 | 0.5806 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0115 | -0.0477 | 0.0349 | 17 | 1092 | -0.0184 | 0.8415 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | 0.0117 | -0.0806 | 0.0754 | 17 | 1092 | -0.0331 | 0.6309 | 0.6309 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4541 | 0.4004 | 0.0385 | 17 | 1092 | 0.4318 | 0.8170 | 0.8170 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4643 | 0.4370 | 0.0337 | 17 | 1092 | 0.4591 | 0.6557 | 0.6557 | 10 | 0.7097 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## CLE
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_rush** (1.073) · Weakest area: **offense_overall** (-1.571)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.594 | 5 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 1.073 | 2 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.623 | 5 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.220 | 9 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -1.571 | 32 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.915 | 28 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -1.322 | 32 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.583 | 31 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.635 | 31 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2097 | 0.1450 | 0.0327 | 17 | 639 | 0.1890 | 1.3447 | -1.3447 | 31 | 0.0323 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2405 | 0.2045 | 0.0323 | 17 | 639 | 0.2231 | 0.5728 | -0.5728 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0798 | 0.0664 | 0.0188 | 17 | 639 | 0.0755 | 0.4854 | -0.4854 | 26 | 0.1935 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1833 | 0.1442 | 0.0234 | 17 | 562 | 0.1643 | 0.8607 | 0.8607 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0943 | 0.0660 | 0.0121 | 17 | 562 | 0.0815 | 1.2859 | 1.2859 | 2 | 0.9677 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8889 | 0.8507 | 0.0691 | 17 | 229 | 0.8704 | 0.2845 | 0.2845 | 10 | 0.7097 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | -0.0522 | 0.0622 | 0.0928 | 17 | 229 | 0.0033 | -0.6352 | -0.6352 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0649 | -0.0013 | 0.0639 | 17 | 1030 | -0.0341 | -0.5129 | 0.5129 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0834 | 0.0046 | 0.0677 | 17 | 1030 | -0.0407 | -0.6693 | 0.6693 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0765 | 0.0797 | 0.0112 | 17 | 1030 | 0.0779 | -0.1550 | 0.1550 | 14 | 0.5806 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0913 | 0.1000 | 0.0206 | 17 | 1030 | 0.0955 | -0.2159 | 0.2159 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.1095 | 0.0361 | 0.0949 | 17 | 1030 | -0.0389 | -0.7908 | 0.7908 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4253 | 0.4536 | 0.0320 | 17 | 1030 | 0.4390 | -0.4562 | 0.4562 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0776 | -0.0760 | 0.0649 | 17 | 1030 | -0.0769 | -0.0138 | 0.0138 | 15 | 0.5484 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3744 | 0.4020 | 0.0330 | 17 | 1030 | 0.3878 | -0.4304 | 0.4304 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4087 | 0.4384 | 0.0255 | 17 | 1030 | 0.4231 | -0.6002 | 0.6002 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.1637 | -0.0054 | 0.0784 | 17 | 1074 | -0.1130 | -1.3730 | -1.3730 | 32 | 0.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.1761 | -0.0001 | 0.0921 | 17 | 1074 | -0.1198 | -1.2994 | -1.2994 | 31 | 0.0323 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0548 | 0.0796 | 0.0177 | 17 | 1074 | 0.0668 | -0.7205 | -0.7205 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0785 | 0.0990 | 0.0195 | 17 | 1074 | 0.0884 | -0.5415 | -0.5415 | 26 | 0.1935 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.2499 | 0.0308 | 0.1280 | 17 | 1074 | -0.1601 | -1.4917 | -1.4917 | 32 | 0.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.3443 | 0.4521 | 0.0418 | 17 | 1074 | 0.3788 | -1.7526 | -1.7526 | 32 | 0.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0688 | -0.0477 | 0.0349 | 17 | 1074 | -0.0648 | -0.4903 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.1149 | -0.0806 | 0.0754 | 17 | 1074 | -0.0983 | -0.2348 | -0.2348 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3392 | 0.4004 | 0.0385 | 17 | 1074 | 0.3645 | -0.9303 | -0.9303 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.3520 | 0.4370 | 0.0337 | 17 | 1074 | 0.3681 | -2.0397 | -2.0397 | 32 | 0.0000 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## DAL
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **offense_overall** (0.835) · Weakest area: **passing_defense** (-0.999)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.973 | 31 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.004 | 18 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.999 | 32 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.858 | 31 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.835 | 5 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.420 | 11 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.416 | 8 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.548 | 7 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.667 | 6 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1410 | 0.1450 | 0.0327 | 17 | 681 | 0.1423 | -0.0837 | 0.0837 | 17 | 0.4839 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1535 | 0.2045 | 0.0323 | 17 | 681 | 0.1782 | -0.8129 | 0.8129 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0455 | 0.0664 | 0.0188 | 17 | 681 | 0.0522 | -0.7561 | 0.7561 | 6 | 0.8387 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1664 | 0.1442 | 0.0234 | 17 | 631 | 0.1556 | 0.4893 | 0.4893 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0555 | 0.0660 | 0.0121 | 17 | 631 | 0.0602 | -0.4814 | -0.4814 | 26 | 0.1935 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8571 | 0.8507 | 0.0691 | 17 | 238 | 0.8540 | 0.0479 | 0.0479 | 16 | 0.5161 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1825 | 0.0622 | 0.0928 | 17 | 238 | 0.1242 | 0.6673 | 0.6673 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0925 | -0.0013 | 0.0639 | 17 | 1078 | 0.0470 | 0.7564 | -0.7564 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.1619 | 0.0046 | 0.0677 | 17 | 1078 | 0.0856 | 1.1963 | -1.1963 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0919 | 0.0797 | 0.0112 | 17 | 1078 | 0.0864 | 0.5981 | -0.5981 | 27 | 0.1613 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1365 | 0.1000 | 0.0206 | 17 | 1078 | 0.1188 | 0.9134 | -0.9134 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.2411 | 0.0361 | 0.0949 | 17 | 1078 | 0.1417 | 1.1129 | -1.1129 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.5087 | 0.4536 | 0.0320 | 17 | 1078 | 0.4820 | 0.8855 | -0.8855 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | 0.0335 | -0.0760 | 0.0649 | 17 | 1078 | -0.0159 | 0.9246 | -0.9246 | 29 | 0.0968 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4491 | 0.4020 | 0.0330 | 17 | 1078 | 0.4263 | 0.7367 | -0.7367 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4861 | 0.4384 | 0.0255 | 17 | 1078 | 0.4630 | 0.9652 | -0.9652 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0947 | -0.0054 | 0.0784 | 17 | 1164 | 0.0627 | 0.8685 | 0.8685 | 4 | 0.9032 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.1086 | -0.0001 | 0.0921 | 17 | 1164 | 0.0738 | 0.8029 | 0.8029 | 5 | 0.8710 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0822 | 0.0796 | 0.0177 | 17 | 1164 | 0.0809 | 0.0772 | 0.0772 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0930 | 0.0990 | 0.0195 | 17 | 1164 | 0.0959 | -0.1580 | -0.1580 | 19 | 0.4194 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.1559 | 0.0308 | 0.1280 | 17 | 1164 | 0.1159 | 0.6648 | 0.6648 | 7 | 0.8065 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4831 | 0.4521 | 0.0418 | 17 | 1164 | 0.4732 | 0.5046 | 0.5046 | 8 | 0.7742 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0474 | -0.0477 | 0.0349 | 17 | 1164 | -0.0475 | 0.0071 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0075 | -0.0806 | 0.0754 | 17 | 1164 | -0.0430 | 0.4995 | 0.4995 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4395 | 0.4004 | 0.0385 | 17 | 1164 | 0.4233 | 0.5960 | 0.5960 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4716 | 0.4370 | 0.0337 | 17 | 1164 | 0.4650 | 0.8324 | 0.8324 | 6 | 0.8387 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## DEN
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_rush** (1.509) · Weakest area: **special_teams** (-0.028)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.716 | 3 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 1.509 | 1 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.977 | 2 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.626 | 3 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.163 | 16 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 1.004 | 1 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.015 | 16 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.213 | 13 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.028 | 22 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1043 | 0.1450 | 0.0327 | 17 | 671 | 0.1173 | -0.8453 | 0.8453 | 3 | 0.9355 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1946 | 0.2045 | 0.0323 | 17 | 671 | 0.1994 | -0.1574 | 0.1574 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0343 | 0.0664 | 0.0188 | 17 | 671 | 0.0446 | -1.1633 | 1.1633 | 1 | 1.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.2150 | 0.1442 | 0.0234 | 17 | 693 | 0.1807 | 1.5592 | 1.5592 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0981 | 0.0660 | 0.0121 | 17 | 693 | 0.0836 | 1.4596 | 1.4596 | 1 | 1.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8750 | 0.8507 | 0.0691 | 17 | 223 | 0.8632 | 0.1810 | 0.1810 | 14 | 0.5806 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0572 | 0.0622 | 0.0928 | 17 | 223 | 0.0597 | -0.0277 | -0.0277 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0556 | -0.0013 | 0.0639 | 17 | 1115 | -0.0293 | -0.4379 | 0.4379 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0584 | 0.0046 | 0.0677 | 17 | 1115 | -0.0279 | -0.4792 | 0.4792 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0577 | 0.0797 | 0.0112 | 17 | 1115 | 0.0676 | -1.0736 | 1.0736 | 1 | 1.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0591 | 0.1000 | 0.0206 | 17 | 1115 | 0.0789 | -1.0209 | 1.0209 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0785 | 0.0361 | 0.0949 | 17 | 1115 | -0.0229 | -0.6221 | 0.6221 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.3709 | 0.4536 | 0.0320 | 17 | 1115 | 0.4110 | -1.3311 | 1.3311 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1053 | -0.0760 | 0.0649 | 17 | 1115 | -0.0921 | -0.2478 | 0.2478 | 8 | 0.7742 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3629 | 0.4020 | 0.0330 | 17 | 1115 | 0.3818 | -0.6104 | 0.6104 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.3776 | 0.4384 | 0.0255 | 17 | 1115 | 0.4071 | -1.2308 | 1.2308 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0222 | -0.0054 | 0.0784 | 17 | 1116 | 0.0134 | 0.2396 | 0.2396 | 15 | 0.5484 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0355 | -0.0001 | 0.0921 | 17 | 1116 | 0.0241 | 0.2630 | 0.2630 | 15 | 0.5484 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0700 | 0.0796 | 0.0177 | 17 | 1116 | 0.0747 | -0.2768 | -0.2768 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0973 | 0.0990 | 0.0195 | 17 | 1116 | 0.0981 | -0.0446 | -0.0446 | 16 | 0.5161 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.1067 | 0.0308 | 0.1280 | 17 | 1116 | 0.0824 | 0.4035 | 0.4035 | 10 | 0.7097 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4471 | 0.4521 | 0.0418 | 17 | 1116 | 0.4487 | -0.0811 | -0.0811 | 21 | 0.3548 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0096 | -0.0477 | 0.0349 | 17 | 1116 | -0.0168 | 0.8860 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0694 | -0.0806 | 0.0754 | 17 | 1116 | -0.0748 | 0.0768 | 0.0768 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4234 | 0.4004 | 0.0385 | 17 | 1116 | 0.4138 | 0.3499 | 0.3499 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4364 | 0.4370 | 0.0337 | 17 | 1116 | 0.4365 | -0.0139 | -0.0139 | 19 | 0.4194 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## DET
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **passing_offense** (0.674) · Weakest area: **pass_protection** (-0.404)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.152 | 12 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.382 | 6 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.332 | 11 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.256 | 23 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.532 | 9 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.404 | 23 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.674 | 6 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.016 | 20 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.398 | 11 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1907 | 0.1450 | 0.0327 | 17 | 624 | 0.1761 | 0.9499 | -0.9499 | 28 | 0.1290 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2014 | 0.2045 | 0.0323 | 17 | 624 | 0.2029 | -0.0503 | 0.0503 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0625 | 0.0664 | 0.0188 | 17 | 624 | 0.0637 | -0.1414 | 0.1414 | 16 | 0.5161 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1559 | 0.1442 | 0.0234 | 17 | 635 | 0.1502 | 0.2582 | 0.2582 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0772 | 0.0660 | 0.0121 | 17 | 635 | 0.0721 | 0.5059 | 0.5059 | 6 | 0.8387 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.7941 | 0.8507 | 0.0691 | 17 | 237 | 0.8216 | -0.4217 | -0.4217 | 27 | 0.1613 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1340 | 0.0622 | 0.0928 | 17 | 237 | 0.0992 | 0.3981 | 0.3981 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0307 | -0.0013 | 0.0639 | 17 | 1080 | -0.0165 | -0.2371 | 0.2371 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0116 | 0.0046 | 0.0677 | 17 | 1080 | 0.0082 | 0.0533 | -0.0533 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0913 | 0.0797 | 0.0112 | 17 | 1080 | 0.0861 | 0.5698 | -0.5698 | 26 | 0.1935 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1125 | 0.1000 | 0.0206 | 17 | 1080 | 0.1064 | 0.3137 | -0.3137 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0074 | 0.0361 | 0.0949 | 17 | 1080 | 0.0213 | -0.1558 | 0.1558 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4220 | 0.4536 | 0.0320 | 17 | 1080 | 0.4374 | -0.5079 | 0.5079 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0369 | -0.0760 | 0.0649 | 17 | 1080 | -0.0546 | 0.3302 | -0.3302 | 23 | 0.2903 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4100 | 0.4020 | 0.0330 | 17 | 1080 | 0.4061 | 0.1253 | -0.1253 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4250 | 0.4384 | 0.0255 | 17 | 1080 | 0.4315 | -0.2711 | 0.2711 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0820 | -0.0054 | 0.0784 | 17 | 1087 | 0.0541 | 0.7582 | 0.7582 | 5 | 0.8710 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0712 | -0.0001 | 0.0921 | 17 | 1087 | 0.0484 | 0.5267 | 0.5267 | 9 | 0.7419 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.1058 | 0.0796 | 0.0177 | 17 | 1087 | 0.0931 | 0.7610 | 0.7610 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0984 | 0.0990 | 0.0195 | 17 | 1087 | 0.0987 | -0.0163 | -0.0163 | 13 | 0.6129 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.1703 | 0.0308 | 0.1280 | 17 | 1087 | 0.1257 | 0.7414 | 0.7414 | 5 | 0.8710 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4840 | 0.4521 | 0.0418 | 17 | 1087 | 0.4738 | 0.5186 | 0.5186 | 7 | 0.8065 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0664 | -0.0477 | 0.0349 | 17 | 1087 | -0.0629 | -0.4350 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0709 | -0.0806 | 0.0754 | 17 | 1087 | -0.0756 | 0.0663 | 0.0663 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3982 | 0.4004 | 0.0385 | 17 | 1087 | 0.3991 | -0.0335 | -0.0335 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4499 | 0.4370 | 0.0337 | 17 | 1087 | 0.4474 | 0.3096 | 0.3096 | 12 | 0.6452 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## GB
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **passing_offense** (0.929) · Weakest area: **defense_overall** (-0.299)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.299 | 22 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.039 | 16 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.083 | 17 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.061 | 19 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.878 | 4 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.233 | 14 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.929 | 3 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.270 | 12 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.177 | 18 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1467 | 0.1450 | 0.0327 | 17 | 552 | 0.1462 | 0.0362 | -0.0362 | 20 | 0.3871 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1708 | 0.2045 | 0.0323 | 17 | 552 | 0.1871 | -0.5374 | 0.5374 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0525 | 0.0664 | 0.0188 | 17 | 552 | 0.0570 | -0.5022 | 0.5022 | 12 | 0.6452 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1623 | 0.1442 | 0.0234 | 17 | 610 | 0.1535 | 0.3989 | 0.3989 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0590 | 0.0660 | 0.0121 | 17 | 610 | 0.0622 | -0.3199 | -0.3199 | 22 | 0.3226 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8235 | 0.8507 | 0.0691 | 17 | 208 | 0.8367 | -0.2026 | -0.2026 | 23 | 0.2903 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0941 | 0.0622 | 0.0928 | 17 | 208 | 0.0787 | 0.1769 | 0.1769 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0429 | -0.0013 | 0.0639 | 17 | 1106 | 0.0215 | 0.3568 | -0.3568 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0416 | 0.0046 | 0.0677 | 17 | 1106 | 0.0237 | 0.2817 | -0.2817 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0672 | 0.0797 | 0.0112 | 17 | 1106 | 0.0728 | -0.6096 | 0.6096 | 7 | 0.8065 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0789 | 0.1000 | 0.0206 | 17 | 1106 | 0.0891 | -0.5255 | 0.5255 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0895 | 0.0361 | 0.0949 | 17 | 1106 | 0.0636 | 0.2901 | -0.2901 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4459 | 0.4536 | 0.0320 | 17 | 1106 | 0.4497 | -0.1244 | 0.1244 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0639 | -0.0760 | 0.0649 | 17 | 1106 | -0.0693 | 0.1024 | -0.1024 | 18 | 0.4516 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4408 | 0.4020 | 0.0330 | 17 | 1106 | 0.4220 | 0.6063 | -0.6063 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4512 | 0.4384 | 0.0255 | 17 | 1106 | 0.4450 | 0.2586 | -0.2586 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0734 | -0.0054 | 0.0784 | 17 | 1028 | 0.0482 | 0.6837 | 0.6837 | 7 | 0.8065 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.1223 | -0.0001 | 0.0921 | 17 | 1028 | 0.0831 | 0.9042 | 0.9042 | 4 | 0.9032 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.1051 | 0.0796 | 0.0177 | 17 | 1028 | 0.0927 | 0.7407 | 0.7407 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1034 | 0.0990 | 0.0195 | 17 | 1028 | 0.1013 | 0.1149 | 0.1149 | 12 | 0.6452 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.2527 | 0.0308 | 0.1280 | 17 | 1028 | 0.1817 | 1.1793 | 1.1793 | 2 | 0.9677 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.5054 | 0.4521 | 0.0418 | 17 | 1028 | 0.4884 | 0.8675 | 0.8675 | 5 | 0.8710 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0651 | -0.0477 | 0.0349 | 17 | 1028 | -0.0618 | -0.4049 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0757 | -0.0806 | 0.0754 | 17 | 1028 | -0.0781 | 0.0334 | 0.0334 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4337 | 0.4004 | 0.0385 | 17 | 1028 | 0.4199 | 0.5074 | 0.5074 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4805 | 0.4370 | 0.0337 | 17 | 1028 | 0.4722 | 1.0459 | 1.0459 | 5 | 0.8710 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## HOU
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **passing_defense** (0.977) · Weakest area: **rushing_offense** (-0.574)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.931 | 1 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.226 | 12 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.977 | 1 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.663 | 2 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.197 | 26 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.576 | 7 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.006 | 17 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.574 | 30 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.368 | 12 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1213 | 0.1450 | 0.0327 | 17 | 643 | 0.1289 | -0.4923 | 0.4923 | 8 | 0.7742 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2371 | 0.2045 | 0.0323 | 17 | 643 | 0.2213 | 0.5192 | -0.5192 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0482 | 0.0664 | 0.0188 | 17 | 643 | 0.0540 | -0.6587 | 0.6587 | 7 | 0.8065 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1440 | 0.1442 | 0.0234 | 17 | 618 | 0.1441 | -0.0035 | -0.0035 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0761 | 0.0660 | 0.0121 | 17 | 618 | 0.0715 | 0.4553 | 0.4553 | 8 | 0.7742 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9231 | 0.8507 | 0.0691 | 17 | 223 | 0.8880 | 0.5392 | 0.5392 | 6 | 0.8387 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1285 | 0.0622 | 0.0928 | 17 | 223 | 0.0964 | 0.3678 | 0.3678 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.1329 | -0.0013 | 0.0639 | 17 | 1027 | -0.0691 | -1.0613 | 1.0613 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.1085 | 0.0046 | 0.0677 | 17 | 1027 | -0.0536 | -0.8596 | 0.8596 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0761 | 0.0797 | 0.0112 | 17 | 1027 | 0.0777 | -0.1775 | 0.1775 | 13 | 0.6129 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0542 | 0.1000 | 0.0206 | 17 | 1027 | 0.0764 | -1.1445 | 1.1445 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.1304 | 0.0361 | 0.0949 | 17 | 1027 | -0.0497 | -0.9043 | 0.9043 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.3883 | 0.4536 | 0.0320 | 17 | 1027 | 0.4200 | -1.0497 | 1.0497 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1292 | -0.0760 | 0.0649 | 17 | 1027 | -0.1052 | -0.4493 | 0.4493 | 3 | 0.9355 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3767 | 0.4020 | 0.0330 | 17 | 1027 | 0.3890 | -0.3950 | 0.3950 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.3953 | 0.4384 | 0.0255 | 17 | 1027 | 0.4162 | -0.8716 | 0.8716 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0125 | -0.0054 | 0.0784 | 17 | 1138 | -0.0102 | -0.0616 | -0.0616 | 23 | 0.2903 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0084 | -0.0001 | 0.0921 | 17 | 1138 | -0.0057 | -0.0610 | -0.0610 | 22 | 0.3226 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0747 | 0.0796 | 0.0177 | 17 | 1138 | 0.0770 | -0.1431 | -0.1431 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0738 | 0.0990 | 0.0195 | 17 | 1138 | 0.0860 | -0.6643 | -0.6643 | 29 | 0.0968 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0669 | 0.0308 | 0.1280 | 17 | 1138 | 0.0554 | 0.1921 | 0.1921 | 15 | 0.5484 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4479 | 0.4521 | 0.0418 | 17 | 1138 | 0.4492 | -0.0679 | -0.0679 | 20 | 0.3871 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0465 | -0.0477 | 0.0349 | 17 | 1138 | -0.0468 | 0.0273 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.1492 | -0.0806 | 0.0754 | 17 | 1138 | -0.1159 | -0.4690 | -0.4690 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3557 | 0.4004 | 0.0385 | 17 | 1138 | 0.3742 | -0.6797 | -0.6797 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4174 | 0.4370 | 0.0337 | 17 | 1138 | 0.4211 | -0.4693 | -0.4693 | 28 | 0.1290 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## IND
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_offense** (0.820) · Weakest area: **pass_rush** (-0.324)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.158 | 19 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.324 | 25 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.212 | 20 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.082 | 12 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.613 | 7 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.410 | 12 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.152 | 11 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.820 | 3 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.661 | 7 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1369 | 0.1450 | 0.0327 | 17 | 599 | 0.1395 | -0.1684 | 0.1684 | 16 | 0.5161 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1838 | 0.2045 | 0.0323 | 17 | 599 | 0.1938 | -0.3306 | 0.3306 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0484 | 0.0664 | 0.0188 | 17 | 599 | 0.0542 | -0.6514 | 0.6514 | 8 | 0.7742 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1346 | 0.1442 | 0.0234 | 17 | 691 | 0.1392 | -0.2110 | -0.2110 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0564 | 0.0660 | 0.0121 | 17 | 691 | 0.0608 | -0.4371 | -0.4371 | 25 | 0.2258 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9444 | 0.8507 | 0.0691 | 17 | 218 | 0.8990 | 0.6985 | 0.6985 | 2 | 0.9677 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1813 | 0.0622 | 0.0928 | 17 | 218 | 0.1236 | 0.6607 | 0.6607 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0023 | -0.0013 | 0.0639 | 17 | 1144 | 0.0005 | 0.0287 | -0.0287 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0133 | 0.0046 | 0.0677 | 17 | 1144 | 0.0091 | 0.0662 | -0.0662 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0825 | 0.0797 | 0.0112 | 17 | 1144 | 0.0812 | 0.1372 | -0.1372 | 21 | 0.3548 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0896 | 0.1000 | 0.0206 | 17 | 1144 | 0.0946 | -0.2593 | 0.2593 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0563 | 0.0361 | 0.0949 | 17 | 1144 | 0.0465 | 0.1097 | -0.1097 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4732 | 0.4536 | 0.0320 | 17 | 1144 | 0.4637 | 0.3149 | -0.3149 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1011 | -0.0760 | 0.0649 | 17 | 1144 | -0.0898 | -0.2123 | 0.2123 | 10 | 0.7097 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4165 | 0.4020 | 0.0330 | 17 | 1144 | 0.4094 | 0.2263 | -0.2263 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4572 | 0.4384 | 0.0255 | 17 | 1144 | 0.4481 | 0.3799 | -0.3799 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0546 | -0.0054 | 0.0784 | 17 | 1053 | 0.0354 | 0.5201 | 0.5201 | 9 | 0.7419 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0833 | -0.0001 | 0.0921 | 17 | 1053 | 0.0566 | 0.6161 | 0.6161 | 7 | 0.8065 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0735 | 0.0796 | 0.0177 | 17 | 1053 | 0.0764 | -0.1777 | -0.1777 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0979 | 0.0990 | 0.0195 | 17 | 1053 | 0.0984 | -0.0307 | -0.0307 | 14 | 0.5806 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0827 | 0.0308 | 0.1280 | 17 | 1053 | 0.0661 | 0.2760 | 0.2760 | 12 | 0.6452 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4741 | 0.4521 | 0.0418 | 17 | 1053 | 0.4671 | 0.3584 | 0.3584 | 10 | 0.7097 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0390 | -0.0477 | 0.0349 | 17 | 1053 | -0.0406 | 0.2027 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | 0.0516 | -0.0806 | 0.0754 | 17 | 1053 | -0.0125 | 0.9040 | 0.9040 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4487 | 0.4004 | 0.0385 | 17 | 1053 | 0.4287 | 0.7353 | 0.7353 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4663 | 0.4370 | 0.0337 | 17 | 1053 | 0.4607 | 0.7037 | 0.7037 | 7 | 0.8065 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## JAX
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **special_teams** (0.744) · Weakest area: **pass_rush** (-0.622)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.466 | 7 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.622 | 28 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.576 | 7 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.484 | 4 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.240 | 15 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.217 | 16 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.294 | 9 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.032 | 24 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.744 | 4 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1289 | 0.1450 | 0.0327 | 17 | 644 | 0.1340 | -0.3349 | 0.3349 | 13 | 0.6129 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2078 | 0.2045 | 0.0323 | 17 | 644 | 0.2062 | 0.0514 | -0.0514 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0637 | 0.0664 | 0.0188 | 17 | 644 | 0.0645 | -0.0992 | 0.0992 | 17 | 0.4839 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1298 | 0.1442 | 0.0234 | 17 | 701 | 0.1368 | -0.3161 | -0.3161 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0456 | 0.0660 | 0.0121 | 17 | 701 | 0.0549 | -0.9281 | -0.9281 | 29 | 0.0968 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8824 | 0.8507 | 0.0691 | 17 | 223 | 0.8670 | 0.2358 | 0.2358 | 12 | 0.6290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1962 | 0.0622 | 0.0928 | 17 | 223 | 0.1313 | 0.7436 | 0.7436 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0589 | -0.0013 | 0.0639 | 17 | 1079 | -0.0310 | -0.4646 | 0.4646 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0788 | 0.0046 | 0.0677 | 17 | 1079 | -0.0384 | -0.6339 | 0.6339 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0656 | 0.0797 | 0.0112 | 17 | 1079 | 0.0720 | -0.6874 | 0.6874 | 6 | 0.8387 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0753 | 0.1000 | 0.0206 | 17 | 1079 | 0.0873 | -0.6167 | 0.6167 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.1128 | 0.0361 | 0.0949 | 17 | 1079 | -0.0406 | -0.8084 | 0.8084 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4322 | 0.4536 | 0.0320 | 17 | 1079 | 0.4426 | -0.3441 | 0.3441 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1057 | -0.0760 | 0.0649 | 17 | 1079 | -0.0923 | -0.2505 | 0.2505 | 7 | 0.8065 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3645 | 0.4020 | 0.0330 | 17 | 1079 | 0.3826 | -0.5862 | 0.5862 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4235 | 0.4384 | 0.0255 | 17 | 1079 | 0.4307 | -0.3006 | 0.3006 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0219 | -0.0054 | 0.0784 | 17 | 1121 | 0.0132 | 0.2366 | 0.2366 | 16 | 0.5161 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0388 | -0.0001 | 0.0921 | 17 | 1121 | 0.0263 | 0.2872 | 0.2872 | 12 | 0.6452 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0885 | 0.0796 | 0.0177 | 17 | 1121 | 0.0842 | 0.2596 | 0.2596 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0776 | 0.0990 | 0.0195 | 17 | 1121 | 0.0880 | -0.5641 | -0.5641 | 28 | 0.1290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0871 | 0.0308 | 0.1280 | 17 | 1121 | 0.0691 | 0.2991 | 0.2991 | 11 | 0.6774 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4720 | 0.4521 | 0.0418 | 17 | 1121 | 0.4657 | 0.3247 | 0.3247 | 11 | 0.6774 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0147 | -0.0477 | 0.0349 | 17 | 1121 | -0.0210 | 0.7663 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0730 | -0.0806 | 0.0754 | 17 | 1121 | -0.0767 | 0.0522 | 0.0522 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3927 | 0.4004 | 0.0385 | 17 | 1121 | 0.3959 | -0.1168 | -0.1168 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4451 | 0.4370 | 0.0337 | 17 | 1121 | 0.4436 | 0.1963 | 0.1963 | 15 | 0.5484 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## KC
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_defense** (0.327) · Weakest area: **pass_protection** (-0.379)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.024 | 15 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.132 | 15 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.044 | 16 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.327 | 8 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.258 | 13 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.379 | 22 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.092 | 13 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.128 | 19 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.170 | 19 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1778 | 0.1450 | 0.0327 | 17 | 686 | 0.1673 | 0.6826 | -0.6826 | 25 | 0.2258 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1515 | 0.2045 | 0.0323 | 17 | 686 | 0.1772 | -0.8443 | 0.8443 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0685 | 0.0664 | 0.0188 | 17 | 686 | 0.0678 | 0.0763 | -0.0763 | 20 | 0.3871 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1684 | 0.1442 | 0.0234 | 17 | 582 | 0.1566 | 0.5329 | 0.5329 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0601 | 0.0660 | 0.0121 | 17 | 582 | 0.0628 | -0.2689 | -0.2689 | 19 | 0.4194 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8684 | 0.8507 | 0.0691 | 17 | 208 | 0.8598 | 0.1320 | 0.1320 | 15 | 0.5484 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0928 | 0.0622 | 0.0928 | 17 | 208 | 0.0780 | 0.1696 | 0.1696 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0040 | -0.0013 | 0.0639 | 17 | 1024 | -0.0027 | -0.0220 | 0.0220 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0076 | 0.0046 | 0.0677 | 17 | 1024 | -0.0017 | -0.0924 | 0.0924 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0773 | 0.0797 | 0.0112 | 17 | 1024 | 0.0784 | -0.1155 | 0.1155 | 15 | 0.5484 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0735 | 0.1000 | 0.0206 | 17 | 1024 | 0.0863 | -0.6610 | 0.6610 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0269 | 0.0361 | 0.0949 | 17 | 1024 | 0.0314 | -0.0499 | 0.0499 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4622 | 0.4536 | 0.0320 | 17 | 1024 | 0.4580 | 0.1376 | -0.1376 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1002 | -0.0760 | 0.0649 | 17 | 1024 | -0.0893 | -0.2045 | 0.2045 | 11 | 0.6774 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3946 | 0.4020 | 0.0330 | 17 | 1024 | 0.3982 | -0.1151 | 0.1151 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4404 | 0.4384 | 0.0255 | 17 | 1024 | 0.4394 | 0.0412 | -0.0412 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0252 | -0.0054 | 0.0784 | 17 | 1094 | 0.0154 | 0.2650 | 0.2650 | 13 | 0.6129 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0421 | -0.0001 | 0.0921 | 17 | 1094 | 0.0286 | 0.3116 | 0.3116 | 11 | 0.6774 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0758 | 0.0796 | 0.0177 | 17 | 1094 | 0.0776 | -0.1096 | -0.1096 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0716 | 0.0990 | 0.0195 | 17 | 1094 | 0.0849 | -0.7223 | -0.7223 | 31 | 0.0323 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0769 | 0.0308 | 0.1280 | 17 | 1094 | 0.0621 | 0.2450 | 0.2450 | 13 | 0.6129 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4606 | 0.4521 | 0.0418 | 17 | 1094 | 0.4579 | 0.1392 | 0.1392 | 13 | 0.6129 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | 0.0050 | -0.0477 | 0.0349 | 17 | 1094 | -0.0051 | 1.2229 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0596 | -0.0806 | 0.0754 | 17 | 1094 | -0.0698 | 0.1437 | 0.1437 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4077 | 0.4004 | 0.0385 | 17 | 1094 | 0.4047 | 0.1118 | 0.1118 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4452 | 0.4370 | 0.0337 | 17 | 1094 | 0.4436 | 0.1967 | 0.1967 | 14 | 0.5806 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## LA
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **offense_overall** (1.526) · Weakest area: **special_teams** (-0.455)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.463 | 8 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.459 | 5 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.354 | 10 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.367 | 6 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 1.526 | 1 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.759 | 3 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 1.095 | 2 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 1.115 | 1 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.455 | 30 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1234 | 0.1450 | 0.0327 | 17 | 624 | 0.1303 | -0.4489 | 0.4489 | 11 | 0.6774 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1573 | 0.2045 | 0.0323 | 17 | 624 | 0.1802 | -0.7521 | 0.7521 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0369 | 0.0664 | 0.0188 | 17 | 624 | 0.0463 | -1.0698 | 1.0698 | 2 | 0.9677 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1748 | 0.1442 | 0.0234 | 17 | 658 | 0.1599 | 0.6735 | 0.6735 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0714 | 0.0660 | 0.0121 | 17 | 658 | 0.0690 | 0.2449 | 0.2449 | 9 | 0.7419 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.7857 | 0.8507 | 0.0691 | 17 | 220 | 0.8172 | -0.4843 | -0.4843 | 28 | 0.1290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | -0.0198 | 0.0622 | 0.0928 | 17 | 220 | 0.0200 | -0.4553 | -0.4553 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0544 | -0.0013 | 0.0639 | 17 | 1109 | -0.0287 | -0.4282 | 0.4282 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0687 | 0.0046 | 0.0677 | 17 | 1109 | -0.0331 | -0.5570 | 0.5570 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0805 | 0.0797 | 0.0112 | 17 | 1109 | 0.0802 | 0.0422 | -0.0422 | 20 | 0.3871 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0791 | 0.1000 | 0.0206 | 17 | 1109 | 0.0892 | -0.5207 | 0.5207 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0562 | 0.0361 | 0.0949 | 17 | 1109 | -0.0114 | -0.5013 | 0.5013 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4407 | 0.4536 | 0.0320 | 17 | 1109 | 0.4470 | -0.2076 | 0.2076 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0976 | -0.0760 | 0.0649 | 17 | 1109 | -0.0878 | -0.1824 | 0.1824 | 12 | 0.6452 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3765 | 0.4020 | 0.0330 | 17 | 1109 | 0.3889 | -0.3980 | 0.3980 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4184 | 0.4384 | 0.0255 | 17 | 1109 | 0.4281 | -0.4048 | 0.4048 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.1594 | -0.0054 | 0.0784 | 17 | 1105 | 0.1067 | 1.4298 | 1.4298 | 1 | 1.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.1491 | -0.0001 | 0.0921 | 17 | 1105 | 0.1013 | 1.1020 | 1.1020 | 2 | 0.9677 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.1154 | 0.0796 | 0.0177 | 17 | 1105 | 0.0980 | 1.0403 | 1.0403 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1191 | 0.0990 | 0.0195 | 17 | 1105 | 0.1094 | 0.5297 | 0.5297 | 3 | 0.9355 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.2231 | 0.0308 | 0.1280 | 17 | 1105 | 0.1616 | 1.0221 | 1.0221 | 3 | 0.9355 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.5272 | 0.4521 | 0.0418 | 17 | 1105 | 0.5032 | 1.2221 | 1.2221 | 2 | 0.9516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | 0.0028 | -0.0477 | 0.0349 | 17 | 1105 | -0.0068 | 1.1733 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | 0.0212 | -0.0806 | 0.0754 | 17 | 1105 | -0.0281 | 0.6961 | 0.6961 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.5011 | 0.4004 | 0.0385 | 17 | 1105 | 0.4594 | 1.5333 | 1.5333 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.5222 | 0.4370 | 0.0337 | 17 | 1105 | 0.5059 | 2.0447 | 2.0447 | 1 | 1.0000 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## LAC
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **defense_overall** (0.571) · Weakest area: **pass_protection** (-0.977)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.571 | 6 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.310 | 7 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.501 | 9 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.103 | 10 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.165 | 24 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.977 | 29 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.182 | 25 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.071 | 25 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.152 | 20 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2012 | 0.1450 | 0.0327 | 17 | 681 | 0.1832 | 1.1675 | -1.1675 | 30 | 0.0645 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2500 | 0.2045 | 0.0323 | 17 | 681 | 0.2280 | 0.7240 | -0.7240 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0881 | 0.0664 | 0.0188 | 17 | 681 | 0.0812 | 0.7857 | -0.7857 | 28 | 0.1290 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1502 | 0.1442 | 0.0234 | 17 | 586 | 0.1473 | 0.1320 | 0.1320 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0768 | 0.0660 | 0.0121 | 17 | 586 | 0.0719 | 0.4889 | 0.4889 | 7 | 0.8065 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9268 | 0.8507 | 0.0691 | 17 | 220 | 0.8899 | 0.5672 | 0.5672 | 5 | 0.8710 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0897 | 0.0622 | 0.0928 | 17 | 220 | 0.0764 | 0.1524 | 0.1524 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0793 | -0.0013 | 0.0639 | 17 | 1001 | -0.0415 | -0.6289 | 0.6289 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0772 | 0.0046 | 0.0677 | 17 | 1001 | -0.0376 | -0.6223 | 0.6223 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0631 | 0.0797 | 0.0112 | 17 | 1001 | 0.0706 | -0.8087 | 0.8087 | 4 | 0.9032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1058 | 0.1000 | 0.0206 | 17 | 1001 | 0.1030 | 0.1467 | -0.1467 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0634 | 0.0361 | 0.0949 | 17 | 1001 | -0.0152 | -0.5406 | 0.5406 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4249 | 0.4536 | 0.0320 | 17 | 1001 | 0.4388 | -0.4618 | 0.4618 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1206 | -0.0760 | 0.0649 | 17 | 1001 | -0.1004 | -0.3762 | 0.3762 | 4 | 0.9032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3968 | 0.4020 | 0.0330 | 17 | 1001 | 0.3993 | -0.0805 | 0.0805 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4156 | 0.4384 | 0.0255 | 17 | 1001 | 0.4266 | -0.4617 | 0.4617 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0451 | -0.0054 | 0.0784 | 17 | 1125 | -0.0324 | -0.3449 | -0.3449 | 26 | 0.1935 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0160 | -0.0001 | 0.0921 | 17 | 1125 | -0.0109 | -0.1173 | -0.1173 | 24 | 0.2581 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0661 | 0.0796 | 0.0177 | 17 | 1125 | 0.0726 | -0.3920 | -0.3920 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0777 | 0.0990 | 0.0195 | 17 | 1125 | 0.0880 | -0.5629 | -0.5629 | 27 | 0.1613 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0012 | 0.0308 | 0.1280 | 17 | 1125 | 0.0106 | -0.1574 | -0.1574 | 23 | 0.2903 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4523 | 0.4521 | 0.0418 | 17 | 1125 | 0.4522 | 0.0032 | 0.0032 | 16 | 0.5161 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0216 | -0.0477 | 0.0349 | 17 | 1125 | -0.0265 | 0.6073 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0800 | -0.0806 | 0.0754 | 17 | 1125 | -0.0803 | 0.0038 | 0.0038 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3908 | 0.4004 | 0.0385 | 17 | 1125 | 0.3947 | -0.1460 | -0.1460 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4356 | 0.4370 | 0.0337 | 17 | 1125 | 0.4358 | -0.0337 | -0.0337 | 20 | 0.3871 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## LV
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_defense** (0.030) · Weakest area: **rushing_offense** (-1.441)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.070 | 16 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.152 | 21 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.412 | 23 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.030 | 14 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -1.338 | 31 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -1.192 | 31 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.740 | 29 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -1.441 | 32 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.142 | 24 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1890 | 0.1450 | 0.0327 | 17 | 598 | 0.1749 | 0.9137 | -0.9137 | 27 | 0.1613 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2886 | 0.2045 | 0.0323 | 17 | 598 | 0.2478 | 1.3382 | -1.3382 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.1070 | 0.0664 | 0.0188 | 17 | 598 | 0.0940 | 1.4706 | -1.4706 | 32 | 0.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1373 | 0.1442 | 0.0234 | 17 | 590 | 0.1406 | -0.1516 | -0.1516 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0627 | 0.0660 | 0.0121 | 17 | 590 | 0.0642 | -0.1517 | -0.1517 | 18 | 0.4516 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8148 | 0.8507 | 0.0691 | 17 | 217 | 0.8322 | -0.2675 | -0.2675 | 25 | 0.2258 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0366 | 0.0622 | 0.0928 | 17 | 217 | 0.0490 | -0.1425 | -0.1425 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0259 | -0.0013 | 0.0639 | 17 | 1096 | -0.0140 | -0.1984 | 0.1984 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0304 | 0.0046 | 0.0677 | 17 | 1096 | 0.0179 | 0.1963 | -0.1963 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0627 | 0.0797 | 0.0112 | 17 | 1096 | 0.0704 | -0.8296 | 0.8296 | 3 | 0.9355 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0977 | 0.1000 | 0.0206 | 17 | 1096 | 0.0988 | -0.0573 | 0.0573 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1057 | 0.0361 | 0.0949 | 17 | 1096 | 0.0719 | 0.3775 | -0.3775 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4814 | 0.4536 | 0.0320 | 17 | 1096 | 0.4679 | 0.4456 | -0.4456 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0902 | -0.0760 | 0.0649 | 17 | 1096 | -0.0838 | -0.1199 | 0.1199 | 13 | 0.6129 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4076 | 0.4020 | 0.0330 | 17 | 1096 | 0.4049 | 0.0885 | -0.0885 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4489 | 0.4384 | 0.0255 | 17 | 1096 | 0.4438 | 0.2127 | -0.2127 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.1635 | -0.0054 | 0.0784 | 17 | 982 | -0.1129 | -1.3715 | -1.3715 | 31 | 0.0323 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.1920 | -0.0001 | 0.0921 | 17 | 982 | -0.1306 | -1.4172 | -1.4172 | 32 | 0.0000 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0619 | 0.0796 | 0.0177 | 17 | 982 | 0.0705 | -0.5142 | -0.5142 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0800 | 0.0990 | 0.0195 | 17 | 982 | 0.0892 | -0.5015 | -0.5015 | 24 | 0.2581 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.1658 | 0.0308 | 0.1280 | 17 | 982 | -0.1029 | -1.0446 | -1.0446 | 30 | 0.0645 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4114 | 0.4521 | 0.0418 | 17 | 982 | 0.4244 | -0.6619 | -0.6619 | 29 | 0.0968 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0513 | -0.0477 | 0.0349 | 17 | 982 | -0.0506 | -0.0835 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.3041 | -0.0806 | 0.0754 | 17 | 982 | -0.1958 | -1.5280 | -1.5280 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3114 | 0.4004 | 0.0385 | 17 | 982 | 0.3482 | -1.3535 | -1.3535 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.3859 | 0.4370 | 0.0337 | 17 | 982 | 0.3957 | -1.2240 | -1.2240 | 30 | 0.0645 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## MIA
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **special_teams** (0.771) · Weakest area: **passing_defense** (-0.941)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.721 | 27 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.191 | 22 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.941 | 30 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.351 | 25 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.105 | 22 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.136 | 17 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.150 | 21 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.201 | 14 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.771 | 3 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1226 | 0.1450 | 0.0327 | 17 | 530 | 0.1298 | -0.4646 | 0.4646 | 10 | 0.7097 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2295 | 0.2045 | 0.0323 | 17 | 530 | 0.2174 | 0.3971 | -0.3971 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0717 | 0.0664 | 0.0188 | 17 | 530 | 0.0700 | 0.1916 | -0.1916 | 21 | 0.3548 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1269 | 0.1442 | 0.0234 | 17 | 591 | 0.1353 | -0.3802 | -0.3802 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0660 | 0.0660 | 0.0121 | 17 | 591 | 0.0660 | -0.0026 | -0.0026 | 16 | 0.5161 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9310 | 0.8507 | 0.0691 | 17 | 214 | 0.8921 | 0.5985 | 0.5985 | 4 | 0.9032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.2012 | 0.0622 | 0.0928 | 17 | 214 | 0.1338 | 0.7710 | 0.7710 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0790 | -0.0013 | 0.0639 | 17 | 1055 | 0.0401 | 0.6480 | -0.6480 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0866 | 0.0046 | 0.0677 | 17 | 1055 | 0.0469 | 0.6238 | -0.6238 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0846 | 0.0797 | 0.0112 | 17 | 1055 | 0.0824 | 0.2405 | -0.2405 | 23 | 0.2903 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1186 | 0.1000 | 0.0206 | 17 | 1055 | 0.1096 | 0.4664 | -0.4664 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1727 | 0.0361 | 0.0949 | 17 | 1055 | 0.1065 | 0.7415 | -0.7415 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.5245 | 0.4536 | 0.0320 | 17 | 1055 | 0.4902 | 1.1399 | -1.1399 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0459 | -0.0760 | 0.0649 | 17 | 1055 | -0.0595 | 0.2541 | -0.2541 | 19 | 0.4194 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4233 | 0.4020 | 0.0330 | 17 | 1055 | 0.4129 | 0.3324 | -0.3324 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4825 | 0.4384 | 0.0255 | 17 | 1055 | 0.4611 | 0.8919 | -0.8919 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0203 | -0.0054 | 0.0784 | 17 | 969 | 0.0121 | 0.2224 | 0.2224 | 17 | 0.4839 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0212 | -0.0001 | 0.0921 | 17 | 969 | -0.0145 | -0.1559 | -0.1559 | 25 | 0.2258 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0811 | 0.0796 | 0.0177 | 17 | 969 | 0.0804 | 0.0452 | 0.0452 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1329 | 0.0990 | 0.0195 | 17 | 969 | 0.1164 | 0.8923 | 0.8923 | 1 | 1.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.0070 | 0.0308 | 0.1280 | 17 | 969 | 0.0051 | -0.2005 | -0.2005 | 24 | 0.2581 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4340 | 0.4521 | 0.0418 | 17 | 969 | 0.4398 | -0.2946 | -0.2946 | 26 | 0.1935 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0779 | -0.0477 | 0.0349 | 17 | 969 | -0.0722 | -0.7019 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0284 | -0.0806 | 0.0754 | 17 | 969 | -0.0537 | 0.3568 | 0.3568 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4034 | 0.4004 | 0.0385 | 17 | 969 | 0.4021 | 0.0459 | 0.0459 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4211 | 0.4370 | 0.0337 | 17 | 969 | 0.4241 | -0.3817 | -0.3817 | 27 | 0.1613 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## MIN
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_rush** (1.026) · Weakest area: **pass_protection** (-1.414)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.621 | 4 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 1.026 | 3 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.876 | 3 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.023 | 15 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.394 | 28 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -1.414 | 32 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.622 | 28 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.340 | 10 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.320 | 14 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2137 | 0.1450 | 0.0327 | 17 | 571 | 0.1917 | 1.4269 | -1.4269 | 32 | 0.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1958 | 0.2045 | 0.0323 | 17 | 571 | 0.2000 | -0.1396 | 0.1396 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.1051 | 0.0664 | 0.0188 | 17 | 571 | 0.0927 | 1.4002 | -1.4002 | 31 | 0.0323 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1810 | 0.1442 | 0.0234 | 17 | 525 | 0.1631 | 0.8096 | 0.8096 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0933 | 0.0660 | 0.0121 | 17 | 525 | 0.0810 | 1.2416 | 1.2416 | 3 | 0.9355 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9429 | 0.8507 | 0.0691 | 17 | 214 | 0.8982 | 0.6866 | 0.6866 | 3 | 0.9355 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1200 | 0.0622 | 0.0928 | 17 | 214 | 0.0920 | 0.3204 | 0.3204 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0904 | -0.0013 | 0.0639 | 17 | 1060 | -0.0472 | -0.7188 | 0.7188 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0866 | 0.0046 | 0.0677 | 17 | 1060 | -0.0424 | -0.6931 | 0.6931 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0610 | 0.0797 | 0.0112 | 17 | 1060 | 0.0694 | -0.9156 | 0.9156 | 2 | 0.9677 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0906 | 0.1000 | 0.0206 | 17 | 1060 | 0.0951 | -0.2352 | 0.2352 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.1220 | 0.0361 | 0.0949 | 17 | 1060 | -0.0453 | -0.8585 | 0.8585 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.3981 | 0.4536 | 0.0320 | 17 | 1060 | 0.4250 | -0.8930 | 0.8930 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0849 | -0.0760 | 0.0649 | 17 | 1060 | -0.0809 | -0.0747 | 0.0747 | 14 | 0.5806 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4173 | 0.4020 | 0.0330 | 17 | 1060 | 0.4099 | 0.2397 | -0.2397 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4160 | 0.4384 | 0.0255 | 17 | 1060 | 0.4269 | -0.4525 | 0.4525 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0499 | -0.0054 | 0.0784 | 17 | 982 | -0.0356 | -0.3861 | -0.3861 | 28 | 0.1290 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0943 | -0.0001 | 0.0921 | 17 | 982 | -0.0642 | -0.6952 | -0.6952 | 28 | 0.1290 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0683 | 0.0796 | 0.0177 | 17 | 982 | 0.0738 | -0.3275 | -0.3275 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1138 | 0.0990 | 0.0195 | 17 | 982 | 0.1066 | 0.3887 | 0.3887 | 7 | 0.8065 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.1560 | 0.0308 | 0.1280 | 17 | 982 | -0.0962 | -0.9926 | -0.9926 | 29 | 0.0968 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4186 | 0.4521 | 0.0418 | 17 | 982 | 0.4293 | -0.5449 | -0.5449 | 28 | 0.1290 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0382 | -0.0477 | 0.0349 | 17 | 982 | -0.0400 | 0.2200 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0616 | -0.0806 | 0.0754 | 17 | 982 | -0.0708 | 0.1298 | 0.1298 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4365 | 0.4004 | 0.0385 | 17 | 982 | 0.4216 | 0.5500 | 0.5500 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4328 | 0.4370 | 0.0337 | 17 | 982 | 0.4336 | -0.1000 | -0.1000 | 22 | 0.3226 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## NE
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **passing_offense** (1.316) · Weakest area: **pass_protection** (-0.217)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.025 | 14 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.130 | 20 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.218 | 13 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.046 | 18 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 1.107 | 2 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.217 | 21 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 1.316 | 1 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.180 | 26 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.069 | 23 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1452 | 0.1450 | 0.0327 | 17 | 613 | 0.1451 | 0.0040 | -0.0040 | 18 | 0.4516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2244 | 0.2045 | 0.0323 | 17 | 613 | 0.2148 | 0.3162 | -0.3162 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0783 | 0.0664 | 0.0188 | 17 | 613 | 0.0745 | 0.4308 | -0.4308 | 24 | 0.2581 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1460 | 0.1442 | 0.0234 | 17 | 589 | 0.1451 | 0.0404 | 0.0404 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0594 | 0.0660 | 0.0121 | 17 | 589 | 0.0624 | -0.3014 | -0.3014 | 20 | 0.3871 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8438 | 0.8507 | 0.0691 | 17 | 212 | 0.8471 | -0.0519 | -0.0519 | 19 | 0.4032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0498 | 0.0622 | 0.0928 | 17 | 212 | 0.0558 | -0.0693 | -0.0693 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0040 | -0.0013 | 0.0639 | 17 | 1008 | 0.0014 | 0.0427 | -0.0427 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0403 | 0.0046 | 0.0677 | 17 | 1008 | -0.0186 | -0.3416 | 0.3416 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0713 | 0.0797 | 0.0112 | 17 | 1008 | 0.0751 | -0.4094 | 0.4094 | 8 | 0.7742 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0885 | 0.1000 | 0.0206 | 17 | 1008 | 0.0941 | -0.2855 | 0.2855 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0381 | 0.0361 | 0.0949 | 17 | 1008 | -0.0021 | -0.4032 | 0.4032 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4516 | 0.4536 | 0.0320 | 17 | 1008 | 0.4526 | -0.0326 | 0.0326 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0770 | -0.0760 | 0.0649 | 17 | 1008 | -0.0766 | -0.0088 | 0.0088 | 16 | 0.5161 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4297 | 0.4020 | 0.0330 | 17 | 1008 | 0.4163 | 0.4329 | -0.4329 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4494 | 0.4384 | 0.0255 | 17 | 1008 | 0.4441 | 0.2228 | -0.2228 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.1209 | -0.0054 | 0.0784 | 17 | 1060 | 0.0805 | 1.0950 | 1.0950 | 2 | 0.9677 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.1545 | -0.0001 | 0.0921 | 17 | 1060 | 0.1050 | 1.1421 | 1.1421 | 1 | 1.0000 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.1126 | 0.0796 | 0.0177 | 17 | 1060 | 0.0966 | 0.9583 | 0.9583 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0976 | 0.0990 | 0.0195 | 17 | 1060 | 0.0983 | -0.0384 | -0.0384 | 15 | 0.5484 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.3045 | 0.0308 | 0.1280 | 17 | 1060 | 0.2169 | 1.4544 | 1.4544 | 1 | 1.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.5465 | 0.4521 | 0.0418 | 17 | 1060 | 0.5163 | 1.5350 | 1.5350 | 1 | 1.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0055 | -0.0477 | 0.0349 | 17 | 1060 | -0.0135 | 0.9808 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0891 | -0.0806 | 0.0754 | 17 | 1060 | -0.0850 | -0.0580 | -0.0580 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3805 | 0.4004 | 0.0385 | 17 | 1060 | 0.3887 | -0.3025 | -0.3025 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4821 | 0.4370 | 0.0337 | 17 | 1060 | 0.4735 | 1.0826 | 1.0826 | 4 | 0.9032 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## NO
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **defense_overall** (0.396) · Weakest area: **special_teams** (-0.962)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.396 | 9 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.262 | 8 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.301 | 12 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.366 | 7 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.389 | 27 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.113 | 18 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.431 | 27 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.518 | 29 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.962 | 32 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1224 | 0.1450 | 0.0327 | 17 | 670 | 0.1296 | -0.4699 | 0.4699 | 9 | 0.7419 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1955 | 0.2045 | 0.0323 | 17 | 670 | 0.1999 | -0.1440 | 0.1440 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0731 | 0.0664 | 0.0188 | 17 | 670 | 0.0710 | 0.2436 | -0.2436 | 22 | 0.3226 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1398 | 0.1442 | 0.0234 | 17 | 565 | 0.1419 | -0.0958 | -0.0958 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0796 | 0.0660 | 0.0121 | 17 | 565 | 0.0735 | 0.6188 | 0.6188 | 5 | 0.8710 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.7143 | 0.8507 | 0.0691 | 17 | 218 | 0.7804 | -1.0166 | -1.0166 | 32 | 0.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | -0.1112 | 0.0622 | 0.0928 | 17 | 218 | -0.0271 | -0.9624 | -0.9624 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0473 | -0.0013 | 0.0639 | 17 | 1070 | -0.0250 | -0.3710 | 0.3710 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0505 | 0.0046 | 0.0677 | 17 | 1070 | -0.0238 | -0.4190 | 0.4190 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0779 | 0.0797 | 0.0112 | 17 | 1070 | 0.0787 | -0.0883 | 0.0883 | 17 | 0.4839 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0839 | 0.1000 | 0.0206 | 17 | 1070 | 0.0917 | -0.4027 | 0.4027 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0155 | 0.0361 | 0.0949 | 17 | 1070 | 0.0095 | -0.2802 | 0.2802 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4336 | 0.4536 | 0.0320 | 17 | 1070 | 0.4433 | -0.3217 | 0.3217 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1359 | -0.0760 | 0.0649 | 17 | 1070 | -0.1089 | -0.5059 | 0.5059 | 2 | 0.9677 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3899 | 0.4020 | 0.0330 | 17 | 1070 | 0.3958 | -0.1881 | 0.1881 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4187 | 0.4384 | 0.0255 | 17 | 1070 | 0.4282 | -0.3988 | 0.3988 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0398 | -0.0054 | 0.0784 | 17 | 1108 | -0.0288 | -0.2990 | -0.2990 | 24 | 0.2581 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.0762 | -0.0001 | 0.0921 | 17 | 1108 | -0.0519 | -0.5620 | -0.5620 | 27 | 0.1613 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0493 | 0.0796 | 0.0177 | 17 | 1108 | 0.0640 | -0.8808 | -0.8808 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0677 | 0.0990 | 0.0195 | 17 | 1108 | 0.0829 | -0.8267 | -0.8267 | 32 | 0.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.0470 | 0.0308 | 0.1280 | 17 | 1108 | -0.0221 | -0.4134 | -0.4134 | 27 | 0.1613 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4522 | 0.4521 | 0.0418 | 17 | 1108 | 0.4522 | 0.0026 | 0.0026 | 17 | 0.4839 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0583 | -0.0477 | 0.0349 | 17 | 1108 | -0.0563 | -0.2467 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.1554 | -0.0806 | 0.0754 | 17 | 1108 | -0.1191 | -0.5114 | -0.5114 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3659 | 0.4004 | 0.0385 | 17 | 1108 | 0.3802 | -0.5243 | -0.5243 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4242 | 0.4370 | 0.0337 | 17 | 1108 | 0.4266 | -0.3064 | -0.3064 | 26 | 0.1935 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## NYG
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_offense** (0.176) · Weakest area: **rushing_defense** (-1.356)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.658 | 25 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.012 | 19 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.109 | 18 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -1.356 | 32 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.034 | 21 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.549 | 25 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.072 | 20 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.176 | 15 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.222 | 27 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1795 | 0.1450 | 0.0327 | 17 | 624 | 0.1685 | 0.7168 | -0.7168 | 26 | 0.1935 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1746 | 0.2045 | 0.0323 | 17 | 624 | 0.1891 | -0.4772 | 0.4772 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0769 | 0.0664 | 0.0188 | 17 | 624 | 0.0736 | 0.3808 | -0.3808 | 23 | 0.2903 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1498 | 0.1442 | 0.0234 | 17 | 621 | 0.1471 | 0.1229 | 0.1229 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0628 | 0.0660 | 0.0121 | 17 | 621 | 0.0643 | -0.1476 | -0.1476 | 17 | 0.4839 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8846 | 0.8507 | 0.0691 | 17 | 217 | 0.8682 | 0.2526 | 0.2526 | 11 | 0.6774 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0221 | 0.0622 | 0.0928 | 17 | 217 | 0.0416 | -0.2225 | -0.2225 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0757 | -0.0013 | 0.0639 | 17 | 1085 | 0.0383 | 0.6208 | -0.6208 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0960 | 0.0046 | 0.0677 | 17 | 1085 | 0.0517 | 0.6953 | -0.6953 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0789 | 0.0797 | 0.0112 | 17 | 1085 | 0.0793 | -0.0380 | 0.0380 | 19 | 0.4194 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1555 | 0.1000 | 0.0206 | 17 | 1085 | 0.1286 | 1.3893 | -1.3893 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0556 | 0.0361 | 0.0949 | 17 | 1085 | 0.0462 | 0.1060 | -0.1060 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4605 | 0.4536 | 0.0320 | 17 | 1085 | 0.4572 | 0.1111 | -0.1111 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | 0.1087 | -0.0760 | 0.0649 | 17 | 1085 | 0.0253 | 1.5598 | -1.5598 | 32 | 0.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4737 | 0.4020 | 0.0330 | 17 | 1085 | 0.4389 | 1.1202 | -1.1202 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4710 | 0.4384 | 0.0255 | 17 | 1085 | 0.4552 | 0.6592 | -0.6592 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0086 | -0.0054 | 0.0784 | 17 | 1137 | -0.0076 | -0.0278 | -0.0278 | 21 | 0.3548 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0425 | -0.0001 | 0.0921 | 17 | 1137 | 0.0289 | 0.3151 | 0.3151 | 10 | 0.7097 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0833 | 0.0796 | 0.0177 | 17 | 1137 | 0.0815 | 0.1092 | 0.1092 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0927 | 0.0990 | 0.0195 | 17 | 1137 | 0.0957 | -0.1673 | -0.1673 | 20 | 0.3871 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0389 | 0.0308 | 0.1280 | 17 | 1137 | 0.0363 | 0.0433 | 0.0433 | 17 | 0.4839 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4295 | 0.4521 | 0.0418 | 17 | 1137 | 0.4367 | -0.3673 | -0.3673 | 27 | 0.1613 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0839 | -0.0477 | 0.0349 | 17 | 1137 | -0.0770 | -0.8400 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0397 | -0.0806 | 0.0754 | 17 | 1137 | -0.0595 | 0.2799 | 0.2799 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4052 | 0.4004 | 0.0385 | 17 | 1137 | 0.4032 | 0.0731 | 0.0731 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4292 | 0.4370 | 0.0337 | 17 | 1137 | 0.4307 | -0.1862 | -0.1862 | 25 | 0.2258 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## NYJ
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **special_teams** (1.446) · Weakest area: **pass_protection** (-1.060)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.863 | 28 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.958 | 31 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.951 | 31 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.277 | 24 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -0.806 | 29 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -1.060 | 30 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.966 | 30 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.020 | 22 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 1.446 | 1 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1908 | 0.1450 | 0.0327 | 17 | 608 | 0.1761 | 0.9516 | -0.9516 | 29 | 0.0968 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2095 | 0.2045 | 0.0323 | 17 | 608 | 0.2071 | 0.0787 | -0.0787 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0987 | 0.0664 | 0.0188 | 17 | 608 | 0.0884 | 1.1687 | -1.1687 | 30 | 0.0645 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1005 | 0.1442 | 0.0234 | 17 | 577 | 0.1217 | -0.9609 | -0.9609 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0451 | 0.0660 | 0.0121 | 17 | 577 | 0.0545 | -0.9549 | -0.9549 | 30 | 0.0645 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9655 | 0.8507 | 0.0691 | 17 | 231 | 0.9099 | 0.8555 | 0.8555 | 1 | 1.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.3229 | 0.0622 | 0.0928 | 17 | 231 | 0.1965 | 1.4463 | 1.4463 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.1382 | -0.0013 | 0.0639 | 17 | 1098 | 0.0705 | 1.1248 | -1.1248 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.1471 | 0.0046 | 0.0677 | 17 | 1098 | 0.0780 | 1.0837 | -1.0837 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0988 | 0.0797 | 0.0112 | 17 | 1098 | 0.0902 | 0.9339 | -0.9339 | 30 | 0.0645 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1113 | 0.1000 | 0.0206 | 17 | 1098 | 0.1058 | 0.2847 | -0.2847 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.2875 | 0.0361 | 0.0949 | 17 | 1098 | 0.1656 | 1.3648 | -1.3648 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4870 | 0.4536 | 0.0320 | 17 | 1098 | 0.4708 | 0.5364 | -0.5364 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0345 | -0.0760 | 0.0649 | 17 | 1098 | -0.0532 | 0.3508 | -0.3508 | 25 | 0.2258 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4144 | 0.4020 | 0.0330 | 17 | 1098 | 0.4084 | 0.1946 | -0.1946 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4572 | 0.4384 | 0.0255 | 17 | 1098 | 0.4481 | 0.3805 | -0.3805 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0858 | -0.0054 | 0.0784 | 17 | 1032 | -0.0601 | -0.6974 | -0.6974 | 29 | 0.0968 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.1293 | -0.0001 | 0.0921 | 17 | 1032 | -0.0880 | -0.9539 | -0.9539 | 29 | 0.0968 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0428 | 0.0796 | 0.0177 | 17 | 1032 | 0.0606 | -1.0694 | -1.0694 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0973 | 0.0990 | 0.0195 | 17 | 1032 | 0.0981 | -0.0464 | -0.0464 | 17 | 0.4839 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.1481 | 0.0308 | 0.1280 | 17 | 1032 | -0.0908 | -0.9504 | -0.9504 | 28 | 0.1290 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.3980 | 0.4521 | 0.0418 | 17 | 1032 | 0.4153 | -0.8788 | -0.8788 | 30 | 0.0645 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.1047 | -0.0477 | 0.0349 | 17 | 1032 | -0.0939 | -1.3240 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.1169 | -0.0806 | 0.0754 | 17 | 1032 | -0.0993 | -0.2478 | -0.2478 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4140 | 0.4004 | 0.0385 | 17 | 1032 | 0.4083 | 0.2069 | 0.2069 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4050 | 0.4370 | 0.0337 | 17 | 1032 | 0.4111 | -0.7659 | -0.7659 | 29 | 0.0968 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## PHI
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **passing_defense** (0.593) · Weakest area: **special_teams** (-0.168)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.295 | 10 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.230 | 11 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.593 | 6 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.012 | 16 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.059 | 19 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.569 | 8 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.009 | 18 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.173 | 16 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.168 | 25 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0995 | 0.1450 | 0.0327 | 17 | 573 | 0.1140 | -0.9460 | 0.9460 | 2 | 0.9677 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2517 | 0.2045 | 0.0323 | 17 | 573 | 0.2289 | 0.7519 | -0.7519 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0611 | 0.0664 | 0.0188 | 17 | 573 | 0.0628 | -0.1927 | 0.1927 | 15 | 0.5484 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1629 | 0.1442 | 0.0234 | 17 | 626 | 0.1538 | 0.4131 | 0.4131 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0671 | 0.0660 | 0.0121 | 17 | 626 | 0.0666 | 0.0476 | 0.0476 | 15 | 0.5484 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.7407 | 0.8507 | 0.0691 | 17 | 217 | 0.7941 | -0.8195 | -0.8195 | 31 | 0.0323 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0319 | 0.0622 | 0.0928 | 17 | 217 | 0.0466 | -0.1680 | -0.1680 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0248 | -0.0013 | 0.0639 | 17 | 1108 | -0.0134 | -0.1896 | 0.1896 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.0513 | 0.0046 | 0.0677 | 17 | 1108 | -0.0242 | -0.4247 | 0.4247 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0735 | 0.0797 | 0.0112 | 17 | 1108 | 0.0763 | -0.3031 | 0.3031 | 11 | 0.6774 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0998 | 0.1000 | 0.0206 | 17 | 1108 | 0.0999 | -0.0046 | 0.0046 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0689 | 0.0361 | 0.0949 | 17 | 1108 | -0.0180 | -0.5702 | 0.5702 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4153 | 0.4536 | 0.0320 | 17 | 1108 | 0.4339 | -0.6159 | 0.6159 | 5 | 0.8710 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1037 | -0.0760 | 0.0649 | 17 | 1108 | -0.0912 | -0.2341 | 0.2341 | 9 | 0.7419 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4150 | 0.4020 | 0.0330 | 17 | 1108 | 0.4087 | 0.2029 | -0.2029 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4251 | 0.4384 | 0.0255 | 17 | 1108 | 0.4315 | -0.2693 | 0.2693 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.0025 | -0.0054 | 0.0784 | 17 | 1033 | -0.0034 | 0.0250 | 0.0250 | 20 | 0.3871 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0343 | -0.0001 | 0.0921 | 17 | 1033 | 0.0233 | 0.2540 | 0.2540 | 17 | 0.4839 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0733 | 0.0796 | 0.0177 | 17 | 1033 | 0.0763 | -0.1823 | -0.1823 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1166 | 0.0990 | 0.0195 | 17 | 1033 | 0.1080 | 0.4624 | 0.4624 | 4 | 0.9032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0765 | 0.0308 | 0.1280 | 17 | 1033 | 0.0618 | 0.2427 | 0.2427 | 14 | 0.5806 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4468 | 0.4521 | 0.0418 | 17 | 1033 | 0.4485 | -0.0863 | -0.0863 | 22 | 0.3226 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0495 | -0.0477 | 0.0349 | 17 | 1033 | -0.0492 | -0.0424 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0468 | -0.0806 | 0.0754 | 17 | 1033 | -0.0632 | 0.2312 | 0.2312 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4079 | 0.4004 | 0.0385 | 17 | 1033 | 0.4048 | 0.1150 | 0.1150 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4327 | 0.4370 | 0.0337 | 17 | 1033 | 0.4335 | -0.1017 | -0.1017 | 23 | 0.2903 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## PIT
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_protection** (0.652) · Weakest area: **passing_offense** (-0.165)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.072 | 13 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.250 | 9 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.030 | 15 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.074 | 20 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.120 | 18 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.652 | 5 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -0.165 | 23 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.569 | 6 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.405 | 10 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1066 | 0.1450 | 0.0327 | 17 | 591 | 0.1189 | -0.7980 | 0.7980 | 5 | 0.8710 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1851 | 0.2045 | 0.0323 | 17 | 591 | 0.1945 | -0.3096 | 0.3096 | 12 | 0.6452 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0525 | 0.0664 | 0.0188 | 17 | 591 | 0.0569 | -0.5051 | 0.5051 | 11 | 0.6774 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1581 | 0.1442 | 0.0234 | 17 | 683 | 0.1514 | 0.3071 | 0.3071 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0703 | 0.0660 | 0.0121 | 17 | 683 | 0.0684 | 0.1925 | 0.1925 | 11 | 0.6774 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8438 | 0.8507 | 0.0691 | 17 | 226 | 0.8471 | -0.0519 | -0.0519 | 19 | 0.4032 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1351 | 0.0622 | 0.0928 | 17 | 226 | 0.0998 | 0.4045 | 0.4045 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0459 | -0.0013 | 0.0639 | 17 | 1142 | -0.0243 | -0.3596 | 0.3596 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0252 | 0.0046 | 0.0677 | 17 | 1142 | 0.0152 | 0.1566 | -0.1566 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0776 | 0.0797 | 0.0112 | 17 | 1142 | 0.0785 | -0.1019 | 0.1019 | 16 | 0.5161 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0976 | 0.1000 | 0.0206 | 17 | 1142 | 0.0988 | -0.0585 | 0.0585 | 18 | 0.4516 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0463 | 0.0361 | 0.0949 | 17 | 1142 | 0.0414 | 0.0553 | -0.0553 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4539 | 0.4536 | 0.0320 | 17 | 1142 | 0.4538 | 0.0039 | -0.0039 | 16 | 0.5161 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0348 | -0.0760 | 0.0649 | 17 | 1142 | -0.0534 | 0.3479 | -0.3479 | 24 | 0.2581 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3976 | 0.4020 | 0.0330 | 17 | 1142 | 0.3997 | -0.0681 | 0.0681 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4378 | 0.4384 | 0.0255 | 17 | 1142 | 0.4381 | -0.0115 | 0.0115 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0004 | -0.0054 | 0.0784 | 17 | 1015 | -0.0014 | 0.0502 | 0.0502 | 19 | 0.4194 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0276 | -0.0001 | 0.0921 | 17 | 1015 | 0.0187 | 0.2050 | 0.2050 | 18 | 0.4516 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0694 | 0.0796 | 0.0177 | 17 | 1015 | 0.0743 | -0.2963 | -0.2963 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1080 | 0.0990 | 0.0195 | 17 | 1015 | 0.1036 | 0.2361 | 0.2361 | 10 | 0.7097 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0357 | 0.0308 | 0.1280 | 17 | 1015 | 0.0341 | 0.0261 | 0.0261 | 19 | 0.4194 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4382 | 0.4521 | 0.0418 | 17 | 1015 | 0.4427 | -0.2250 | -0.2250 | 24 | 0.2581 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0356 | -0.0477 | 0.0349 | 17 | 1015 | -0.0379 | 0.2812 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0014 | -0.0806 | 0.0754 | 17 | 1015 | -0.0398 | 0.5411 | 0.5411 | 7 | 0.8065 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4396 | 0.4004 | 0.0385 | 17 | 1015 | 0.4234 | 0.5969 | 0.5969 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4414 | 0.4370 | 0.0337 | 17 | 1015 | 0.4405 | 0.1061 | 0.1061 | 17 | 0.4839 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## SEA
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **rushing_defense** (1.028) · Weakest area: **rushing_offense** (-0.008)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.738 | 2 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.220 | 13 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | 0.632 | 4 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 1.028 | 1 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.464 | 10 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.562 | 9 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.823 | 4 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.008 | 21 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.642 | 8 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1158 | 0.1450 | 0.0327 | 17 | 518 | 0.1252 | -0.6061 | 0.6061 | 6 | 0.8387 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2322 | 0.2045 | 0.0323 | 17 | 518 | 0.2188 | 0.4402 | -0.4402 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0521 | 0.0664 | 0.0188 | 17 | 518 | 0.0567 | -0.5171 | 0.5171 | 9 | 0.7419 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1597 | 0.1442 | 0.0234 | 17 | 689 | 0.1521 | 0.3407 | 0.3407 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0682 | 0.0660 | 0.0121 | 17 | 689 | 0.0672 | 0.0987 | 0.0987 | 12 | 0.6452 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8542 | 0.8507 | 0.0691 | 17 | 218 | 0.8525 | 0.0257 | 0.0257 | 17 | 0.4839 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1779 | 0.0622 | 0.0928 | 17 | 218 | 0.1218 | 0.6416 | 0.6416 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | -0.0702 | -0.0013 | 0.0639 | 17 | 1106 | -0.0368 | -0.5559 | 0.5559 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | -0.1128 | 0.0046 | 0.0677 | 17 | 1106 | -0.0559 | -0.8926 | 0.8926 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0639 | 0.0797 | 0.0112 | 17 | 1106 | 0.0710 | -0.7735 | 0.7735 | 5 | 0.8710 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0477 | 0.1000 | 0.0206 | 17 | 1106 | 0.0731 | -1.3059 | 1.3059 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.0784 | 0.0361 | 0.0949 | 17 | 1106 | -0.0229 | -0.6216 | 0.6216 | 6 | 0.8387 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4136 | 0.4536 | 0.0320 | 17 | 1106 | 0.4330 | -0.6431 | 0.6431 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.2055 | -0.0760 | 0.0649 | 17 | 1106 | -0.1470 | -1.0934 | 1.0934 | 1 | 1.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3581 | 0.4020 | 0.0330 | 17 | 1106 | 0.3794 | -0.6856 | 0.6856 | 1 | 1.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4005 | 0.4384 | 0.0255 | 17 | 1106 | 0.4189 | -0.7661 | 0.7661 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0442 | -0.0054 | 0.0784 | 17 | 1039 | 0.0283 | 0.4301 | 0.4301 | 10 | 0.7097 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0365 | -0.0001 | 0.0921 | 17 | 1039 | 0.0247 | 0.2702 | 0.2702 | 14 | 0.5806 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.1100 | 0.0796 | 0.0177 | 17 | 1039 | 0.0953 | 0.8850 | 0.8850 | 3 | 0.9355 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1079 | 0.0990 | 0.0195 | 17 | 1039 | 0.1036 | 0.2354 | 0.2354 | 11 | 0.6774 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.1174 | 0.0308 | 0.1280 | 17 | 1039 | 0.0897 | 0.4604 | 0.4604 | 9 | 0.7419 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.5212 | 0.4521 | 0.0418 | 17 | 1039 | 0.4991 | 1.1244 | 1.1244 | 4 | 0.9032 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0899 | -0.0477 | 0.0349 | 17 | 1039 | -0.0818 | -0.9793 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0758 | -0.0806 | 0.0754 | 17 | 1039 | -0.0782 | 0.0325 | 0.0325 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3971 | 0.4004 | 0.0385 | 17 | 1039 | 0.3985 | -0.0490 | -0.0490 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4658 | 0.4370 | 0.0337 | 17 | 1039 | 0.4603 | 0.6928 | 0.6928 | 8 | 0.7742 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## SF
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **special_teams** (0.800) · Weakest area: **pass_rush** (-1.371)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.680 | 26 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -1.371 | 32 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.612 | 25 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.196 | 21 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.692 | 6 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.560 | 10 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.670 | 7 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.294 | 11 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.800 | 2 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1314 | 0.1450 | 0.0327 | 17 | 624 | 0.1358 | -0.2824 | 0.2824 | 14 | 0.5806 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1941 | 0.2045 | 0.0323 | 17 | 624 | 0.1992 | -0.1657 | 0.1657 | 14 | 0.5806 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0433 | 0.0664 | 0.0188 | 17 | 624 | 0.0507 | -0.8377 | 0.8377 | 4 | 0.9032 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.0905 | 0.1442 | 0.0234 | 17 | 630 | 0.1165 | -1.1820 | -1.1820 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0317 | 0.0660 | 0.0121 | 17 | 630 | 0.0472 | -1.5608 | -1.5608 | 32 | 0.0000 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.9167 | 0.8507 | 0.0691 | 17 | 207 | 0.8847 | 0.4915 | 0.4915 | 7 | 0.8065 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.2064 | 0.0622 | 0.0928 | 17 | 207 | 0.1365 | 0.8003 | 0.8003 | 2 | 0.9677 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0768 | -0.0013 | 0.0639 | 17 | 1063 | 0.0389 | 0.6301 | -0.6301 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0700 | 0.0046 | 0.0677 | 17 | 1063 | 0.0383 | 0.4971 | -0.4971 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0714 | 0.0797 | 0.0112 | 17 | 1063 | 0.0752 | -0.4035 | 0.4035 | 9 | 0.7419 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0827 | 0.1000 | 0.0206 | 17 | 1063 | 0.0911 | -0.4314 | 0.4314 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1431 | 0.0361 | 0.0949 | 17 | 1063 | 0.0912 | 0.5806 | -0.5806 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4937 | 0.4536 | 0.0320 | 17 | 1063 | 0.4743 | 0.6433 | -0.6433 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0694 | -0.0760 | 0.0649 | 17 | 1063 | -0.0724 | 0.0554 | -0.0554 | 17 | 0.4839 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4637 | 0.4020 | 0.0330 | 17 | 1063 | 0.4338 | 0.9636 | -0.9636 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4835 | 0.4384 | 0.0255 | 17 | 1063 | 0.4617 | 0.9136 | -0.9136 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0236 | -0.0054 | 0.0784 | 17 | 1095 | 0.0143 | 0.2512 | 0.2512 | 14 | 0.5806 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0910 | -0.0001 | 0.0921 | 17 | 1095 | 0.0618 | 0.6726 | 0.6726 | 6 | 0.8387 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0817 | 0.0796 | 0.0177 | 17 | 1095 | 0.0807 | 0.0626 | 0.0626 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0858 | 0.0990 | 0.0195 | 17 | 1095 | 0.0922 | -0.3491 | -0.3491 | 23 | 0.2903 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.1673 | 0.0308 | 0.1280 | 17 | 1095 | 0.1236 | 0.7257 | 0.7257 | 6 | 0.8387 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.5272 | 0.4521 | 0.0418 | 17 | 1095 | 0.5032 | 1.2221 | 1.2221 | 2 | 0.9516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0301 | -0.0477 | 0.0349 | 17 | 1095 | -0.0335 | 0.4077 | 0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0328 | -0.0806 | 0.0754 | 17 | 1095 | -0.0560 | 0.3264 | 0.3264 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4176 | 0.4004 | 0.0385 | 17 | 1095 | 0.4105 | 0.2623 | 0.2623 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4849 | 0.4370 | 0.0337 | 17 | 1095 | 0.4758 | 1.1511 | 1.1511 | 3 | 0.9355 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## TB
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **pass_protection** (0.718) · Weakest area: **passing_defense** (-0.483)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.244 | 21 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | -0.295 | 24 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.483 | 24 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.383 | 5 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.040 | 20 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.718 | 4 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.020 | 15 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.022 | 23 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | -0.204 | 26 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0878 | 0.1450 | 0.0327 | 17 | 638 | 0.1061 | -1.1892 | 1.1892 | 1 | 1.0000 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2106 | 0.2045 | 0.0323 | 17 | 638 | 0.2077 | 0.0974 | -0.0974 | 23 | 0.2903 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0596 | 0.0664 | 0.0188 | 17 | 638 | 0.0618 | -0.2478 | 0.2478 | 13 | 0.6129 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1344 | 0.1442 | 0.0234 | 17 | 640 | 0.1391 | -0.2157 | -0.2157 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0578 | 0.0660 | 0.0121 | 17 | 640 | 0.0615 | -0.3747 | -0.3747 | 23 | 0.2903 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8421 | 0.8507 | 0.0691 | 17 | 223 | 0.8463 | -0.0641 | -0.0641 | 21 | 0.3548 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.0254 | 0.0622 | 0.0928 | 17 | 223 | 0.0433 | -0.2044 | -0.2044 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0446 | -0.0013 | 0.0639 | 17 | 1025 | 0.0224 | 0.3704 | -0.3704 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.0166 | 0.0046 | 0.0677 | 17 | 1025 | 0.0108 | 0.0912 | -0.0912 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0859 | 0.0797 | 0.0112 | 17 | 1025 | 0.0831 | 0.3057 | -0.3057 | 24 | 0.2581 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0901 | 0.1000 | 0.0206 | 17 | 1025 | 0.0949 | -0.2455 | 0.2455 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.0861 | 0.0361 | 0.0949 | 17 | 1025 | 0.0619 | 0.2715 | -0.2715 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4969 | 0.4536 | 0.0320 | 17 | 1025 | 0.4759 | 0.6951 | -0.6951 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.1168 | -0.0760 | 0.0649 | 17 | 1025 | -0.0984 | -0.3443 | 0.3443 | 5 | 0.8710 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3662 | 0.4020 | 0.0330 | 17 | 1025 | 0.3835 | -0.5590 | 0.5590 | 4 | 0.9032 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4517 | 0.4384 | 0.0255 | 17 | 1025 | 0.4453 | 0.2694 | -0.2694 | 20 | 0.3871 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0150 | -0.0054 | 0.0784 | 17 | 1116 | 0.0085 | 0.1770 | 0.1770 | 18 | 0.4516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0057 | -0.0001 | 0.0921 | 17 | 1116 | 0.0038 | 0.0430 | 0.0430 | 20 | 0.3871 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0862 | 0.0796 | 0.0177 | 17 | 1116 | 0.0830 | 0.1927 | 0.1927 | 9 | 0.7419 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0787 | 0.0990 | 0.0195 | 17 | 1116 | 0.0886 | -0.5357 | -0.5357 | 25 | 0.2258 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0413 | 0.0308 | 0.1280 | 17 | 1116 | 0.0380 | 0.0561 | 0.0561 | 16 | 0.5161 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4404 | 0.4521 | 0.0418 | 17 | 1116 | 0.4442 | -0.1893 | -0.1893 | 23 | 0.2903 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0694 | -0.0477 | 0.0349 | 17 | 1116 | -0.0653 | -0.5041 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0873 | -0.0806 | 0.0754 | 17 | 1116 | -0.0840 | -0.0454 | -0.0454 | 24 | 0.2581 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4005 | 0.4004 | 0.0385 | 17 | 1116 | 0.4004 | 0.0014 | 0.0014 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4328 | 0.4370 | 0.0337 | 17 | 1116 | 0.4336 | -0.0999 | -0.0999 | 21 | 0.3548 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## TEN
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **special_teams** (0.362) · Weakest area: **offense_overall** (-1.122)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.608 | 24 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.213 | 14 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.699 | 26 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | 0.051 | 13 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | -1.122 | 30 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | -0.630 | 26 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | -1.012 | 31 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | -0.317 | 27 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.362 | 13 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1703 | 0.1450 | 0.0327 | 17 | 646 | 0.1622 | 0.5254 | -0.5254 | 23 | 0.2903 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.1944 | 0.2045 | 0.0323 | 17 | 646 | 0.1993 | -0.1607 | 0.1607 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0867 | 0.0664 | 0.0188 | 17 | 646 | 0.0802 | 0.7343 | -0.7343 | 27 | 0.1613 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1544 | 0.1442 | 0.0234 | 17 | 596 | 0.1494 | 0.2243 | 0.2243 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0705 | 0.0660 | 0.0121 | 17 | 596 | 0.0685 | 0.2013 | 0.2013 | 10 | 0.7097 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.8056 | 0.8507 | 0.0691 | 17 | 242 | 0.8274 | -0.3365 | -0.3365 | 26 | 0.1935 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1276 | 0.0622 | 0.0928 | 17 | 242 | 0.0959 | 0.3625 | 0.3625 | 13 | 0.6129 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.0897 | -0.0013 | 0.0639 | 17 | 1035 | 0.0456 | 0.7335 | -0.7335 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.1060 | 0.0046 | 0.0677 | 17 | 1035 | 0.0568 | 0.7710 | -0.7710 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0973 | 0.0797 | 0.0112 | 17 | 1035 | 0.0894 | 0.8619 | -0.8619 | 29 | 0.0968 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0918 | 0.1000 | 0.0206 | 17 | 1035 | 0.0958 | -0.2037 | 0.2037 | 17 | 0.4839 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.1861 | 0.0361 | 0.0949 | 17 | 1035 | 0.1134 | 0.8144 | -0.8144 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4899 | 0.4536 | 0.0320 | 17 | 1035 | 0.4723 | 0.5835 | -0.5835 | 25 | 0.2258 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | -0.0426 | -0.0760 | 0.0649 | 17 | 1035 | -0.0577 | 0.2823 | -0.2823 | 20 | 0.3871 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.3871 | 0.4020 | 0.0330 | 17 | 1035 | 0.3943 | -0.2325 | 0.2325 | 8 | 0.7742 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4541 | 0.4384 | 0.0255 | 17 | 1035 | 0.4465 | 0.3180 | -0.3180 | 22 | 0.3226 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | -0.1056 | -0.0054 | 0.0784 | 17 | 1046 | -0.0736 | -0.8697 | -0.8697 | 30 | 0.0645 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | -0.1484 | -0.0001 | 0.0921 | 17 | 1046 | -0.1010 | -1.0951 | -1.0951 | 30 | 0.0645 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0635 | 0.0796 | 0.0177 | 17 | 1046 | 0.0713 | -0.4679 | -0.4679 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.0944 | 0.0990 | 0.0195 | 17 | 1046 | 0.0967 | -0.1205 | -0.1205 | 18 | 0.4516 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | -0.1963 | 0.0308 | 0.1280 | 17 | 1046 | -0.1237 | -1.2068 | -1.2068 | 31 | 0.0323 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.3684 | 0.4521 | 0.0418 | 17 | 1046 | 0.3952 | -1.3602 | -1.3602 | 31 | 0.0323 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0699 | -0.0477 | 0.0349 | 17 | 1046 | -0.0657 | -0.5153 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.1168 | -0.0806 | 0.0754 | 17 | 1046 | -0.0992 | -0.2471 | -0.2471 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.3750 | 0.4004 | 0.0385 | 17 | 1046 | 0.3855 | -0.3861 | -0.3861 | 27 | 0.1613 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.3786 | 0.4370 | 0.0337 | 17 | 1046 | 0.3897 | -1.4007 | -1.4007 | 31 | 0.0323 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

## WAS
Record: no games yet · Points for/against: —/— · Point differential: — · Data confidence: prior_season_only
Strongest area: **offense_overall** (0.426) · Weakest area: **defense_overall** (-1.045)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -1.045 | 32 | 0.000 | 0.000 | prior_season_only |
| pass_rush | Pass-Rush Strength Index | 0.034 | 17 | 0.000 | 0.000 | prior_season_only |
| passing_defense | Pass-Defense Strength Index | -0.870 | 28 | 0.000 | 0.000 | prior_season_only |
| rushing_defense | Run-Defense Strength Index | -0.656 | 29 | 0.000 | 0.000 | prior_season_only |
| offense_overall | Offensive Strength Index | 0.426 | 11 | 0.000 | 0.000 | prior_season_only |
| pass_protection | Pass-Protection Strength Index | 0.103 | 19 | 0.000 | 0.000 | prior_season_only |
| passing_offense | Passing-Offense Strength Index | 0.063 | 14 | 0.000 | 0.000 | prior_season_only |
| rushing_offense | Rushing-Offense Strength Index | 0.352 | 9 | 0.000 | 0.000 | prior_season_only |
| special_teams | Special-Teams Strength Index | 0.313 | 15 | 0.000 | 0.000 | prior_season_only |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1365 | 0.1450 | 0.0327 | 17 | 564 | 0.1392 | -0.1761 | 0.1761 | 15 | 0.5484 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_protection.rush_stuffed_rate_approx | 0.2091 | 0.2045 | 0.0323 | 17 | 564 | 0.2069 | 0.0733 | -0.0733 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_protection.sack_rate_allowed | 0.0656 | 0.0664 | 0.0188 | 17 | 564 | 0.0659 | -0.0291 | 0.0291 | 18 | 0.4516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| pass_rush.qb_hit_rate_generated | 0.1429 | 0.1442 | 0.0234 | 17 | 616 | 0.1435 | -0.0290 | -0.0290 | 19 | 0.4194 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| pass_rush.sack_rate_generated | 0.0682 | 0.0660 | 0.0121 | 17 | 616 | 0.0672 | 0.0972 | 0.0972 | 13 | 0.6129 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.fg_pct | 0.7667 | 0.8507 | 0.0691 | 17 | 218 | 0.8074 | -0.6263 | -0.6263 | 29 | 0.0968 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| special_teams.st_epa_per_play | 0.1186 | 0.0622 | 0.0928 | 17 | 218 | 0.0913 | 0.3129 | 0.3129 | 15 | 0.5484 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.early_down_epa_per_play | 0.1483 | -0.0013 | 0.0639 | 17 | 1116 | 0.0757 | 1.2061 | -1.2061 | 32 | 0.0000 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.epa_per_play | 0.1517 | 0.0046 | 0.0677 | 17 | 1116 | 0.0804 | 1.1187 | -1.1187 | 31 | 0.0323 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_pass_rate | 0.0860 | 0.0797 | 0.0112 | 17 | 1116 | 0.0832 | 0.3107 | -0.3107 | 25 | 0.2258 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1176 | 0.1000 | 0.0206 | 17 | 1116 | 0.1091 | 0.4425 | -0.4425 | 26 | 0.1935 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | 0.2240 | 0.0361 | 0.0949 | 17 | 1116 | 0.1329 | 1.0203 | -1.0203 | 30 | 0.0645 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_success_rate | 0.4984 | 0.4536 | 0.0320 | 17 | 1116 | 0.4767 | 0.7193 | -0.7193 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.rush_epa_per_play | 0.0262 | -0.0760 | 0.0649 | 17 | 1116 | -0.0200 | 0.8625 | -0.8625 | 28 | 0.1290 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.rush_success_rate | 0.4444 | 0.4020 | 0.0330 | 17 | 1116 | 0.4239 | 0.6634 | -0.6634 | 29 | 0.0968 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_defense.success_rate | 0.4785 | 0.4384 | 0.0255 | 17 | 1116 | 0.4591 | 0.8115 | -0.8115 | 28 | 0.1290 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.early_down_epa_per_play | 0.0361 | -0.0054 | 0.0784 | 17 | 1029 | 0.0228 | 0.3594 | 0.3594 | 11 | 0.6774 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.epa_per_play | 0.0347 | -0.0001 | 0.0921 | 17 | 1029 | 0.0236 | 0.2574 | 0.2574 | 16 | 0.5161 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.explosive_pass_rate | 0.0709 | 0.0796 | 0.0177 | 17 | 1029 | 0.0751 | -0.2514 | -0.2514 | 21 | 0.3548 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.explosive_rush_rate | 0.1106 | 0.0990 | 0.0195 | 17 | 1029 | 0.1050 | 0.3049 | 0.3049 | 9 | 0.7419 | prior_season_only | NOT_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_epa_per_dropback | 0.0378 | 0.0308 | 0.1280 | 17 | 1029 | 0.0355 | 0.0373 | 0.0373 | 18 | 0.4516 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.pass_success_rate | 0.4770 | 0.4521 | 0.0418 | 17 | 1029 | 0.4690 | 0.4044 | 0.4044 | 9 | 0.7419 | prior_season_only | UNVALIDATED_RANK_PERSISTENT | 0.0000 |
| team_offense.proe | -0.0777 | -0.0477 | 0.0349 | 17 | 1029 | -0.0720 | -0.6959 | -0.0000 | — | — | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |
| team_offense.rush_epa_per_play | -0.0388 | -0.0806 | 0.0754 | 17 | 1029 | -0.0591 | 0.2855 | 0.2855 | 11 | 0.6774 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.rush_success_rate | 0.4279 | 0.4004 | 0.0385 | 17 | 1029 | 0.4165 | 0.4187 | 0.4187 | 10 | 0.7097 | prior_season_only | RANK_PERSISTENT | 0.0000 |
| team_offense.success_rate | 0.4645 | 0.4370 | 0.0337 | 17 | 1029 | 0.4593 | 0.6616 | 0.6616 | 9 | 0.7419 | prior_season_only | VALIDATED_PERSISTENCE | 0.0000 |

