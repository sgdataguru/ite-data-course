# W05 AI-Assist Overlay — Lab L12

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L12's 2-hour plan — "Verify-the-reasoning block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. My data is [daily energy demand, 2 years]. Choose a cross-validation strategy, implement it, and justify the choice in 3 sentences.
2. Here is my CV loop: [paste]. Is the scaler inside or outside the loop? What does that mean for my scores?
3. My 5-fold scores vary from 0.61 to 0.89. Explain what that variance tells me about my data or my pipeline.

## Failure gallery — how AI goes wrong on THIS task
### K-fold on time series
The AI uses plain KFold on temporal data - training on the future to predict the past. Fix: TimeSeriesSplit.

### Scaler outside CV
The AI scales before cross_val_score, leaking fold statistics. Fix: make_pipeline puts the scaler inside.


## Reflection scaffold (worked example)
> The AI chose TimeSeriesSplit correctly but couldn't articulate WHY until I asked for the justification - the reasoning mattered more than the code. Its first loop had the scaler outside; the pipeline fix was the whole lesson.
