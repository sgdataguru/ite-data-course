# DE5002FP — Lab Index (Agent 3)

| Session | Lab folder | One-line description |
|---|---|---|
| S02 | `L01_Messy_Data/` | Load & fix a messy HDB CSV: types, dates, NaNs, outliers, duplicate column |
| S04 | `L02_Scaling/` | StandardScaler / MinMaxScaler / RobustScaler pipelines + outlier-collapse demo |
| S06 | `L03_Encoding/` | One-hot, ordinal (explicit order), and cardinality trade-offs |
| S08 | `L04_Imbalance/` | 990:10 fraud: under/over/SMOTE fold-safe; accuracy vs F1 |
| S09 | `L05_C1_MiniProject/` | End-to-end C1 prep for tree/KNN/logistic + decisions table |
| S09B | (L05 peer-review clinic) | Audit a partner's decisions table against the algorithm-prep matrix |
| S11 | `L06_Bias_Audit/` | Representation, group stats, 3 findings with numeric evidence |
| S13 | `L07_Fairness_Metrics/` | Demographic parity, equalised odds, predictive parity via fairlearn |
| S15 | `L08_Mitigations/` | Reweighing + resampling; before/after + trade-off |
| S17 | `L09_Bias_Report/` | Assemble the 5-section 1-page bias report |
| S18 | `L10_Two_Datasets/` | Full audit cycle on lending.csv; compare datasets |
| S18B | (L09 peer-review clinic) | Review bias reports against the traceability checklist |
| S20 | `L11_Splits_Leakage/` | 70/15/15 splits; leakage demo; disjoint-index assertion |
| S22 | `L12_Cross_Validation/` | TimeSeriesSplit, StratifiedKFold, scaler-inside-CV |
| S24 | `L13_Augmentation/` | Gaussian jitter on tabular; labels unchanged; distribution overlay |
| S25 | `L14_Synthetic_Data/` | SMOTE vs GenAI synthesis; plausibility checks |
| S27 | `L15_Vibe_Coding/` | AI-assisted redo of Lab 5; prompt log + diff + reflection |
| S29 | `L16_Critique_Fix/` | Three planted AI failures: find, explain, fix |
| S31 | `L17_Prompt_Library/` | Build + test 8 five-part prompts |
| S32 | `L18_Final_QA/` | Data-readiness checklist: types, leakage, balance, constraints |
| S34 | Consolidation lab | 6 timed micro-tasks, self-marked |
| S36/S37 | Mock + Practical Test | Agent 5 papers (AI-free, invigilated) |
| S38–S41 | Project studio | Agent 5 brief; milestones 25/50/75/100% |

**Folder convention:** every lab = `starter/` (notebook, data, requirements, README, pytest progress tests) + `solution/` (worked notebook, solution tests, exit-ticket guidance). Regenerate datasets: `python generate_all.py`.
