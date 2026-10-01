# L16 - Critiquing & Fixing AI Output (AI-assist core)

**Week:** W07 | **Session:** S29 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W07** (session S29). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Lab 15 complete - you have prompt-log experience
- [ ] Week 7 theory S28 read (risks & limitations of AI code)

## What you'll be able to do
- Find and fix three planted AI failures: hallucinated API, SMOTE-before-split, leakage
- Name each failure class, not just the code change

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:20 | Setup + run the three scripts, watch them fail differently | Instructor-led |
| 0:20-0:45 | Task 1: script 1 - the hallucinated API | Pairs |
| 0:45-1:10 | Task 2: script 2 - SMOTE before split (silent lie) | Pairs |
| 1:10-1:35 | Task 3: script 3 - scaler on full data (contamination) | Pairs |
| 1:35-1:50 | AI-assist block: ask the AI to critique its own output - tally what it missed | With AI assistant |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `hasattr(sklearn.preprocessing, "SmartEncoder")` - test whether a class really exists
- `try: import ... except ImportError:` - catch a failed import gracefully
- `imblearn Pipeline([('smote', ...), ('clf', ...)])` - the fold-safe fix for script 2

## Stuck?
- Hint 1: script 1 crashes; scripts 2 and 3 run fine and lie - that's the point.
- Hint 2: the fix for 2 is structural (Pipeline), not cosmetic.
- Hint 3: your paragraph must name the failure CLASS.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
