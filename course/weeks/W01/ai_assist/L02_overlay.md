# W01 AI-Assist Overlay — Lab L02

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L02's 2-hour plan — "Justify-or-challenge block".
**Maturity level:** Week 1-2: explain-my-error (small blocks, heavy scaffolding)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. My floor_area_sqm column has this distribution: [paste describe() output]. I am using KNN. Which scaler should I use and why, in 3 sentences?
2. Here is my scaling code: [paste code]. Is there any train-test leakage in it? Point to the exact line if so.
3. I added a 400 sqm outlier and my min-max scaling collapsed. Explain what happened and which scaler resists this.

## Failure gallery — how AI goes wrong on THIS task
### Fit-on-everything
The AI fits the scaler on the full dataset before splitting - contamination. Fix: fit on train, transform test with the same scaler.

### Wrong ranges reported
The AI applies RobustScaler but reports min-max ranges as if they were [0,1]. Fix: verify by computing the transformed ranges yourself.


## Reflection scaffold (worked example)
> The AI correctly picked RobustScaler for my outlier-heavy data and caught that I'd forgotten random_state. It initially fit the scaler on all rows - I moved the fit after the split and re-ran.
