# L13 - Augmentation on Tabular Data

**Week:** W06 | **Session:** S24 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W06** (session S24). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Week 5 complete - augmented data needs split-awareness
- [ ] Week 6 theory S23 read (augmentation taxonomy)

## What you'll be able to do
- Apply Gaussian jitter without touching labels
- Verify augmented data with distribution overlays

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + augmentation vs synthesis | Instructor-led |
| 0:15-0:45 | Task 1: jitter the numeric features (seeded) | Solo |
| 0:45-0:55 | Checkpoint: pytest tests/ -v | Self-check |
| 0:55-1:25 | Task 2: labels-unchanged assertion + overlay chart | Pairs |
| 1:25-1:45 | AI-assist block: ask the AI to write the jitter, then check it didn't touch labels | With AI assistant |
| 1:45-2:00 | Task 3: export the sanity-check chart | Solo |
| 2:00-2:10 | Exit ticket + reflection | Solo |

## Python survival kit
- `rng = np.random.default_rng(42)` - a seeded random generator - same numbers every run
- `col + rng.normal(0, 0.05*col.std(), len(col))` - add noise worth 5% of the column's spread
- `pd.concat([df, aug])` - stack original + augmented rows
- `plt.hist(..., alpha=0.6)` - overlapping histograms for comparison

## Stuck?
- Hint 1: jitter features, NEVER the label.
- Hint 2: assert labels unchanged before and after.
- Hint 3: 5% of std is enough - more distorts the data.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
