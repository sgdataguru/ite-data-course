# L05 - C1 Consolidation Mini-Project

**Week:** W02 | **Session:** S09 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W02** (session S09). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Labs 1-4 complete - this lab reuses all of them
- [ ] Week 2 theory S05 + S07 read

## What you'll be able to do
- Run a full C1 prep: clean, scale, encode, prep for 3 algorithms
- Justify every prep decision in a decisions table

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + review the algorithm-prep matrix | Instructor-led |
| 0:15-1:00 | Task 1: assemble prep for tree / KNN / logistic | Solo |
| 1:00-1:10 | Checkpoint: pytest tests/ -v | Self-check |
| 1:10-1:35 | AI-assist block: ask the AI to review your decisions table for mismatches | With AI assistant |
| 1:35-1:50 | Task 2: write the prep-decisions table | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `ColumnTransformer([...])` - apply different prep to different columns in one object
- `make_pipeline(...)` - chain steps so they run in order
- `pd.DataFrame([...], columns=[...])` - build your decisions table

## Stuck?
- Hint 1: trees don't need scaling; KNN and logistic do.
- Hint 2: the decisions table is the graded artefact - justify, don't just execute.
- Hint 3: reuse your Lab 3 encoders; don't rebuild from scratch.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
