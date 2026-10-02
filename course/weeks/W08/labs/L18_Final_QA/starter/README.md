# L18 - Final Dataset QA & Readiness Checklist

**Week:** W08 | **Session:** S32 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W08** (session S32). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Labs 11-17 complete - the checklist uses all of them
- [ ] Your project dataset chosen (Agent 5's brief)

## What you'll be able to do
- Run a full readiness check: types, leakage, balance, constraints
- Fix or justify every red flag

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + the checklist walkthrough | Instructor-led |
| 0:15-0:50 | Task 1: implement (or vibe-code) the checklist runner | Solo |
| 0:50-1:00 | Checkpoint: pytest tests/ -v | Self-check |
| 1:00-1:30 | Task 2: run it on your project dataset; fix red flags | Pairs |
| 1:30-1:50 | AI-assist block: ask the AI to review your checklist for missed leakage checks | With AI assistant |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `df.notna().all()` - no empty cells anywhere
- `df["col"].between(lo, hi).all()` - every value inside the plausible range
- `df["target"].value_counts(normalize=True)` - class balance, reported not assumed

## Stuck?
- Hint 1: if you vibe-code the runner, verify it covers leakage - AI checklists skip it.
- Hint 2: every red flag is either fixed or justified in writing.
- Hint 3: this checklist is your project's final gate.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
