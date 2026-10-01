# Lab 3 — Encoding Categorical Data (C1)

**Session:** S06 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
One-hot town; ordinal-encode flat_type with explicit order; report shape/memory costs.

## Dataset: `cleaned_hdb.csv`
| town | str | 10 nominal values | no order |
| flat_type | str | 4 values | genuinely ordinal 3<4<5<EXEC |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
