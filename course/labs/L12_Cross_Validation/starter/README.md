# Lab 12 — KFold, StratifiedKFold, TimeSeriesSplit (C3)

**Session:** S22 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
TimeSeriesSplit on energy (no time travel); stratified folds on fraud; scaler inside the CV loop.

## Dataset: `energy_demand.csv + fraud.csv`
| date | str | daily | strictly temporal |
| demand_mw | float | demand | trend+seasonality |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
