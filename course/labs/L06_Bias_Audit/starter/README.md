# Lab 6 — Dataset Bias Audit (C2)

**Session:** S11 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
Audit adult_like.csv: group-wise stats, representation gaps, 3 findings with numeric evidence.

## Dataset: `adult_like.csv`
| group | str | A/B | 70/30 representation bias planted |
| hours_per_week | float | hours | noisy for group B (measurement bias) |
| income_gt_50k | int | label | historical gap planted |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
