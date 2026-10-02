# L11 - Splits in Practice

**Week:** W05 | **Session:** S20 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W05** (session S20). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Weeks 1-4 complete - you have a fully prepped dataset to split
- [ ] Week 5 theory S19 read (splits & leakage)

## What you'll be able to do
- Build seeded 70/15/15 splits
- Demonstrate leakage and measure the score difference

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + the sacred test set | Instructor-led |
| 0:15-0:45 | Task 1: 70/15/15 seeded splits + disjoint assertion | Solo |
| 0:45-0:55 | Checkpoint: pytest tests/ -v | Self-check |
| 0:55-1:25 | Task 2: the leakage demo - scale before vs after split | Pairs |
| 1:25-1:45 | AI-assist block: ask the AI to spot the leaky feature in a column list | With AI assistant |
| 1:45-2:00 | Task 3: compare scores + explain the difference | Solo |
| 2:00-2:10 | Exit ticket + reflection | Solo |

## Python survival kit
- `train_test_split(X, y, test_size=0.30, random_state=42)` - first split: 70% train, 30% holdout
- `train_test_split(Xtmp, test_size=0.33)` - second split: carve 15% val + 15% test from the holdout
- `set(a.index) & set(b.index)` - the overlap between two index sets - should be empty
- `r2_score(y_test, pred)` - how good a regression prediction is (1.0 = perfect)

## Stuck?
- Hint 1: two train_test_split calls make 70/15/15.
- Hint 2: the buggy path fits the scaler on ALL rows before splitting.
- Hint 3: assert the index sets are disjoint - keep that check forever.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
