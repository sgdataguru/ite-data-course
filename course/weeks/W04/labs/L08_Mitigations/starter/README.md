# L08 - Applying Mitigations

**Week:** W04 | **Session:** S15 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W04** (session S15). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 7 complete - you have baseline gaps to close
- [ ] Week 4 theory S14 read (sensitive attributes & mitigation)

## What you'll be able to do
- Apply reweighing to close a fairness gap
- Report the accuracy-fairness trade-off honestly

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + reweighing intuition | Instructor-led |
| 0:15-0:45 | Task 1: compute reweighing weights | Solo |
| 0:45-0:55 | Checkpoint: pytest tests/ -v | Self-check |
| 0:55-1:20 | Task 2: retrain with weights, recompute gaps | Pairs |
| 1:20-1:40 | AI-assist block: ask the AI to draft your mitigation report section, then verify | With AI assistant |
| 1:40-2:00 | Task 3: before/after table + trade-off sentence | Solo |
| 2:00-2:10 | Exit ticket + reflection | Solo |

## Python survival kit
- `model.fit(X, y, sample_weight=w)` - train with importance weights
- `w[mask] = p_g * p_o / p_go` - the reweighing formula: expected share / actual share
- `mf.difference()` - re-measure the gap after mitigation

## Stuck?
- Hint 1: weights sum to the original row count - check it.
- Hint 2: mitigation is never free - report the accuracy cost too.
- Hint 3: never apply mitigation to the test set.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
