# L15 - Vibe Coding Data Prep (AI-assist core)

**Week:** W07 | **Session:** S27 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W07** (session S27). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 5 complete - your manual solution IS the baseline
- [ ] Week 7 theory S26 read (vibe coding principles)

## What you'll be able to do
- Run the full loop: prompt, draft, run, verify, refine
- Diff AI output against your manual Lab 5 baseline

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + the loop and the 6-point checklist | Instructor-led |
| 0:15-0:30 | Task 1: manual baseline recap (your Lab 5) | Solo |
| 0:30-1:20 | Task 2: full vibe-coding loop on the same task | With AI assistant |
| 1:20-1:30 | Checkpoint: pytest tests/ -v on the AI-assisted pipeline | Self-check |
| 1:30-1:50 | Task 3: diff + prompt log completion | Solo |
| 1:50-2:00 | Exit ticket + reflection (required) | Solo |

## Python survival kit
- `prompt = f"Role: ... Schema: {df.columns.tolist()} ..."` - build a 5-part prompt with your real schema
- `pytest tests/ -v` - verify the AI's code against the lab's checks
- `pd.testing.assert_series_equal(a, b)` - programmatically diff two columns

## Stuck?
- Hint 1: attempt first - the baseline exists so the diff is meaningful.
- Hint 2: log every prompt: intent, prompt, outcome.
- Hint 3: the reflection is graded: right / wrong / what you changed.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
