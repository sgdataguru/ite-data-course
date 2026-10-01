# DE5002FP — Datasets (Agent 3, updated for folder-based labs)

All synthetic datasets are generated deterministically by `generate_all.py` (fixed seeds; byte-identical across runs). `cleaned_hdb.csv` is the Lab 1 solution output, pre-generated for Labs 2–5, 11, 13, 15, 16, 18.

| Dataset | File | Source / generator | Licence | Known planted issues | Used in |
|---|---|---|---|---|---|
| HDB resale (messy) | `hdb_messy.csv` | `generate_all.py` (HDB-style synthetic) | N/A (synthetic) | `$`-strings, mixed dates, NaNs, duplicate column, outliers | L01 |
| HDB resale (cleaned) | `cleaned_hdb.csv` | Lab 1 solution output | N/A | — (clean) | L02, L03, L05, L11, L13, L15, L16, L18 |
| Fraud | `fraud.csv` | `generate_all.py` | N/A (synthetic) | 990:10 class imbalance | L04, L12, L16 |
| Adult-like income | `adult_like.csv` | `generate_all.py` (UCI-Adult-style) | N/A (synthetic; real UCI Adult via `fetch_data.py` for extension) | representation 70/30, historical income gap, measurement noise | L06–L09 |
| Lending | `lending.csv` | `generate_all.py` (German-Credit-style) | N/A (synthetic) | district-based approval bias, 92:8 imbalance | L10 |
| Energy demand | `energy_demand.csv` | `generate_all.py` | N/A (synthetic) | trend + weekly/yearly seasonality (temporal ordering matters) | L12 |
| Minority sample | `minority_sample.csv` | `generate_all.py` | N/A (synthetic) | 95:5 label imbalance | L14 |
| Planted-bug scripts | `script_1/2/3.py` | `_complete_labs.py` | N/A | hallucinated API; SMOTE-before-split; test-set leakage | L16 |

**Public-dataset extension:** for the real-data practice in L06–L10, instructors run `fetch_data.py` (provided per lab) to download UCI Adult and German Credit; a small local sample CSV ships in each lab's `data/` so every lab runs offline.

**Reproducibility:** `python generate_all.py` regenerates all CSVs byte-identically (verified via SHA-1 across two runs).
