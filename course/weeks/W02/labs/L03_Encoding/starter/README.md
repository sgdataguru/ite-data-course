# L03 - Encoding Categorical Data

**Week:** W02 | **Session:** S06 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W02** (session S06). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Week 1 complete (Lab 1's cleaned_hdb.csv)
- [ ] Week 2 theory S05 read (one-hot vs label vs target encoding)

## What you'll be able to do
- One-hot encode a nominal column without inventing fake order
- Ordinal-encode with an explicit order you control
- Explain the memory cost of one-hot on high-cardinality columns

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:10 | Setup + load cleaned data | Instructor-led |
| 0:10-0:35 | Task 1: one-hot encode town | Solo |
| 0:35-0:45 | Checkpoint: pytest tests/ -v | Self-check |
| 0:45-1:10 | Task 2: ordinal-encode flat_type with explicit order | Pairs |
| 1:10-1:30 | AI-assist block: ask the AI to critique your encoding choices | With AI assistant |
| 1:30-1:50 | Task 3: report shapes/memory before & after | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `OneHotEncoder(sparse_output=False, handle_unknown="ignore")` - one 0/1 column per category; unseen values won't crash
- `OrdinalEncoder(categories=[["3-ROOM","4-ROOM","5-ROOM","EXECUTIVE"]])` - encode with YOUR order, not alphabetical
- `df.memory_usage()` - how much memory each column uses
- `ohe.fit_transform(df[["town"]])` - learn the categories and encode in one step

## Stuck?
- Hint 1: town has no natural order - one-hot it.
- Hint 2: flat_type IS ordered, but only if you pass the categories explicitly.
- Hint 3: compare df.shape[1] before and after to see the column explosion.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
