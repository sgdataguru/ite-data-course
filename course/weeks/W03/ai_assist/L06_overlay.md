# W03 AI-Assist Overlay — Lab L06

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L06's 2-hour plan — "Brainstorm-then-verify block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is my dataset description: [paste schema + describe()]. List the plausible bias sources (historical, representation, measurement, aggregation, deployment) and what evidence I'd look for in the data.
2. Write pandas code for group-wise summary statistics of income_gt_50k by group, and missingness counts by group.
3. Draft one bias-risk paragraph from these numbers: [paste your group stats]. Use numbers, not adjectives.

## Failure gallery — how AI goes wrong on THIS task
### Adjective findings
The AI writes 'the model seems biased' with no numbers. Fix: demand evidence - every finding cites a computed value.

### Drop-the-column
The AI suggests removing the sensitive attribute entirely to 'avoid bias'. Fix: you need it to measure; proxies survive deletion anyway.


## Reflection scaffold (worked example)
> The AI's brainstorm matched two of my three findings and suggested one I'd missed (aggregation). But its findings had zero numbers. I made it rewrite with evidence, then verified each number myself.
