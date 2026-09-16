# Team Profiles — 2026 (through Week 1)

> These indices are **transparent research indices**, not ratings, probabilities, or predictions of game outcomes. Each is an equal-weight mean of its member metrics' oriented, shrunk z-scores (reference-SD units). The member metrics are shown alongside every index. This project does not model game winners, scores, or spreads.

Every profile shows the domain indices AND the underlying per-metric numbers (raw value, league reference mean/SD, sample size, shrunk value, percentile, confidence). Full detail: `outputs/team_strength/team_metrics_weekly.parquet`.

## ARI
Record: 1-0-0 · Points for/against: 26/14 · Point differential: 12 · Data confidence: low
Strongest area: **offense_overall** (0.219) · Weakest area: **special_teams** (-0.231)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.095 | 10 | 0.996 | 0.996 | low |
| pass_rush | Pass-Rush Strength Index | 0.017 | 13 | 0.781 | 0.781 | low |
| passing_defense | Pass-Defense Strength Index | 0.120 | 7 | 0.999 | 0.999 | low |
| rushing_defense | Run-Defense Strength Index | 0.149 | 7 | 0.610 | 0.610 | low |
| offense_overall | Offensive Strength Index | 0.219 | 9 | 0.326 | 0.326 | low |
| pass_protection | Pass-Protection Strength Index | 0.149 | 7 | 0.673 | 0.673 | low |
| passing_offense | Passing-Offense Strength Index | 0.143 | 8 | 0.295 | 0.295 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.014 | 18 | 0.474 | 0.474 | low |
| special_teams | Special-Teams Strength Index | -0.231 | 30 | 0.209 | 0.209 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1282 | 0.1450 | 0.0327 | 1 | 39 | 0.1431 | -0.0570 | 0.0570 | 13 | 0.5968 | low | UNVALIDATED_RANK_PERSISTENT | -0.0210 |
| pass_protection.rush_stuffed_rate_approx | 0.1667 | 0.2045 | 0.0323 | 1 | 39 | 0.2023 | -0.0689 | 0.0689 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0226 |
| pass_protection.sack_rate_allowed | 0.0256 | 0.0664 | 0.0188 | 1 | 39 | 0.0619 | -0.2412 | 0.2412 | 7 | 0.8065 | low | UNVALIDATED_RANK_PERSISTENT | -0.0132 |
| pass_rush.qb_hit_rate_generated | 0.1143 | 0.1442 | 0.0234 | 1 | 35 | 0.1424 | -0.0751 | -0.0751 | 24 | 0.2581 | low | RANK_PERSISTENT | 0.0152 |
| pass_rush.sack_rate_generated | 0.0857 | 0.0660 | 0.0121 | 1 | 35 | 0.0674 | 0.1088 | 0.1088 | 9 | 0.7419 | low | NOT_RANK_PERSISTENT | 0.0110 |
| special_teams.fg_pct | 0.8000 | 0.8507 | 0.0691 | 1 | 13 | 0.8477 | -0.0432 | -0.0432 | 21 | 0.2593 | low | NOT_RANK_PERSISTENT | 0.0450 |
| special_teams.st_epa_per_play | -0.3020 | 0.0622 | 0.0928 | 1 | 13 | 0.0408 | -0.2308 | -0.2308 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0194 |
| team_defense.early_down_epa_per_play | -0.0516 | -0.0013 | 0.0639 | 1 | 55 | -0.0043 | -0.0463 | 0.0463 | 13 | 0.6129 | low | RANK_PERSISTENT | -0.0699 |
| team_defense.epa_per_play | -0.1668 | 0.0046 | 0.0677 | 1 | 55 | -0.0055 | -0.1488 | 0.1488 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0539 |
| team_defense.explosive_pass_rate | 0.0571 | 0.0797 | 0.0112 | 1 | 55 | 0.0782 | -0.1340 | 0.1340 | 13 | 0.6129 | low | NOT_RANK_PERSISTENT | -0.0038 |
| team_defense.explosive_rush_rate | 0.0625 | 0.1000 | 0.0206 | 1 | 55 | 0.0978 | -0.1070 | 0.1070 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0147 |
| team_defense.pass_epa_per_dropback | -0.1907 | 0.0361 | 0.0949 | 1 | 55 | 0.0228 | -0.1406 | 0.1406 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0799 |
| team_defense.pass_success_rate | 0.4000 | 0.4536 | 0.0320 | 1 | 55 | 0.4505 | -0.0985 | 0.0985 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0370 |
| team_defense.rush_epa_per_play | -0.3604 | -0.0760 | 0.0649 | 1 | 55 | -0.0950 | -0.2920 | 0.2920 | 4 | 0.9032 | low | NOT_RANK_PERSISTENT | -0.0399 |
| team_defense.rush_success_rate | 0.3750 | 0.4020 | 0.0330 | 1 | 55 | 0.4004 | -0.0481 | 0.0481 | 11 | 0.6774 | low | RANK_PERSISTENT | -0.0166 |
| team_defense.success_rate | 0.4000 | 0.4384 | 0.0255 | 1 | 55 | 0.4361 | -0.0887 | 0.0887 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0279 |
| team_offense.early_down_epa_per_play | 0.1342 | -0.0054 | 0.0784 | 1 | 72 | 0.0101 | 0.1979 | 0.1979 | 9 | 0.7419 | low | UNVALIDATED_RANK_PERSISTENT | 0.0197 |
| team_offense.epa_per_play | 0.1391 | -0.0001 | 0.0921 | 1 | 72 | 0.0153 | 0.1681 | 0.1681 | 8 | 0.7742 | low | VALIDATED_PERSISTENCE | 0.0247 |
| team_offense.explosive_pass_rate | 0.0513 | 0.0796 | 0.0177 | 1 | 72 | 0.0779 | -0.0939 | -0.0939 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0054 |
| team_offense.explosive_rush_rate | 0.0667 | 0.0990 | 0.0195 | 1 | 72 | 0.0971 | -0.0974 | -0.0974 | 22 | 0.2903 | low | NOT_RANK_PERSISTENT | 0.0112 |
| team_offense.pass_epa_per_dropback | 0.2891 | 0.0308 | 0.1280 | 1 | 72 | 0.0595 | 0.2243 | 0.2243 | 9 | 0.7419 | low | UNVALIDATED_RANK_PERSISTENT | 0.0335 |
| team_offense.pass_success_rate | 0.5641 | 0.4521 | 0.0418 | 1 | 72 | 0.4645 | 0.2976 | 0.2976 | 5 | 0.8710 | low | UNVALIDATED_RANK_PERSISTENT | 0.0132 |
| team_offense.proe | -0.0466 | -0.0477 | 0.0349 | 1 | 72 | -0.0475 | 0.0066 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0413 |
| team_offense.rush_epa_per_play | -0.0443 | -0.0806 | 0.0754 | 1 | 72 | -0.0785 | 0.0283 | 0.0283 | 11 | 0.6774 | low | RANK_PERSISTENT | 0.0339 |
| team_offense.rush_success_rate | 0.4000 | 0.4004 | 0.0385 | 1 | 72 | 0.4003 | -0.0007 | -0.0007 | 18 | 0.4032 | low | RANK_PERSISTENT | 0.0192 |
| team_offense.success_rate | 0.4861 | 0.4370 | 0.0337 | 1 | 72 | 0.4468 | 0.2914 | 0.2914 | 6 | 0.8387 | low | VALIDATED_PERSISTENCE | 0.0155 |

## ATL
Record: 0-1-0 · Points for/against: 13/20 · Point differential: -7 · Data confidence: low
Strongest area: **passing_defense** (0.208) · Weakest area: **offense_overall** (-0.406)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.196 | 3 | 0.346 | 0.346 | low |
| pass_rush | Pass-Rush Strength Index | -0.060 | 21 | -0.630 | -0.630 | low |
| passing_defense | Pass-Defense Strength Index | 0.208 | 3 | 0.109 | 0.109 | low |
| rushing_defense | Run-Defense Strength Index | 0.176 | 4 | 0.377 | 0.377 | low |
| offense_overall | Offensive Strength Index | -0.406 | 32 | -0.660 | -0.660 | low |
| pass_protection | Pass-Protection Strength Index | -0.339 | 29 | -0.939 | -0.939 | low |
| passing_offense | Passing-Offense Strength Index | -0.273 | 31 | -0.247 | -0.247 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.025 | 16 | -0.107 | -0.107 | low |
| special_teams | Special-Teams Strength Index | -0.129 | 28 | 0.124 | 0.124 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1923 | 0.1450 | 0.0327 | 1 | 26 | 0.1503 | 0.1607 | -0.1607 | 24 | 0.2581 | low | UNVALIDATED_RANK_PERSISTENT | 0.0187 |
| pass_protection.rush_stuffed_rate_approx | 0.2500 | 0.2045 | 0.0323 | 1 | 26 | 0.2072 | 0.0827 | -0.0827 | 22 | 0.3065 | low | RANK_PERSISTENT | 0.0119 |
| pass_protection.sack_rate_allowed | 0.1538 | 0.0664 | 0.0188 | 1 | 26 | 0.0761 | 0.5173 | -0.5173 | 31 | 0.0323 | low | UNVALIDATED_RANK_PERSISTENT | 0.0245 |
| pass_rush.qb_hit_rate_generated | 0.1395 | 0.1442 | 0.0234 | 1 | 43 | 0.1439 | -0.0117 | -0.0117 | 18 | 0.4516 | low | RANK_PERSISTENT | -0.0002 |
| pass_rush.sack_rate_generated | 0.0465 | 0.0660 | 0.0121 | 1 | 43 | 0.0647 | -0.1081 | -0.1081 | 21 | 0.3387 | low | NOT_RANK_PERSISTENT | -0.0151 |
| special_teams.fg_pct | 0.5000 | 0.8507 | 0.0691 | 1 | 16 | 0.8301 | -0.2984 | -0.2984 | 26 | 0.0370 | low | NOT_RANK_PERSISTENT | -0.0051 |
| special_teams.st_epa_per_play | -0.1421 | 0.0622 | 0.0928 | 1 | 16 | 0.0502 | -0.1295 | -0.1295 | 28 | 0.1290 | low | RANK_PERSISTENT | 0.0115 |
| team_defense.early_down_epa_per_play | -0.1460 | -0.0013 | 0.0639 | 1 | 65 | -0.0098 | -0.1333 | 0.1333 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0177 |
| team_defense.epa_per_play | -0.2515 | 0.0046 | 0.0677 | 1 | 65 | -0.0105 | -0.2223 | 0.2223 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0170 |
| team_defense.explosive_pass_rate | 0.0698 | 0.0797 | 0.0112 | 1 | 65 | 0.0790 | -0.0589 | 0.0589 | 17 | 0.4839 | low | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.0556 | 0.1000 | 0.0206 | 1 | 65 | 0.0973 | -0.1268 | 0.1268 | 6 | 0.8387 | low | RANK_PERSISTENT | 0.0031 |
| team_defense.pass_epa_per_dropback | -0.3239 | 0.0361 | 0.0949 | 1 | 65 | 0.0149 | -0.2232 | 0.2232 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0036 |
| team_defense.pass_success_rate | 0.3488 | 0.4536 | 0.0320 | 1 | 65 | 0.4475 | -0.1924 | 0.1924 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0057 |
| team_defense.rush_epa_per_play | -0.2522 | -0.0760 | 0.0649 | 1 | 65 | -0.0877 | -0.1809 | 0.1809 | 6 | 0.8387 | low | NOT_RANK_PERSISTENT | -0.0383 |
| team_defense.rush_success_rate | 0.2778 | 0.4020 | 0.0330 | 1 | 65 | 0.3947 | -0.2216 | 0.2216 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0229 |
| team_defense.success_rate | 0.3385 | 0.4384 | 0.0255 | 1 | 65 | 0.4325 | -0.2309 | 0.2309 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0130 |
| team_offense.early_down_epa_per_play | -0.2658 | -0.0054 | 0.0784 | 1 | 60 | -0.0343 | -0.3691 | -0.3691 | 31 | 0.0323 | low | UNVALIDATED_RANK_PERSISTENT | -0.0787 |
| team_offense.epa_per_play | -0.3577 | -0.0001 | 0.0921 | 1 | 60 | -0.0399 | -0.4315 | -0.4315 | 31 | 0.0323 | low | VALIDATED_PERSISTENCE | -0.0345 |
| team_offense.explosive_pass_rate | 0.1154 | 0.0796 | 0.0177 | 1 | 60 | 0.0817 | 0.1188 | 0.1188 | 7 | 0.8065 | low | RANK_PERSISTENT | 0.0016 |
| team_offense.explosive_rush_rate | 0.0938 | 0.0990 | 0.0195 | 1 | 60 | 0.0987 | -0.0159 | -0.0159 | 15 | 0.5484 | low | NOT_RANK_PERSISTENT | -0.0074 |
| team_offense.pass_epa_per_dropback | -0.6063 | 0.0308 | 0.1280 | 1 | 60 | -0.0400 | -0.5532 | -0.5532 | 32 | 0.0000 | low | UNVALIDATED_RANK_PERSISTENT | -0.0554 |
| team_offense.pass_success_rate | 0.3077 | 0.4521 | 0.0418 | 1 | 60 | 0.4360 | -0.3836 | -0.3836 | 32 | 0.0000 | low | UNVALIDATED_RANK_PERSISTENT | -0.0166 |
| team_offense.proe | -0.2039 | -0.0477 | 0.0349 | 1 | 60 | -0.0790 | -0.8964 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0014 |
| team_offense.rush_epa_per_play | -0.1126 | -0.0806 | 0.0754 | 1 | 60 | -0.0825 | -0.0250 | -0.0250 | 20 | 0.3871 | low | RANK_PERSISTENT | -0.0057 |
| team_offense.rush_success_rate | 0.4375 | 0.4004 | 0.0385 | 1 | 60 | 0.4032 | 0.0741 | 0.0741 | 11 | 0.6613 | low | RANK_PERSISTENT | -0.0053 |
| team_offense.success_rate | 0.3667 | 0.4370 | 0.0337 | 1 | 60 | 0.4229 | -0.4167 | -0.4167 | 28 | 0.1290 | low | VALIDATED_PERSISTENCE | -0.0203 |

## BAL
Record: 1-0-0 · Points for/against: 41/23 · Point differential: 18 · Data confidence: low
Strongest area: **offense_overall** (0.278) · Weakest area: **rushing_defense** (-0.264)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.133 | 5 | 0.309 | 0.309 | low |
| pass_rush | Pass-Rush Strength Index | 0.132 | 7 | 0.708 | 0.708 | low |
| passing_defense | Pass-Defense Strength Index | 0.213 | 2 | 0.423 | 0.423 | low |
| rushing_defense | Run-Defense Strength Index | -0.264 | 32 | -0.356 | -0.356 | low |
| offense_overall | Offensive Strength Index | 0.278 | 5 | 0.013 | 0.013 | low |
| pass_protection | Pass-Protection Strength Index | 0.063 | 13 | 0.702 | 0.702 | low |
| passing_offense | Passing-Offense Strength Index | 0.239 | 5 | 0.131 | 0.131 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.108 | 7 | -0.437 | -0.437 | low |
| special_teams | Special-Teams Strength Index | 0.164 | 6 | -0.255 | -0.255 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1034 | 0.1450 | 0.0327 | 1 | 29 | 0.1404 | -0.1411 | 0.1411 | 8 | 0.7742 | low | UNVALIDATED_RANK_PERSISTENT | -0.0187 |
| pass_protection.rush_stuffed_rate_approx | 0.0938 | 0.2045 | 0.0323 | 1 | 29 | 0.1980 | -0.2014 | 0.2014 | 4 | 0.9032 | low | RANK_PERSISTENT | 0.0072 |
| pass_protection.sack_rate_allowed | 0.0690 | 0.0664 | 0.0188 | 1 | 29 | 0.0667 | 0.0151 | -0.0151 | 18 | 0.4516 | low | UNVALIDATED_RANK_PERSISTENT | -0.0156 |
| pass_rush.qb_hit_rate_generated | 0.2647 | 0.1442 | 0.0234 | 1 | 34 | 0.1513 | 0.3030 | 0.3030 | 4 | 0.9032 | low | RANK_PERSISTENT | 0.0099 |
| pass_rush.sack_rate_generated | 0.0588 | 0.0660 | 0.0121 | 1 | 34 | 0.0656 | -0.0400 | -0.0400 | 19 | 0.4194 | low | NOT_RANK_PERSISTENT | 0.0120 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 15 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0075 |
| special_teams.st_epa_per_play | 0.3214 | 0.0622 | 0.0928 | 1 | 15 | 0.0775 | 0.1642 | 0.1642 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0236 |
| team_defense.early_down_epa_per_play | -0.1866 | -0.0013 | 0.0639 | 1 | 54 | -0.0122 | -0.1706 | 0.1706 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0294 |
| team_defense.epa_per_play | -0.2246 | 0.0046 | 0.0677 | 1 | 54 | -0.0089 | -0.1990 | 0.1990 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0240 |
| team_defense.explosive_pass_rate | 0.0588 | 0.0797 | 0.0112 | 1 | 54 | 0.0783 | -0.1240 | 0.1240 | 14 | 0.5806 | low | NOT_RANK_PERSISTENT | -0.0084 |
| team_defense.explosive_rush_rate | 0.2632 | 0.1000 | 0.0206 | 1 | 54 | 0.1096 | 0.4661 | -0.4661 | 32 | 0.0000 | low | RANK_PERSISTENT | 0.0084 |
| team_defense.pass_epa_per_dropback | -0.4408 | 0.0361 | 0.0949 | 1 | 54 | 0.0081 | -0.2957 | 0.2957 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0566 |
| team_defense.pass_success_rate | 0.3824 | 0.4536 | 0.0320 | 1 | 54 | 0.4494 | -0.1309 | 0.1309 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0080 |
| team_defense.rush_epa_per_play | 0.1160 | -0.0760 | 0.0649 | 1 | 54 | -0.0632 | 0.1970 | -0.1970 | 28 | 0.1290 | low | NOT_RANK_PERSISTENT | 0.0341 |
| team_defense.rush_success_rate | 0.4737 | 0.4020 | 0.0330 | 1 | 54 | 0.4062 | 0.1279 | -0.1279 | 26 | 0.1935 | low | RANK_PERSISTENT | 0.0044 |
| team_defense.success_rate | 0.4259 | 0.4384 | 0.0255 | 1 | 54 | 0.4377 | -0.0288 | 0.0288 | 13 | 0.6129 | low | RANK_PERSISTENT | -0.0029 |
| team_offense.early_down_epa_per_play | 0.2714 | -0.0054 | 0.0784 | 1 | 64 | 0.0254 | 0.3924 | 0.3924 | 4 | 0.9032 | low | UNVALIDATED_RANK_PERSISTENT | 0.0063 |
| team_offense.epa_per_play | 0.2087 | -0.0001 | 0.0921 | 1 | 64 | 0.0231 | 0.2520 | 0.2520 | 6 | 0.8387 | low | VALIDATED_PERSISTENCE | -0.0020 |
| team_offense.explosive_pass_rate | 0.1034 | 0.0796 | 0.0177 | 1 | 64 | 0.0810 | 0.0792 | 0.0792 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0018 |
| team_offense.explosive_rush_rate | 0.1250 | 0.0990 | 0.0195 | 1 | 64 | 0.1005 | 0.0782 | 0.0782 | 7 | 0.7903 | low | NOT_RANK_PERSISTENT | -0.0134 |
| team_offense.pass_epa_per_dropback | 0.4595 | 0.0308 | 0.1280 | 1 | 64 | 0.0784 | 0.3722 | 0.3722 | 5 | 0.8710 | low | UNVALIDATED_RANK_PERSISTENT | 0.0566 |
| team_offense.pass_success_rate | 0.5517 | 0.4521 | 0.0418 | 1 | 64 | 0.4632 | 0.2647 | 0.2647 | 6 | 0.8387 | low | UNVALIDATED_RANK_PERSISTENT | 0.0022 |
| team_offense.proe | -0.1051 | -0.0477 | 0.0349 | 1 | 64 | -0.0592 | -0.3294 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0398 |
| team_offense.rush_epa_per_play | 0.1015 | -0.0806 | 0.0754 | 1 | 64 | -0.0699 | 0.1421 | 0.1421 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0505 |
| team_offense.rush_success_rate | 0.4375 | 0.4004 | 0.0385 | 1 | 64 | 0.4032 | 0.0741 | 0.0741 | 11 | 0.6613 | low | RANK_PERSISTENT | -0.0079 |
| team_offense.success_rate | 0.4688 | 0.4370 | 0.0337 | 1 | 64 | 0.4433 | 0.1885 | 0.1885 | 12 | 0.6452 | low | VALIDATED_PERSISTENCE | -0.0006 |

## BUF
Record: 1-0-0 · Points for/against: 36/31 · Point differential: 5 · Data confidence: low
Strongest area: **passing_offense** (0.252) · Weakest area: **rushing_offense** (-0.156)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.083 | 22 | -0.284 | -0.284 | low |
| pass_rush | Pass-Rush Strength Index | 0.103 | 10 | -0.139 | -0.139 | low |
| passing_defense | Pass-Defense Strength Index | -0.062 | 20 | -0.622 | -0.622 | low |
| rushing_defense | Run-Defense Strength Index | -0.044 | 21 | 0.734 | 0.734 | low |
| offense_overall | Offensive Strength Index | 0.229 | 8 | -0.868 | -0.868 | low |
| pass_protection | Pass-Protection Strength Index | 0.099 | 10 | -0.125 | -0.125 | low |
| passing_offense | Passing-Offense Strength Index | 0.252 | 4 | -0.538 | -0.538 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.156 | 25 | -1.062 | -1.062 | low |
| special_teams | Special-Teams Strength Index | 0.161 | 7 | -0.044 | -0.044 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0938 | 0.1450 | 0.0327 | 1 | 32 | 0.1393 | -0.1740 | 0.1740 | 7 | 0.8065 | low | UNVALIDATED_RANK_PERSISTENT | 0.0114 |
| pass_protection.rush_stuffed_rate_approx | 0.1579 | 0.2045 | 0.0323 | 1 | 32 | 0.2018 | -0.0848 | 0.0848 | 7 | 0.7903 | low | RANK_PERSISTENT | 0.0208 |
| pass_protection.sack_rate_allowed | 0.0625 | 0.0664 | 0.0188 | 1 | 32 | 0.0660 | -0.0231 | 0.0231 | 17 | 0.4839 | low | UNVALIDATED_RANK_PERSISTENT | -0.0019 |
| pass_rush.qb_hit_rate_generated | 0.2143 | 0.1442 | 0.0234 | 1 | 42 | 0.1483 | 0.1762 | 0.1762 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0052 |
| pass_rush.sack_rate_generated | 0.0714 | 0.0660 | 0.0121 | 1 | 42 | 0.0664 | 0.0298 | 0.0298 | 13 | 0.5968 | low | NOT_RANK_PERSISTENT | -0.0007 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 14 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0191 |
| special_teams.st_epa_per_play | 0.3164 | 0.0622 | 0.0928 | 1 | 14 | 0.0772 | 0.1610 | 0.1610 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0041 |
| team_defense.early_down_epa_per_play | 0.1003 | -0.0013 | 0.0639 | 1 | 79 | 0.0047 | 0.0935 | -0.0935 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0287 |
| team_defense.epa_per_play | 0.0713 | 0.0046 | 0.0677 | 1 | 79 | 0.0085 | 0.0579 | -0.0579 | 20 | 0.3871 | low | RANK_PERSISTENT | 0.0098 |
| team_defense.explosive_pass_rate | 0.0952 | 0.0797 | 0.0112 | 1 | 79 | 0.0807 | 0.0924 | -0.0924 | 20 | 0.3871 | low | NOT_RANK_PERSISTENT | 0.0054 |
| team_defense.explosive_rush_rate | 0.0968 | 0.1000 | 0.0206 | 1 | 79 | 0.0998 | -0.0091 | 0.0091 | 20 | 0.3871 | low | RANK_PERSISTENT | -0.0165 |
| team_defense.pass_epa_per_dropback | 0.0974 | 0.0361 | 0.0949 | 1 | 79 | 0.0397 | 0.0380 | -0.0380 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0569 |
| team_defense.pass_success_rate | 0.5000 | 0.4536 | 0.0320 | 1 | 79 | 0.4564 | 0.0851 | -0.0851 | 22 | 0.2903 | low | RANK_PERSISTENT | 0.0206 |
| team_defense.rush_epa_per_play | 0.0303 | -0.0760 | 0.0649 | 1 | 79 | -0.0689 | 0.1091 | -0.1091 | 24 | 0.2581 | low | NOT_RANK_PERSISTENT | -0.0615 |
| team_defense.rush_success_rate | 0.4194 | 0.4020 | 0.0330 | 1 | 79 | 0.4030 | 0.0310 | -0.0310 | 18 | 0.4516 | low | RANK_PERSISTENT | -0.0150 |
| team_defense.success_rate | 0.4810 | 0.4384 | 0.0255 | 1 | 79 | 0.4409 | 0.0985 | -0.0985 | 24 | 0.2581 | low | RANK_PERSISTENT | 0.0066 |
| team_offense.early_down_epa_per_play | 0.3013 | -0.0054 | 0.0784 | 1 | 55 | 0.0287 | 0.4347 | 0.4347 | 3 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0442 |
| team_offense.epa_per_play | 0.3002 | -0.0001 | 0.0921 | 1 | 55 | 0.0332 | 0.3624 | 0.3624 | 4 | 0.9032 | low | VALIDATED_PERSISTENCE | -0.0654 |
| team_offense.explosive_pass_rate | 0.1562 | 0.0796 | 0.0177 | 1 | 55 | 0.0841 | 0.2543 | 0.2543 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0083 |
| team_offense.explosive_rush_rate | 0.1053 | 0.0990 | 0.0195 | 1 | 55 | 0.0994 | 0.0188 | 0.0188 | 12 | 0.6452 | low | NOT_RANK_PERSISTENT | -0.0081 |
| team_offense.pass_epa_per_dropback | 0.5582 | 0.0308 | 0.1280 | 1 | 55 | 0.0894 | 0.4579 | 0.4579 | 3 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0596 |
| team_offense.pass_success_rate | 0.4688 | 0.4521 | 0.0418 | 1 | 55 | 0.4539 | 0.0443 | 0.0443 | 15 | 0.5484 | low | UNVALIDATED_RANK_PERSISTENT | -0.0284 |
| team_offense.proe | -0.0361 | -0.0477 | 0.0349 | 1 | 55 | -0.0454 | 0.0664 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0113 |
| team_offense.rush_epa_per_play | -0.2628 | -0.0806 | 0.0754 | 1 | 55 | -0.0913 | -0.1422 | -0.1422 | 28 | 0.1290 | low | RANK_PERSISTENT | -0.0721 |
| team_offense.rush_success_rate | 0.3158 | 0.4004 | 0.0385 | 1 | 55 | 0.3939 | -0.1689 | -0.1689 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0450 |
| team_offense.success_rate | 0.4182 | 0.4370 | 0.0337 | 1 | 55 | 0.4332 | -0.1113 | -0.1113 | 21 | 0.3548 | low | VALIDATED_PERSISTENCE | -0.0448 |

## CAR
Record: 0-1-0 · Points for/against: 37/59 · Point differential: -22 · Data confidence: low
Strongest area: **offense_overall** (0.207) · Weakest area: **passing_defense** (-0.319)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.276 | 30 | -0.140 | -0.140 | low |
| pass_rush | Pass-Rush Strength Index | -0.119 | 26 | 0.722 | 0.722 | low |
| passing_defense | Pass-Defense Strength Index | -0.319 | 30 | 0.085 | 0.085 | low |
| rushing_defense | Run-Defense Strength Index | -0.087 | 24 | -0.062 | -0.062 | low |
| offense_overall | Offensive Strength Index | 0.207 | 10 | 0.387 | 0.387 | low |
| pass_protection | Pass-Protection Strength Index | 0.108 | 8 | 0.023 | 0.023 | low |
| passing_offense | Passing-Offense Strength Index | 0.154 | 7 | 0.387 | 0.387 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.044 | 15 | -0.096 | -0.096 | low |
| special_teams | Special-Teams Strength Index | -0.055 | 24 | -0.366 | -0.366 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1163 | 0.1450 | 0.0327 | 1 | 43 | 0.1418 | -0.0975 | 0.0975 | 10 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | -0.0051 |
| pass_protection.rush_stuffed_rate_approx | 0.1818 | 0.2045 | 0.0323 | 1 | 43 | 0.2032 | -0.0413 | 0.0413 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0213 |
| pass_protection.sack_rate_allowed | 0.0465 | 0.0664 | 0.0188 | 1 | 43 | 0.0642 | -0.1177 | 0.1177 | 11 | 0.6613 | low | UNVALIDATED_RANK_PERSISTENT | 0.0021 |
| pass_rush.qb_hit_rate_generated | 0.0789 | 0.1442 | 0.0234 | 1 | 38 | 0.1403 | -0.1639 | -0.1639 | 28 | 0.1290 | low | RANK_PERSISTENT | 0.0219 |
| pass_rush.sack_rate_generated | 0.0526 | 0.0660 | 0.0121 | 1 | 38 | 0.0652 | -0.0742 | -0.0742 | 20 | 0.3871 | low | NOT_RANK_PERSISTENT | 0.0061 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 19 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0207 |
| special_teams.st_epa_per_play | -0.0245 | 0.0622 | 0.0928 | 1 | 19 | 0.0571 | -0.0549 | -0.0549 | 24 | 0.2581 | low | RANK_PERSISTENT | -0.0340 |
| team_defense.early_down_epa_per_play | 0.3233 | -0.0013 | 0.0639 | 1 | 75 | 0.0178 | 0.2989 | -0.2989 | 31 | 0.0323 | low | RANK_PERSISTENT | 0.0243 |
| team_defense.epa_per_play | 0.3605 | 0.0046 | 0.0677 | 1 | 75 | 0.0255 | 0.3090 | -0.3090 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0076 |
| team_defense.explosive_pass_rate | 0.1053 | 0.0797 | 0.0112 | 1 | 75 | 0.0814 | 0.1520 | -0.1520 | 24 | 0.2581 | low | NOT_RANK_PERSISTENT | 0.0045 |
| team_defense.explosive_rush_rate | 0.1143 | 0.1000 | 0.0206 | 1 | 75 | 0.1008 | 0.0409 | -0.0409 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0054 |
| team_defense.pass_epa_per_dropback | 0.5378 | 0.0361 | 0.0949 | 1 | 75 | 0.0656 | 0.3111 | -0.3111 | 29 | 0.0968 | low | RANK_PERSISTENT | -0.0131 |
| team_defense.pass_success_rate | 0.6316 | 0.4536 | 0.0320 | 1 | 75 | 0.4641 | 0.3267 | -0.3267 | 30 | 0.0645 | low | RANK_PERSISTENT | -0.0011 |
| team_defense.rush_epa_per_play | 0.1428 | -0.0760 | 0.0649 | 1 | 75 | -0.0614 | 0.2246 | -0.2246 | 31 | 0.0323 | low | NOT_RANK_PERSISTENT | -0.0135 |
| team_defense.rush_success_rate | 0.4000 | 0.4020 | 0.0330 | 1 | 75 | 0.4019 | -0.0035 | 0.0035 | 12 | 0.5968 | low | RANK_PERSISTENT | 0.0043 |
| team_defense.success_rate | 0.5333 | 0.4384 | 0.0255 | 1 | 75 | 0.4440 | 0.2194 | -0.2194 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0038 |
| team_offense.early_down_epa_per_play | 0.1826 | -0.0054 | 0.0784 | 1 | 68 | 0.0155 | 0.2664 | 0.2664 | 7 | 0.8065 | low | UNVALIDATED_RANK_PERSISTENT | 0.0485 |
| team_offense.epa_per_play | 0.1296 | -0.0001 | 0.0921 | 1 | 68 | 0.0143 | 0.1566 | 0.1566 | 9 | 0.7419 | low | VALIDATED_PERSISTENCE | 0.0311 |
| team_offense.explosive_pass_rate | 0.1163 | 0.0796 | 0.0177 | 1 | 68 | 0.0817 | 0.1218 | 0.1218 | 6 | 0.8387 | low | RANK_PERSISTENT | 0.0051 |
| team_offense.explosive_rush_rate | 0.0909 | 0.0990 | 0.0195 | 1 | 68 | 0.0985 | -0.0244 | -0.0244 | 16 | 0.5000 | low | NOT_RANK_PERSISTENT | 0.0036 |
| team_offense.pass_epa_per_dropback | 0.3118 | 0.0308 | 0.1280 | 1 | 68 | 0.0620 | 0.2440 | 0.2440 | 8 | 0.7742 | low | UNVALIDATED_RANK_PERSISTENT | 0.0703 |
| team_offense.pass_success_rate | 0.4884 | 0.4521 | 0.0418 | 1 | 68 | 0.4561 | 0.0964 | 0.0964 | 12 | 0.6452 | low | UNVALIDATED_RANK_PERSISTENT | 0.0135 |
| team_offense.proe | -0.0133 | -0.0477 | 0.0349 | 1 | 68 | -0.0408 | 0.1973 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0387 |
| team_offense.rush_epa_per_play | -0.1062 | -0.0806 | 0.0754 | 1 | 68 | -0.0821 | -0.0200 | -0.0200 | 19 | 0.4194 | low | RANK_PERSISTENT | -0.0059 |
| team_offense.rush_success_rate | 0.4545 | 0.4004 | 0.0385 | 1 | 68 | 0.4045 | 0.1082 | 0.1082 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0043 |
| team_offense.success_rate | 0.4706 | 0.4370 | 0.0337 | 1 | 68 | 0.4437 | 0.1994 | 0.1994 | 11 | 0.6774 | low | VALIDATED_PERSISTENCE | 0.0069 |

## CHI
Record: 1-0-0 · Points for/against: 59/37 · Point differential: 22 · Data confidence: low
Strongest area: **offense_overall** (0.491) · Weakest area: **defense_overall** (-0.117)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.117 | 24 | 0.374 | 0.374 | low |
| pass_rush | Pass-Rush Strength Index | -0.089 | 24 | 0.168 | 0.168 | low |
| passing_defense | Pass-Defense Strength Index | -0.117 | 24 | 0.159 | 0.159 | low |
| rushing_defense | Run-Defense Strength Index | -0.012 | 17 | 0.408 | 0.408 | low |
| offense_overall | Offensive Strength Index | 0.491 | 3 | -0.084 | -0.084 | low |
| pass_protection | Pass-Protection Strength Index | 0.153 | 6 | -0.789 | -0.789 | low |
| passing_offense | Passing-Offense Strength Index | 0.334 | 2 | 0.051 | 0.051 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.087 | 11 | -0.678 | -0.678 | low |
| special_teams | Special-Teams Strength Index | 0.188 | 5 | 0.173 | 0.173 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0789 | 0.1450 | 0.0327 | 1 | 38 | 0.1377 | -0.2243 | 0.2243 | 5 | 0.8710 | low | UNVALIDATED_RANK_PERSISTENT | 0.0201 |
| pass_protection.rush_stuffed_rate_approx | 0.2000 | 0.2045 | 0.0323 | 1 | 38 | 0.2043 | -0.0082 | 0.0082 | 17 | 0.4677 | low | RANK_PERSISTENT | 0.0194 |
| pass_protection.sack_rate_allowed | 0.0526 | 0.0664 | 0.0188 | 1 | 38 | 0.0649 | -0.0815 | 0.0815 | 13 | 0.6129 | low | UNVALIDATED_RANK_PERSISTENT | 0.0181 |
| pass_rush.qb_hit_rate_generated | 0.1163 | 0.1442 | 0.0234 | 1 | 43 | 0.1425 | -0.0701 | -0.0701 | 23 | 0.2903 | low | RANK_PERSISTENT | 0.0030 |
| pass_rush.sack_rate_generated | 0.0465 | 0.0660 | 0.0121 | 1 | 43 | 0.0647 | -0.1081 | -0.1081 | 21 | 0.3387 | low | NOT_RANK_PERSISTENT | 0.0025 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 18 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0111 |
| special_teams.st_epa_per_play | 0.3582 | 0.0622 | 0.0928 | 1 | 18 | 0.0796 | 0.1875 | 0.1875 | 5 | 0.8710 | low | RANK_PERSISTENT | 0.0160 |
| team_defense.early_down_epa_per_play | 0.1826 | -0.0013 | 0.0639 | 1 | 68 | 0.0095 | 0.1693 | -0.1693 | 26 | 0.1935 | low | RANK_PERSISTENT | -0.0262 |
| team_defense.epa_per_play | 0.1296 | 0.0046 | 0.0677 | 1 | 68 | 0.0119 | 0.1086 | -0.1086 | 24 | 0.2581 | low | RANK_PERSISTENT | -0.0082 |
| team_defense.explosive_pass_rate | 0.1163 | 0.0797 | 0.0112 | 1 | 68 | 0.0821 | 0.2175 | -0.2175 | 27 | 0.1613 | low | NOT_RANK_PERSISTENT | -0.0104 |
| team_defense.explosive_rush_rate | 0.0909 | 0.1000 | 0.0206 | 1 | 68 | 0.0994 | -0.0258 | 0.0258 | 16 | 0.5000 | low | RANK_PERSISTENT | -0.0084 |
| team_defense.pass_epa_per_dropback | 0.3118 | 0.0361 | 0.0949 | 1 | 68 | 0.0523 | 0.1709 | -0.1709 | 25 | 0.2258 | low | RANK_PERSISTENT | 0.0087 |
| team_defense.pass_success_rate | 0.4884 | 0.4536 | 0.0320 | 1 | 68 | 0.4557 | 0.0638 | -0.0638 | 21 | 0.3548 | low | RANK_PERSISTENT | -0.0131 |
| team_defense.rush_epa_per_play | -0.1062 | -0.0760 | 0.0649 | 1 | 68 | -0.0780 | -0.0310 | 0.0310 | 14 | 0.5806 | low | NOT_RANK_PERSISTENT | -0.0205 |
| team_defense.rush_success_rate | 0.4545 | 0.4020 | 0.0330 | 1 | 68 | 0.4051 | 0.0938 | -0.0938 | 23 | 0.2903 | low | RANK_PERSISTENT | -0.0165 |
| team_defense.success_rate | 0.4706 | 0.4384 | 0.0255 | 1 | 68 | 0.4403 | 0.0744 | -0.0744 | 22 | 0.3226 | low | RANK_PERSISTENT | -0.0150 |
| team_offense.early_down_epa_per_play | 0.3233 | -0.0054 | 0.0784 | 1 | 75 | 0.0311 | 0.4658 | 0.4658 | 2 | 0.9677 | low | UNVALIDATED_RANK_PERSISTENT | -0.0175 |
| team_offense.epa_per_play | 0.3605 | -0.0001 | 0.0921 | 1 | 75 | 0.0399 | 0.4352 | 0.4352 | 2 | 0.9677 | low | VALIDATED_PERSISTENCE | -0.0115 |
| team_offense.explosive_pass_rate | 0.1053 | 0.0796 | 0.0177 | 1 | 75 | 0.0811 | 0.0852 | 0.0852 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0058 |
| team_offense.explosive_rush_rate | 0.1143 | 0.0990 | 0.0195 | 1 | 75 | 0.0999 | 0.0460 | 0.0460 | 11 | 0.6774 | low | NOT_RANK_PERSISTENT | -0.0078 |
| team_offense.pass_epa_per_dropback | 0.5378 | 0.0308 | 0.1280 | 1 | 75 | 0.0871 | 0.4402 | 0.4402 | 4 | 0.9032 | low | UNVALIDATED_RANK_PERSISTENT | -0.0041 |
| team_offense.pass_success_rate | 0.6316 | 0.4521 | 0.0418 | 1 | 75 | 0.4720 | 0.4769 | 0.4769 | 3 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | 0.0214 |
| team_offense.proe | -0.0437 | -0.0477 | 0.0349 | 1 | 75 | -0.0469 | 0.0227 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0152 |
| team_offense.rush_epa_per_play | 0.1428 | -0.0806 | 0.0754 | 1 | 75 | -0.0675 | 0.1744 | 0.1744 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0319 |
| team_offense.rush_success_rate | 0.4000 | 0.4004 | 0.0385 | 1 | 75 | 0.4003 | -0.0007 | -0.0007 | 18 | 0.4032 | low | RANK_PERSISTENT | -0.0360 |
| team_offense.success_rate | 0.5333 | 0.4370 | 0.0337 | 1 | 75 | 0.4562 | 0.5713 | 0.5713 | 4 | 0.9032 | low | VALIDATED_PERSISTENCE | 0.0032 |

## CIN
Record: 1-0-0 · Points for/against: 33/27 · Point differential: 6 · Data confidence: low
Strongest area: **special_teams** (0.214) · Weakest area: **rushing_defense** (-0.068)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.025 | 20 | 0.850 | 0.850 | low |
| pass_rush | Pass-Rush Strength Index | 0.153 | 6 | 0.516 | 0.516 | low |
| passing_defense | Pass-Defense Strength Index | 0.059 | 11 | 0.826 | 0.826 | low |
| rushing_defense | Run-Defense Strength Index | -0.068 | 22 | 0.566 | 0.566 | low |
| offense_overall | Offensive Strength Index | 0.119 | 12 | -0.027 | -0.027 | low |
| pass_protection | Pass-Protection Strength Index | 0.087 | 11 | -0.160 | -0.160 | low |
| passing_offense | Passing-Offense Strength Index | 0.037 | 12 | 0.217 | 0.217 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.050 | 13 | -0.674 | -0.674 | low |
| special_teams | Special-Teams Strength Index | 0.214 | 3 | -0.504 | -0.504 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1622 | 0.1450 | 0.0327 | 1 | 37 | 0.1469 | 0.0583 | -0.0583 | 21 | 0.3548 | low | UNVALIDATED_RANK_PERSISTENT | 0.0015 |
| pass_protection.rush_stuffed_rate_approx | 0.1600 | 0.2045 | 0.0323 | 1 | 37 | 0.2019 | -0.0810 | 0.0810 | 9 | 0.7419 | low | RANK_PERSISTENT | 0.0317 |
| pass_protection.sack_rate_allowed | 0.0270 | 0.0664 | 0.0188 | 1 | 37 | 0.0620 | -0.2330 | 0.2330 | 9 | 0.7419 | low | UNVALIDATED_RANK_PERSISTENT | 0.0051 |
| pass_rush.qb_hit_rate_generated | 0.1667 | 0.1442 | 0.0234 | 1 | 36 | 0.1455 | 0.0565 | 0.0565 | 10 | 0.6935 | low | RANK_PERSISTENT | 0.0094 |
| pass_rush.sack_rate_generated | 0.1111 | 0.0660 | 0.0121 | 1 | 36 | 0.0691 | 0.2493 | 0.2493 | 5 | 0.8710 | low | NOT_RANK_PERSISTENT | 0.0076 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 14 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0129 |
| special_teams.st_epa_per_play | 0.4002 | 0.0622 | 0.0928 | 1 | 14 | 0.0821 | 0.2141 | 0.2141 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0468 |
| team_defense.early_down_epa_per_play | -0.0398 | -0.0013 | 0.0639 | 1 | 56 | -0.0036 | -0.0355 | 0.0355 | 16 | 0.5161 | low | RANK_PERSISTENT | -0.0645 |
| team_defense.epa_per_play | -0.0814 | 0.0046 | 0.0677 | 1 | 56 | -0.0005 | -0.0746 | 0.0746 | 12 | 0.6452 | low | RANK_PERSISTENT | -0.0657 |
| team_defense.explosive_pass_rate | 0.0556 | 0.0797 | 0.0112 | 1 | 56 | 0.0781 | -0.1434 | 0.1434 | 12 | 0.6452 | low | NOT_RANK_PERSISTENT | -0.0121 |
| team_defense.explosive_rush_rate | 0.0588 | 0.1000 | 0.0206 | 1 | 56 | 0.0975 | -0.1175 | 0.1175 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0117 |
| team_defense.pass_epa_per_dropback | -0.2925 | 0.0361 | 0.0949 | 1 | 56 | 0.0168 | -0.2037 | 0.2037 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0928 |
| team_defense.pass_success_rate | 0.5000 | 0.4536 | 0.0320 | 1 | 56 | 0.4564 | 0.0851 | -0.0851 | 22 | 0.2903 | low | RANK_PERSISTENT | -0.0216 |
| team_defense.rush_epa_per_play | 0.1183 | -0.0760 | 0.0649 | 1 | 56 | -0.0630 | 0.1995 | -0.1995 | 29 | 0.0968 | low | NOT_RANK_PERSISTENT | -0.0475 |
| team_defense.rush_success_rate | 0.4706 | 0.4020 | 0.0330 | 1 | 56 | 0.4060 | 0.1224 | -0.1224 | 24 | 0.2581 | low | RANK_PERSISTENT | -0.0131 |
| team_defense.success_rate | 0.5179 | 0.4384 | 0.0255 | 1 | 56 | 0.4431 | 0.1836 | -0.1836 | 28 | 0.1290 | low | RANK_PERSISTENT | -0.0145 |
| team_offense.early_down_epa_per_play | 0.0821 | -0.0054 | 0.0784 | 1 | 63 | 0.0043 | 0.1240 | 0.1240 | 12 | 0.6452 | low | UNVALIDATED_RANK_PERSISTENT | 0.0337 |
| team_offense.epa_per_play | 0.0013 | -0.0001 | 0.0921 | 1 | 63 | 0.0000 | 0.0018 | 0.0018 | 18 | 0.4516 | low | VALIDATED_PERSISTENCE | -0.0081 |
| team_offense.explosive_pass_rate | 0.0811 | 0.0796 | 0.0177 | 1 | 63 | 0.0797 | 0.0050 | 0.0050 | 15 | 0.5484 | low | RANK_PERSISTENT | 0.0058 |
| team_offense.explosive_rush_rate | 0.1600 | 0.0990 | 0.0195 | 1 | 63 | 0.1026 | 0.1836 | 0.1836 | 5 | 0.8710 | low | NOT_RANK_PERSISTENT | 0.0073 |
| team_offense.pass_epa_per_dropback | -0.0361 | 0.0308 | 0.1280 | 1 | 63 | 0.0234 | -0.0580 | -0.0580 | 21 | 0.3548 | low | UNVALIDATED_RANK_PERSISTENT | 0.0275 |
| team_offense.pass_success_rate | 0.5135 | 0.4521 | 0.0418 | 1 | 63 | 0.4589 | 0.1632 | 0.1632 | 8 | 0.7742 | low | UNVALIDATED_RANK_PERSISTENT | 0.0044 |
| team_offense.proe | 0.0413 | -0.0477 | 0.0349 | 1 | 63 | -0.0299 | 0.5106 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0115 |
| team_offense.rush_epa_per_play | 0.0495 | -0.0806 | 0.0754 | 1 | 63 | -0.0729 | 0.1016 | 0.1016 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0399 |
| team_offense.rush_success_rate | 0.4000 | 0.4004 | 0.0385 | 1 | 63 | 0.4003 | -0.0007 | -0.0007 | 18 | 0.4032 | low | RANK_PERSISTENT | -0.0315 |
| team_offense.success_rate | 0.4762 | 0.4370 | 0.0337 | 1 | 63 | 0.4448 | 0.2326 | 0.2326 | 10 | 0.7097 | low | VALIDATED_PERSISTENCE | -0.0143 |

## CLE
Record: 0-1-0 · Points for/against: 10/34 · Point differential: -24 · Data confidence: low
Strongest area: **special_teams** (0.280) · Weakest area: **pass_protection** (-0.503)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.307 | 32 | -0.902 | -0.902 | low |
| pass_rush | Pass-Rush Strength Index | -0.092 | 25 | -1.165 | -1.165 | low |
| passing_defense | Pass-Defense Strength Index | -0.468 | 32 | -1.092 | -1.092 | low |
| rushing_defense | Run-Defense Strength Index | -0.145 | 29 | -0.365 | -0.365 | low |
| offense_overall | Offensive Strength Index | -0.129 | 22 | 1.442 | 1.442 | low |
| pass_protection | Pass-Protection Strength Index | -0.503 | 32 | 0.412 | 0.412 | low |
| passing_offense | Passing-Offense Strength Index | -0.039 | 18 | 1.283 | 1.283 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.006 | 19 | 0.588 | 0.588 | low |
| special_teams | Special-Teams Strength Index | 0.280 | 1 | 0.915 | 0.915 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2667 | 0.1450 | 0.0327 | 1 | 30 | 0.1585 | 0.4132 | -0.4132 | 30 | 0.0645 | low | UNVALIDATED_RANK_PERSISTENT | -0.0305 |
| pass_protection.rush_stuffed_rate_approx | 0.1579 | 0.2045 | 0.0323 | 1 | 30 | 0.2018 | -0.0848 | 0.0848 | 7 | 0.7903 | low | RANK_PERSISTENT | -0.0213 |
| pass_protection.sack_rate_allowed | 0.1667 | 0.0664 | 0.0188 | 1 | 30 | 0.0775 | 0.5932 | -0.5932 | 32 | 0.0000 | low | UNVALIDATED_RANK_PERSISTENT | 0.0020 |
| pass_rush.qb_hit_rate_generated | 0.1250 | 0.1442 | 0.0234 | 1 | 24 | 0.1430 | -0.0482 | -0.0482 | 21 | 0.3548 | low | RANK_PERSISTENT | -0.0213 |
| pass_rush.sack_rate_generated | 0.0417 | 0.0660 | 0.0121 | 1 | 24 | 0.0644 | -0.1349 | -0.1349 | 23 | 0.2903 | low | NOT_RANK_PERSISTENT | -0.0171 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 12 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0109 |
| special_teams.st_epa_per_play | 0.5044 | 0.0622 | 0.0928 | 1 | 12 | 0.0882 | 0.2801 | 0.2801 | 1 | 1.0000 | low | RANK_PERSISTENT | 0.0850 |
| team_defense.early_down_epa_per_play | 0.3255 | -0.0013 | 0.0639 | 1 | 54 | 0.0179 | 0.3009 | -0.3009 | 32 | 0.0000 | low | RANK_PERSISTENT | 0.0520 |
| team_defense.epa_per_play | 0.3098 | 0.0046 | 0.0677 | 1 | 54 | 0.0225 | 0.2650 | -0.2650 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0633 |
| team_defense.explosive_pass_rate | 0.1667 | 0.0797 | 0.0112 | 1 | 54 | 0.0855 | 0.5169 | -0.5169 | 32 | 0.0000 | low | NOT_RANK_PERSISTENT | 0.0075 |
| team_defense.explosive_rush_rate | 0.1724 | 0.1000 | 0.0206 | 1 | 54 | 0.1042 | 0.2069 | -0.2069 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0087 |
| team_defense.pass_epa_per_dropback | 0.7926 | 0.0361 | 0.0949 | 1 | 54 | 0.0806 | 0.4690 | -0.4690 | 32 | 0.0000 | low | RANK_PERSISTENT | 0.1195 |
| team_defense.pass_success_rate | 0.7083 | 0.4536 | 0.0320 | 1 | 54 | 0.4686 | 0.4676 | -0.4676 | 32 | 0.0000 | low | RANK_PERSISTENT | 0.0296 |
| team_defense.rush_epa_per_play | -0.0530 | -0.0760 | 0.0649 | 1 | 54 | -0.0745 | 0.0236 | -0.0236 | 20 | 0.3871 | low | NOT_RANK_PERSISTENT | 0.0024 |
| team_defense.rush_success_rate | 0.5172 | 0.4020 | 0.0330 | 1 | 54 | 0.4088 | 0.2056 | -0.2056 | 31 | 0.0323 | low | RANK_PERSISTENT | 0.0210 |
| team_defense.success_rate | 0.5926 | 0.4384 | 0.0255 | 1 | 54 | 0.4475 | 0.3563 | -0.3563 | 32 | 0.0000 | low | RANK_PERSISTENT | 0.0243 |
| team_offense.early_down_epa_per_play | -0.0791 | -0.0054 | 0.0784 | 1 | 51 | -0.0136 | -0.1044 | -0.1044 | 21 | 0.3548 | low | UNVALIDATED_RANK_PERSISTENT | 0.0994 |
| team_offense.epa_per_play | -0.2057 | -0.0001 | 0.0921 | 1 | 51 | -0.0230 | -0.2480 | -0.2480 | 26 | 0.1935 | low | VALIDATED_PERSISTENCE | 0.0968 |
| team_offense.explosive_pass_rate | 0.1000 | 0.0796 | 0.0177 | 1 | 51 | 0.0808 | 0.0678 | 0.0678 | 11 | 0.6774 | low | RANK_PERSISTENT | 0.0140 |
| team_offense.explosive_rush_rate | 0.0526 | 0.0990 | 0.0195 | 1 | 51 | 0.0963 | -0.1397 | -0.1397 | 28 | 0.1129 | low | NOT_RANK_PERSISTENT | 0.0078 |
| team_offense.pass_epa_per_dropback | -0.2254 | 0.0308 | 0.1280 | 1 | 51 | 0.0023 | -0.2224 | -0.2224 | 26 | 0.1935 | low | UNVALIDATED_RANK_PERSISTENT | 0.1624 |
| team_offense.pass_success_rate | 0.4667 | 0.4521 | 0.0418 | 1 | 51 | 0.4537 | 0.0388 | 0.0388 | 17 | 0.4839 | low | UNVALIDATED_RANK_PERSISTENT | 0.0749 |
| team_offense.proe | -0.1360 | -0.0477 | 0.0349 | 1 | 51 | -0.0654 | -0.5068 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0006 |
| team_offense.rush_epa_per_play | -0.1194 | -0.0806 | 0.0754 | 1 | 51 | -0.0829 | -0.0303 | -0.0303 | 21 | 0.3548 | low | RANK_PERSISTENT | 0.0154 |
| team_offense.rush_success_rate | 0.4211 | 0.4004 | 0.0385 | 1 | 51 | 0.4020 | 0.0413 | 0.0413 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0374 |
| team_offense.success_rate | 0.4314 | 0.4370 | 0.0337 | 1 | 51 | 0.4358 | -0.0331 | -0.0331 | 18 | 0.4516 | low | VALIDATED_PERSISTENCE | 0.0677 |

## DAL
Record: 0-1-0 · Points for/against: 20/28 · Point differential: -8 · Data confidence: low
Strongest area: **pass_protection** (0.301) · Weakest area: **passing_defense** (-0.419)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.290 | 31 | 0.683 | 0.683 | low |
| pass_rush | Pass-Rush Strength Index | -0.006 | 15 | -0.010 | -0.010 | low |
| passing_defense | Pass-Defense Strength Index | -0.419 | 31 | 0.580 | 0.580 | low |
| rushing_defense | Run-Defense Strength Index | -0.116 | 27 | 0.743 | 0.743 | low |
| offense_overall | Offensive Strength Index | 0.233 | 6 | -0.602 | -0.602 | low |
| pass_protection | Pass-Protection Strength Index | 0.301 | 4 | -0.119 | -0.119 | low |
| passing_offense | Passing-Offense Strength Index | 0.012 | 15 | -0.404 | -0.404 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.004 | 20 | -0.544 | -0.544 | low |
| special_teams | Special-Teams Strength Index | -0.111 | 27 | -0.778 | -0.778 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0833 | 0.1450 | 0.0327 | 1 | 36 | 0.1381 | -0.2094 | 0.2094 | 6 | 0.8387 | low | UNVALIDATED_RANK_PERSISTENT | -0.0041 |
| pass_protection.rush_stuffed_rate_approx | 0.2353 | 0.2045 | 0.0323 | 1 | 36 | 0.2063 | 0.0559 | -0.0559 | 20 | 0.3871 | low | RANK_PERSISTENT | 0.0281 |
| pass_protection.sack_rate_allowed | 0.0000 | 0.0664 | 0.0188 | 1 | 36 | 0.0590 | -0.3929 | 0.3929 | 1 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | 0.0068 |
| pass_rush.qb_hit_rate_generated | 0.1515 | 0.1442 | 0.0234 | 1 | 33 | 0.1446 | 0.0185 | 0.0185 | 13 | 0.5645 | low | RANK_PERSISTENT | -0.0110 |
| pass_rush.sack_rate_generated | 0.0606 | 0.0660 | 0.0121 | 1 | 33 | 0.0657 | -0.0301 | -0.0301 | 17 | 0.4677 | low | NOT_RANK_PERSISTENT | 0.0054 |
| special_teams.fg_pct | — | 0.8507 | 0.0691 | 1 | 10 | — | — | — | — | — | low | NOT_RANK_PERSISTENT | — |
| special_teams.st_epa_per_play | -0.1130 | 0.0622 | 0.0928 | 1 | 10 | 0.0519 | -0.1110 | -0.1110 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0723 |
| team_defense.early_down_epa_per_play | 0.2224 | -0.0013 | 0.0639 | 1 | 66 | 0.0119 | 0.2060 | -0.2060 | 28 | 0.1290 | low | RANK_PERSISTENT | -0.0352 |
| team_defense.epa_per_play | 0.3629 | 0.0046 | 0.0677 | 1 | 66 | 0.0257 | 0.3111 | -0.3111 | 32 | 0.0000 | low | RANK_PERSISTENT | -0.0600 |
| team_defense.explosive_pass_rate | 0.0000 | 0.0797 | 0.0112 | 1 | 66 | 0.0744 | -0.4735 | 0.4735 | 1 | 0.9355 | low | NOT_RANK_PERSISTENT | -0.0120 |
| team_defense.explosive_rush_rate | 0.1212 | 0.1000 | 0.0206 | 1 | 66 | 0.1012 | 0.0607 | -0.0607 | 23 | 0.2742 | low | RANK_PERSISTENT | -0.0176 |
| team_defense.pass_epa_per_dropback | 0.6670 | 0.0361 | 0.0949 | 1 | 66 | 0.0732 | 0.3912 | -0.3912 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0685 |
| team_defense.pass_success_rate | 0.6970 | 0.4536 | 0.0320 | 1 | 66 | 0.4680 | 0.4467 | -0.4467 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0141 |
| team_defense.rush_epa_per_play | 0.0587 | -0.0760 | 0.0649 | 1 | 66 | -0.0670 | 0.1383 | -0.1383 | 26 | 0.1935 | low | NOT_RANK_PERSISTENT | -0.0511 |
| team_defense.rush_success_rate | 0.4848 | 0.4020 | 0.0330 | 1 | 66 | 0.4069 | 0.1478 | -0.1478 | 29 | 0.0968 | low | RANK_PERSISTENT | -0.0194 |
| team_defense.success_rate | 0.5909 | 0.4384 | 0.0255 | 1 | 66 | 0.4474 | 0.3524 | -0.3524 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0156 |
| team_offense.early_down_epa_per_play | 0.0655 | -0.0054 | 0.0784 | 1 | 58 | 0.0025 | 0.1005 | 0.1005 | 14 | 0.5806 | low | UNVALIDATED_RANK_PERSISTENT | -0.0602 |
| team_offense.epa_per_play | 0.2709 | -0.0001 | 0.0921 | 1 | 58 | 0.0300 | 0.3270 | 0.3270 | 5 | 0.8710 | low | VALIDATED_PERSISTENCE | -0.0438 |
| team_offense.explosive_pass_rate | 0.0000 | 0.0796 | 0.0177 | 1 | 58 | 0.0749 | -0.2640 | -0.2640 | 28 | 0.0645 | low | RANK_PERSISTENT | -0.0060 |
| team_offense.explosive_rush_rate | 0.0000 | 0.0990 | 0.0195 | 1 | 58 | 0.0932 | -0.2982 | -0.2982 | 32 | 0.0000 | low | NOT_RANK_PERSISTENT | -0.0027 |
| team_offense.pass_epa_per_dropback | 0.3144 | 0.0308 | 0.1280 | 1 | 58 | 0.0623 | 0.2462 | 0.2462 | 7 | 0.8065 | low | UNVALIDATED_RANK_PERSISTENT | -0.0536 |
| team_offense.pass_success_rate | 0.4722 | 0.4521 | 0.0418 | 1 | 58 | 0.4543 | 0.0535 | 0.0535 | 14 | 0.5806 | low | UNVALIDATED_RANK_PERSISTENT | -0.0189 |
| team_offense.proe | -0.0633 | -0.0477 | 0.0349 | 1 | 58 | -0.0508 | -0.0896 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0034 |
| team_offense.rush_epa_per_play | -0.0999 | -0.0806 | 0.0754 | 1 | 58 | -0.0817 | -0.0150 | -0.0150 | 18 | 0.4516 | low | RANK_PERSISTENT | -0.0388 |
| team_offense.rush_success_rate | 0.4118 | 0.4004 | 0.0385 | 1 | 58 | 0.4012 | 0.0228 | 0.0228 | 16 | 0.5161 | low | RANK_PERSISTENT | -0.0221 |
| team_offense.success_rate | 0.4828 | 0.4370 | 0.0337 | 1 | 58 | 0.4461 | 0.2715 | 0.2715 | 8 | 0.7742 | low | VALIDATED_PERSISTENCE | -0.0189 |

## DEN
Record: 0-1-0 · Points for/against: 10/31 · Point differential: -21 · Data confidence: low
Strongest area: **special_teams** (0.126) · Weakest area: **offense_overall** (-0.373)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.030 | 15 | -0.686 | -0.686 | low |
| pass_rush | Pass-Rush Strength Index | -0.006 | 15 | -1.515 | -1.515 | low |
| passing_defense | Pass-Defense Strength Index | 0.030 | 15 | -0.947 | -0.947 | low |
| rushing_defense | Run-Defense Strength Index | -0.141 | 28 | -0.767 | -0.767 | low |
| offense_overall | Offensive Strength Index | -0.373 | 31 | -0.536 | -0.536 | low |
| pass_protection | Pass-Protection Strength Index | -0.173 | 27 | -1.177 | -1.177 | low |
| passing_offense | Passing-Offense Strength Index | -0.277 | 32 | -0.292 | -0.292 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.191 | 29 | -0.404 | -0.404 | low |
| special_teams | Special-Teams Strength Index | 0.126 | 12 | 0.153 | 0.153 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1515 | 0.1450 | 0.0327 | 1 | 33 | 0.1457 | 0.0221 | -0.0221 | 17 | 0.4355 | low | UNVALIDATED_RANK_PERSISTENT | 0.0284 |
| pass_protection.rush_stuffed_rate_approx | 0.2000 | 0.2045 | 0.0323 | 1 | 33 | 0.2043 | -0.0082 | 0.0082 | 17 | 0.4677 | low | RANK_PERSISTENT | 0.0048 |
| pass_protection.sack_rate_allowed | 0.1212 | 0.0664 | 0.0188 | 1 | 33 | 0.0725 | 0.3242 | -0.3242 | 29 | 0.0968 | low | UNVALIDATED_RANK_PERSISTENT | 0.0279 |
| pass_rush.qb_hit_rate_generated | 0.1515 | 0.1442 | 0.0234 | 1 | 33 | 0.1446 | 0.0185 | 0.0185 | 13 | 0.5645 | low | RANK_PERSISTENT | -0.0361 |
| pass_rush.sack_rate_generated | 0.0606 | 0.0660 | 0.0121 | 1 | 33 | 0.0657 | -0.0301 | -0.0301 | 17 | 0.4677 | low | NOT_RANK_PERSISTENT | -0.0180 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 14 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0037 |
| special_teams.st_epa_per_play | 0.2605 | 0.0622 | 0.0928 | 1 | 14 | 0.0739 | 0.1256 | 0.1256 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0142 |
| team_defense.early_down_epa_per_play | -0.1314 | -0.0013 | 0.0639 | 1 | 66 | -0.0090 | -0.1198 | 0.1198 | 10 | 0.7097 | low | RANK_PERSISTENT | 0.0203 |
| team_defense.epa_per_play | 0.1183 | 0.0046 | 0.0677 | 1 | 66 | 0.0113 | 0.0987 | -0.0987 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0392 |
| team_defense.explosive_pass_rate | 0.0606 | 0.0797 | 0.0112 | 1 | 66 | 0.0784 | -0.1134 | 0.1134 | 15 | 0.5484 | low | NOT_RANK_PERSISTENT | 0.0108 |
| team_defense.explosive_rush_rate | 0.1250 | 0.1000 | 0.0206 | 1 | 66 | 0.1014 | 0.0715 | -0.0715 | 25 | 0.2097 | low | RANK_PERSISTENT | 0.0225 |
| team_defense.pass_epa_per_dropback | 0.0263 | 0.0361 | 0.0949 | 1 | 66 | 0.0355 | -0.0061 | 0.0061 | 16 | 0.5161 | low | RANK_PERSISTENT | 0.0584 |
| team_defense.pass_success_rate | 0.4242 | 0.4536 | 0.0320 | 1 | 66 | 0.4519 | -0.0540 | 0.0540 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0409 |
| team_defense.rush_epa_per_play | 0.2585 | -0.0760 | 0.0649 | 1 | 66 | -0.0537 | 0.3434 | -0.3434 | 32 | 0.0000 | low | NOT_RANK_PERSISTENT | 0.0384 |
| team_defense.rush_success_rate | 0.4062 | 0.4020 | 0.0330 | 1 | 66 | 0.4022 | 0.0076 | -0.0076 | 16 | 0.5161 | low | RANK_PERSISTENT | 0.0204 |
| team_defense.success_rate | 0.4091 | 0.4384 | 0.0255 | 1 | 66 | 0.4367 | -0.0677 | 0.0677 | 11 | 0.6774 | low | RANK_PERSISTENT | 0.0296 |
| team_offense.early_down_epa_per_play | -0.1524 | -0.0054 | 0.0784 | 1 | 50 | -0.0217 | -0.2083 | -0.2083 | 25 | 0.2258 | low | UNVALIDATED_RANK_PERSISTENT | -0.0351 |
| team_offense.epa_per_play | -0.3777 | -0.0001 | 0.0921 | 1 | 50 | -0.0421 | -0.4556 | -0.4556 | 32 | 0.0000 | low | VALIDATED_PERSISTENCE | -0.0662 |
| team_offense.explosive_pass_rate | 0.0000 | 0.0796 | 0.0177 | 1 | 50 | 0.0749 | -0.2640 | -0.2640 | 28 | 0.0645 | low | RANK_PERSISTENT | 0.0002 |
| team_offense.explosive_rush_rate | 0.0667 | 0.0990 | 0.0195 | 1 | 50 | 0.0971 | -0.0974 | -0.0974 | 22 | 0.2903 | low | NOT_RANK_PERSISTENT | -0.0010 |
| team_offense.pass_epa_per_dropback | -0.4429 | 0.0308 | 0.1280 | 1 | 50 | -0.0219 | -0.4113 | -0.4113 | 31 | 0.0323 | low | UNVALIDATED_RANK_PERSISTENT | -0.1043 |
| team_offense.pass_success_rate | 0.3939 | 0.4521 | 0.0418 | 1 | 50 | 0.4456 | -0.1545 | -0.1545 | 25 | 0.2097 | low | UNVALIDATED_RANK_PERSISTENT | -0.0031 |
| team_offense.proe | -0.0226 | -0.0477 | 0.0349 | 1 | 50 | -0.0427 | 0.1441 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0259 |
| team_offense.rush_epa_per_play | -0.2283 | -0.0806 | 0.0754 | 1 | 50 | -0.0893 | -0.1153 | -0.1153 | 26 | 0.1935 | low | RANK_PERSISTENT | -0.0145 |
| team_offense.rush_success_rate | 0.2667 | 0.4004 | 0.0385 | 1 | 50 | 0.3901 | -0.2670 | -0.2670 | 29 | 0.0968 | low | RANK_PERSISTENT | -0.0238 |
| team_offense.success_rate | 0.3600 | 0.4370 | 0.0337 | 1 | 50 | 0.4216 | -0.4562 | -0.4562 | 29 | 0.0968 | low | VALIDATED_PERSISTENCE | -0.0149 |

## DET
Record: 1-0-0 · Points for/against: 31/30 · Point differential: 1 · Data confidence: low
Strongest area: **rushing_offense** (0.103) · Weakest area: **passing_offense** (-0.100)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.007 | 19 | -0.159 | -0.159 | low |
| pass_rush | Pass-Rush Strength Index | 0.042 | 12 | -0.340 | -0.340 | low |
| passing_defense | Pass-Defense Strength Index | -0.002 | 18 | -0.334 | -0.334 | low |
| rushing_defense | Run-Defense Strength Index | 0.070 | 12 | 0.327 | 0.327 | low |
| offense_overall | Offensive Strength Index | 0.023 | 14 | -0.508 | -0.508 | low |
| pass_protection | Pass-Protection Strength Index | 0.039 | 14 | 0.443 | 0.443 | low |
| passing_offense | Passing-Offense Strength Index | -0.100 | 24 | -0.773 | -0.773 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.103 | 8 | 0.086 | 0.086 | low |
| special_teams | Special-Teams Strength Index | -0.037 | 23 | -0.435 | -0.435 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1951 | 0.1450 | 0.0327 | 1 | 41 | 0.1506 | 0.1702 | -0.1702 | 25 | 0.2258 | low | UNVALIDATED_RANK_PERSISTENT | -0.0255 |
| pass_protection.rush_stuffed_rate_approx | 0.2222 | 0.2045 | 0.0323 | 1 | 41 | 0.2056 | 0.0322 | -0.0322 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0027 |
| pass_protection.sack_rate_allowed | 0.0244 | 0.0664 | 0.0188 | 1 | 41 | 0.0617 | -0.2486 | 0.2486 | 6 | 0.8387 | low | UNVALIDATED_RANK_PERSISTENT | -0.0020 |
| pass_rush.qb_hit_rate_generated | 0.1452 | 0.1442 | 0.0234 | 1 | 62 | 0.1442 | 0.0025 | 0.0025 | 17 | 0.4839 | low | RANK_PERSISTENT | -0.0060 |
| pass_rush.sack_rate_generated | 0.0806 | 0.0660 | 0.0121 | 1 | 62 | 0.0670 | 0.0808 | 0.0808 | 10 | 0.7097 | low | NOT_RANK_PERSISTENT | -0.0051 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 18 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0379 |
| special_teams.st_epa_per_play | 0.0034 | 0.0622 | 0.0928 | 1 | 18 | 0.0588 | -0.0373 | -0.0373 | 23 | 0.2903 | low | RANK_PERSISTENT | -0.0404 |
| team_defense.early_down_epa_per_play | -0.0138 | -0.0013 | 0.0639 | 1 | 88 | -0.0020 | -0.0115 | 0.0115 | 17 | 0.4839 | low | RANK_PERSISTENT | 0.0144 |
| team_defense.epa_per_play | 0.0299 | 0.0046 | 0.0677 | 1 | 88 | 0.0061 | 0.0220 | -0.0220 | 18 | 0.4516 | low | RANK_PERSISTENT | -0.0021 |
| team_defense.explosive_pass_rate | 0.0968 | 0.0797 | 0.0112 | 1 | 88 | 0.0808 | 0.1016 | -0.1016 | 21 | 0.3548 | low | NOT_RANK_PERSISTENT | -0.0053 |
| team_defense.explosive_rush_rate | 0.0870 | 0.1000 | 0.0206 | 1 | 88 | 0.0992 | -0.0371 | 0.0371 | 15 | 0.5484 | low | RANK_PERSISTENT | -0.0072 |
| team_defense.pass_epa_per_dropback | 0.0006 | 0.0361 | 0.0949 | 1 | 88 | 0.0340 | -0.0220 | 0.0220 | 13 | 0.6129 | low | RANK_PERSISTENT | 0.0127 |
| team_defense.pass_success_rate | 0.4677 | 0.4536 | 0.0320 | 1 | 88 | 0.4545 | 0.0259 | -0.0259 | 17 | 0.4839 | low | RANK_PERSISTENT | 0.0171 |
| team_defense.rush_epa_per_play | -0.0751 | -0.0760 | 0.0649 | 1 | 88 | -0.0759 | 0.0010 | -0.0010 | 18 | 0.4516 | low | NOT_RANK_PERSISTENT | -0.0214 |
| team_defense.rush_success_rate | 0.3043 | 0.4020 | 0.0330 | 1 | 88 | 0.3962 | -0.1742 | 0.1742 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0099 |
| team_defense.success_rate | 0.4432 | 0.4384 | 0.0255 | 1 | 88 | 0.4387 | 0.0111 | -0.0111 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0072 |
| team_offense.early_down_epa_per_play | -0.0070 | -0.0054 | 0.0784 | 1 | 77 | -0.0056 | -0.0023 | -0.0023 | 15 | 0.5484 | low | UNVALIDATED_RANK_PERSISTENT | -0.0596 |
| team_offense.epa_per_play | -0.0272 | -0.0001 | 0.0921 | 1 | 77 | -0.0031 | -0.0327 | -0.0327 | 19 | 0.4194 | low | VALIDATED_PERSISTENCE | -0.0515 |
| team_offense.explosive_pass_rate | 0.0244 | 0.0796 | 0.0177 | 1 | 77 | 0.0763 | -0.1831 | -0.1831 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0167 |
| team_offense.explosive_rush_rate | 0.1944 | 0.0990 | 0.0195 | 1 | 77 | 0.1046 | 0.2874 | 0.2874 | 3 | 0.9355 | low | NOT_RANK_PERSISTENT | 0.0059 |
| team_offense.pass_epa_per_dropback | 0.0122 | 0.0308 | 0.1280 | 1 | 77 | 0.0287 | -0.0161 | -0.0161 | 18 | 0.4516 | low | UNVALIDATED_RANK_PERSISTENT | -0.0969 |
| team_offense.pass_success_rate | 0.4146 | 0.4521 | 0.0418 | 1 | 77 | 0.4479 | -0.0995 | -0.0995 | 21 | 0.3548 | low | UNVALIDATED_RANK_PERSISTENT | -0.0258 |
| team_offense.proe | -0.0240 | -0.0477 | 0.0349 | 1 | 77 | -0.0430 | 0.1359 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0199 |
| team_offense.rush_epa_per_play | -0.0720 | -0.0806 | 0.0754 | 1 | 77 | -0.0801 | 0.0067 | 0.0067 | 14 | 0.5806 | low | RANK_PERSISTENT | -0.0045 |
| team_offense.rush_success_rate | 0.5000 | 0.4004 | 0.0385 | 1 | 77 | 0.4080 | 0.1990 | 0.1990 | 3 | 0.9355 | low | RANK_PERSISTENT | 0.0090 |
| team_offense.success_rate | 0.4545 | 0.4370 | 0.0337 | 1 | 77 | 0.4405 | 0.1043 | 0.1043 | 13 | 0.6129 | low | VALIDATED_PERSISTENCE | -0.0069 |

## GB
Record: 0-1-0 · Points for/against: 22/39 · Point differential: -17 · Data confidence: low
Strongest area: **rushing_defense** (0.126) · Weakest area: **pass_protection** (-0.368)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.118 | 7 | 0.417 | 0.417 | low |
| pass_rush | Pass-Rush Strength Index | 0.122 | 8 | 0.083 | 0.083 | low |
| passing_defense | Pass-Defense Strength Index | 0.078 | 8 | 0.161 | 0.161 | low |
| rushing_defense | Run-Defense Strength Index | 0.126 | 8 | 0.187 | 0.187 | low |
| offense_overall | Offensive Strength Index | -0.127 | 21 | -1.005 | -1.005 | low |
| pass_protection | Pass-Protection Strength Index | -0.368 | 30 | -0.601 | -0.601 | low |
| passing_offense | Passing-Offense Strength Index | 0.020 | 14 | -0.909 | -0.909 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.221 | 30 | -0.492 | -0.492 | low |
| special_teams | Special-Teams Strength Index | 0.108 | 14 | -0.069 | -0.069 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.3261 | 0.1450 | 0.0327 | 1 | 46 | 0.1651 | 0.6149 | -0.6149 | 32 | 0.0000 | low | UNVALIDATED_RANK_PERSISTENT | 0.0189 |
| pass_protection.rush_stuffed_rate_approx | 0.2727 | 0.2045 | 0.0323 | 1 | 46 | 0.2085 | 0.1240 | -0.1240 | 27 | 0.1452 | low | RANK_PERSISTENT | 0.0214 |
| pass_protection.sack_rate_allowed | 0.0870 | 0.0664 | 0.0188 | 1 | 46 | 0.0687 | 0.1216 | -0.1216 | 25 | 0.2258 | low | UNVALIDATED_RANK_PERSISTENT | 0.0117 |
| pass_rush.qb_hit_rate_generated | 0.1667 | 0.1442 | 0.0234 | 1 | 30 | 0.1455 | 0.0565 | 0.0565 | 10 | 0.6935 | low | RANK_PERSISTENT | -0.0080 |
| pass_rush.sack_rate_generated | 0.1000 | 0.0660 | 0.0121 | 1 | 30 | 0.0683 | 0.1878 | 0.1878 | 6 | 0.8387 | low | NOT_RANK_PERSISTENT | 0.0061 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 15 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0228 |
| special_teams.st_epa_per_play | 0.2331 | 0.0622 | 0.0928 | 1 | 15 | 0.0723 | 0.1083 | 0.1083 | 14 | 0.5806 | low | RANK_PERSISTENT | -0.0064 |
| team_defense.early_down_epa_per_play | -0.2792 | -0.0013 | 0.0639 | 1 | 61 | -0.0177 | -0.2559 | 0.2559 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0391 |
| team_defense.epa_per_play | 0.0553 | 0.0046 | 0.0677 | 1 | 61 | 0.0076 | 0.0441 | -0.0441 | 19 | 0.4194 | low | RANK_PERSISTENT | -0.0161 |
| team_defense.explosive_pass_rate | 0.0333 | 0.0797 | 0.0112 | 1 | 61 | 0.0766 | -0.2754 | 0.2754 | 10 | 0.7097 | low | NOT_RANK_PERSISTENT | 0.0037 |
| team_defense.explosive_rush_rate | 0.0357 | 0.1000 | 0.0206 | 1 | 61 | 0.0962 | -0.1835 | 0.1835 | 2 | 0.9677 | low | RANK_PERSISTENT | 0.0070 |
| team_defense.pass_epa_per_dropback | 0.0426 | 0.0361 | 0.0949 | 1 | 61 | 0.0365 | 0.0040 | -0.0040 | 17 | 0.4839 | low | RANK_PERSISTENT | -0.0271 |
| team_defense.pass_success_rate | 0.3667 | 0.4536 | 0.0320 | 1 | 61 | 0.4485 | -0.1597 | 0.1597 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0011 |
| team_defense.rush_epa_per_play | -0.1245 | -0.0760 | 0.0649 | 1 | 61 | -0.0792 | -0.0498 | 0.0498 | 11 | 0.6774 | low | NOT_RANK_PERSISTENT | -0.0099 |
| team_defense.rush_success_rate | 0.3214 | 0.4020 | 0.0330 | 1 | 61 | 0.3972 | -0.1437 | 0.1437 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0247 |
| team_defense.success_rate | 0.3770 | 0.4384 | 0.0255 | 1 | 61 | 0.4348 | -0.1418 | 0.1418 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0102 |
| team_offense.early_down_epa_per_play | 0.1076 | -0.0054 | 0.0784 | 1 | 68 | 0.0072 | 0.1601 | 0.1601 | 10 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | -0.0410 |
| team_offense.epa_per_play | -0.1813 | -0.0001 | 0.0921 | 1 | 68 | -0.0203 | -0.2186 | -0.2186 | 25 | 0.2258 | low | VALIDATED_PERSISTENCE | -0.1034 |
| team_offense.explosive_pass_rate | 0.1522 | 0.0796 | 0.0177 | 1 | 68 | 0.0838 | 0.2408 | 0.2408 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0089 |
| team_offense.explosive_rush_rate | 0.0909 | 0.0990 | 0.0195 | 1 | 68 | 0.0985 | -0.0244 | -0.0244 | 16 | 0.5000 | low | NOT_RANK_PERSISTENT | -0.0027 |
| team_offense.pass_epa_per_dropback | -0.0588 | 0.0308 | 0.1280 | 1 | 68 | 0.0208 | -0.0778 | -0.0778 | 22 | 0.3226 | low | UNVALIDATED_RANK_PERSISTENT | -0.1609 |
| team_offense.pass_success_rate | 0.4130 | 0.4521 | 0.0418 | 1 | 68 | 0.4477 | -0.1037 | -0.1037 | 22 | 0.3226 | low | UNVALIDATED_RANK_PERSISTENT | -0.0406 |
| team_offense.proe | -0.0303 | -0.0477 | 0.0349 | 1 | 68 | -0.0442 | 0.1000 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0176 |
| team_offense.rush_epa_per_play | -0.4376 | -0.0806 | 0.0754 | 1 | 68 | -0.1016 | -0.2786 | -0.2786 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0235 |
| team_offense.rush_success_rate | 0.3182 | 0.4004 | 0.0385 | 1 | 68 | 0.3940 | -0.1641 | -0.1641 | 24 | 0.2581 | low | RANK_PERSISTENT | -0.0259 |
| team_offense.success_rate | 0.3824 | 0.4370 | 0.0337 | 1 | 68 | 0.4260 | -0.3237 | -0.3237 | 26 | 0.1935 | low | VALIDATED_PERSISTENCE | -0.0462 |

## HOU
Record: 0-1-0 · Points for/against: 31/36 · Point differential: -5 · Data confidence: low
Strongest area: **offense_overall** (0.166) · Weakest area: **passing_defense** (-0.176)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.163 | 27 | -1.094 | -1.094 | low |
| pass_rush | Pass-Rush Strength Index | -0.073 | 22 | -0.299 | -0.299 | low |
| passing_defense | Pass-Defense Strength Index | -0.176 | 27 | -1.153 | -1.153 | low |
| rushing_defense | Run-Defense Strength Index | 0.110 | 10 | -0.553 | -0.553 | low |
| offense_overall | Offensive Strength Index | 0.166 | 11 | 0.363 | 0.363 | low |
| pass_protection | Pass-Protection Strength Index | -0.132 | 23 | -0.708 | -0.708 | low |
| passing_offense | Passing-Offense Strength Index | 0.079 | 11 | 0.085 | 0.085 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.062 | 12 | 0.637 | 0.637 | low |
| special_teams | Special-Teams Strength Index | 0.121 | 13 | -0.247 | -0.247 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2143 | 0.1450 | 0.0327 | 1 | 42 | 0.1527 | 0.2353 | -0.2353 | 26 | 0.1935 | low | UNVALIDATED_RANK_PERSISTENT | 0.0238 |
| pass_protection.rush_stuffed_rate_approx | 0.2581 | 0.2045 | 0.0323 | 1 | 42 | 0.2077 | 0.0973 | -0.0973 | 24 | 0.2581 | low | RANK_PERSISTENT | -0.0136 |
| pass_protection.sack_rate_allowed | 0.0714 | 0.0664 | 0.0188 | 1 | 42 | 0.0670 | 0.0297 | -0.0297 | 19 | 0.4032 | low | UNVALIDATED_RANK_PERSISTENT | 0.0129 |
| pass_rush.qb_hit_rate_generated | 0.0938 | 0.1442 | 0.0234 | 1 | 32 | 0.1412 | -0.1267 | -0.1267 | 26 | 0.1935 | low | RANK_PERSISTENT | -0.0029 |
| pass_rush.sack_rate_generated | 0.0625 | 0.0660 | 0.0121 | 1 | 32 | 0.0658 | -0.0196 | -0.0196 | 16 | 0.5161 | low | NOT_RANK_PERSISTENT | -0.0057 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 17 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0285 |
| special_teams.st_epa_per_play | 0.2524 | 0.0622 | 0.0928 | 1 | 17 | 0.0734 | 0.1205 | 0.1205 | 13 | 0.6129 | low | RANK_PERSISTENT | -0.0230 |
| team_defense.early_down_epa_per_play | 0.3013 | -0.0013 | 0.0639 | 1 | 55 | 0.0165 | 0.2786 | -0.2786 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0856 |
| team_defense.epa_per_play | 0.3002 | 0.0046 | 0.0677 | 1 | 55 | 0.0220 | 0.2567 | -0.2567 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0756 |
| team_defense.explosive_pass_rate | 0.1562 | 0.0797 | 0.0112 | 1 | 55 | 0.0848 | 0.4550 | -0.4550 | 31 | 0.0323 | low | NOT_RANK_PERSISTENT | 0.0071 |
| team_defense.explosive_rush_rate | 0.1053 | 0.1000 | 0.0206 | 1 | 55 | 0.1003 | 0.0152 | -0.0152 | 21 | 0.3548 | low | RANK_PERSISTENT | 0.0239 |
| team_defense.pass_epa_per_dropback | 0.5582 | 0.0361 | 0.0949 | 1 | 55 | 0.0668 | 0.3237 | -0.3237 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.1165 |
| team_defense.pass_success_rate | 0.4688 | 0.4536 | 0.0320 | 1 | 55 | 0.4545 | 0.0277 | -0.0277 | 18 | 0.4516 | low | RANK_PERSISTENT | 0.0345 |
| team_defense.rush_epa_per_play | -0.2628 | -0.0760 | 0.0649 | 1 | 55 | -0.0885 | -0.1918 | 0.1918 | 5 | 0.8710 | low | NOT_RANK_PERSISTENT | 0.0167 |
| team_defense.rush_success_rate | 0.3158 | 0.4020 | 0.0330 | 1 | 55 | 0.3969 | -0.1537 | 0.1537 | 8 | 0.7742 | low | RANK_PERSISTENT | 0.0080 |
| team_defense.success_rate | 0.4182 | 0.4384 | 0.0255 | 1 | 55 | 0.4372 | -0.0467 | 0.0467 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0210 |
| team_offense.early_down_epa_per_play | 0.1003 | -0.0054 | 0.0784 | 1 | 79 | 0.0064 | 0.1498 | 0.1498 | 11 | 0.6774 | low | UNVALIDATED_RANK_PERSISTENT | 0.0166 |
| team_offense.epa_per_play | 0.0713 | -0.0001 | 0.0921 | 1 | 79 | 0.0078 | 0.0861 | 0.0861 | 13 | 0.6129 | low | VALIDATED_PERSISTENCE | 0.0135 |
| team_offense.explosive_pass_rate | 0.0952 | 0.0796 | 0.0177 | 1 | 79 | 0.0805 | 0.0520 | 0.0520 | 13 | 0.6129 | low | RANK_PERSISTENT | 0.0035 |
| team_offense.explosive_rush_rate | 0.0968 | 0.0990 | 0.0195 | 1 | 79 | 0.0989 | -0.0067 | -0.0067 | 13 | 0.6129 | low | NOT_RANK_PERSISTENT | 0.0128 |
| team_offense.pass_epa_per_dropback | 0.0974 | 0.0308 | 0.1280 | 1 | 79 | 0.0382 | 0.0578 | 0.0578 | 14 | 0.5806 | low | UNVALIDATED_RANK_PERSISTENT | -0.0172 |
| team_offense.pass_success_rate | 0.5000 | 0.4521 | 0.0418 | 1 | 79 | 0.4574 | 0.1273 | 0.1273 | 9 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | 0.0082 |
| team_offense.proe | -0.1236 | -0.0477 | 0.0349 | 1 | 79 | -0.0629 | -0.4352 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0161 |
| team_offense.rush_epa_per_play | 0.0303 | -0.0806 | 0.0754 | 1 | 79 | -0.0741 | 0.0866 | 0.0866 | 9 | 0.7419 | low | RANK_PERSISTENT | 0.0419 |
| team_offense.rush_success_rate | 0.4194 | 0.4004 | 0.0385 | 1 | 79 | 0.4018 | 0.0379 | 0.0379 | 15 | 0.5484 | low | RANK_PERSISTENT | 0.0276 |
| team_offense.success_rate | 0.4810 | 0.4370 | 0.0337 | 1 | 79 | 0.4458 | 0.2612 | 0.2612 | 9 | 0.7419 | low | VALIDATED_PERSISTENCE | 0.0246 |

## IND
Record: 0-1-0 · Points for/against: 23/41 · Point differential: -18 · Data confidence: low
Strongest area: **rushing_offense** (0.150) · Weakest area: **passing_defense** (-0.221)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.166 | 28 | -0.008 | -0.008 | low |
| pass_rush | Pass-Rush Strength Index | -0.043 | 19 | 0.281 | 0.281 | low |
| passing_defense | Pass-Defense Strength Index | -0.221 | 29 | -0.009 | -0.009 | low |
| rushing_defense | Run-Defense Strength Index | -0.106 | 26 | -0.187 | -0.187 | low |
| offense_overall | Offensive Strength Index | -0.198 | 26 | -0.811 | -0.811 | low |
| pass_protection | Pass-Protection Strength Index | -0.181 | 28 | -0.591 | -0.591 | low |
| passing_offense | Passing-Offense Strength Index | -0.221 | 30 | -0.373 | -0.373 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.150 | 2 | -0.670 | -0.670 | low |
| special_teams | Special-Teams Strength Index | 0.134 | 10 | -0.527 | -0.527 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2647 | 0.1450 | 0.0327 | 1 | 34 | 0.1583 | 0.4065 | -0.4065 | 29 | 0.0968 | low | UNVALIDATED_RANK_PERSISTENT | 0.0188 |
| pass_protection.rush_stuffed_rate_approx | 0.2632 | 0.2045 | 0.0323 | 1 | 34 | 0.2080 | 0.1066 | -0.1066 | 25 | 0.2097 | low | RANK_PERSISTENT | 0.0141 |
| pass_protection.sack_rate_allowed | 0.0588 | 0.0664 | 0.0188 | 1 | 34 | 0.0656 | -0.0449 | 0.0449 | 14 | 0.5806 | low | UNVALIDATED_RANK_PERSISTENT | 0.0114 |
| pass_rush.qb_hit_rate_generated | 0.1034 | 0.1442 | 0.0234 | 1 | 29 | 0.1418 | -0.1024 | -0.1024 | 25 | 0.2258 | low | RANK_PERSISTENT | 0.0025 |
| pass_rush.sack_rate_generated | 0.0690 | 0.0660 | 0.0121 | 1 | 29 | 0.0662 | 0.0161 | 0.0161 | 15 | 0.5484 | low | NOT_RANK_PERSISTENT | 0.0055 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 16 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0395 |
| special_teams.st_epa_per_play | 0.2736 | 0.0622 | 0.0928 | 1 | 16 | 0.0747 | 0.1339 | 0.1339 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0489 |
| team_defense.early_down_epa_per_play | 0.2714 | -0.0013 | 0.0639 | 1 | 64 | 0.0147 | 0.2512 | -0.2512 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0142 |
| team_defense.epa_per_play | 0.2087 | 0.0046 | 0.0677 | 1 | 64 | 0.0166 | 0.1772 | -0.1772 | 27 | 0.1613 | low | RANK_PERSISTENT | 0.0075 |
| team_defense.explosive_pass_rate | 0.1034 | 0.0797 | 0.0112 | 1 | 64 | 0.0813 | 0.1412 | -0.1412 | 23 | 0.2903 | low | NOT_RANK_PERSISTENT | 0.0000 |
| team_defense.explosive_rush_rate | 0.1250 | 0.1000 | 0.0206 | 1 | 64 | 0.1014 | 0.0715 | -0.0715 | 25 | 0.2097 | low | RANK_PERSISTENT | 0.0068 |
| team_defense.pass_epa_per_dropback | 0.4595 | 0.0361 | 0.0949 | 1 | 64 | 0.0610 | 0.2625 | -0.2625 | 28 | 0.1290 | low | RANK_PERSISTENT | 0.0145 |
| team_defense.pass_success_rate | 0.5517 | 0.4536 | 0.0320 | 1 | 64 | 0.4594 | 0.1801 | -0.1801 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0043 |
| team_defense.rush_epa_per_play | 0.1015 | -0.0760 | 0.0649 | 1 | 64 | -0.0642 | 0.1822 | -0.1822 | 27 | 0.1613 | low | NOT_RANK_PERSISTENT | 0.0256 |
| team_defense.rush_success_rate | 0.4375 | 0.4020 | 0.0330 | 1 | 64 | 0.4041 | 0.0634 | -0.0634 | 21 | 0.3387 | low | RANK_PERSISTENT | -0.0054 |
| team_defense.success_rate | 0.4688 | 0.4384 | 0.0255 | 1 | 64 | 0.4402 | 0.0701 | -0.0701 | 21 | 0.3548 | low | RANK_PERSISTENT | -0.0079 |
| team_offense.early_down_epa_per_play | -0.1866 | -0.0054 | 0.0784 | 1 | 54 | -0.0255 | -0.2568 | -0.2568 | 28 | 0.1290 | low | UNVALIDATED_RANK_PERSISTENT | -0.0609 |
| team_offense.epa_per_play | -0.2246 | -0.0001 | 0.0921 | 1 | 54 | -0.0251 | -0.2709 | -0.2709 | 27 | 0.1613 | low | VALIDATED_PERSISTENCE | -0.0817 |
| team_offense.explosive_pass_rate | 0.0588 | 0.0796 | 0.0177 | 1 | 54 | 0.0784 | -0.0688 | -0.0688 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0019 |
| team_offense.explosive_rush_rate | 0.2632 | 0.0990 | 0.0195 | 1 | 54 | 0.1087 | 0.4943 | 0.4943 | 1 | 1.0000 | low | NOT_RANK_PERSISTENT | 0.0103 |
| team_offense.pass_epa_per_dropback | -0.4408 | 0.0308 | 0.1280 | 1 | 54 | -0.0216 | -0.4095 | -0.4095 | 30 | 0.0645 | low | UNVALIDATED_RANK_PERSISTENT | -0.0877 |
| team_offense.pass_success_rate | 0.3824 | 0.4521 | 0.0418 | 1 | 54 | 0.4443 | -0.1852 | -0.1852 | 27 | 0.1613 | low | UNVALIDATED_RANK_PERSISTENT | -0.0227 |
| team_offense.proe | -0.0592 | -0.0477 | 0.0349 | 1 | 54 | -0.0500 | -0.0662 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0094 |
| team_offense.rush_epa_per_play | 0.1160 | -0.0806 | 0.0754 | 1 | 54 | -0.0690 | 0.1534 | 0.1534 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0566 |
| team_offense.rush_success_rate | 0.4737 | 0.4004 | 0.0385 | 1 | 54 | 0.4060 | 0.1464 | 0.1464 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0227 |
| team_offense.success_rate | 0.4259 | 0.4370 | 0.0337 | 1 | 54 | 0.4348 | -0.0654 | -0.0654 | 20 | 0.3871 | low | VALIDATED_PERSISTENCE | -0.0259 |

## JAX
Record: 1-0-0 · Points for/against: 34/10 · Point differential: 24 · Data confidence: low
Strongest area: **offense_overall** (0.589) · Weakest area: **rushing_defense** (0.049)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.090 | 11 | -0.376 | -0.376 | low |
| pass_rush | Pass-Rush Strength Index | 0.432 | 1 | 1.054 | 1.054 | low |
| passing_defense | Pass-Defense Strength Index | 0.069 | 9 | -0.507 | -0.507 | low |
| rushing_defense | Run-Defense Strength Index | 0.049 | 13 | -0.436 | -0.436 | low |
| offense_overall | Offensive Strength Index | 0.589 | 1 | 0.348 | 0.348 | low |
| pass_protection | Pass-Protection Strength Index | 0.107 | 9 | -0.110 | -0.110 | low |
| passing_offense | Passing-Offense Strength Index | 0.544 | 1 | 0.249 | 0.249 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.127 | 6 | 0.160 | 0.160 | low |
| special_teams | Special-Teams Strength Index | 0.134 | 11 | -0.610 | -0.610 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1250 | 0.1450 | 0.0327 | 1 | 24 | 0.1428 | -0.0679 | 0.0679 | 12 | 0.6452 | low | UNVALIDATED_RANK_PERSISTENT | 0.0087 |
| pass_protection.rush_stuffed_rate_approx | 0.2414 | 0.2045 | 0.0323 | 1 | 24 | 0.2067 | 0.0670 | -0.0670 | 21 | 0.3548 | low | RANK_PERSISTENT | 0.0005 |
| pass_protection.sack_rate_allowed | 0.0417 | 0.0664 | 0.0188 | 1 | 24 | 0.0637 | -0.1464 | 0.1464 | 10 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | -0.0009 |
| pass_rush.qb_hit_rate_generated | 0.2667 | 0.1442 | 0.0234 | 1 | 30 | 0.1514 | 0.3079 | 0.3079 | 3 | 0.9355 | low | RANK_PERSISTENT | 0.0146 |
| pass_rush.sack_rate_generated | 0.1667 | 0.0660 | 0.0121 | 1 | 30 | 0.0728 | 0.5566 | 0.5566 | 1 | 1.0000 | low | NOT_RANK_PERSISTENT | 0.0179 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 11 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0075 |
| special_teams.st_epa_per_play | 0.2731 | 0.0622 | 0.0928 | 1 | 11 | 0.0746 | 0.1336 | 0.1336 | 11 | 0.6774 | low | RANK_PERSISTENT | -0.0566 |
| team_defense.early_down_epa_per_play | -0.0791 | -0.0013 | 0.0639 | 1 | 51 | -0.0059 | -0.0716 | 0.0716 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0251 |
| team_defense.epa_per_play | -0.2057 | 0.0046 | 0.0677 | 1 | 51 | -0.0078 | -0.1826 | 0.1826 | 7 | 0.8065 | low | RANK_PERSISTENT | 0.0306 |
| team_defense.explosive_pass_rate | 0.1000 | 0.0797 | 0.0112 | 1 | 51 | 0.0810 | 0.1207 | -0.1207 | 22 | 0.3226 | low | NOT_RANK_PERSISTENT | 0.0091 |
| team_defense.explosive_rush_rate | 0.0526 | 0.1000 | 0.0206 | 1 | 51 | 0.0972 | -0.1352 | 0.1352 | 4 | 0.8871 | low | RANK_PERSISTENT | 0.0099 |
| team_defense.pass_epa_per_dropback | -0.2254 | 0.0361 | 0.0949 | 1 | 51 | 0.0207 | -0.1621 | 0.1621 | 7 | 0.8065 | low | RANK_PERSISTENT | 0.0613 |
| team_defense.pass_success_rate | 0.4667 | 0.4536 | 0.0320 | 1 | 51 | 0.4544 | 0.0239 | -0.0239 | 16 | 0.5161 | low | RANK_PERSISTENT | 0.0118 |
| team_defense.rush_epa_per_play | -0.1194 | -0.0760 | 0.0649 | 1 | 51 | -0.0789 | -0.0445 | 0.0445 | 12 | 0.6452 | low | NOT_RANK_PERSISTENT | 0.0134 |
| team_defense.rush_success_rate | 0.4211 | 0.4020 | 0.0330 | 1 | 51 | 0.4031 | 0.0340 | -0.0340 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0205 |
| team_defense.success_rate | 0.4314 | 0.4384 | 0.0255 | 1 | 51 | 0.4380 | -0.0162 | 0.0162 | 15 | 0.5484 | low | RANK_PERSISTENT | 0.0072 |
| team_offense.early_down_epa_per_play | 0.3255 | -0.0054 | 0.0784 | 1 | 54 | 0.0314 | 0.4689 | 0.4689 | 1 | 1.0000 | low | UNVALIDATED_RANK_PERSISTENT | 0.0182 |
| team_offense.epa_per_play | 0.3098 | -0.0001 | 0.0921 | 1 | 54 | 0.0343 | 0.3740 | 0.3740 | 3 | 0.9355 | low | VALIDATED_PERSISTENCE | 0.0080 |
| team_offense.explosive_pass_rate | 0.1667 | 0.0796 | 0.0177 | 1 | 54 | 0.0847 | 0.2889 | 0.2889 | 1 | 1.0000 | low | RANK_PERSISTENT | 0.0005 |
| team_offense.explosive_rush_rate | 0.1724 | 0.0990 | 0.0195 | 1 | 54 | 0.1033 | 0.2210 | 0.2210 | 4 | 0.9032 | low | NOT_RANK_PERSISTENT | 0.0153 |
| team_offense.pass_epa_per_dropback | 0.7926 | 0.0308 | 0.1280 | 1 | 54 | 0.1154 | 0.6614 | 0.6614 | 1 | 1.0000 | low | UNVALIDATED_RANK_PERSISTENT | 0.0464 |
| team_offense.pass_success_rate | 0.7083 | 0.4521 | 0.0418 | 1 | 54 | 0.4806 | 0.6808 | 0.6808 | 1 | 1.0000 | low | UNVALIDATED_RANK_PERSISTENT | 0.0149 |
| team_offense.proe | -0.0614 | -0.0477 | 0.0349 | 1 | 54 | -0.0504 | -0.0786 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0294 |
| team_offense.rush_epa_per_play | -0.0530 | -0.0806 | 0.0754 | 1 | 54 | -0.0790 | 0.0215 | 0.0215 | 13 | 0.6129 | low | RANK_PERSISTENT | -0.0023 |
| team_offense.rush_success_rate | 0.5172 | 0.4004 | 0.0385 | 1 | 54 | 0.4094 | 0.2334 | 0.2334 | 2 | 0.9677 | low | RANK_PERSISTENT | 0.0135 |
| team_offense.success_rate | 0.5926 | 0.4370 | 0.0337 | 1 | 54 | 0.4681 | 0.9226 | 0.9226 | 1 | 1.0000 | low | VALIDATED_PERSISTENCE | 0.0245 |

## KC
Record: 1-0-0 · Points for/against: 31/10 · Point differential: 21 · Data confidence: low
Strongest area: **defense_overall** (0.217) · Weakest area: **offense_overall** (-0.067)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.217 | 2 | 0.193 | 0.193 | low |
| pass_rush | Pass-Rush Strength Index | 0.162 | 5 | 0.030 | 0.030 | low |
| passing_defense | Pass-Defense Strength Index | 0.203 | 4 | 0.247 | 0.247 | low |
| rushing_defense | Run-Defense Strength Index | 0.164 | 5 | -0.163 | -0.163 | low |
| offense_overall | Offensive Strength Index | -0.067 | 18 | -0.325 | -0.325 | low |
| pass_protection | Pass-Protection Strength Index | 0.006 | 16 | 0.386 | 0.386 | low |
| passing_offense | Passing-Offense Strength Index | -0.047 | 19 | -0.138 | -0.138 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.138 | 5 | 0.010 | 0.010 | low |
| special_teams | Special-Teams Strength Index | 0.136 | 9 | -0.034 | -0.034 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1515 | 0.1450 | 0.0327 | 1 | 33 | 0.1457 | 0.0221 | -0.0221 | 17 | 0.4355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0216 |
| pass_protection.rush_stuffed_rate_approx | 0.1250 | 0.2045 | 0.0323 | 1 | 33 | 0.1999 | -0.1446 | 0.1446 | 5 | 0.8710 | low | RANK_PERSISTENT | 0.0226 |
| pass_protection.sack_rate_allowed | 0.0606 | 0.0664 | 0.0188 | 1 | 33 | 0.0658 | -0.0343 | 0.0343 | 15 | 0.5323 | low | UNVALIDATED_RANK_PERSISTENT | -0.0021 |
| pass_rush.qb_hit_rate_generated | 0.1515 | 0.1442 | 0.0234 | 1 | 33 | 0.1446 | 0.0185 | 0.0185 | 13 | 0.5645 | low | RANK_PERSISTENT | -0.0120 |
| pass_rush.sack_rate_generated | 0.1212 | 0.0660 | 0.0121 | 1 | 33 | 0.0697 | 0.3052 | 0.3052 | 4 | 0.9032 | low | NOT_RANK_PERSISTENT | 0.0069 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 12 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0003 |
| special_teams.st_epa_per_play | 0.2765 | 0.0622 | 0.0928 | 1 | 12 | 0.0748 | 0.1358 | 0.1358 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0031 |
| team_defense.early_down_epa_per_play | -0.1524 | -0.0013 | 0.0639 | 1 | 50 | -0.0102 | -0.1391 | 0.1391 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0075 |
| team_defense.epa_per_play | -0.3777 | 0.0046 | 0.0677 | 1 | 50 | -0.0179 | -0.3319 | 0.3319 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0162 |
| team_defense.explosive_pass_rate | 0.0000 | 0.0797 | 0.0112 | 1 | 50 | 0.0744 | -0.4735 | 0.4735 | 1 | 0.9355 | low | NOT_RANK_PERSISTENT | -0.0040 |
| team_defense.explosive_rush_rate | 0.0667 | 0.1000 | 0.0206 | 1 | 50 | 0.0980 | -0.0951 | 0.0951 | 9 | 0.7097 | low | RANK_PERSISTENT | 0.0117 |
| team_defense.pass_epa_per_dropback | -0.4429 | 0.0361 | 0.0949 | 1 | 50 | 0.0079 | -0.2970 | 0.2970 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0234 |
| team_defense.pass_success_rate | 0.3939 | 0.4536 | 0.0320 | 1 | 50 | 0.4501 | -0.1096 | 0.1096 | 7 | 0.7903 | low | RANK_PERSISTENT | -0.0079 |
| team_defense.rush_epa_per_play | -0.2283 | -0.0760 | 0.0649 | 1 | 50 | -0.0862 | -0.1564 | 0.1564 | 7 | 0.8065 | low | NOT_RANK_PERSISTENT | 0.0031 |
| team_defense.rush_success_rate | 0.2667 | 0.4020 | 0.0330 | 1 | 50 | 0.3940 | -0.2414 | 0.2414 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0042 |
| team_defense.success_rate | 0.3600 | 0.4384 | 0.0255 | 1 | 50 | 0.4338 | -0.1812 | 0.1812 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0057 |
| team_offense.early_down_epa_per_play | -0.1314 | -0.0054 | 0.0784 | 1 | 66 | -0.0194 | -0.1787 | -0.1787 | 23 | 0.2903 | low | UNVALIDATED_RANK_PERSISTENT | -0.0348 |
| team_offense.epa_per_play | 0.1183 | -0.0001 | 0.0921 | 1 | 66 | 0.0130 | 0.1428 | 0.1428 | 11 | 0.6774 | low | VALIDATED_PERSISTENCE | -0.0155 |
| team_offense.explosive_pass_rate | 0.0606 | 0.0796 | 0.0177 | 1 | 66 | 0.0785 | -0.0629 | -0.0629 | 18 | 0.4516 | low | RANK_PERSISTENT | 0.0008 |
| team_offense.explosive_rush_rate | 0.1250 | 0.0990 | 0.0195 | 1 | 66 | 0.1005 | 0.0782 | 0.0782 | 7 | 0.7903 | low | NOT_RANK_PERSISTENT | 0.0156 |
| team_offense.pass_epa_per_dropback | 0.0263 | 0.0308 | 0.1280 | 1 | 66 | 0.0303 | -0.0039 | -0.0039 | 17 | 0.4839 | low | UNVALIDATED_RANK_PERSISTENT | -0.0318 |
| team_offense.pass_success_rate | 0.4242 | 0.4521 | 0.0418 | 1 | 66 | 0.4490 | -0.0740 | -0.0740 | 19 | 0.4194 | low | UNVALIDATED_RANK_PERSISTENT | -0.0089 |
| team_offense.proe | -0.0114 | -0.0477 | 0.0349 | 1 | 66 | -0.0404 | 0.2085 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0354 |
| team_offense.rush_epa_per_play | 0.2585 | -0.0806 | 0.0754 | 1 | 66 | -0.0607 | 0.2647 | 0.2647 | 1 | 1.0000 | low | RANK_PERSISTENT | 0.0091 |
| team_offense.rush_success_rate | 0.4062 | 0.4004 | 0.0385 | 1 | 66 | 0.4008 | 0.0117 | 0.0117 | 17 | 0.4839 | low | RANK_PERSISTENT | -0.0039 |
| team_offense.success_rate | 0.4091 | 0.4370 | 0.0337 | 1 | 66 | 0.4314 | -0.1652 | -0.1652 | 22 | 0.3226 | low | VALIDATED_PERSISTENCE | -0.0122 |

## LA
Record: 0-1-0 · Points for/against: 7/27 · Point differential: -20 · Data confidence: low
Strongest area: **rushing_offense** (0.046) · Weakest area: **pass_rush** (-0.294)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.218 | 29 | -0.681 | -0.681 | low |
| pass_rush | Pass-Rush Strength Index | -0.294 | 31 | -0.753 | -0.753 | low |
| passing_defense | Pass-Defense Strength Index | -0.172 | 26 | -0.527 | -0.527 | low |
| rushing_defense | Run-Defense Strength Index | -0.195 | 31 | -0.562 | -0.562 | low |
| offense_overall | Offensive Strength Index | -0.146 | 23 | -1.672 | -1.672 | low |
| pass_protection | Pass-Protection Strength Index | -0.026 | 20 | -0.785 | -0.785 | low |
| passing_offense | Passing-Offense Strength Index | -0.187 | 28 | -1.282 | -1.282 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.046 | 14 | -1.069 | -1.069 | low |
| special_teams | Special-Teams Strength Index | -0.035 | 22 | 0.421 | 0.421 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2759 | 0.1450 | 0.0327 | 1 | 29 | 0.1595 | 0.4444 | -0.4444 | 31 | 0.0323 | low | UNVALIDATED_RANK_PERSISTENT | 0.0292 |
| pass_protection.rush_stuffed_rate_approx | 0.1481 | 0.2045 | 0.0323 | 1 | 29 | 0.2012 | -0.1025 | 0.1025 | 6 | 0.8387 | low | RANK_PERSISTENT | 0.0210 |
| pass_protection.sack_rate_allowed | 0.0000 | 0.0664 | 0.0188 | 1 | 29 | 0.0590 | -0.3929 | 0.3929 | 1 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | 0.0127 |
| pass_rush.qb_hit_rate_generated | 0.0556 | 0.1442 | 0.0234 | 1 | 36 | 0.1390 | -0.2227 | -0.2227 | 30 | 0.0645 | low | RANK_PERSISTENT | -0.0210 |
| pass_rush.sack_rate_generated | 0.0000 | 0.0660 | 0.0121 | 1 | 36 | 0.0616 | -0.3654 | -0.3654 | 28 | 0.0645 | low | NOT_RANK_PERSISTENT | -0.0074 |
| special_teams.fg_pct | — | 0.8507 | 0.0691 | 1 | 10 | — | — | — | — | — | low | NOT_RANK_PERSISTENT | — |
| special_teams.st_epa_per_play | 0.0075 | 0.0622 | 0.0928 | 1 | 10 | 0.0590 | -0.0347 | -0.0347 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0390 |
| team_defense.early_down_epa_per_play | 0.2050 | -0.0013 | 0.0639 | 1 | 65 | 0.0108 | 0.1900 | -0.1900 | 27 | 0.1613 | low | RANK_PERSISTENT | 0.0395 |
| team_defense.epa_per_play | 0.1902 | 0.0046 | 0.0677 | 1 | 65 | 0.0155 | 0.1611 | -0.1611 | 26 | 0.1935 | low | RANK_PERSISTENT | 0.0487 |
| team_defense.explosive_pass_rate | 0.0278 | 0.0797 | 0.0112 | 1 | 65 | 0.0762 | -0.3085 | 0.3085 | 8 | 0.7742 | low | NOT_RANK_PERSISTENT | -0.0039 |
| team_defense.explosive_rush_rate | 0.1429 | 0.1000 | 0.0206 | 1 | 65 | 0.1025 | 0.1225 | -0.1225 | 27 | 0.1613 | low | RANK_PERSISTENT | 0.0132 |
| team_defense.pass_epa_per_dropback | 0.2077 | 0.0361 | 0.0949 | 1 | 65 | 0.0462 | 0.1064 | -0.1064 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0577 |
| team_defense.pass_success_rate | 0.5833 | 0.4536 | 0.0320 | 1 | 65 | 0.4613 | 0.2381 | -0.2381 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0143 |
| team_defense.rush_epa_per_play | 0.1416 | -0.0760 | 0.0649 | 1 | 65 | -0.0615 | 0.2233 | -0.2233 | 30 | 0.0645 | low | NOT_RANK_PERSISTENT | 0.0264 |
| team_defense.rush_success_rate | 0.5357 | 0.4020 | 0.0330 | 1 | 65 | 0.4098 | 0.2386 | -0.2386 | 32 | 0.0000 | low | RANK_PERSISTENT | 0.0210 |
| team_defense.success_rate | 0.5692 | 0.4384 | 0.0255 | 1 | 65 | 0.4461 | 0.3024 | -0.3024 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0180 |
| team_offense.early_down_epa_per_play | -0.1079 | -0.0054 | 0.0784 | 1 | 60 | -0.0168 | -0.1452 | -0.1452 | 22 | 0.3226 | low | UNVALIDATED_RANK_PERSISTENT | -0.1235 |
| team_offense.epa_per_play | -0.2255 | -0.0001 | 0.0921 | 1 | 60 | -0.0252 | -0.2720 | -0.2720 | 28 | 0.1290 | low | VALIDATED_PERSISTENCE | -0.1265 |
| team_offense.explosive_pass_rate | 0.0690 | 0.0796 | 0.0177 | 1 | 60 | 0.0790 | -0.0352 | -0.0352 | 17 | 0.4839 | low | RANK_PERSISTENT | -0.0191 |
| team_offense.explosive_rush_rate | 0.0741 | 0.0990 | 0.0195 | 1 | 60 | 0.0975 | -0.0751 | -0.0751 | 20 | 0.3871 | low | NOT_RANK_PERSISTENT | -0.0118 |
| team_offense.pass_epa_per_dropback | -0.3516 | 0.0308 | 0.1280 | 1 | 60 | -0.0117 | -0.3320 | -0.3320 | 29 | 0.0968 | low | UNVALIDATED_RANK_PERSISTENT | -0.1733 |
| team_offense.pass_success_rate | 0.3793 | 0.4521 | 0.0418 | 1 | 60 | 0.4440 | -0.1933 | -0.1933 | 28 | 0.1290 | low | UNVALIDATED_RANK_PERSISTENT | -0.0592 |
| team_offense.proe | -0.2147 | -0.0477 | 0.0349 | 1 | 60 | -0.0811 | -0.9584 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0743 |
| team_offense.rush_epa_per_play | -0.1713 | -0.0806 | 0.0754 | 1 | 60 | -0.0859 | -0.0708 | -0.0708 | 24 | 0.2581 | low | RANK_PERSISTENT | -0.0578 |
| team_offense.rush_success_rate | 0.4815 | 0.4004 | 0.0385 | 1 | 60 | 0.4066 | 0.1620 | 0.1620 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0528 |
| team_offense.success_rate | 0.4333 | 0.4370 | 0.0337 | 1 | 60 | 0.4362 | -0.0215 | -0.0215 | 17 | 0.4839 | low | VALIDATED_PERSISTENCE | -0.0697 |

## LAC
Record: 0-1-0 · Points for/against: 14/26 · Point differential: -12 · Data confidence: low
Strongest area: **rushing_defense** (0.022) · Weakest area: **special_teams** (-0.286)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.117 | 23 | -0.688 | -0.688 | low |
| pass_rush | Pass-Rush Strength Index | -0.132 | 27 | -0.442 | -0.442 | low |
| passing_defense | Pass-Defense Strength Index | -0.180 | 28 | -0.681 | -0.681 | low |
| rushing_defense | Run-Defense Strength Index | 0.022 | 14 | -0.081 | -0.081 | low |
| offense_overall | Offensive Strength Index | -0.162 | 24 | 0.003 | 0.003 | low |
| pass_protection | Pass-Protection Strength Index | -0.005 | 19 | 0.972 | 0.972 | low |
| passing_offense | Passing-Offense Strength Index | -0.135 | 27 | 0.047 | 0.047 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.135 | 24 | -0.063 | -0.063 | low |
| special_teams | Special-Teams Strength Index | -0.286 | 32 | -0.438 | -0.438 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1143 | 0.1450 | 0.0327 | 1 | 35 | 0.1416 | -0.1043 | 0.1043 | 9 | 0.7419 | low | UNVALIDATED_RANK_PERSISTENT | -0.0416 |
| pass_protection.rush_stuffed_rate_approx | 0.2500 | 0.2045 | 0.0323 | 1 | 35 | 0.2072 | 0.0827 | -0.0827 | 22 | 0.3065 | low | RANK_PERSISTENT | -0.0207 |
| pass_protection.sack_rate_allowed | 0.0857 | 0.0664 | 0.0188 | 1 | 35 | 0.0686 | 0.1142 | -0.1142 | 24 | 0.2581 | low | UNVALIDATED_RANK_PERSISTENT | -0.0126 |
| pass_rush.qb_hit_rate_generated | 0.1282 | 0.1442 | 0.0234 | 1 | 39 | 0.1432 | -0.0401 | -0.0401 | 19 | 0.4032 | low | RANK_PERSISTENT | -0.0040 |
| pass_rush.sack_rate_generated | 0.0256 | 0.0660 | 0.0121 | 1 | 39 | 0.0634 | -0.2235 | -0.2235 | 26 | 0.1935 | low | NOT_RANK_PERSISTENT | -0.0086 |
| special_teams.fg_pct | — | 0.8507 | 0.0691 | 1 | 11 | — | — | — | — | — | low | NOT_RANK_PERSISTENT | — |
| special_teams.st_epa_per_play | -0.3890 | 0.0622 | 0.0928 | 1 | 11 | 0.0357 | -0.2859 | -0.2859 | 32 | 0.0000 | low | RANK_PERSISTENT | -0.0407 |
| team_defense.early_down_epa_per_play | 0.1342 | -0.0013 | 0.0639 | 1 | 72 | 0.0067 | 0.1248 | -0.1248 | 24 | 0.2581 | low | RANK_PERSISTENT | 0.0481 |
| team_defense.epa_per_play | 0.1391 | 0.0046 | 0.0677 | 1 | 72 | 0.0125 | 0.1168 | -0.1168 | 25 | 0.2258 | low | RANK_PERSISTENT | 0.0501 |
| team_defense.explosive_pass_rate | 0.0513 | 0.0797 | 0.0112 | 1 | 72 | 0.0778 | -0.1688 | 0.1688 | 11 | 0.6774 | low | NOT_RANK_PERSISTENT | 0.0072 |
| team_defense.explosive_rush_rate | 0.0667 | 0.1000 | 0.0206 | 1 | 72 | 0.0980 | -0.0951 | 0.0951 | 9 | 0.7097 | low | RANK_PERSISTENT | -0.0050 |
| team_defense.pass_epa_per_dropback | 0.2891 | 0.0361 | 0.0949 | 1 | 72 | 0.0510 | 0.1568 | -0.1568 | 24 | 0.2581 | low | RANK_PERSISTENT | 0.0662 |
| team_defense.pass_success_rate | 0.5641 | 0.4536 | 0.0320 | 1 | 72 | 0.4601 | 0.2028 | -0.2028 | 28 | 0.1290 | low | RANK_PERSISTENT | 0.0213 |
| team_defense.rush_epa_per_play | -0.0443 | -0.0760 | 0.0649 | 1 | 72 | -0.0739 | 0.0325 | -0.0325 | 22 | 0.3226 | low | NOT_RANK_PERSISTENT | 0.0265 |
| team_defense.rush_success_rate | 0.4000 | 0.4020 | 0.0330 | 1 | 72 | 0.4019 | -0.0035 | 0.0035 | 12 | 0.5968 | low | RANK_PERSISTENT | 0.0025 |
| team_defense.success_rate | 0.4861 | 0.4384 | 0.0255 | 1 | 72 | 0.4412 | 0.1103 | -0.1103 | 27 | 0.1613 | low | RANK_PERSISTENT | 0.0146 |
| team_offense.early_down_epa_per_play | -0.0516 | -0.0054 | 0.0784 | 1 | 55 | -0.0105 | -0.0655 | -0.0655 | 20 | 0.3871 | low | UNVALIDATED_RANK_PERSISTENT | 0.0219 |
| team_offense.epa_per_play | -0.1668 | -0.0001 | 0.0921 | 1 | 55 | -0.0186 | -0.2011 | -0.2011 | 24 | 0.2581 | low | VALIDATED_PERSISTENCE | -0.0077 |
| team_offense.explosive_pass_rate | 0.0571 | 0.0796 | 0.0177 | 1 | 55 | 0.0783 | -0.0744 | -0.0744 | 20 | 0.3871 | low | RANK_PERSISTENT | 0.0056 |
| team_offense.explosive_rush_rate | 0.0625 | 0.0990 | 0.0195 | 1 | 55 | 0.0969 | -0.1100 | -0.1100 | 25 | 0.2258 | low | NOT_RANK_PERSISTENT | 0.0088 |
| team_offense.pass_epa_per_dropback | -0.1907 | 0.0308 | 0.1280 | 1 | 55 | 0.0062 | -0.1923 | -0.1923 | 24 | 0.2581 | low | UNVALIDATED_RANK_PERSISTENT | -0.0045 |
| team_offense.pass_success_rate | 0.4000 | 0.4521 | 0.0418 | 1 | 55 | 0.4463 | -0.1384 | -0.1384 | 23 | 0.2903 | low | UNVALIDATED_RANK_PERSISTENT | -0.0059 |
| team_offense.proe | -0.0702 | -0.0477 | 0.0349 | 1 | 55 | -0.0522 | -0.1290 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0257 |
| team_offense.rush_epa_per_play | -0.3604 | -0.0806 | 0.0754 | 1 | 55 | -0.0971 | -0.2184 | -0.2184 | 29 | 0.0968 | low | RANK_PERSISTENT | -0.0168 |
| team_offense.rush_success_rate | 0.3750 | 0.4004 | 0.0385 | 1 | 55 | 0.3984 | -0.0507 | -0.0507 | 22 | 0.3226 | low | RANK_PERSISTENT | 0.0037 |
| team_offense.success_rate | 0.4000 | 0.4370 | 0.0337 | 1 | 55 | 0.4296 | -0.2191 | -0.2191 | 24 | 0.2581 | low | VALIDATED_PERSISTENCE | -0.0063 |

## LV
Record: 1-0-0 · Points for/against: 27/13 · Point differential: 14 · Data confidence: low
Strongest area: **pass_protection** (0.333) · Weakest area: **offense_overall** (-0.120)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.155 | 4 | 0.225 | 0.225 | low |
| pass_rush | Pass-Rush Strength Index | 0.316 | 2 | 0.467 | 0.467 | low |
| passing_defense | Pass-Defense Strength Index | 0.144 | 6 | 0.556 | 0.556 | low |
| rushing_defense | Run-Defense Strength Index | 0.262 | 2 | 0.233 | 0.233 | low |
| offense_overall | Offensive Strength Index | -0.120 | 19 | 1.217 | 1.217 | low |
| pass_protection | Pass-Protection Strength Index | 0.333 | 3 | 1.525 | 1.525 | low |
| passing_offense | Passing-Offense Strength Index | -0.088 | 23 | 0.652 | 0.652 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.023 | 17 | 1.464 | 1.464 | low |
| special_teams | Special-Teams Strength Index | 0.247 | 2 | 0.390 | 0.390 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0645 | 0.1450 | 0.0327 | 1 | 31 | 0.1361 | -0.2733 | 0.2733 | 4 | 0.9032 | low | UNVALIDATED_RANK_PERSISTENT | -0.0388 |
| pass_protection.rush_stuffed_rate_approx | 0.2727 | 0.2045 | 0.0323 | 1 | 31 | 0.2085 | 0.1240 | -0.1240 | 27 | 0.1452 | low | RANK_PERSISTENT | -0.0393 |
| pass_protection.sack_rate_allowed | 0.0000 | 0.0664 | 0.0188 | 1 | 31 | 0.0590 | -0.3929 | 0.3929 | 1 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0350 |
| pass_rush.qb_hit_rate_generated | 0.2432 | 0.1442 | 0.0234 | 1 | 37 | 0.1500 | 0.2490 | 0.2490 | 5 | 0.8710 | low | RANK_PERSISTENT | 0.0094 |
| pass_rush.sack_rate_generated | 0.1351 | 0.0660 | 0.0121 | 1 | 37 | 0.0707 | 0.3822 | 0.3822 | 3 | 0.9355 | low | NOT_RANK_PERSISTENT | 0.0064 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 11 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0273 |
| special_teams.st_epa_per_play | 0.4525 | 0.0622 | 0.0928 | 1 | 11 | 0.0852 | 0.2473 | 0.2473 | 2 | 0.9677 | low | RANK_PERSISTENT | 0.0362 |
| team_defense.early_down_epa_per_play | -0.0413 | -0.0013 | 0.0639 | 1 | 55 | -0.0037 | -0.0368 | 0.0368 | 15 | 0.5484 | low | RANK_PERSISTENT | 0.0103 |
| team_defense.epa_per_play | -0.2421 | 0.0046 | 0.0677 | 1 | 55 | -0.0099 | -0.2142 | 0.2142 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0278 |
| team_defense.explosive_pass_rate | 0.1351 | 0.0797 | 0.0112 | 1 | 55 | 0.0834 | 0.3295 | -0.3295 | 28 | 0.1290 | low | NOT_RANK_PERSISTENT | 0.0130 |
| team_defense.explosive_rush_rate | 0.0667 | 0.1000 | 0.0206 | 1 | 55 | 0.0980 | -0.0951 | 0.0951 | 9 | 0.7097 | low | RANK_PERSISTENT | -0.0008 |
| team_defense.pass_epa_per_dropback | -0.2059 | 0.0361 | 0.0949 | 1 | 55 | 0.0219 | -0.1501 | 0.1501 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0501 |
| team_defense.pass_success_rate | 0.3784 | 0.4536 | 0.0320 | 1 | 55 | 0.4492 | -0.1382 | 0.1382 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0187 |
| team_defense.rush_epa_per_play | -0.3987 | -0.0760 | 0.0649 | 1 | 55 | -0.0975 | -0.3313 | 0.3313 | 3 | 0.9355 | low | NOT_RANK_PERSISTENT | -0.0137 |
| team_defense.rush_success_rate | 0.2000 | 0.4020 | 0.0330 | 1 | 55 | 0.3901 | -0.3603 | 0.3603 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0148 |
| team_defense.success_rate | 0.3455 | 0.4384 | 0.0255 | 1 | 55 | 0.4329 | -0.2148 | 0.2148 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0109 |
| team_offense.early_down_epa_per_play | -0.2099 | -0.0054 | 0.0784 | 1 | 65 | -0.0281 | -0.2899 | -0.2899 | 30 | 0.0645 | low | UNVALIDATED_RANK_PERSISTENT | 0.0848 |
| team_offense.epa_per_play | -0.0288 | -0.0001 | 0.0921 | 1 | 65 | -0.0033 | -0.0346 | -0.0346 | 20 | 0.3871 | low | VALIDATED_PERSISTENCE | 0.1273 |
| team_offense.explosive_pass_rate | 0.0323 | 0.0796 | 0.0177 | 1 | 65 | 0.0768 | -0.1570 | -0.1570 | 24 | 0.2581 | low | RANK_PERSISTENT | 0.0063 |
| team_offense.explosive_rush_rate | 0.1212 | 0.0990 | 0.0195 | 1 | 65 | 0.1003 | 0.0668 | 0.0668 | 9 | 0.7258 | low | NOT_RANK_PERSISTENT | 0.0111 |
| team_offense.pass_epa_per_dropback | 0.0073 | 0.0308 | 0.1280 | 1 | 65 | 0.0282 | -0.0204 | -0.0204 | 19 | 0.4194 | low | UNVALIDATED_RANK_PERSISTENT | 0.1311 |
| team_offense.pass_success_rate | 0.4194 | 0.4521 | 0.0418 | 1 | 65 | 0.4484 | -0.0869 | -0.0869 | 20 | 0.3871 | low | UNVALIDATED_RANK_PERSISTENT | 0.0240 |
| team_offense.proe | -0.0713 | -0.0477 | 0.0349 | 1 | 65 | -0.0524 | -0.1355 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0018 |
| team_offense.rush_epa_per_play | -0.0828 | -0.0806 | 0.0754 | 1 | 65 | -0.0807 | -0.0017 | -0.0017 | 16 | 0.5161 | low | RANK_PERSISTENT | 0.1150 |
| team_offense.rush_success_rate | 0.4242 | 0.4004 | 0.0385 | 1 | 65 | 0.4022 | 0.0477 | 0.0477 | 13 | 0.6129 | low | RANK_PERSISTENT | 0.0540 |
| team_offense.success_rate | 0.4308 | 0.4370 | 0.0337 | 1 | 65 | 0.4357 | -0.0367 | -0.0367 | 19 | 0.4194 | low | VALIDATED_PERSISTENCE | 0.0401 |

## MIA
Record: 0-1-0 · Points for/against: 13/27 · Point differential: -14 · Data confidence: low
Strongest area: **defense_overall** (0.080) · Weakest area: **pass_protection** (-0.370)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.080 | 13 | 0.801 | 0.801 | low |
| pass_rush | Pass-Rush Strength Index | -0.283 | 30 | -0.091 | -0.091 | low |
| passing_defense | Pass-Defense Strength Index | 0.040 | 14 | 0.981 | 0.981 | low |
| rushing_defense | Run-Defense Strength Index | -0.031 | 19 | 0.320 | 0.320 | low |
| offense_overall | Offensive Strength Index | -0.295 | 29 | -0.190 | -0.190 | low |
| pass_protection | Pass-Protection Strength Index | -0.370 | 31 | -0.507 | -0.507 | low |
| passing_offense | Passing-Offense Strength Index | -0.072 | 21 | 0.078 | 0.078 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.324 | 32 | -0.526 | -0.526 | low |
| special_teams | Special-Teams Strength Index | -0.093 | 26 | -0.864 | -0.864 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2432 | 0.1450 | 0.0327 | 1 | 37 | 0.1559 | 0.3336 | -0.3336 | 28 | 0.1290 | low | UNVALIDATED_RANK_PERSISTENT | 0.0261 |
| pass_protection.rush_stuffed_rate_approx | 0.4000 | 0.2045 | 0.0323 | 1 | 37 | 0.2160 | 0.3554 | -0.3554 | 32 | 0.0000 | low | RANK_PERSISTENT | -0.0013 |
| pass_protection.sack_rate_allowed | 0.1351 | 0.0664 | 0.0188 | 1 | 37 | 0.0740 | 0.4066 | -0.4066 | 30 | 0.0645 | low | UNVALIDATED_RANK_PERSISTENT | 0.0040 |
| pass_rush.qb_hit_rate_generated | 0.0645 | 0.1442 | 0.0234 | 1 | 31 | 0.1395 | -0.2002 | -0.2002 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0042 |
| pass_rush.sack_rate_generated | 0.0000 | 0.0660 | 0.0121 | 1 | 31 | 0.0616 | -0.3654 | -0.3654 | 28 | 0.0645 | low | NOT_RANK_PERSISTENT | -0.0044 |
| special_teams.fg_pct | 0.6667 | 0.8507 | 0.0691 | 1 | 14 | 0.8399 | -0.1566 | -0.1566 | 23 | 0.1481 | low | NOT_RANK_PERSISTENT | -0.0522 |
| special_teams.st_epa_per_play | -0.0850 | 0.0622 | 0.0928 | 1 | 14 | 0.0536 | -0.0933 | -0.0933 | 26 | 0.1935 | low | RANK_PERSISTENT | -0.0802 |
| team_defense.early_down_epa_per_play | -0.2099 | -0.0013 | 0.0639 | 1 | 65 | -0.0136 | -0.1921 | 0.1921 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0537 |
| team_defense.epa_per_play | -0.0288 | 0.0046 | 0.0677 | 1 | 65 | 0.0026 | -0.0290 | 0.0290 | 13 | 0.6129 | low | RANK_PERSISTENT | -0.0442 |
| team_defense.explosive_pass_rate | 0.0323 | 0.0797 | 0.0112 | 1 | 65 | 0.0765 | -0.2818 | 0.2818 | 9 | 0.7419 | low | NOT_RANK_PERSISTENT | -0.0059 |
| team_defense.explosive_rush_rate | 0.1212 | 0.1000 | 0.0206 | 1 | 65 | 0.1012 | 0.0607 | -0.0607 | 23 | 0.2742 | low | RANK_PERSISTENT | -0.0084 |
| team_defense.pass_epa_per_dropback | 0.0073 | 0.0361 | 0.0949 | 1 | 65 | 0.0344 | -0.0179 | 0.0179 | 14 | 0.5806 | low | RANK_PERSISTENT | -0.0720 |
| team_defense.pass_success_rate | 0.4194 | 0.4536 | 0.0320 | 1 | 65 | 0.4516 | -0.0629 | 0.0629 | 13 | 0.6129 | low | RANK_PERSISTENT | -0.0385 |
| team_defense.rush_epa_per_play | -0.0828 | -0.0760 | 0.0649 | 1 | 65 | -0.0765 | -0.0070 | 0.0070 | 17 | 0.4839 | low | NOT_RANK_PERSISTENT | -0.0170 |
| team_defense.rush_success_rate | 0.4242 | 0.4020 | 0.0330 | 1 | 65 | 0.4033 | 0.0397 | -0.0397 | 20 | 0.3871 | low | RANK_PERSISTENT | -0.0097 |
| team_defense.success_rate | 0.4308 | 0.4384 | 0.0255 | 1 | 65 | 0.4379 | -0.0176 | 0.0176 | 14 | 0.5806 | low | RANK_PERSISTENT | -0.0232 |
| team_offense.early_down_epa_per_play | -0.0413 | -0.0054 | 0.0784 | 1 | 55 | -0.0094 | -0.0509 | -0.0509 | 18 | 0.4516 | low | UNVALIDATED_RANK_PERSISTENT | -0.0214 |
| team_offense.epa_per_play | -0.2421 | -0.0001 | 0.0921 | 1 | 55 | -0.0270 | -0.2919 | -0.2919 | 29 | 0.0968 | low | VALIDATED_PERSISTENCE | -0.0125 |
| team_offense.explosive_pass_rate | 0.1351 | 0.0796 | 0.0177 | 1 | 55 | 0.0828 | 0.1843 | 0.1843 | 5 | 0.8710 | low | RANK_PERSISTENT | 0.0025 |
| team_offense.explosive_rush_rate | 0.0667 | 0.0990 | 0.0195 | 1 | 55 | 0.0971 | -0.0974 | -0.0974 | 22 | 0.2903 | low | NOT_RANK_PERSISTENT | -0.0193 |
| team_offense.pass_epa_per_dropback | -0.2059 | 0.0308 | 0.1280 | 1 | 55 | 0.0045 | -0.2055 | -0.2055 | 25 | 0.2258 | low | UNVALIDATED_RANK_PERSISTENT | -0.0006 |
| team_offense.pass_success_rate | 0.3784 | 0.4521 | 0.0418 | 1 | 55 | 0.4439 | -0.1958 | -0.1958 | 29 | 0.0968 | low | UNVALIDATED_RANK_PERSISTENT | 0.0041 |
| team_offense.proe | -0.0812 | -0.0477 | 0.0349 | 1 | 55 | -0.0544 | -0.1922 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0178 |
| team_offense.rush_epa_per_play | -0.3987 | -0.0806 | 0.0754 | 1 | 55 | -0.0993 | -0.2483 | -0.2483 | 30 | 0.0645 | low | RANK_PERSISTENT | -0.0456 |
| team_offense.rush_success_rate | 0.2000 | 0.4004 | 0.0385 | 1 | 55 | 0.3850 | -0.4001 | -0.4001 | 32 | 0.0000 | low | RANK_PERSISTENT | -0.0172 |
| team_offense.success_rate | 0.3455 | 0.4370 | 0.0337 | 1 | 55 | 0.4187 | -0.5425 | -0.5425 | 30 | 0.0645 | low | VALIDATED_PERSISTENCE | -0.0054 |

## MIN
Record: 1-0-0 · Points for/against: 39/22 · Point differential: 17 · Data confidence: low
Strongest area: **pass_rush** (0.286) · Weakest area: **offense_overall** (-0.225)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.064 | 14 | -0.558 | -0.558 | low |
| pass_rush | Pass-Rush Strength Index | 0.286 | 4 | -0.739 | -0.739 | low |
| passing_defense | Pass-Defense Strength Index | 0.067 | 10 | -0.809 | -0.809 | low |
| rushing_defense | Run-Defense Strength Index | 0.182 | 3 | 0.159 | 0.159 | low |
| offense_overall | Offensive Strength Index | -0.225 | 27 | 0.168 | 0.168 | low |
| pass_protection | Pass-Protection Strength Index | -0.136 | 24 | 1.277 | 1.277 | low |
| passing_offense | Passing-Offense Strength Index | -0.123 | 25 | 0.498 | 0.498 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.096 | 23 | -0.436 | -0.436 | low |
| special_teams | Special-Teams Strength Index | 0.089 | 15 | -0.231 | -0.231 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1667 | 0.1450 | 0.0327 | 1 | 30 | 0.1474 | 0.0736 | -0.0736 | 22 | 0.3065 | low | UNVALIDATED_RANK_PERSISTENT | -0.0443 |
| pass_protection.rush_stuffed_rate_approx | 0.1786 | 0.2045 | 0.0323 | 1 | 30 | 0.2030 | -0.0472 | 0.0472 | 13 | 0.6129 | low | RANK_PERSISTENT | 0.0030 |
| pass_protection.sack_rate_allowed | 0.1000 | 0.0664 | 0.0188 | 1 | 30 | 0.0701 | 0.1987 | -0.1987 | 27 | 0.1613 | low | UNVALIDATED_RANK_PERSISTENT | -0.0226 |
| pass_rush.qb_hit_rate_generated | 0.3261 | 0.1442 | 0.0234 | 1 | 46 | 0.1549 | 0.4572 | 0.4572 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0082 |
| pass_rush.sack_rate_generated | 0.0870 | 0.0660 | 0.0121 | 1 | 46 | 0.0674 | 0.1157 | 0.1157 | 8 | 0.7742 | low | NOT_RANK_PERSISTENT | -0.0136 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 15 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | -0.0387 |
| special_teams.st_epa_per_play | 0.2031 | 0.0622 | 0.0928 | 1 | 15 | 0.0705 | 0.0893 | 0.0893 | 15 | 0.5484 | low | RANK_PERSISTENT | -0.0215 |
| team_defense.early_down_epa_per_play | 0.1076 | -0.0013 | 0.0639 | 1 | 68 | 0.0051 | 0.1003 | -0.1003 | 23 | 0.2903 | low | RANK_PERSISTENT | 0.0523 |
| team_defense.epa_per_play | -0.1813 | 0.0046 | 0.0677 | 1 | 68 | -0.0063 | -0.1614 | 0.1614 | 8 | 0.7742 | low | RANK_PERSISTENT | 0.0360 |
| team_defense.explosive_pass_rate | 0.1522 | 0.0797 | 0.0112 | 1 | 68 | 0.0845 | 0.4308 | -0.4308 | 29 | 0.0968 | low | NOT_RANK_PERSISTENT | 0.0151 |
| team_defense.explosive_rush_rate | 0.0909 | 0.1000 | 0.0206 | 1 | 68 | 0.0994 | -0.0258 | 0.0258 | 16 | 0.5000 | low | RANK_PERSISTENT | 0.0043 |
| team_defense.pass_epa_per_dropback | -0.0588 | 0.0361 | 0.0949 | 1 | 68 | 0.0305 | -0.0588 | 0.0588 | 11 | 0.6774 | low | RANK_PERSISTENT | 0.0759 |
| team_defense.pass_success_rate | 0.4130 | 0.4536 | 0.0320 | 1 | 68 | 0.4513 | -0.0745 | 0.0745 | 11 | 0.6774 | low | RANK_PERSISTENT | 0.0262 |
| team_defense.rush_epa_per_play | -0.4376 | -0.0760 | 0.0649 | 1 | 68 | -0.1001 | -0.3711 | 0.3711 | 2 | 0.9677 | low | NOT_RANK_PERSISTENT | -0.0193 |
| team_defense.rush_success_rate | 0.3182 | 0.4020 | 0.0330 | 1 | 68 | 0.3970 | -0.1495 | 0.1495 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0128 |
| team_defense.success_rate | 0.3824 | 0.4384 | 0.0255 | 1 | 68 | 0.4351 | -0.1295 | 0.1295 | 7 | 0.8065 | low | RANK_PERSISTENT | 0.0082 |
| team_offense.early_down_epa_per_play | -0.2792 | -0.0054 | 0.0784 | 1 | 61 | -0.0358 | -0.3881 | -0.3881 | 32 | 0.0000 | low | UNVALIDATED_RANK_PERSISTENT | -0.0002 |
| team_offense.epa_per_play | 0.0553 | -0.0001 | 0.0921 | 1 | 61 | 0.0060 | 0.0669 | 0.0669 | 14 | 0.5806 | low | VALIDATED_PERSISTENCE | 0.0702 |
| team_offense.explosive_pass_rate | 0.0333 | 0.0796 | 0.0177 | 1 | 61 | 0.0769 | -0.1534 | -0.1534 | 23 | 0.2903 | low | RANK_PERSISTENT | 0.0031 |
| team_offense.explosive_rush_rate | 0.0357 | 0.0990 | 0.0195 | 1 | 61 | 0.0953 | -0.1906 | -0.1906 | 31 | 0.0323 | low | NOT_RANK_PERSISTENT | -0.0113 |
| team_offense.pass_epa_per_dropback | 0.0426 | 0.0308 | 0.1280 | 1 | 61 | 0.0321 | 0.0103 | 0.0103 | 16 | 0.5161 | low | UNVALIDATED_RANK_PERSISTENT | 0.1283 |
| team_offense.pass_success_rate | 0.3667 | 0.4521 | 0.0418 | 1 | 61 | 0.4426 | -0.2269 | -0.2269 | 30 | 0.0645 | low | UNVALIDATED_RANK_PERSISTENT | 0.0133 |
| team_offense.proe | -0.1288 | -0.0477 | 0.0349 | 1 | 61 | -0.0639 | -0.4652 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0239 |
| team_offense.rush_epa_per_play | -0.1245 | -0.0806 | 0.0754 | 1 | 61 | -0.0832 | -0.0343 | -0.0343 | 22 | 0.3226 | low | RANK_PERSISTENT | -0.0124 |
| team_offense.rush_success_rate | 0.3214 | 0.4004 | 0.0385 | 1 | 61 | 0.3943 | -0.1576 | -0.1576 | 23 | 0.2903 | low | RANK_PERSISTENT | -0.0273 |
| team_offense.success_rate | 0.3770 | 0.4370 | 0.0337 | 1 | 61 | 0.4250 | -0.3552 | -0.3552 | 27 | 0.1613 | low | VALIDATED_PERSISTENCE | -0.0086 |

## NE
Record: 0-1-0 · Points for/against: 10/13 · Point differential: -3 · Data confidence: low
Strongest area: **pass_rush** (0.120) · Weakest area: **rushing_offense** (-0.322)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.009 | 16 | -0.016 | -0.016 | low |
| pass_rush | Pass-Rush Strength Index | 0.120 | 9 | 0.251 | 0.251 | low |
| passing_defense | Pass-Defense Strength Index | -0.084 | 22 | -0.302 | -0.302 | low |
| rushing_defense | Run-Defense Strength Index | 0.114 | 9 | 0.160 | 0.160 | low |
| offense_overall | Offensive Strength Index | -0.172 | 25 | -1.279 | -1.279 | low |
| pass_protection | Pass-Protection Strength Index | 0.029 | 15 | 0.247 | 0.247 | low |
| passing_offense | Passing-Offense Strength Index | -0.014 | 17 | -1.330 | -1.330 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.322 | 31 | -0.142 | -0.142 | low |
| special_teams | Special-Teams Strength Index | 0.027 | 17 | 0.096 | 0.096 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1190 | 0.1450 | 0.0327 | 1 | 42 | 0.1421 | -0.0881 | 0.0881 | 11 | 0.6774 | low | UNVALIDATED_RANK_PERSISTENT | -0.0030 |
| pass_protection.rush_stuffed_rate_approx | 0.3333 | 0.2045 | 0.0323 | 1 | 42 | 0.2121 | 0.2342 | -0.2342 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0027 |
| pass_protection.sack_rate_allowed | 0.0714 | 0.0664 | 0.0188 | 1 | 42 | 0.0670 | 0.0297 | -0.0297 | 19 | 0.4032 | low | UNVALIDATED_RANK_PERSISTENT | -0.0075 |
| pass_rush.qb_hit_rate_generated | 0.2222 | 0.1442 | 0.0234 | 1 | 27 | 0.1488 | 0.1962 | 0.1962 | 6 | 0.8387 | low | RANK_PERSISTENT | 0.0036 |
| pass_rush.sack_rate_generated | 0.0741 | 0.0660 | 0.0121 | 1 | 27 | 0.0666 | 0.0444 | 0.0444 | 12 | 0.6452 | low | NOT_RANK_PERSISTENT | 0.0042 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 10 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0124 |
| special_teams.st_epa_per_play | 0.1045 | 0.0622 | 0.0928 | 1 | 10 | 0.0647 | 0.0268 | 0.0268 | 17 | 0.4839 | low | RANK_PERSISTENT | 0.0089 |
| team_defense.early_down_epa_per_play | 0.0728 | -0.0013 | 0.0639 | 1 | 49 | 0.0031 | 0.0683 | -0.0683 | 20 | 0.3871 | low | RANK_PERSISTENT | 0.0016 |
| team_defense.epa_per_play | 0.0286 | 0.0046 | 0.0677 | 1 | 49 | 0.0060 | 0.0209 | -0.0209 | 17 | 0.4839 | low | RANK_PERSISTENT | 0.0246 |
| team_defense.explosive_pass_rate | 0.1111 | 0.0797 | 0.0112 | 1 | 49 | 0.0818 | 0.1868 | -0.1868 | 25 | 0.2258 | low | NOT_RANK_PERSISTENT | 0.0067 |
| team_defense.explosive_rush_rate | 0.0952 | 0.1000 | 0.0206 | 1 | 49 | 0.0997 | -0.0135 | 0.0135 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0056 |
| team_defense.pass_epa_per_dropback | 0.2260 | 0.0361 | 0.0949 | 1 | 49 | 0.0473 | 0.1177 | -0.1177 | 23 | 0.2903 | low | RANK_PERSISTENT | 0.0494 |
| team_defense.pass_success_rate | 0.4815 | 0.4536 | 0.0320 | 1 | 49 | 0.4553 | 0.0511 | -0.0511 | 20 | 0.3871 | low | RANK_PERSISTENT | 0.0027 |
| team_defense.rush_epa_per_play | -0.1946 | -0.0760 | 0.0649 | 1 | 49 | -0.0839 | -0.1217 | 0.1217 | 8 | 0.7742 | low | NOT_RANK_PERSISTENT | -0.0073 |
| team_defense.rush_success_rate | 0.2857 | 0.4020 | 0.0330 | 1 | 49 | 0.3951 | -0.2074 | 0.2074 | 6 | 0.8387 | low | RANK_PERSISTENT | -0.0211 |
| team_defense.success_rate | 0.3878 | 0.4384 | 0.0255 | 1 | 49 | 0.4354 | -0.1170 | 0.1170 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0087 |
| team_offense.early_down_epa_per_play | -0.1720 | -0.0054 | 0.0784 | 1 | 71 | -0.0239 | -0.2362 | -0.2362 | 27 | 0.1613 | low | UNVALIDATED_RANK_PERSISTENT | -0.1044 |
| team_offense.epa_per_play | -0.0924 | -0.0001 | 0.0921 | 1 | 71 | -0.0104 | -0.1113 | -0.1113 | 22 | 0.3226 | low | VALIDATED_PERSISTENCE | -0.1154 |
| team_offense.explosive_pass_rate | 0.0000 | 0.0796 | 0.0177 | 1 | 71 | 0.0749 | -0.2640 | -0.2640 | 28 | 0.0645 | low | RANK_PERSISTENT | -0.0217 |
| team_offense.explosive_rush_rate | 0.0370 | 0.0990 | 0.0195 | 1 | 71 | 0.0954 | -0.1866 | -0.1866 | 30 | 0.0645 | low | NOT_RANK_PERSISTENT | -0.0029 |
| team_offense.pass_epa_per_dropback | 0.0655 | 0.0308 | 0.1280 | 1 | 71 | 0.0346 | 0.0301 | 0.0301 | 15 | 0.5484 | low | UNVALIDATED_RANK_PERSISTENT | -0.1823 |
| team_offense.pass_success_rate | 0.5238 | 0.4521 | 0.0418 | 1 | 71 | 0.4600 | 0.1906 | 0.1906 | 7 | 0.8065 | low | UNVALIDATED_RANK_PERSISTENT | -0.0562 |
| team_offense.proe | -0.0626 | -0.0477 | 0.0349 | 1 | 71 | -0.0507 | -0.0857 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0372 |
| team_offense.rush_epa_per_play | -0.4505 | -0.0806 | 0.0754 | 1 | 71 | -0.1024 | -0.2887 | -0.2887 | 32 | 0.0000 | low | RANK_PERSISTENT | -0.0174 |
| team_offense.rush_success_rate | 0.2222 | 0.4004 | 0.0385 | 1 | 71 | 0.3867 | -0.3557 | -0.3557 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0020 |
| team_offense.success_rate | 0.4085 | 0.4370 | 0.0337 | 1 | 71 | 0.4313 | -0.1690 | -0.1690 | 23 | 0.2903 | low | VALIDATED_PERSISTENCE | -0.0422 |

## NO
Record: 0-1-0 · Points for/against: 30/31 · Point differential: -1 · Data confidence: low
Strongest area: **passing_defense** (0.043) · Weakest area: **rushing_defense** (-0.150)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.002 | 17 | -0.398 | -0.398 | low |
| pass_rush | Pass-Rush Strength Index | -0.051 | 20 | -0.313 | -0.313 | low |
| passing_defense | Pass-Defense Strength Index | 0.043 | 12 | -0.258 | -0.258 | low |
| rushing_defense | Run-Defense Strength Index | -0.150 | 30 | -0.515 | -0.515 | low |
| offense_overall | Offensive Strength Index | 0.020 | 15 | 0.410 | 0.410 | low |
| pass_protection | Pass-Protection Strength Index | -0.042 | 21 | -0.156 | -0.156 | low |
| passing_offense | Passing-Offense Strength Index | 0.024 | 13 | 0.455 | 0.455 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.094 | 22 | 0.424 | 0.424 | low |
| special_teams | Special-Teams Strength Index | -0.134 | 29 | 0.829 | 0.829 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1452 | 0.1450 | 0.0327 | 1 | 62 | 0.1450 | 0.0006 | -0.0006 | 16 | 0.5161 | low | UNVALIDATED_RANK_PERSISTENT | 0.0154 |
| pass_protection.rush_stuffed_rate_approx | 0.1739 | 0.2045 | 0.0323 | 1 | 62 | 0.2027 | -0.0557 | 0.0557 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0029 |
| pass_protection.sack_rate_allowed | 0.0806 | 0.0664 | 0.0188 | 1 | 62 | 0.0680 | 0.0842 | -0.0842 | 23 | 0.2903 | low | UNVALIDATED_RANK_PERSISTENT | -0.0030 |
| pass_rush.qb_hit_rate_generated | 0.1951 | 0.1442 | 0.0234 | 1 | 41 | 0.1472 | 0.1281 | 0.1281 | 8 | 0.7742 | low | RANK_PERSISTENT | 0.0052 |
| pass_rush.sack_rate_generated | 0.0244 | 0.0660 | 0.0121 | 1 | 41 | 0.0633 | -0.2304 | -0.2304 | 27 | 0.1613 | low | NOT_RANK_PERSISTENT | -0.0102 |
| special_teams.fg_pct | 0.5000 | 0.8507 | 0.0691 | 1 | 16 | 0.8301 | -0.2984 | -0.2984 | 26 | 0.0370 | low | NOT_RANK_PERSISTENT | 0.0497 |
| special_teams.st_epa_per_play | -0.1488 | 0.0622 | 0.0928 | 1 | 16 | 0.0498 | -0.1337 | -0.1337 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0769 |
| team_defense.early_down_epa_per_play | -0.0070 | -0.0013 | 0.0639 | 1 | 77 | -0.0016 | -0.0052 | 0.0052 | 18 | 0.4516 | low | RANK_PERSISTENT | 0.0234 |
| team_defense.epa_per_play | -0.0272 | 0.0046 | 0.0677 | 1 | 77 | 0.0027 | -0.0276 | 0.0276 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0265 |
| team_defense.explosive_pass_rate | 0.0244 | 0.0797 | 0.0112 | 1 | 77 | 0.0760 | -0.3286 | 0.3286 | 6 | 0.8387 | low | NOT_RANK_PERSISTENT | -0.0027 |
| team_defense.explosive_rush_rate | 0.1944 | 0.1000 | 0.0206 | 1 | 77 | 0.1055 | 0.2699 | -0.2699 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0139 |
| team_defense.pass_epa_per_dropback | 0.0122 | 0.0361 | 0.0949 | 1 | 77 | 0.0347 | -0.0148 | 0.0148 | 15 | 0.5484 | low | RANK_PERSISTENT | 0.0252 |
| team_defense.pass_success_rate | 0.4146 | 0.4536 | 0.0320 | 1 | 77 | 0.4513 | -0.0716 | 0.0716 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0080 |
| team_defense.rush_epa_per_play | -0.0720 | -0.0760 | 0.0649 | 1 | 77 | -0.0757 | 0.0041 | -0.0041 | 19 | 0.4194 | low | NOT_RANK_PERSISTENT | 0.0331 |
| team_defense.rush_success_rate | 0.5000 | 0.4020 | 0.0330 | 1 | 77 | 0.4077 | 0.1749 | -0.1749 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0120 |
| team_defense.success_rate | 0.4545 | 0.4384 | 0.0255 | 1 | 77 | 0.4393 | 0.0373 | -0.0373 | 20 | 0.3871 | low | RANK_PERSISTENT | 0.0111 |
| team_offense.early_down_epa_per_play | -0.0138 | -0.0054 | 0.0784 | 1 | 88 | -0.0063 | -0.0120 | -0.0120 | 16 | 0.5161 | low | UNVALIDATED_RANK_PERSISTENT | 0.0225 |
| team_offense.epa_per_play | 0.0299 | -0.0001 | 0.0921 | 1 | 88 | 0.0032 | 0.0362 | 0.0362 | 15 | 0.5484 | low | VALIDATED_PERSISTENCE | 0.0551 |
| team_offense.explosive_pass_rate | 0.0968 | 0.0796 | 0.0177 | 1 | 88 | 0.0806 | 0.0571 | 0.0571 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0166 |
| team_offense.explosive_rush_rate | 0.0870 | 0.0990 | 0.0195 | 1 | 88 | 0.0983 | -0.0363 | -0.0363 | 18 | 0.4516 | low | NOT_RANK_PERSISTENT | 0.0154 |
| team_offense.pass_epa_per_dropback | 0.0006 | 0.0308 | 0.1280 | 1 | 88 | 0.0274 | -0.0262 | -0.0262 | 20 | 0.3871 | low | UNVALIDATED_RANK_PERSISTENT | 0.0495 |
| team_offense.pass_success_rate | 0.4677 | 0.4521 | 0.0418 | 1 | 88 | 0.4538 | 0.0416 | 0.0416 | 16 | 0.5161 | low | UNVALIDATED_RANK_PERSISTENT | 0.0016 |
| team_offense.proe | 0.0069 | -0.0477 | 0.0349 | 1 | 88 | -0.0368 | 0.3130 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0195 |
| team_offense.rush_epa_per_play | -0.0751 | -0.0806 | 0.0754 | 1 | 88 | -0.0803 | 0.0043 | 0.0043 | 15 | 0.5484 | low | RANK_PERSISTENT | 0.0389 |
| team_offense.rush_success_rate | 0.3043 | 0.4004 | 0.0385 | 1 | 88 | 0.3930 | -0.1917 | -0.1917 | 26 | 0.1935 | low | RANK_PERSISTENT | 0.0128 |
| team_offense.success_rate | 0.4432 | 0.4370 | 0.0337 | 1 | 88 | 0.4382 | 0.0369 | 0.0369 | 14 | 0.5806 | low | VALIDATED_PERSISTENCE | 0.0116 |

## NYG
Record: 1-0-0 · Points for/against: 28/20 · Point differential: 8 · Data confidence: low
Strongest area: **offense_overall** (0.558) · Weakest area: **pass_rush** (-0.259)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.132 | 26 | 0.527 | 0.527 | low |
| pass_rush | Pass-Rush Strength Index | -0.259 | 29 | -0.247 | -0.247 | low |
| passing_defense | Pass-Defense Strength Index | -0.103 | 23 | 0.005 | 0.005 | low |
| rushing_defense | Run-Defense Strength Index | 0.098 | 11 | 1.454 | 1.454 | low |
| offense_overall | Offensive Strength Index | 0.558 | 2 | 0.524 | 0.524 | low |
| pass_protection | Pass-Protection Strength Index | 0.006 | 16 | 0.555 | 0.555 | low |
| passing_offense | Passing-Offense Strength Index | 0.313 | 3 | 0.385 | 0.385 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.139 | 4 | -0.038 | -0.038 | low |
| special_teams | Special-Teams Strength Index | 0.004 | 18 | 0.226 | 0.226 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1515 | 0.1450 | 0.0327 | 1 | 33 | 0.1457 | 0.0221 | -0.0221 | 17 | 0.4355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0227 |
| pass_protection.rush_stuffed_rate_approx | 0.0909 | 0.2045 | 0.0323 | 1 | 33 | 0.1979 | -0.2066 | 0.2066 | 3 | 0.9355 | low | RANK_PERSISTENT | 0.0088 |
| pass_protection.sack_rate_allowed | 0.0606 | 0.0664 | 0.0188 | 1 | 33 | 0.0658 | -0.0343 | 0.0343 | 15 | 0.5323 | low | UNVALIDATED_RANK_PERSISTENT | -0.0078 |
| pass_rush.qb_hit_rate_generated | 0.0833 | 0.1442 | 0.0234 | 1 | 36 | 0.1406 | -0.1529 | -0.1529 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0065 |
| pass_rush.sack_rate_generated | 0.0000 | 0.0660 | 0.0121 | 1 | 36 | 0.0616 | -0.3654 | -0.3654 | 28 | 0.0645 | low | NOT_RANK_PERSISTENT | -0.0026 |
| special_teams.fg_pct | — | 0.8507 | 0.0691 | 1 | 9 | — | — | — | — | — | low | NOT_RANK_PERSISTENT | — |
| special_teams.st_epa_per_play | 0.0683 | 0.0622 | 0.0928 | 1 | 9 | 0.0626 | 0.0038 | 0.0038 | 18 | 0.4516 | low | RANK_PERSISTENT | 0.0210 |
| team_defense.early_down_epa_per_play | 0.0655 | -0.0013 | 0.0639 | 1 | 58 | 0.0026 | 0.0616 | -0.0616 | 19 | 0.4194 | low | RANK_PERSISTENT | -0.0357 |
| team_defense.epa_per_play | 0.2709 | 0.0046 | 0.0677 | 1 | 58 | 0.0203 | 0.2312 | -0.2312 | 28 | 0.1290 | low | RANK_PERSISTENT | -0.0314 |
| team_defense.explosive_pass_rate | 0.0000 | 0.0797 | 0.0112 | 1 | 58 | 0.0744 | -0.4735 | 0.4735 | 1 | 0.9355 | low | NOT_RANK_PERSISTENT | -0.0049 |
| team_defense.explosive_rush_rate | 0.0000 | 0.1000 | 0.0206 | 1 | 58 | 0.0941 | -0.2855 | 0.2855 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0345 |
| team_defense.pass_epa_per_dropback | 0.3144 | 0.0361 | 0.0949 | 1 | 58 | 0.0525 | 0.1725 | -0.1725 | 26 | 0.1935 | low | RANK_PERSISTENT | 0.0063 |
| team_defense.pass_success_rate | 0.4722 | 0.4536 | 0.0320 | 1 | 58 | 0.4547 | 0.0341 | -0.0341 | 19 | 0.4194 | low | RANK_PERSISTENT | -0.0025 |
| team_defense.rush_epa_per_play | -0.0999 | -0.0760 | 0.0649 | 1 | 58 | -0.0776 | -0.0245 | 0.0245 | 15 | 0.5484 | low | NOT_RANK_PERSISTENT | -0.1029 |
| team_defense.rush_success_rate | 0.4118 | 0.4020 | 0.0330 | 1 | 58 | 0.4026 | 0.0175 | -0.0175 | 17 | 0.4839 | low | RANK_PERSISTENT | -0.0364 |
| team_defense.success_rate | 0.4828 | 0.4384 | 0.0255 | 1 | 58 | 0.4410 | 0.1025 | -0.1025 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0142 |
| team_offense.early_down_epa_per_play | 0.2224 | -0.0054 | 0.0784 | 1 | 66 | 0.0199 | 0.3229 | 0.3229 | 5 | 0.8710 | low | UNVALIDATED_RANK_PERSISTENT | 0.0275 |
| team_offense.epa_per_play | 0.3629 | -0.0001 | 0.0921 | 1 | 66 | 0.0402 | 0.4380 | 0.4380 | 1 | 1.0000 | low | VALIDATED_PERSISTENCE | 0.0113 |
| team_offense.explosive_pass_rate | 0.0000 | 0.0796 | 0.0177 | 1 | 66 | 0.0749 | -0.2640 | -0.2640 | 28 | 0.0645 | low | RANK_PERSISTENT | -0.0066 |
| team_offense.explosive_rush_rate | 0.1212 | 0.0990 | 0.0195 | 1 | 66 | 0.1003 | 0.0668 | 0.0668 | 9 | 0.7258 | low | NOT_RANK_PERSISTENT | 0.0046 |
| team_offense.pass_epa_per_dropback | 0.6670 | 0.0308 | 0.1280 | 1 | 66 | 0.1015 | 0.5524 | 0.5524 | 2 | 0.9677 | low | UNVALIDATED_RANK_PERSISTENT | 0.0652 |
| team_offense.pass_success_rate | 0.6970 | 0.4521 | 0.0418 | 1 | 66 | 0.4793 | 0.6506 | 0.6506 | 2 | 0.9677 | low | UNVALIDATED_RANK_PERSISTENT | 0.0426 |
| team_offense.proe | -0.0434 | -0.0477 | 0.0349 | 1 | 66 | -0.0468 | 0.0250 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0302 |
| team_offense.rush_epa_per_play | 0.0587 | -0.0806 | 0.0754 | 1 | 66 | -0.0724 | 0.1087 | 0.1087 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0129 |
| team_offense.rush_success_rate | 0.4848 | 0.4004 | 0.0385 | 1 | 66 | 0.4069 | 0.1687 | 0.1687 | 4 | 0.9032 | low | RANK_PERSISTENT | 0.0037 |
| team_offense.success_rate | 0.5909 | 0.4370 | 0.0337 | 1 | 66 | 0.4677 | 0.9127 | 0.9127 | 2 | 0.9677 | low | VALIDATED_PERSISTENCE | 0.0371 |

## NYJ
Record: 1-0-0 · Points for/against: 23/10 · Point differential: 13 · Data confidence: low
Strongest area: **pass_protection** (0.377) · Weakest area: **rushing_defense** (-0.087)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.088 | 12 | 0.951 | 0.951 | low |
| pass_rush | Pass-Rush Strength Index | 0.010 | 14 | 0.968 | 0.968 | low |
| passing_defense | Pass-Defense Strength Index | 0.043 | 13 | 0.993 | 0.993 | low |
| rushing_defense | Run-Defense Strength Index | -0.087 | 23 | 0.189 | 0.189 | low |
| offense_overall | Offensive Strength Index | 0.229 | 7 | 1.035 | 1.035 | low |
| pass_protection | Pass-Protection Strength Index | 0.377 | 1 | 1.437 | 1.437 | low |
| passing_offense | Passing-Offense Strength Index | 0.217 | 6 | 1.183 | 1.183 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.088 | 10 | 0.109 | 0.109 | low |
| special_teams | Special-Teams Strength Index | 0.146 | 8 | -1.300 | -1.300 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0385 | 0.1450 | 0.0327 | 1 | 26 | 0.1332 | -0.3618 | 0.3618 | 1 | 1.0000 | low | UNVALIDATED_RANK_PERSISTENT | -0.0430 |
| pass_protection.rush_stuffed_rate_approx | 0.1944 | 0.2045 | 0.0323 | 1 | 26 | 0.2039 | -0.0183 | 0.0183 | 16 | 0.5161 | low | RANK_PERSISTENT | -0.0031 |
| pass_protection.sack_rate_allowed | 0.0000 | 0.0664 | 0.0188 | 1 | 26 | 0.0590 | -0.3929 | 0.3929 | 1 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0293 |
| pass_rush.qb_hit_rate_generated | 0.1282 | 0.1442 | 0.0234 | 1 | 39 | 0.1432 | -0.0401 | -0.0401 | 19 | 0.4032 | low | RANK_PERSISTENT | 0.0215 |
| pass_rush.sack_rate_generated | 0.0769 | 0.0660 | 0.0121 | 1 | 39 | 0.0668 | 0.0602 | 0.0602 | 11 | 0.6774 | low | NOT_RANK_PERSISTENT | 0.0122 |
| special_teams.fg_pct | 0.7500 | 0.8507 | 0.0691 | 1 | 12 | 0.8448 | -0.0857 | -0.0857 | 22 | 0.2222 | low | NOT_RANK_PERSISTENT | -0.0651 |
| special_teams.st_epa_per_play | 0.2927 | 0.0622 | 0.0928 | 1 | 12 | 0.0758 | 0.1461 | 0.1461 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.1207 |
| team_defense.early_down_epa_per_play | -0.1542 | -0.0013 | 0.0639 | 1 | 50 | -0.0103 | -0.1408 | 0.1408 | 7 | 0.8065 | low | RANK_PERSISTENT | -0.0808 |
| team_defense.epa_per_play | -0.1411 | 0.0046 | 0.0677 | 1 | 50 | -0.0040 | -0.1265 | 0.1265 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.0820 |
| team_defense.explosive_pass_rate | 0.0000 | 0.0797 | 0.0112 | 1 | 50 | 0.0744 | -0.4735 | 0.4735 | 1 | 0.9355 | low | NOT_RANK_PERSISTENT | -0.0158 |
| team_defense.explosive_rush_rate | 0.2000 | 0.1000 | 0.0206 | 1 | 50 | 0.1058 | 0.2857 | -0.2857 | 31 | 0.0323 | low | RANK_PERSISTENT | 0.0000 |
| team_defense.pass_epa_per_dropback | -0.1244 | 0.0361 | 0.0949 | 1 | 50 | 0.0267 | -0.0995 | 0.0995 | 10 | 0.7097 | low | RANK_PERSISTENT | -0.1389 |
| team_defense.pass_success_rate | 0.4615 | 0.4536 | 0.0320 | 1 | 50 | 0.4541 | 0.0145 | -0.0145 | 15 | 0.5484 | low | RANK_PERSISTENT | -0.0167 |
| team_defense.rush_epa_per_play | -0.0960 | -0.0760 | 0.0649 | 1 | 50 | -0.0773 | -0.0206 | 0.0206 | 16 | 0.5161 | low | NOT_RANK_PERSISTENT | -0.0241 |
| team_defense.rush_success_rate | 0.4000 | 0.4020 | 0.0330 | 1 | 50 | 0.4019 | -0.0035 | 0.0035 | 12 | 0.5968 | low | RANK_PERSISTENT | -0.0065 |
| team_defense.success_rate | 0.4400 | 0.4384 | 0.0255 | 1 | 50 | 0.4385 | 0.0037 | -0.0037 | 18 | 0.4516 | low | RANK_PERSISTENT | -0.0096 |
| team_offense.early_down_epa_per_play | 0.1740 | -0.0054 | 0.0784 | 1 | 64 | 0.0145 | 0.2542 | 0.2542 | 8 | 0.7742 | low | UNVALIDATED_RANK_PERSISTENT | 0.0746 |
| team_offense.epa_per_play | 0.1265 | -0.0001 | 0.0921 | 1 | 64 | 0.0139 | 0.1527 | 0.1527 | 10 | 0.7097 | low | VALIDATED_PERSISTENCE | 0.1019 |
| team_offense.explosive_pass_rate | 0.1538 | 0.0796 | 0.0177 | 1 | 64 | 0.0839 | 0.2464 | 0.2464 | 3 | 0.9355 | low | RANK_PERSISTENT | 0.0233 |
| team_offense.explosive_rush_rate | 0.0833 | 0.0990 | 0.0195 | 1 | 64 | 0.0981 | -0.0472 | -0.0472 | 19 | 0.4194 | low | NOT_RANK_PERSISTENT | -0.0000 |
| team_offense.pass_epa_per_dropback | 0.3501 | 0.0308 | 0.1280 | 1 | 64 | 0.0663 | 0.2773 | 0.2773 | 6 | 0.8387 | low | UNVALIDATED_RANK_PERSISTENT | 0.1571 |
| team_offense.pass_success_rate | 0.5000 | 0.4521 | 0.0418 | 1 | 64 | 0.4574 | 0.1273 | 0.1273 | 9 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | 0.0421 |
| team_offense.proe | -0.1201 | -0.0477 | 0.0349 | 1 | 64 | -0.0622 | -0.4155 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0317 |
| team_offense.rush_epa_per_play | -0.0378 | -0.0806 | 0.0754 | 1 | 64 | -0.0781 | 0.0334 | 0.0334 | 10 | 0.7097 | low | RANK_PERSISTENT | 0.0212 |
| team_offense.rush_success_rate | 0.4722 | 0.4004 | 0.0385 | 1 | 64 | 0.4059 | 0.1435 | 0.1435 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0024 |
| team_offense.success_rate | 0.4844 | 0.4370 | 0.0337 | 1 | 64 | 0.4464 | 0.2811 | 0.2811 | 7 | 0.8065 | low | VALIDATED_PERSISTENCE | 0.0353 |

## PHI
Record: 1-0-0 · Points for/against: 24/22 · Point differential: 2 · Data confidence: low
Strongest area: **passing_defense** (0.013) · Weakest area: **offense_overall** (-0.275)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.003 | 18 | -0.298 | -0.298 | low |
| pass_rush | Pass-Rush Strength Index | -0.225 | 28 | -0.455 | -0.455 | low |
| passing_defense | Pass-Defense Strength Index | 0.013 | 17 | -0.580 | -0.580 | low |
| rushing_defense | Run-Defense Strength Index | -0.029 | 18 | -0.041 | -0.041 | low |
| offense_overall | Offensive Strength Index | -0.275 | 28 | -0.334 | -0.334 | low |
| pass_protection | Pass-Protection Strength Index | -0.084 | 22 | -0.653 | -0.653 | low |
| passing_offense | Passing-Offense Strength Index | 0.000 | 16 | 0.009 | 0.009 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.171 | 27 | -0.344 | -0.344 | low |
| special_teams | Special-Teams Strength Index | 0.003 | 19 | 0.171 | 0.171 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1515 | 0.1450 | 0.0327 | 1 | 33 | 0.1457 | 0.0221 | -0.0221 | 17 | 0.4355 | low | UNVALIDATED_RANK_PERSISTENT | 0.0317 |
| pass_protection.rush_stuffed_rate_approx | 0.2632 | 0.2045 | 0.0323 | 1 | 33 | 0.2080 | 0.1066 | -0.1066 | 25 | 0.2097 | low | RANK_PERSISTENT | -0.0209 |
| pass_protection.sack_rate_allowed | 0.0909 | 0.0664 | 0.0188 | 1 | 33 | 0.0691 | 0.1450 | -0.1450 | 26 | 0.1935 | low | UNVALIDATED_RANK_PERSISTENT | 0.0063 |
| pass_rush.qb_hit_rate_generated | 0.0526 | 0.1442 | 0.0234 | 1 | 38 | 0.1388 | -0.2301 | -0.2301 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0151 |
| pass_rush.sack_rate_generated | 0.0263 | 0.0660 | 0.0121 | 1 | 38 | 0.0634 | -0.2198 | -0.2198 | 25 | 0.2258 | low | NOT_RANK_PERSISTENT | -0.0032 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 16 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0654 |
| special_teams.st_epa_per_play | 0.0677 | 0.0622 | 0.0928 | 1 | 16 | 0.0626 | 0.0034 | 0.0034 | 19 | 0.4194 | low | RANK_PERSISTENT | 0.0159 |
| team_defense.early_down_epa_per_play | -0.0462 | -0.0013 | 0.0639 | 1 | 69 | -0.0039 | -0.0413 | 0.0413 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0095 |
| team_defense.epa_per_play | 0.0733 | 0.0046 | 0.0677 | 1 | 69 | 0.0086 | 0.0597 | -0.0597 | 21 | 0.3548 | low | RANK_PERSISTENT | 0.0328 |
| team_defense.explosive_pass_rate | 0.0263 | 0.0797 | 0.0112 | 1 | 69 | 0.0761 | -0.3171 | 0.3171 | 7 | 0.8065 | low | NOT_RANK_PERSISTENT | -0.0002 |
| team_defense.explosive_rush_rate | 0.0690 | 0.1000 | 0.0206 | 1 | 69 | 0.0981 | -0.0885 | 0.0885 | 12 | 0.6452 | low | RANK_PERSISTENT | -0.0017 |
| team_defense.pass_epa_per_dropback | 0.1676 | 0.0361 | 0.0949 | 1 | 69 | 0.0439 | 0.0815 | -0.0815 | 21 | 0.3548 | low | RANK_PERSISTENT | 0.0618 |
| team_defense.pass_success_rate | 0.3947 | 0.4536 | 0.0320 | 1 | 69 | 0.4502 | -0.1081 | 0.1081 | 9 | 0.7419 | low | RANK_PERSISTENT | 0.0163 |
| team_defense.rush_epa_per_play | -0.0465 | -0.0760 | 0.0649 | 1 | 69 | -0.0740 | 0.0303 | -0.0303 | 21 | 0.3548 | low | NOT_RANK_PERSISTENT | 0.0172 |
| team_defense.rush_success_rate | 0.4828 | 0.4020 | 0.0330 | 1 | 69 | 0.4067 | 0.1441 | -0.1441 | 28 | 0.1290 | low | RANK_PERSISTENT | -0.0019 |
| team_defense.success_rate | 0.4348 | 0.4384 | 0.0255 | 1 | 69 | 0.4382 | -0.0083 | 0.0083 | 17 | 0.4839 | low | RANK_PERSISTENT | 0.0066 |
| team_offense.early_down_epa_per_play | -0.2043 | -0.0054 | 0.0784 | 1 | 53 | -0.0275 | -0.2819 | -0.2819 | 29 | 0.0968 | low | UNVALIDATED_RANK_PERSISTENT | -0.0241 |
| team_offense.epa_per_play | 0.0272 | -0.0001 | 0.0921 | 1 | 53 | 0.0029 | 0.0330 | 0.0330 | 17 | 0.4839 | low | VALIDATED_PERSISTENCE | -0.0203 |
| team_offense.explosive_pass_rate | 0.0909 | 0.0796 | 0.0177 | 1 | 53 | 0.0802 | 0.0376 | 0.0376 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0039 |
| team_offense.explosive_rush_rate | 0.0526 | 0.0990 | 0.0195 | 1 | 53 | 0.0963 | -0.1397 | -0.1397 | 28 | 0.1129 | low | NOT_RANK_PERSISTENT | -0.0118 |
| team_offense.pass_epa_per_dropback | 0.1658 | 0.0308 | 0.1280 | 1 | 53 | 0.0458 | 0.1173 | 0.1173 | 13 | 0.6129 | low | UNVALIDATED_RANK_PERSISTENT | -0.0161 |
| team_offense.pass_success_rate | 0.3939 | 0.4521 | 0.0418 | 1 | 53 | 0.4456 | -0.1545 | -0.1545 | 25 | 0.2097 | low | UNVALIDATED_RANK_PERSISTENT | -0.0029 |
| team_offense.proe | -0.0734 | -0.0477 | 0.0349 | 1 | 53 | -0.0528 | -0.1473 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | -0.0037 |
| team_offense.rush_epa_per_play | -0.1666 | -0.0806 | 0.0754 | 1 | 53 | -0.0857 | -0.0671 | -0.0671 | 23 | 0.2903 | low | RANK_PERSISTENT | -0.0225 |
| team_offense.rush_success_rate | 0.2632 | 0.4004 | 0.0385 | 1 | 53 | 0.3898 | -0.2740 | -0.2740 | 30 | 0.0645 | low | RANK_PERSISTENT | -0.0150 |
| team_offense.success_rate | 0.3396 | 0.4370 | 0.0337 | 1 | 53 | 0.4175 | -0.5770 | -0.5770 | 31 | 0.0323 | low | VALIDATED_PERSISTENCE | -0.0160 |

## PIT
Record: 1-0-0 · Points for/against: 20/13 · Point differential: 7 · Data confidence: low
Strongest area: **passing_defense** (0.333) · Weakest area: **offense_overall** (-0.362)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.241 | 1 | 0.170 | 0.170 | low |
| pass_rush | Pass-Rush Strength Index | 0.303 | 3 | 0.054 | 0.054 | low |
| passing_defense | Pass-Defense Strength Index | 0.333 | 1 | 0.363 | 0.363 | low |
| rushing_defense | Run-Defense Strength Index | -0.003 | 16 | 0.071 | 0.071 | low |
| offense_overall | Offensive Strength Index | -0.362 | 30 | -0.483 | -0.483 | low |
| pass_protection | Pass-Protection Strength Index | 0.068 | 12 | -0.583 | -0.583 | low |
| passing_offense | Passing-Offense Strength Index | -0.205 | 29 | -0.040 | -0.040 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.189 | 28 | -0.758 | -0.758 | low |
| special_teams | Special-Teams Strength Index | -0.002 | 20 | -0.407 | -0.407 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1395 | 0.1450 | 0.0327 | 1 | 43 | 0.1444 | -0.0185 | 0.0185 | 15 | 0.5484 | low | UNVALIDATED_RANK_PERSISTENT | 0.0255 |
| pass_protection.rush_stuffed_rate_approx | 0.2778 | 0.2045 | 0.0323 | 1 | 43 | 0.2088 | 0.1332 | -0.1332 | 29 | 0.0968 | low | RANK_PERSISTENT | 0.0143 |
| pass_protection.sack_rate_allowed | 0.0465 | 0.0664 | 0.0188 | 1 | 43 | 0.0642 | -0.1177 | 0.1177 | 11 | 0.6613 | low | UNVALIDATED_RANK_PERSISTENT | 0.0073 |
| pass_rush.qb_hit_rate_generated | 0.1923 | 0.1442 | 0.0234 | 1 | 26 | 0.1470 | 0.1210 | 0.1210 | 9 | 0.7419 | low | RANK_PERSISTENT | -0.0044 |
| pass_rush.sack_rate_generated | 0.1538 | 0.0660 | 0.0121 | 1 | 26 | 0.0719 | 0.4857 | 0.4857 | 2 | 0.9677 | low | NOT_RANK_PERSISTENT | 0.0035 |
| special_teams.fg_pct | 0.6667 | 0.8507 | 0.0691 | 1 | 13 | 0.8399 | -0.1566 | -0.1566 | 23 | 0.1481 | low | NOT_RANK_PERSISTENT | -0.0072 |
| special_teams.st_epa_per_play | 0.0586 | 0.0622 | 0.0928 | 1 | 13 | 0.0620 | -0.0023 | -0.0023 | 20 | 0.3871 | low | RANK_PERSISTENT | -0.0378 |
| team_defense.early_down_epa_per_play | -0.2658 | -0.0013 | 0.0639 | 1 | 60 | -0.0169 | -0.2435 | 0.2435 | 2 | 0.9677 | low | RANK_PERSISTENT | 0.0074 |
| team_defense.epa_per_play | -0.3577 | 0.0046 | 0.0677 | 1 | 60 | -0.0167 | -0.3146 | 0.3146 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0319 |
| team_defense.explosive_pass_rate | 0.1154 | 0.0797 | 0.0112 | 1 | 60 | 0.0821 | 0.2122 | -0.2122 | 26 | 0.1935 | low | NOT_RANK_PERSISTENT | 0.0035 |
| team_defense.explosive_rush_rate | 0.0938 | 0.1000 | 0.0206 | 1 | 60 | 0.0996 | -0.0177 | 0.0177 | 18 | 0.4516 | low | RANK_PERSISTENT | 0.0008 |
| team_defense.pass_epa_per_dropback | -0.6063 | 0.0361 | 0.0949 | 1 | 60 | -0.0017 | -0.3983 | 0.3983 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0430 |
| team_defense.pass_success_rate | 0.3077 | 0.4536 | 0.0320 | 1 | 60 | 0.4451 | -0.2679 | 0.2679 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0087 |
| team_defense.rush_epa_per_play | -0.1126 | -0.0760 | 0.0649 | 1 | 60 | -0.0784 | -0.0376 | 0.0376 | 13 | 0.6129 | low | NOT_RANK_PERSISTENT | -0.0250 |
| team_defense.rush_success_rate | 0.4375 | 0.4020 | 0.0330 | 1 | 60 | 0.4041 | 0.0634 | -0.0634 | 21 | 0.3387 | low | RANK_PERSISTENT | 0.0043 |
| team_defense.success_rate | 0.3667 | 0.4384 | 0.0255 | 1 | 60 | 0.4342 | -0.1658 | 0.1658 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0039 |
| team_offense.early_down_epa_per_play | -0.1460 | -0.0054 | 0.0784 | 1 | 65 | -0.0210 | -0.1994 | -0.1994 | 24 | 0.2581 | low | UNVALIDATED_RANK_PERSISTENT | -0.0196 |
| team_offense.epa_per_play | -0.2515 | -0.0001 | 0.0921 | 1 | 65 | -0.0281 | -0.3033 | -0.3033 | 30 | 0.0645 | low | VALIDATED_PERSISTENCE | -0.0468 |
| team_offense.explosive_pass_rate | 0.0698 | 0.0796 | 0.0177 | 1 | 65 | 0.0790 | -0.0325 | -0.0325 | 16 | 0.5161 | low | RANK_PERSISTENT | 0.0047 |
| team_offense.explosive_rush_rate | 0.0556 | 0.0990 | 0.0195 | 1 | 65 | 0.0965 | -0.1309 | -0.1309 | 27 | 0.1613 | low | NOT_RANK_PERSISTENT | -0.0072 |
| team_offense.pass_epa_per_dropback | -0.3239 | 0.0308 | 0.1280 | 1 | 65 | -0.0086 | -0.3080 | -0.3080 | 28 | 0.1290 | low | UNVALIDATED_RANK_PERSISTENT | -0.0428 |
| team_offense.pass_success_rate | 0.3488 | 0.4521 | 0.0418 | 1 | 65 | 0.4406 | -0.2743 | -0.2743 | 31 | 0.0323 | low | UNVALIDATED_RANK_PERSISTENT | -0.0021 |
| team_offense.proe | 0.0505 | -0.0477 | 0.0349 | 1 | 65 | -0.0281 | 0.5637 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0098 |
| team_offense.rush_epa_per_play | -0.2522 | -0.0806 | 0.0754 | 1 | 65 | -0.0907 | -0.1339 | -0.1339 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0509 |
| team_offense.rush_success_rate | 0.2778 | 0.4004 | 0.0385 | 1 | 65 | 0.3909 | -0.2448 | -0.2448 | 28 | 0.1290 | low | RANK_PERSISTENT | -0.0324 |
| team_offense.success_rate | 0.3385 | 0.4370 | 0.0337 | 1 | 65 | 0.4173 | -0.5839 | -0.5839 | 32 | 0.0000 | low | VALIDATED_PERSISTENCE | -0.0233 |

## SEA
Record: 1-0-0 · Points for/against: 13/10 · Point differential: 3 · Data confidence: low
Strongest area: **rushing_defense** (0.295) · Weakest area: **rushing_offense** (-0.159)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.104 | 8 | -0.635 | -0.635 | low |
| pass_rush | Pass-Rush Strength Index | -0.017 | 17 | -0.236 | -0.236 | low |
| passing_defense | Pass-Defense Strength Index | -0.074 | 21 | -0.706 | -0.706 | low |
| rushing_defense | Run-Defense Strength Index | 0.295 | 1 | -0.733 | -0.733 | low |
| offense_overall | Offensive Strength Index | -0.049 | 17 | -0.513 | -0.513 | low |
| pass_protection | Pass-Protection Strength Index | -0.154 | 25 | -0.715 | -0.715 | low |
| passing_offense | Passing-Offense Strength Index | 0.117 | 9 | -0.706 | -0.706 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.159 | 26 | -0.151 | -0.151 | low |
| special_teams | Special-Teams Strength Index | 0.037 | 16 | -0.604 | -0.604 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.2222 | 0.1450 | 0.0327 | 1 | 27 | 0.1536 | 0.2622 | -0.2622 | 27 | 0.1613 | low | UNVALIDATED_RANK_PERSISTENT | 0.0284 |
| pass_protection.rush_stuffed_rate_approx | 0.1905 | 0.2045 | 0.0323 | 1 | 27 | 0.2037 | -0.0256 | 0.0256 | 15 | 0.5484 | low | RANK_PERSISTENT | -0.0151 |
| pass_protection.sack_rate_allowed | 0.0741 | 0.0664 | 0.0188 | 1 | 27 | 0.0673 | 0.0454 | -0.0454 | 21 | 0.3548 | low | UNVALIDATED_RANK_PERSISTENT | 0.0106 |
| pass_rush.qb_hit_rate_generated | 0.1190 | 0.1442 | 0.0234 | 1 | 42 | 0.1427 | -0.0632 | -0.0632 | 22 | 0.3226 | low | RANK_PERSISTENT | -0.0095 |
| pass_rush.sack_rate_generated | 0.0714 | 0.0660 | 0.0121 | 1 | 42 | 0.0664 | 0.0298 | 0.0298 | 13 | 0.5968 | low | NOT_RANK_PERSISTENT | -0.0008 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 11 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0070 |
| special_teams.st_epa_per_play | 0.1209 | 0.0622 | 0.0928 | 1 | 11 | 0.0657 | 0.0372 | 0.0372 | 16 | 0.5161 | low | RANK_PERSISTENT | -0.0561 |
| team_defense.early_down_epa_per_play | -0.1720 | -0.0013 | 0.0639 | 1 | 71 | -0.0114 | -0.1572 | 0.1572 | 6 | 0.8387 | low | RANK_PERSISTENT | 0.0255 |
| team_defense.epa_per_play | -0.0924 | 0.0046 | 0.0677 | 1 | 71 | -0.0011 | -0.0842 | 0.0842 | 11 | 0.6774 | low | RANK_PERSISTENT | 0.0548 |
| team_defense.explosive_pass_rate | 0.0000 | 0.0797 | 0.0112 | 1 | 71 | 0.0744 | -0.4735 | 0.4735 | 1 | 0.9355 | low | NOT_RANK_PERSISTENT | 0.0034 |
| team_defense.explosive_rush_rate | 0.0370 | 0.1000 | 0.0206 | 1 | 71 | 0.0963 | -0.1797 | 0.1797 | 3 | 0.9355 | low | RANK_PERSISTENT | 0.0232 |
| team_defense.pass_epa_per_dropback | 0.0655 | 0.0361 | 0.0949 | 1 | 71 | 0.0378 | 0.0182 | -0.0182 | 18 | 0.4516 | low | RANK_PERSISTENT | 0.0607 |
| team_defense.pass_success_rate | 0.5238 | 0.4536 | 0.0320 | 1 | 71 | 0.4578 | 0.1288 | -0.1288 | 26 | 0.1935 | low | RANK_PERSISTENT | 0.0247 |
| team_defense.rush_epa_per_play | -0.4505 | -0.0760 | 0.0649 | 1 | 71 | -0.1010 | -0.3844 | 0.3844 | 1 | 1.0000 | low | NOT_RANK_PERSISTENT | 0.0460 |
| team_defense.rush_success_rate | 0.2222 | 0.4020 | 0.0330 | 1 | 71 | 0.3914 | -0.3207 | 0.3207 | 2 | 0.9677 | low | RANK_PERSISTENT | 0.0120 |
| team_defense.success_rate | 0.4085 | 0.4384 | 0.0255 | 1 | 71 | 0.4366 | -0.0692 | 0.0692 | 10 | 0.7097 | low | RANK_PERSISTENT | 0.0177 |
| team_offense.early_down_epa_per_play | 0.0728 | -0.0054 | 0.0784 | 1 | 49 | 0.0033 | 0.1109 | 0.1109 | 13 | 0.6129 | low | UNVALIDATED_RANK_PERSISTENT | -0.0250 |
| team_offense.epa_per_play | 0.0286 | -0.0001 | 0.0921 | 1 | 49 | 0.0031 | 0.0347 | 0.0347 | 16 | 0.5161 | low | VALIDATED_PERSISTENCE | -0.0217 |
| team_offense.explosive_pass_rate | 0.1111 | 0.0796 | 0.0177 | 1 | 49 | 0.0814 | 0.1046 | 0.1046 | 8 | 0.7742 | low | RANK_PERSISTENT | -0.0138 |
| team_offense.explosive_rush_rate | 0.0952 | 0.0990 | 0.0195 | 1 | 49 | 0.0988 | -0.0114 | -0.0114 | 14 | 0.5806 | low | NOT_RANK_PERSISTENT | -0.0048 |
| team_offense.pass_epa_per_dropback | 0.2260 | 0.0308 | 0.1280 | 1 | 49 | 0.0525 | 0.1695 | 0.1695 | 10 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | -0.0372 |
| team_offense.pass_success_rate | 0.4815 | 0.4521 | 0.0418 | 1 | 49 | 0.4553 | 0.0781 | 0.0781 | 13 | 0.6129 | low | UNVALIDATED_RANK_PERSISTENT | -0.0438 |
| team_offense.proe | -0.0757 | -0.0477 | 0.0349 | 1 | 49 | -0.0533 | -0.1605 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0285 |
| team_offense.rush_epa_per_play | -0.1946 | -0.0806 | 0.0754 | 1 | 49 | -0.0873 | -0.0890 | -0.0890 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0092 |
| team_offense.rush_success_rate | 0.2857 | 0.4004 | 0.0385 | 1 | 49 | 0.3915 | -0.2290 | -0.2290 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0069 |
| team_offense.success_rate | 0.3878 | 0.4370 | 0.0337 | 1 | 49 | 0.4271 | -0.2917 | -0.2917 | 25 | 0.2258 | low | VALIDATED_PERSISTENCE | -0.0332 |

## SF
Record: 1-0-0 · Points for/against: 27/7 · Point differential: 20 · Data confidence: low
Strongest area: **offense_overall** (0.437) · Weakest area: **special_teams** (-0.082)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.103 | 9 | 0.783 | 0.783 | low |
| pass_rush | Pass-Rush Strength Index | -0.017 | 18 | 1.354 | 1.354 | low |
| passing_defense | Pass-Defense Strength Index | 0.188 | 5 | 0.800 | 0.800 | low |
| rushing_defense | Run-Defense Strength Index | 0.010 | 15 | 0.206 | 0.206 | low |
| offense_overall | Offensive Strength Index | 0.437 | 4 | -0.254 | -0.254 | low |
| pass_protection | Pass-Protection Strength Index | 0.348 | 2 | -0.212 | -0.212 | low |
| passing_offense | Passing-Offense Strength Index | 0.110 | 10 | -0.560 | -0.560 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.222 | 1 | -0.073 | -0.073 | low |
| special_teams | Special-Teams Strength Index | -0.082 | 25 | -0.882 | -0.882 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0556 | 0.1450 | 0.0327 | 1 | 36 | 0.1351 | -0.3037 | 0.3037 | 3 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | -0.0007 |
| pass_protection.rush_stuffed_rate_approx | 0.0714 | 0.2045 | 0.0323 | 1 | 36 | 0.1967 | -0.2420 | 0.2420 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0025 |
| pass_protection.sack_rate_allowed | 0.0000 | 0.0664 | 0.0188 | 1 | 36 | 0.0590 | -0.3929 | 0.3929 | 1 | 0.9355 | low | UNVALIDATED_RANK_PERSISTENT | 0.0084 |
| pass_rush.qb_hit_rate_generated | 0.2759 | 0.1442 | 0.0234 | 1 | 29 | 0.1519 | 0.3310 | 0.3310 | 2 | 0.9677 | low | RANK_PERSISTENT | 0.0354 |
| pass_rush.sack_rate_generated | 0.0000 | 0.0660 | 0.0121 | 1 | 29 | 0.0616 | -0.3654 | -0.3654 | 28 | 0.0645 | low | NOT_RANK_PERSISTENT | 0.0144 |
| special_teams.fg_pct | 0.6667 | 0.8507 | 0.0691 | 1 | 10 | 0.8399 | -0.1566 | -0.1566 | 23 | 0.1481 | low | NOT_RANK_PERSISTENT | -0.0448 |
| special_teams.st_epa_per_play | -0.0671 | 0.0622 | 0.0928 | 1 | 10 | 0.0546 | -0.0819 | -0.0819 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0819 |
| team_defense.early_down_epa_per_play | -0.1079 | -0.0013 | 0.0639 | 1 | 60 | -0.0076 | -0.0981 | 0.0981 | 11 | 0.6774 | low | RANK_PERSISTENT | -0.0465 |
| team_defense.epa_per_play | -0.2255 | 0.0046 | 0.0677 | 1 | 60 | -0.0089 | -0.1998 | 0.1998 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0472 |
| team_defense.explosive_pass_rate | 0.0690 | 0.0797 | 0.0112 | 1 | 60 | 0.0790 | -0.0637 | 0.0637 | 16 | 0.5161 | low | NOT_RANK_PERSISTENT | 0.0038 |
| team_defense.explosive_rush_rate | 0.0741 | 0.1000 | 0.0206 | 1 | 60 | 0.0984 | -0.0739 | 0.0739 | 13 | 0.6129 | low | RANK_PERSISTENT | 0.0074 |
| team_defense.pass_epa_per_dropback | -0.3516 | 0.0361 | 0.0949 | 1 | 60 | 0.0133 | -0.2404 | 0.2404 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0779 |
| team_defense.pass_success_rate | 0.3793 | 0.4536 | 0.0320 | 1 | 60 | 0.4493 | -0.1365 | 0.1365 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0250 |
| team_defense.rush_epa_per_play | -0.1713 | -0.0760 | 0.0649 | 1 | 60 | -0.0823 | -0.0978 | 0.0978 | 9 | 0.7419 | low | NOT_RANK_PERSISTENT | -0.0099 |
| team_defense.rush_success_rate | 0.4815 | 0.4020 | 0.0330 | 1 | 60 | 0.4067 | 0.1418 | -0.1418 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0271 |
| team_defense.success_rate | 0.4333 | 0.4384 | 0.0255 | 1 | 60 | 0.4381 | -0.0117 | 0.0117 | 16 | 0.5161 | low | RANK_PERSISTENT | -0.0236 |
| team_offense.early_down_epa_per_play | 0.2050 | -0.0054 | 0.0784 | 1 | 65 | 0.0180 | 0.2982 | 0.2982 | 6 | 0.8387 | low | UNVALIDATED_RANK_PERSISTENT | 0.0037 |
| team_offense.epa_per_play | 0.1902 | -0.0001 | 0.0921 | 1 | 65 | 0.0210 | 0.2296 | 0.2296 | 7 | 0.8065 | low | VALIDATED_PERSISTENCE | -0.0408 |
| team_offense.explosive_pass_rate | 0.0278 | 0.0796 | 0.0177 | 1 | 65 | 0.0765 | -0.1718 | -0.1718 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0042 |
| team_offense.explosive_rush_rate | 0.1429 | 0.0990 | 0.0195 | 1 | 65 | 0.1016 | 0.1320 | 0.1320 | 6 | 0.8387 | low | NOT_RANK_PERSISTENT | 0.0094 |
| team_offense.pass_epa_per_dropback | 0.2077 | 0.0308 | 0.1280 | 1 | 65 | 0.0504 | 0.1536 | 0.1536 | 11 | 0.6774 | low | UNVALIDATED_RANK_PERSISTENT | -0.0732 |
| team_offense.pass_success_rate | 0.5833 | 0.4521 | 0.0418 | 1 | 65 | 0.4667 | 0.3487 | 0.3487 | 4 | 0.9032 | low | UNVALIDATED_RANK_PERSISTENT | -0.0365 |
| team_offense.proe | 0.0358 | -0.0477 | 0.0349 | 1 | 65 | -0.0310 | 0.4791 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0025 |
| team_offense.rush_epa_per_play | 0.1416 | -0.0806 | 0.0754 | 1 | 65 | -0.0675 | 0.1734 | 0.1734 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0115 |
| team_offense.rush_success_rate | 0.5357 | 0.4004 | 0.0385 | 1 | 65 | 0.4108 | 0.2703 | 0.2703 | 1 | 1.0000 | low | RANK_PERSISTENT | 0.0003 |
| team_offense.success_rate | 0.5692 | 0.4370 | 0.0337 | 1 | 65 | 0.4634 | 0.7841 | 0.7841 | 3 | 0.9355 | low | VALIDATED_PERSISTENCE | -0.0124 |

## TB
Record: 0-1-0 · Points for/against: 27/33 · Point differential: -6 · Data confidence: low
Strongest area: **special_teams** (0.214) · Weakest area: **pass_protection** (-0.169)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.054 | 21 | 0.190 | 0.190 | low |
| pass_rush | Pass-Rush Strength Index | -0.085 | 23 | 0.210 | 0.210 | low |
| passing_defense | Pass-Defense Strength Index | -0.033 | 19 | 0.451 | 0.451 | low |
| rushing_defense | Run-Defense Strength Index | -0.099 | 25 | -0.482 | -0.482 | low |
| offense_overall | Offensive Strength Index | 0.111 | 13 | 0.071 | 0.071 | low |
| pass_protection | Pass-Protection Strength Index | -0.169 | 26 | -0.888 | -0.888 | low |
| passing_offense | Passing-Offense Strength Index | -0.078 | 22 | -0.098 | -0.098 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.148 | 3 | 0.170 | 0.170 | low |
| special_teams | Special-Teams Strength Index | 0.214 | 4 | 0.418 | 0.418 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1667 | 0.1450 | 0.0327 | 1 | 36 | 0.1474 | 0.0736 | -0.0736 | 22 | 0.3065 | low | UNVALIDATED_RANK_PERSISTENT | 0.0413 |
| pass_protection.rush_stuffed_rate_approx | 0.2941 | 0.2045 | 0.0323 | 1 | 36 | 0.2098 | 0.1629 | -0.1629 | 30 | 0.0645 | low | RANK_PERSISTENT | 0.0021 |
| pass_protection.sack_rate_allowed | 0.1111 | 0.0664 | 0.0188 | 1 | 36 | 0.0714 | 0.2645 | -0.2645 | 28 | 0.1290 | low | UNVALIDATED_RANK_PERSISTENT | 0.0096 |
| pass_rush.qb_hit_rate_generated | 0.1622 | 0.1442 | 0.0234 | 1 | 37 | 0.1452 | 0.0452 | 0.0452 | 12 | 0.6452 | low | RANK_PERSISTENT | 0.0061 |
| pass_rush.sack_rate_generated | 0.0270 | 0.0660 | 0.0121 | 1 | 37 | 0.0634 | -0.2158 | -0.2158 | 24 | 0.2581 | low | NOT_RANK_PERSISTENT | 0.0019 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 13 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0132 |
| special_teams.st_epa_per_play | 0.3999 | 0.0622 | 0.0928 | 1 | 13 | 0.0821 | 0.2140 | 0.2140 | 4 | 0.9032 | low | RANK_PERSISTENT | 0.0388 |
| team_defense.early_down_epa_per_play | 0.0821 | -0.0013 | 0.0639 | 1 | 63 | 0.0036 | 0.0768 | -0.0768 | 21 | 0.3548 | low | RANK_PERSISTENT | -0.0188 |
| team_defense.epa_per_play | 0.0013 | 0.0046 | 0.0677 | 1 | 63 | 0.0044 | -0.0028 | 0.0028 | 15 | 0.5484 | low | RANK_PERSISTENT | -0.0064 |
| team_defense.explosive_pass_rate | 0.0811 | 0.0797 | 0.0112 | 1 | 63 | 0.0798 | 0.0083 | -0.0083 | 18 | 0.4516 | low | NOT_RANK_PERSISTENT | -0.0033 |
| team_defense.explosive_rush_rate | 0.1600 | 0.1000 | 0.0206 | 1 | 63 | 0.1035 | 0.1715 | -0.1715 | 28 | 0.1290 | low | RANK_PERSISTENT | 0.0086 |
| team_defense.pass_epa_per_dropback | -0.0361 | 0.0361 | 0.0949 | 1 | 63 | 0.0319 | -0.0448 | 0.0448 | 12 | 0.6452 | low | RANK_PERSISTENT | -0.0300 |
| team_defense.pass_success_rate | 0.5135 | 0.4536 | 0.0320 | 1 | 63 | 0.4572 | 0.1099 | -0.1099 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0188 |
| team_defense.rush_epa_per_play | 0.0495 | -0.0760 | 0.0649 | 1 | 63 | -0.0676 | 0.1288 | -0.1288 | 25 | 0.2258 | low | NOT_RANK_PERSISTENT | 0.0307 |
| team_defense.rush_success_rate | 0.4000 | 0.4020 | 0.0330 | 1 | 63 | 0.4019 | -0.0035 | 0.0035 | 12 | 0.5968 | low | RANK_PERSISTENT | 0.0183 |
| team_defense.success_rate | 0.4762 | 0.4384 | 0.0255 | 1 | 63 | 0.4406 | 0.0873 | -0.0873 | 23 | 0.2903 | low | RANK_PERSISTENT | -0.0046 |
| team_offense.early_down_epa_per_play | -0.0398 | -0.0054 | 0.0784 | 1 | 56 | -0.0092 | -0.0489 | -0.0489 | 17 | 0.4839 | low | UNVALIDATED_RANK_PERSISTENT | -0.0177 |
| team_offense.epa_per_play | -0.0814 | -0.0001 | 0.0921 | 1 | 56 | -0.0092 | -0.0980 | -0.0980 | 21 | 0.3548 | low | VALIDATED_PERSISTENCE | -0.0130 |
| team_offense.explosive_pass_rate | 0.0556 | 0.0796 | 0.0177 | 1 | 56 | 0.0782 | -0.0797 | -0.0797 | 21 | 0.3548 | low | RANK_PERSISTENT | -0.0048 |
| team_offense.explosive_rush_rate | 0.0588 | 0.0990 | 0.0195 | 1 | 56 | 0.0967 | -0.1210 | -0.1210 | 26 | 0.1935 | low | NOT_RANK_PERSISTENT | 0.0081 |
| team_offense.pass_epa_per_dropback | -0.2925 | 0.0308 | 0.1280 | 1 | 56 | -0.0051 | -0.2807 | -0.2807 | 27 | 0.1613 | low | UNVALIDATED_RANK_PERSISTENT | -0.0431 |
| team_offense.pass_success_rate | 0.5000 | 0.4521 | 0.0418 | 1 | 56 | 0.4574 | 0.1273 | 0.1273 | 9 | 0.7097 | low | UNVALIDATED_RANK_PERSISTENT | 0.0132 |
| team_offense.proe | -0.0271 | -0.0477 | 0.0349 | 1 | 56 | -0.0436 | 0.1183 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0217 |
| team_offense.rush_epa_per_play | 0.1183 | -0.0806 | 0.0754 | 1 | 56 | -0.0689 | 0.1553 | 0.1553 | 4 | 0.9032 | low | RANK_PERSISTENT | 0.0151 |
| team_offense.rush_success_rate | 0.4706 | 0.4004 | 0.0385 | 1 | 56 | 0.4058 | 0.1402 | 0.1402 | 9 | 0.7419 | low | RANK_PERSISTENT | 0.0053 |
| team_offense.success_rate | 0.5179 | 0.4370 | 0.0337 | 1 | 56 | 0.4531 | 0.4796 | 0.4796 | 5 | 0.8710 | low | VALIDATED_PERSISTENCE | 0.0195 |

## TEN
Record: 0-1-0 · Points for/against: 10/23 · Point differential: -13 · Data confidence: low
Strongest area: **pass_protection** (-0.003) · Weakest area: **pass_rush** (-0.316)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | -0.124 | 25 | 0.483 | 0.483 | low |
| pass_rush | Pass-Rush Strength Index | -0.316 | 32 | -0.528 | -0.528 | low |
| passing_defense | Pass-Defense Strength Index | -0.140 | 25 | 0.559 | 0.559 | low |
| rushing_defense | Run-Defense Strength Index | -0.039 | 20 | -0.090 | -0.090 | low |
| offense_overall | Offensive Strength Index | -0.121 | 20 | 1.001 | 1.001 | low |
| pass_protection | Pass-Protection Strength Index | -0.003 | 18 | 0.627 | 0.627 | low |
| passing_offense | Passing-Offense Strength Index | -0.125 | 26 | 0.887 | 0.887 | low |
| rushing_offense | Rushing-Offense Strength Index | -0.006 | 21 | 0.310 | 0.310 | low |
| special_teams | Special-Teams Strength Index | -0.256 | 31 | -0.619 | -0.619 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.1282 | 0.1450 | 0.0327 | 1 | 39 | 0.1431 | -0.0570 | 0.0570 | 13 | 0.5968 | low | UNVALIDATED_RANK_PERSISTENT | -0.0191 |
| pass_protection.rush_stuffed_rate_approx | 0.0000 | 0.2045 | 0.0323 | 1 | 39 | 0.1925 | -0.3719 | 0.3719 | 1 | 1.0000 | low | RANK_PERSISTENT | -0.0068 |
| pass_protection.sack_rate_allowed | 0.0769 | 0.0664 | 0.0188 | 1 | 39 | 0.0676 | 0.0622 | -0.0622 | 22 | 0.3226 | low | UNVALIDATED_RANK_PERSISTENT | -0.0126 |
| pass_rush.qb_hit_rate_generated | 0.0385 | 0.1442 | 0.0234 | 1 | 26 | 0.1380 | -0.2657 | -0.2657 | 32 | 0.0000 | low | RANK_PERSISTENT | -0.0115 |
| pass_rush.sack_rate_generated | 0.0000 | 0.0660 | 0.0121 | 1 | 26 | 0.0616 | -0.3654 | -0.3654 | 28 | 0.0645 | low | NOT_RANK_PERSISTENT | -0.0068 |
| special_teams.fg_pct | 1.0000 | 0.8507 | 0.0691 | 1 | 15 | 0.8595 | 0.1270 | 0.1270 | 1 | 0.6481 | low | NOT_RANK_PERSISTENT | 0.0320 |
| special_teams.st_epa_per_play | -0.3421 | 0.0622 | 0.0928 | 1 | 15 | 0.0385 | -0.2562 | -0.2562 | 31 | 0.0323 | low | RANK_PERSISTENT | -0.0574 |
| team_defense.early_down_epa_per_play | 0.1740 | -0.0013 | 0.0639 | 1 | 64 | 0.0090 | 0.1614 | -0.1614 | 25 | 0.2258 | low | RANK_PERSISTENT | -0.0366 |
| team_defense.epa_per_play | 0.1265 | 0.0046 | 0.0677 | 1 | 64 | 0.0118 | 0.1058 | -0.1058 | 23 | 0.2903 | low | RANK_PERSISTENT | -0.0451 |
| team_defense.explosive_pass_rate | 0.1538 | 0.0797 | 0.0112 | 1 | 64 | 0.0846 | 0.4407 | -0.4407 | 30 | 0.0645 | low | NOT_RANK_PERSISTENT | -0.0047 |
| team_defense.explosive_rush_rate | 0.0833 | 0.1000 | 0.0206 | 1 | 64 | 0.0990 | -0.0475 | 0.0475 | 14 | 0.5806 | low | RANK_PERSISTENT | 0.0032 |
| team_defense.pass_epa_per_dropback | 0.3501 | 0.0361 | 0.0949 | 1 | 64 | 0.0546 | 0.1947 | -0.1947 | 27 | 0.1613 | low | RANK_PERSISTENT | -0.0588 |
| team_defense.pass_success_rate | 0.5000 | 0.4536 | 0.0320 | 1 | 64 | 0.4564 | 0.0851 | -0.0851 | 22 | 0.2903 | low | RANK_PERSISTENT | -0.0160 |
| team_defense.rush_epa_per_play | -0.0378 | -0.0760 | 0.0649 | 1 | 64 | -0.0734 | 0.0393 | -0.0393 | 23 | 0.2903 | low | NOT_RANK_PERSISTENT | -0.0158 |
| team_defense.rush_success_rate | 0.4722 | 0.4020 | 0.0330 | 1 | 64 | 0.4061 | 0.1253 | -0.1253 | 25 | 0.2258 | low | RANK_PERSISTENT | 0.0118 |
| team_defense.success_rate | 0.4844 | 0.4384 | 0.0255 | 1 | 64 | 0.4411 | 0.1063 | -0.1063 | 26 | 0.1935 | low | RANK_PERSISTENT | -0.0054 |
| team_offense.early_down_epa_per_play | -0.1542 | -0.0054 | 0.0784 | 1 | 50 | -0.0219 | -0.2110 | -0.2110 | 26 | 0.1935 | low | UNVALIDATED_RANK_PERSISTENT | 0.0516 |
| team_offense.epa_per_play | -0.1411 | -0.0001 | 0.0921 | 1 | 50 | -0.0158 | -0.1701 | -0.1701 | 23 | 0.2903 | low | VALIDATED_PERSISTENCE | 0.0852 |
| team_offense.explosive_pass_rate | 0.0000 | 0.0796 | 0.0177 | 1 | 50 | 0.0749 | -0.2640 | -0.2640 | 28 | 0.0645 | low | RANK_PERSISTENT | 0.0036 |
| team_offense.explosive_rush_rate | 0.2000 | 0.0990 | 0.0195 | 1 | 50 | 0.1050 | 0.3041 | 0.3041 | 2 | 0.9677 | low | NOT_RANK_PERSISTENT | 0.0083 |
| team_offense.pass_epa_per_dropback | -0.1244 | 0.0308 | 0.1280 | 1 | 50 | 0.0135 | -0.1348 | -0.1348 | 23 | 0.2903 | low | UNVALIDATED_RANK_PERSISTENT | 0.1372 |
| team_offense.pass_success_rate | 0.4615 | 0.4521 | 0.0418 | 1 | 50 | 0.4531 | 0.0251 | 0.0251 | 18 | 0.4516 | low | UNVALIDATED_RANK_PERSISTENT | 0.0579 |
| team_offense.proe | 0.0378 | -0.0477 | 0.0349 | 1 | 50 | -0.0306 | 0.4906 | 0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0351 |
| team_offense.rush_epa_per_play | -0.0960 | -0.0806 | 0.0754 | 1 | 50 | -0.0815 | -0.0120 | -0.0120 | 17 | 0.4839 | low | RANK_PERSISTENT | 0.0177 |
| team_offense.rush_success_rate | 0.4000 | 0.4004 | 0.0385 | 1 | 50 | 0.4003 | -0.0007 | -0.0007 | 18 | 0.4032 | low | RANK_PERSISTENT | 0.0148 |
| team_offense.success_rate | 0.4400 | 0.4370 | 0.0337 | 1 | 50 | 0.4376 | 0.0180 | 0.0180 | 15 | 0.5484 | low | VALIDATED_PERSISTENCE | 0.0479 |

## WAS
Record: 0-1-0 · Points for/against: 22/24 · Point differential: -2 · Data confidence: low
Strongest area: **pass_protection** (0.275) · Weakest area: **passing_offense** (-0.070)

### Domain indices
| domain | label | index_value | rank_of_league | delta_vs_prev_week | delta_vs_preseason | min_confidence |
| --- | --- | --- | --- | --- | --- | --- |
| defense_overall | Defensive Strength Index | 0.132 | 6 | 1.177 | 1.177 | low |
| pass_rush | Pass-Rush Strength Index | 0.078 | 11 | 0.044 | 0.044 | low |
| passing_defense | Pass-Defense Strength Index | 0.015 | 16 | 0.884 | 0.884 | low |
| rushing_defense | Run-Defense Strength Index | 0.159 | 6 | 0.815 | 0.815 | low |
| offense_overall | Offensive Strength Index | 0.006 | 16 | -0.420 | -0.420 | low |
| pass_protection | Pass-Protection Strength Index | 0.275 | 5 | 0.173 | 0.173 | low |
| passing_offense | Passing-Offense Strength Index | -0.070 | 20 | -0.134 | -0.134 | low |
| rushing_offense | Rushing-Offense Strength Index | 0.096 | 9 | -0.257 | -0.257 | low |
| special_teams | Special-Teams Strength Index | -0.032 | 21 | -0.345 | -0.345 | low |

### Underlying metrics
| metric | raw_value | ref_mean | ref_sd | n_games | n_opportunities | shrunk_value | z_shrunk | oriented_z_shrunk | rank_of_league | percentile | confidence | phase3_status | delta_shrunk_vs_prev_week |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pass_protection.qb_hit_rate_allowed | 0.0526 | 0.1450 | 0.0327 | 1 | 38 | 0.1347 | -0.3136 | 0.3136 | 2 | 0.9677 | low | UNVALIDATED_RANK_PERSISTENT | -0.0045 |
| pass_protection.rush_stuffed_rate_approx | 0.1724 | 0.2045 | 0.0323 | 1 | 38 | 0.2026 | -0.0584 | 0.0584 | 11 | 0.6774 | low | RANK_PERSISTENT | -0.0043 |
| pass_protection.sack_rate_allowed | 0.0263 | 0.0664 | 0.0188 | 1 | 38 | 0.0620 | -0.2372 | 0.2372 | 8 | 0.7742 | low | UNVALIDATED_RANK_PERSISTENT | -0.0039 |
| pass_rush.qb_hit_rate_generated | 0.1515 | 0.1442 | 0.0234 | 1 | 33 | 0.1446 | 0.0185 | 0.0185 | 13 | 0.5645 | low | RANK_PERSISTENT | 0.0011 |
| pass_rush.sack_rate_generated | 0.0909 | 0.0660 | 0.0121 | 1 | 33 | 0.0677 | 0.1375 | 0.1375 | 7 | 0.8065 | low | NOT_RANK_PERSISTENT | 0.0005 |
| special_teams.fg_pct | 0.5000 | 0.8507 | 0.0691 | 1 | 15 | 0.8301 | -0.2984 | -0.2984 | 26 | 0.0370 | low | NOT_RANK_PERSISTENT | 0.0227 |
| special_teams.st_epa_per_play | 0.0112 | 0.0622 | 0.0928 | 1 | 15 | 0.0592 | -0.0323 | -0.0323 | 21 | 0.3548 | low | RANK_PERSISTENT | -0.0321 |
| team_defense.early_down_epa_per_play | -0.2043 | -0.0013 | 0.0639 | 1 | 53 | -0.0132 | -0.1869 | 0.1869 | 4 | 0.9032 | low | RANK_PERSISTENT | -0.0890 |
| team_defense.epa_per_play | 0.0272 | 0.0046 | 0.0677 | 1 | 53 | 0.0059 | 0.0197 | -0.0197 | 16 | 0.5161 | low | RANK_PERSISTENT | -0.0745 |
| team_defense.explosive_pass_rate | 0.0909 | 0.0797 | 0.0112 | 1 | 53 | 0.0804 | 0.0667 | -0.0667 | 19 | 0.4194 | low | NOT_RANK_PERSISTENT | -0.0027 |
| team_defense.explosive_rush_rate | 0.0526 | 0.1000 | 0.0206 | 1 | 53 | 0.0972 | -0.1352 | 0.1352 | 4 | 0.8871 | low | RANK_PERSISTENT | -0.0119 |
| team_defense.pass_epa_per_dropback | 0.1658 | 0.0361 | 0.0949 | 1 | 53 | 0.0438 | 0.0804 | -0.0804 | 20 | 0.3871 | low | RANK_PERSISTENT | -0.0892 |
| team_defense.pass_success_rate | 0.3939 | 0.4536 | 0.0320 | 1 | 53 | 0.4501 | -0.1096 | 0.1096 | 7 | 0.7903 | low | RANK_PERSISTENT | -0.0266 |
| team_defense.rush_epa_per_play | -0.1666 | -0.0760 | 0.0649 | 1 | 53 | -0.0820 | -0.0930 | 0.0930 | 10 | 0.7097 | low | NOT_RANK_PERSISTENT | -0.0621 |
| team_defense.rush_success_rate | 0.2632 | 0.4020 | 0.0330 | 1 | 53 | 0.3938 | -0.2476 | 0.2476 | 3 | 0.9355 | low | RANK_PERSISTENT | -0.0300 |
| team_defense.success_rate | 0.3396 | 0.4384 | 0.0255 | 1 | 53 | 0.4326 | -0.2283 | 0.2283 | 2 | 0.9677 | low | RANK_PERSISTENT | -0.0265 |
| team_offense.early_down_epa_per_play | -0.0462 | -0.0054 | 0.0784 | 1 | 69 | -0.0099 | -0.0578 | -0.0578 | 19 | 0.4194 | low | UNVALIDATED_RANK_PERSISTENT | -0.0327 |
| team_offense.epa_per_play | 0.0733 | -0.0001 | 0.0921 | 1 | 69 | 0.0080 | 0.0886 | 0.0886 | 12 | 0.6452 | low | VALIDATED_PERSISTENCE | -0.0155 |
| team_offense.explosive_pass_rate | 0.0263 | 0.0796 | 0.0177 | 1 | 69 | 0.0764 | -0.1767 | -0.1767 | 26 | 0.1935 | low | RANK_PERSISTENT | 0.0013 |
| team_offense.explosive_rush_rate | 0.0690 | 0.0990 | 0.0195 | 1 | 69 | 0.0972 | -0.0905 | -0.0905 | 21 | 0.3548 | low | NOT_RANK_PERSISTENT | -0.0077 |
| team_offense.pass_epa_per_dropback | 0.1676 | 0.0308 | 0.1280 | 1 | 69 | 0.0460 | 0.1188 | 0.1188 | 12 | 0.6452 | low | UNVALIDATED_RANK_PERSISTENT | 0.0104 |
| team_offense.pass_success_rate | 0.3947 | 0.4521 | 0.0418 | 1 | 69 | 0.4457 | -0.1523 | -0.1523 | 24 | 0.2581 | low | UNVALIDATED_RANK_PERSISTENT | -0.0233 |
| team_offense.proe | -0.0763 | -0.0477 | 0.0349 | 1 | 69 | -0.0534 | -0.1638 | -0.0000 | — | — | low | VALIDATED_PERSISTENCE | 0.0185 |
| team_offense.rush_epa_per_play | -0.0465 | -0.0806 | 0.0754 | 1 | 69 | -0.0786 | 0.0266 | 0.0266 | 12 | 0.6452 | low | RANK_PERSISTENT | -0.0195 |
| team_offense.rush_success_rate | 0.4828 | 0.4004 | 0.0385 | 1 | 69 | 0.4067 | 0.1645 | 0.1645 | 5 | 0.8710 | low | RANK_PERSISTENT | -0.0098 |
| team_offense.success_rate | 0.4348 | 0.4370 | 0.0337 | 1 | 69 | 0.4365 | -0.0129 | -0.0129 | 16 | 0.5161 | low | VALIDATED_PERSISTENCE | -0.0228 |

