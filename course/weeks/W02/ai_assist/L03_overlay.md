# W02 AI-Assist Overlay — Lab L03

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L03's 2-hour plan — "Critique-my-choices block".
**Maturity level:** Week 1-2: explain-my-error (small blocks, heavy scaffolding)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. I one-hot encoded town (10 values) and ordinal-encoded flat_type with the order 3-ROOM<4-ROOM<5-ROOM<EXECUTIVE. Critique these two choices in 3 sentences.
2. My dataset has a street_name column with 8,000 different values. Why is one-hot a bad idea here, and what should I do instead?
3. Write fold-safe target encoding for my high-cardinality column inside a cross-validation loop.

## Failure gallery — how AI goes wrong on THIS task
### Label-encodes nominal
The AI label-encodes town, inventing an order the model will use. Fix: one-hot with handle_unknown='ignore'.

### Alphabetical ordinal
The AI ordinal-encodes flat_type alphabetically so EXECUTIVE codes below 3-ROOM. Fix: pass categories=[...] explicitly.


## Reflection scaffold (worked example)
> The AI spotted my alphabetical ordinal order immediately - good catch. It then suggested label-encoding town 'for simplicity', which would invent an order. I kept one-hot and documented why.
