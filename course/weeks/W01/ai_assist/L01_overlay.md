# W01 AI-Assist Overlay — Lab L01

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L01's 2-hour plan — "Explain-my-error block (Week 1-2 maturity level)".
**Maturity level:** Week 1-2: explain-my-error (small blocks, heavy scaffolding)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. My code `df['resale_price'].astype(float)` failed with this error: [paste error]. Explain in simple English what is wrong and how to fix it.
2. I have a column with values like "$530,000". Write one line of pandas code to turn it into numbers, and explain each part.
3. After converting my price column, what two sanity checks should I run to catch conversion bugs?

## Failure gallery — how AI goes wrong on THIS task
### Silent coercion
The AI suggests errors='ignore' on the cast - bad values survive as strings with no warning. Fix: coerce, then assert the dtype and check the range.

### Zero-fill trap
The AI fills missing prices with 0 - a missing price is not a free flat. Fix: NaN and decide (drop/impute) explicitly.


## Reflection scaffold (worked example)
> The AI explained my comma error clearly and its fix worked. It wanted to fill missing prices with 0, which would corrupt the data. I used median imputation instead and added a range check.
