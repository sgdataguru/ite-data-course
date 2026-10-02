# L01 - Load & Fix a Messy Dataset

**Week:** W01 | **Session:** S02 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W01** (session S02). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Week 1 theory S01 read (data types & conversion)
- [ ] Environment checked: pip install -r requirements.txt
- [ ] Jupyter opens and runs a print() cell

## What you'll be able to do
- Turn a messy price column like "$530,000" into numbers a model can use
- Parse dates that come in two different formats
- Decide what to do with missing values - and justify your choice
- Spot impossible values (a 9,999 sqm flat?) before they ruin your analysis

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + run the first cells together | Instructor-led |
| 0:15-0:45 | Task 1: fix the price column | Solo |
| 0:45-0:55 | Checkpoint: run pytest tests/ -v | Self-check |
| 0:55-1:15 | Task 2: parse the mixed dates | Pairs |
| 1:15-1:35 | AI-assist block: ask the AI to explain your hardest error | With AI assistant |
| 1:35-1:50 | Task 3: missing values + outliers, then export | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `pd.read_csv("data/hdb_messy.csv")` - load the messy file into a table
- `df.head()` - peek at the first 5 rows
- `df.info()` - every column, its type, and empty-cell counts
- `df["col"].str.replace("$", "", regex=False)` - delete every $ in a text column
- `.astype(float)` - turn text into decimal numbers
- `pd.to_datetime(col, format="mixed", dayfirst=True)` - parse dates, day-first for dd/mm/yyyy rows
- `df["col"].fillna(df["col"].median())` - replace empty cells with the middle value
- `df.drop(columns=["name"])` - remove a column

## Stuck?
- Hint 1: the $ and comma are characters - remove them first, then cast.
- Hint 2: pd.to_datetime with format="mixed" handles both date styles.
- Hint 3: fix the 9999/-50 outliers BEFORE imputing, or your median becomes garbage.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
