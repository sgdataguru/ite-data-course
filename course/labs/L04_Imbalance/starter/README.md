# Lab 4 — Imbalance & Algorithm-Aware Prep (C1)

**Session:** S08 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
Diagnose 990:10 fraud imbalance; apply under/over/SMOTE fold-safely; compare accuracy vs F1 vs recall.

## Dataset: `fraud.csv`
| txn_amount | float | amount | — |
| txn_distance_km | float | distance | — |
| txn_hour_dev | float | hour deviation | — |
| is_fraud | int | label | 990:10 imbalance |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
