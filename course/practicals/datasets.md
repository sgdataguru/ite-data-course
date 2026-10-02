# DE5002FP — Datasets (Agent 3)

| Dataset | Source | Licence | Preprocessing notes | Used in |
|---|---|---|---|---|
| HDB Resale Prices | data.gov.sg | Singapore Open Data Licence | Filter 2017–2024; price strings → float; derive flat age | Labs 1–5, 11, 13, 15; project option A |
| UCI Adult Income | archive.ics.uci.edu | UCI open licence (citation) | Strip whitespace in categoricals; `?` → NaN; sex/race = sensitive attributes | Labs 6–10; practical test analogue |
| Bank Marketing | UCI | UCI open licence | Semicolon separator; `y` target; strong class imbalance (~11%) | Lab 4 alternative, imbalance practice |
| Lending Club / Statlog German Credit | UCI / Kaggle | Open (verify per source) | German Credit preferred: small, clean, `sex` derivable from attributes | Lab 10, project option B |
| Energy Demand (time series) | UCI ElectricityLoadDiagrams / Kaggle hourly energy | Open | Hourly → daily aggregate; strictly temporal ordering | Lab 12 |
| Fashion-MNIST (subset) | GitHub (zalandoresearch) | MIT | Sample 2,000 images; normalise 0–1 | Lab 13 |
| Synthetic fraud dataset | Generated in-lab (script provided) | N/A | 990:10 imbalance by construction | Lab 4, 12 |
| MRT ridership | LTA MyTransport / data.gov.sg | Singapore Open Data Licence | Optional enrichment for project | Project extension |
| Hospital readmission (synthetic) | Generated from SingHealth-style schema | N/A (synthetic) | Sensitive attributes: age, ethnicity proxy | Project option C |

**Availability rule:** instructor downloads and verifies all datasets before Week 1; local copies distributed via LMS to avoid network dependency in labs and tests.
