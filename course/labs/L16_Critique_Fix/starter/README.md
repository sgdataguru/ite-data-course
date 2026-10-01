# Lab 16 — Critiquing & Fixing AI Output (C3, AI-assist core)

**Session:** S29 · **Duration:** 2 hrs · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
Three planted-failure scripts: hallucinated API, SMOTE-before-split, test leakage. Find, explain, fix.

## Dataset: `script_1/2/3.py`
| script_1.py | py | prep code | hallucinated import |
| script_2.py | py | prep code | SMOTE before split |
| script_3.py | py | prep code | scaler on full data |

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
