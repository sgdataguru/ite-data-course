# Lab 2 — Scaling Pipelines (C1)

**Session:** S04 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
Build StandardScaler / MinMaxScaler / RobustScaler pipelines on cleaned HDB data; show the outlier collapse; export a comparison chart.

## Dataset: `cleaned_hdb.csv`
| floor_area_sqm | float | area sqm | — |
| storey | float | storey | — |
| lease_commence | int | lease year | — |
| resale_price | float | price | target |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
