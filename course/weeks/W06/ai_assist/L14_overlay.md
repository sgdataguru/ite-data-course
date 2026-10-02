# W06 AI-Assist Overlay — Lab L14

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 30 minutes inside Lab L14's 2-hour plan — "Schema-stats-only synthesis block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Generate 50 synthetic rows matching this schema [paste schema] and these summary statistics [paste describe()]. Do NOT reproduce real records. Then critique your own output for plausibility.
2. Compare my real vs synthetic distributions: [paste stats]. Which synthetic set (SMOTE or your generated rows) stays closer to the real data, and where does each drift?
3. What plausibility constraints should I assert on synthetic rows for this schema (ranges, no negatives, valid categories)?

## Failure gallery — how AI goes wrong on THIS task
### Impossible rows
The AI generates negative ages and 999-room flats - plausible-looking, impossible values. Fix: assert domain constraints on every generated row.

### Ratio drift
The AI's synthetic rows quietly change the class ratio. Fix: check value_counts before and after.

### Memorisation risk
The AI offers to 'reuse' real rows 'for realism'. Fix: schema + statistics only, never raw data in the prompt.


## Reflection scaffold (worked example)
> The AI's synthetic rows looked convincing but included two negative feature values my plausibility check caught. SMOTE stayed closer to the real distribution. My verdict: SMOTE for training, GenAI rows only with constraint checks - and never raw rows in the prompt.
