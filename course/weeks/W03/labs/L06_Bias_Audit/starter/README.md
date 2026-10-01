# L06 - Dataset Bias Audit

**Week:** W03 | **Session:** S11 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W03** (session S11). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Week 3 theory S10 read (sources of bias)
- [ ] Weeks 1-2 labs complete

## What you'll be able to do
- Audit a dataset for representation bias with group-wise stats
- Write 3 bias findings, each backed by a number

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + the five bias sources recap | Instructor-led |
| 0:15-0:40 | Task 1: group-wise summary stats | Solo |
| 0:40-0:50 | Checkpoint: pytest tests/ -v | Self-check |
| 0:50-1:15 | Task 2: representation + missingness by group | Pairs |
| 1:15-1:35 | AI-assist block: ask the AI to brainstorm bias sources, then verify with your own numbers | With AI assistant |
| 1:35-2:10 | Task 3: write 3 findings with evidence | Solo |
| 2:10-2:20 | Exit ticket + reflection | Solo |

## Python survival kit
- `df.groupby("group")["col"].mean()` - the mean separately per group
- `df["group"].value_counts(normalize=True)` - each group's share of the sample
- `df.groupby("group").std()` - the spread per group - measurement-bias clue

## Stuck?
- Hint 1: representation = value_counts(normalize=True) vs the real population.
- Hint 2: 'seems biased' earns nothing - every finding needs a number.
- Hint 3: hours_per_week has higher variance for group B - that's measurement bias.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
