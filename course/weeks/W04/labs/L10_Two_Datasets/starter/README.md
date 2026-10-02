# L10 - C2 Consolidation on Two Datasets

**Week:** W04 | **Session:** S18 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W04** (session S18). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Labs 6-9 complete - this is the compressed full cycle
- [ ] Bring your Lab 9 report as the template

## What you'll be able to do
- Run the full audit cycle on a lending dataset
- Compare bias risk across two datasets and argue which is riskier

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + lending dataset intro | Instructor-led |
| 0:15-1:00 | Task 1: full audit cycle (Labs 6-8 compressed) | Solo |
| 1:00-1:10 | Checkpoint: pytest tests/ -v | Self-check |
| 1:10-1:30 | AI-assist block: ask the AI to challenge your comparison, then defend with numbers | With AI assistant |
| 1:30-1:50 | Task 2: comparison paragraph | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `df.groupby("district").approved.mean()` - approval rate per district - the proxy-bias view
- `MetricFrame(...)` - same tool as Lab 7, new sensitive feature: district

## Stuck?
- Hint 1: district is a proxy attribute - treat it as sensitive (PDPA context).
- Hint 2: the comparison paragraph is the exit artefact.
- Hint 3: cite the district gap number in your verdict.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
