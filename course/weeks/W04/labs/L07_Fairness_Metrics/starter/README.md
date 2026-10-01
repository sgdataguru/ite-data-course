# L07 - Computing Fairness Metrics

**Week:** W04 | **Session:** S13 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W04** (session S13). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 6 complete - you know where the bias lives
- [ ] Week 3 theory S12 read (the three fairness metrics)

## What you'll be able to do
- Compute demographic parity, equalised odds, and predictive parity by group
- Interpret each gap in plain English

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:20 | Setup + train the baseline classifier | Instructor-led |
| 0:20-0:55 | Task 1: MetricFrame - selection rate, TPR, precision by group | Solo |
| 0:55-1:05 | Checkpoint: pytest tests/ -v | Self-check |
| 1:05-1:25 | AI-assist block: ask the AI to explain your worst gap in plain English, then check it | With AI assistant |
| 1:25-1:50 | Task 2: gap table + interpretations | Pairs |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `MetricFrame(metrics=..., y_true=..., y_pred=..., sensitive_features=...)` - any metric, computed separately per group
- `mf.by_group` - the per-group values side by side
- `mf.difference()` - the gap: largest minus smallest group value
- `recall_score(y, p)` - TPR: of real positives, how many were caught

## Stuck?
- Hint 1: selection rate = (pred == 1).mean() per group.
- Hint 2: equalised odds needs BOTH TPR and FPR compared.
- Hint 3: the interpretation sentence is graded as hard as the number.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
