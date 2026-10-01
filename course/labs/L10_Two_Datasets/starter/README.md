# Lab 10 — C2 Consolidation on Two Datasets (C2)

**Session:** S18 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
Full audit cycle on lending.csv; compare against adult_like findings.

## Dataset: `lending.csv`
| district | str | 5 SG districts | historical approval bias planted |
| credit_score | float | score | — |
| monthly_income | float | income | — |
| approved | int | label | 92:8 imbalance |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
