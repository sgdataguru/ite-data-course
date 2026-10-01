# L04 - Imbalance & Algorithm-Aware Prep

**Week:** W02 | **Session:** S08 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W02** (session S08). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Week 2 theory S07 read (SMOTE intuition, algorithm-specific prep)
- [ ] Labs 1-3 complete

## What you'll be able to do
- Diagnose a 990:10 imbalanced fraud dataset
- Apply under/over/SMOTE so only training folds are resampled
- Explain why 99% accuracy can mean a useless model

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + see the lying metric demo | Instructor-led |
| 0:15-0:40 | Task 1: baseline KNN - accuracy vs recall | Solo |
| 0:40-0:50 | Checkpoint: pytest tests/ -v | Self-check |
| 0:50-1:20 | Task 2: three resampling strategies via imblearn Pipeline | Pairs |
| 1:20-1:40 | AI-assist block: ask the AI to argue under vs over vs SMOTE for your data | With AI assistant |
| 1:40-1:50 | Task 3: results table accuracy/recall/F1 | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `df["is_fraud"].value_counts()` - count each class - see the 990:10 imbalance
- `from imblearn.pipeline import Pipeline` - a pipeline that resamples INSIDE training folds only
- `SMOTE(random_state=42)` - synthesise minority points between neighbours
- `recall_score(y_test, pred)` - of all real frauds, how many did we catch?
- `f1_score(y_test, pred)` - the balance of precision and recall

## Stuck?
- Hint 1: put SMOTE inside the imblearn Pipeline, never before the split.
- Hint 2: accuracy near 99% with recall near 0 = the model never predicts fraud.
- Hint 3: stratify=y in train_test_split keeps the ratio in both halves.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
