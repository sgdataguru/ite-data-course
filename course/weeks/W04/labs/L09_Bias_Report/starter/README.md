# L09 - 1-Page Bias Assessment Report

**Week:** W04 | **Session:** S17 | **Duration:** 2 hrs

## Week & session map
This lab sits in **W04** (session S17). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
- [ ] Labs 6-8 complete - the report is built from their results
- [ ] Week 4 theory S16 read (documentation for traceability)

## What you'll be able to do
- Assemble the standard 5-section bias report from your Labs 6-8 results

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
| 0:00-0:15 | Setup + the 5-section structure | Instructor-led |
| 0:15-1:00 | Task 1: draft all 5 sections from your lab results | Solo |
| 1:00-1:10 | Checkpoint: pytest tests/ -v | Self-check |
| 1:10-1:35 | AI-assist block: ask the AI to review your report for missing traceability, then fix | With AI assistant |
| 1:35-1:50 | Task 2: polish evidence - numbers not adjectives | Solo |
| 1:50-2:00 | Exit ticket + reflection | Solo |

## Python survival kit
- `open("bias_report.md", "w")` - create your report file
- `df.to_markdown()` - turn a results table into Markdown for the report

## Stuck?
- Hint 1: the 5 sections: scope, risks, metrics, mitigations, residual risks.
- Hint 2: every claim needs a number from Labs 6-8.
- Hint 3: this exact template is reused in the project - learn it now.
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
