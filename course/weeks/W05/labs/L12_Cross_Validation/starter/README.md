# L12 - KFold, StratifiedKFold, TimeSeriesSplit

**Week:** W05 | **Session:** S22 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W05** (session S22). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 11 complete - splits before folds
- [ ] Week 5 theory S21 read (cross-validation methods)

## What you'll be able to do
- Show why plain k-fold breaks time series
- Keep class ratios stable with stratified folds
- Put the scaler inside the CV loop

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + fold mechanics on the board | Instructor-led |
| 0:15-0:45 | Task 1: TimeSeriesSplit on energy - no time travel | Solo |
| 0:45-0:55 | Checkpoint: pytest tests/ -v | Self-check |
| 0:55-1:25 | Task 2: KFold vs StratifiedKFold ratios on fraud | Pairs |
| 1:25-1:45 | AI-assist block: ask the AI to choose a CV strategy, then verify its reasoning | With AI assistant |
| 1:45-2:00 | Task 3: pipeline-based cross_val_score | Solo |
| 2:00-2:10 | Exit ticket + reflection | Solo |

## Python survival kit
- `TimeSeriesSplit(n_splits=5)` - expanding-window folds: train on the past only
- `StratifiedKFold(5, shuffle=True, random_state=42)` - folds that keep the class ratio
- `cross_val_score(pipe, X, y, cv=5)` - run the whole loop and collect the scores
- `make_pipeline(StandardScaler(), model)` - scaler INSIDE the loop - refits per fold

## Stuck?
- Hint 1: for time data, train.max() < test.min() in every fold.
- Hint 2: compare fold positive-ratios: KFold wobbles, Stratified doesn't.
- Hint 3: if the scaler is outside the CV loop, you've leaked.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
