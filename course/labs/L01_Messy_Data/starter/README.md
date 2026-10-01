# Lab 1 — Load & Fix a Messy Dataset (C1)

**Session:** S02 · **Duration:** 2 hrs · **Competency:** C1 · **AI-assist:** 1 hr (overlay from Agent 4)

## Scenario
You are a junior data analyst at a Singapore property analytics firm. A colleague's export of HDB resale data went wrong. Produce a clean, typed DataFrame ready for scaling (Lab 2).

## Dataset: `data/hdb_messy.csv` (6,000 rows)

| Column | Dtype (raw) | Description | Known issues |
|---|---|---|---|
| town | str | HDB town (10 values) | — |
| flat_type | str | 3-ROOM … EXECUTIVE | — |
| floor_area_sqm | float | Floor area in sqm | 47 NaNs; 5 implausible values (9999, -50, 0, 400, 250) |
| storey | float | Storey number | 5 NaNs |
| lease_commence | int | Lease commencement year | — |
| resale_price | str | Price like "$530,000" | String-formatted with $ and commas |
| sale_date | str | Sale date | Mixed formats: %Y-%m-%d and %d/%m/%Y |
| floor_area_sqm.1 | float | Stray duplicate of floor_area_sqm | Export artefact |

## Expected outcome
`cleaned_hdb.csv`: all numerics typed, dates parsed, no NaNs, no duplicate columns, plausible ranges.

## Time budget
- Audit & price fix: 30 min · Dates: 20 min · Missing/outliers: 30 min · Audit & export: 20 min

## Self-check
`pytest tests/ -v` — all 6 tests must pass before you leave.
