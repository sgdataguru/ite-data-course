# W04 AI-Assist Overlay — Lab L09

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 25 minutes inside Lab L09's 2-hour plan — "Traceability-review block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is my bias report: [paste]. Review it against the 5-section structure (scope, risks, metrics, mitigations, residual risks) and list every missing traceability element.
2. Rewrite this finding so the evidence is numeric: 'the dataset seems to under-represent group B'.
3. What three facts must a datasheet entry record about this dataset's provenance? Answer for my adult_like.csv.

## Failure gallery — how AI goes wrong on THIS task
### Fabricated provenance
The AI invents collection dates and sources for the datasheet. Fix: only document what you can verify from the data itself.

### Structure over substance
The AI confirms all 5 sections exist without checking each claim has a number. Fix: ask it to flag adjective-only claims.


## Reflection scaffold (worked example)
> The AI found two gaps I'd missed: my residual-risks section was empty and one finding had no number. It then invented a collection date for the datasheet - I deleted that and wrote only what I could verify.
