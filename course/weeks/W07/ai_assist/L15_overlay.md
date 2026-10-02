# W07 AI-Assist Overlay — Lab L15

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 50 minutes inside Lab L15's 2-hour plan — "Full vibe-coding loop (core lab)".
**Maturity level:** Week 7-8: full vibe-coding loops (40+ min core blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. You are preparing an HDB dataset for KNN. Standardise floor_area_sqm, storey, lease_commence; one-hot town with handle_unknown='ignore'; ordinal-encode flat_type as 3<4<5<EXEC. Output a single sklearn ColumnTransformer.
2. Your previous output label-encoded town. town is nominal - use OneHotEncoder(handle_unknown='ignore') and re-output the full transformer.
3. Now justify each prep choice in one sentence per column, as if for a decisions table.

## Failure gallery — how AI goes wrong on THIS task
### First-draft encoding bug
The AI label-encodes town despite the constraint - refined in round 2.

### Alphabetical ordinal
The AI's flat_type order is alphabetical until explicitly constrained.

### No justification
The AI cannot say WHY tree prep skips scaling - the human adds the rationale.


## Reflection scaffold (worked example)
> The AI got the pipeline structure right and fast. It label-encoded town (wrong) and could not justify treatment choices. I fixed the encoding, added handle_unknown, and wrote the rationale myself. The diff against my Lab 5 baseline showed we converged on the same pipeline - but mine, I can defend.
