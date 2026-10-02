# W08 AI-Assist Overlay — Lab L18

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L18's 2-hour plan — "Checklist-review block".
**Maturity level:** Week 7-8: full vibe-coding loops (40+ min core blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is my data-readiness checklist runner: [paste]. Does it check for train-test leakage? If not, add that check.
2. What domain constraints should my readiness check assert for an HDB dataset? Give the ranges and the reasoning.
3. Review my checklist output: [paste]. Which red flags are fixable in 10 minutes, and which need a documented justification?

## Failure gallery — how AI goes wrong on THIS task
### Skips leakage
The AI's checklist covers types, NaNs, and ranges but never leakage - the planted M3 lesson. Fix: add the fitted-on-train-only check.

### Runs-is-correct fallacy
The AI's tests only assert the code runs, not that outputs are right. Fix: assert actual values.


## Reflection scaffold (worked example)
> The AI's checklist was professional-looking and missed leakage entirely - exactly what the theory note predicted. I added the leakage check and it immediately flagged my own scaler bug from an earlier lab. Every red flag is now fixed or justified in writing.
