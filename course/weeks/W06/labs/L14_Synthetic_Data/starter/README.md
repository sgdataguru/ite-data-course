# L14 - Synthetic Data with SMOTE + GenAI

**Week:** W06 | **Session:** S25 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W06** (session S25). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 13 complete - augmentation before synthesis
- [ ] Week 6 theory S23 read; Agent 4's tool policy read (never paste raw rows)

## What you'll be able to do
- Generate synthetic minority rows with SMOTE and with a GenAI tool
- Judge which synthetic set is safer to train on

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + SMOTE vs GANs vs LLM recap | Instructor-led |
| 0:15-0:45 | Task 1: SMOTE synthesis + plausibility checks | Solo |
| 0:45-0:55 | Checkpoint: pytest tests/ -v | Self-check |
| 0:55-1:25 | Task 2: GenAI synthesis - schema + stats prompts ONLY (no raw rows) | With AI assistant |
| 1:25-1:50 | Task 3: distribution comparison chart | Pairs |
| 1:50-2:00 | Task 4: safety verdict + reflection | Solo |

## Python survival kit
- `SMOTE(random_state=42, k_neighbors=3)` - interpolate new minority points between neighbours
- `df.describe()` - your data's summary stats - safe to put in a prompt
- `(Xs >= X.min()).all()` - plausibility check: no impossible values

## Stuck?
- Hint 1: the GenAI prompt gets schema + describe() - never real rows.
- Hint 2: SMOTE shrinks variance (interpolation); GenAI can hallucinate values.
- Hint 3: the verdict must cite your comparison chart.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
