# L17 - Prompt Library Build (AI-assist core)

**Week:** W08 | **Session:** S31 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W08** (session S31). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Labs 15-16 complete - you've seen good and bad prompts
- [ ] Week 8 theory S30 read (prompt design)

## What you'll be able to do
- Build 8 tested, five-part prompts - one per module topic
- Record 6-point checklist results for each

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + the 5-part structure with examples | Instructor-led |
| 0:15-0:50 | Task 1: draft 8 prompts (one per topic) | Solo |
| 0:50-1:30 | Task 2: test each on a real task from earlier labs | With AI assistant |
| 1:30-1:40 | Checkpoint: pytest tests/ -v | Self-check |
| 1:40-1:50 | Task 3: record checklist results + polish | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `f"Role: ... Context: ... Schema: {cols} ..."` - the 5-part template as a format string
- `df.describe().to_dict()` - stats for the Context part - safe to share

## Stuck?
- Hint 1: one prompt per topic: cleaning, scaling, encoding, imbalance, metrics, mitigation, splitting, QA.
- Hint 2: a prompt without constraints gets generic code.
- Hint 3: untested prompts don't count - record the checklist result.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
