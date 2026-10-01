# S26 — Vibe Coding: AI-Assisted Code Generation Principles (C3, 1 hr)

## Concept Note

**What vibe coding is — and isn't.** "Vibe coding" describes working with an AI assistant in natural language to produce code: you describe intent, the AI drafts, you steer. Done well, it's *accelerated engineering* — you remain the designer, reviewer, and owner. Done badly, it's copy-paste-and-pray. The difference is you.

**The four principles:**

1. **You specify, it drafts.** The quality of output is bounded by the quality of your prompt: role, context, data schema, constraints, examples.
2. **You verify, it generates.** AI output is a *hypothesis*, not a deliverable. Every generated block gets tested before it earns trust.
3. **You own the result.** "The AI wrote it" is not a defence — for correctness, licensing, or data breaches. The human in the loop is accountable.
4. **First principles first.** This is why 60% of this module is conventional: you can only evaluate AI output on skills you already possess. You can't spot a wrong SMOTE if you don't know what SMOTE does.

**The workflow loop.** Intent → prompt → draft → run → verify → refine. The loop is the skill; the code is the by-product.

**Worked example by hand.** Prompt evolution for one task ("encode town column"):
- Weak: "encode this column" → AI guesses; maybe label-encodes a nominal column (the S05 mistake).
- Strong: "You are helping prep an HDB dataset for a random forest. The column `town` is nominal with 26 values. One-hot encode it with pandas, group any town with < 100 rows into 'OTHER' first, and show the resulting column count." → Specific, constrained, verifiable.
Same tool, different outcome. The prompt is the program.

**What you will later ask an AI to do:** this session *is* the AI-assisted content — Lab 15 runs the full loop on a real prep task.

## Slide Outline

1. **Title** — Vibe coding: steering, not surrendering.
2. **Definition** — natural-language-driven code generation.
3. **Accelerated engineering vs copy-paste-and-pray** — the human difference.
4. **Principle 1: you specify** — prompt quality bounds output quality.
5. **Principle 2: you verify** — output is a hypothesis.
6. **Principle 3: you own it** — accountability stays human.
7. **Principle 4: first principles first** — why 60% of this module is AI-free.
8. **The loop** — intent → prompt → draft → run → verify → refine.
9. **Worked example** — weak prompt vs strong prompt, side by side.
10. **The prompt is the program** — prompt design as an engineering skill.
11. **Recap + lab preview** — Lab 15: the full loop on real data.

## Mini-Quiz

1. **MCQ:** In vibe coding, accountability for the final code rests with: (a) the AI vendor (b) the human user ✅ (c) the reviewer (d) nobody.
2. **MCQ:** The strongest prompt includes: (a) just the task (b) role, context, schema, constraints, examples ✅ (c) the entire dataset pasted in (d) only the word "please".
3. **MCQ:** AI-generated code should be treated as: (a) production-ready (b) a hypothesis to verify ✅ (c) documentation (d) a unit test.
4. **Short answer:** Why does this module teach 60% of content without AI before interleaving AI-assist? *(Answer: evaluation requires first principles — you can only judge, correct, and take responsibility for AI output using knowledge you hold independently; otherwise you can't detect plausible-but-wrong code.)*
