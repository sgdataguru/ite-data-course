# L02 - Scaling Pipelines

**Week:** W01 | **Session:** S04 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W01** (session S04). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 1 complete - you need cleaned_hdb.csv from your solution folder
- [ ] Week 1 theory S03 read (scaling vs normalisation vs standardisation)

## What you'll be able to do
- Build StandardScaler, MinMaxScaler, and RobustScaler pipelines
- Show why one outlier can collapse a min-max scale
- Fit a scaler on training data only - and explain why

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + load your Lab 1 cleaned CSV | Instructor-led |
| 0:15-0:45 | Task 1: fit 3 scalers on TRAIN only | Solo |
| 0:45-0:55 | Checkpoint: pytest tests/ -v | Self-check |
| 0:55-1:15 | Task 2: inject the 400 sqm outlier, watch min-max collapse | Pairs |
| 1:15-1:35 | AI-assist block: ask the AI to justify or challenge your scaler choice | With AI assistant |
| 1:35-1:50 | Task 3: plot before/after + export chart | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `train_test_split(X, test_size=0.2, random_state=42)` - split into train (80%) and test (20%), repeatable
- `StandardScaler().fit(X_train)` - learn mean & spread from training data only
- `scaler.transform(X_test)` - apply the learned stats to the test data
- `plt.hist(col, bins=40)` - draw a histogram
- `plt.savefig("chart.png")` - save your chart as a file

## Stuck?
- Hint 1: fit() learns, transform() applies - never fit on the test set.
- Hint 2: for the outlier demo, change one value to 400 and re-fit min-max.
- Hint 3: the chart needs 4 panels: raw + three scalers.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
