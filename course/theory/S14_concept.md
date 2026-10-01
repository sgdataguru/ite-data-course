# S14 — Sensitive Attributes & Mitigation Strategies (C2, 1 hr)

## Concept Note

**Sensitive attributes in a Singapore/APAC context.** Under PDPA, personal data — and especially race, religion, health, and biometric data — is regulated. In practice, sensitive attributes for fairness work include: race/ethnicity, religion, gender, age, marital status, disability, nationality, and proxies (postal district, name-derived ethnicity, school attended). Two hard truths: (1) you often *cannot* simply delete the sensitive column, because proxies reconstruct it; (2) you often *must* keep it during analysis to *measure* fairness, even if the final model excludes it.

**Mitigation strategies (three stages):**

1. **Pre-processing** — fix the data before training. **Reweighing**: give under-represented group-outcome combinations larger weights so the training objective sees a balanced world. **Resampling**: over/under-sample group-outcome cells, in the spirit of C1's imbalance tools.
2. **In-processing** — constraints inside training (fairness-aware loss functions). Conceptual only at this level.
3. **Post-processing** — adjust decision thresholds per group to equalise a chosen metric. Simple and effective, but controversial: it uses the sensitive attribute at decision time.

**Worked example by hand.** Loan data: Group A approved 80% historically, Group B 50%, though qualification rates are similar. Reweighing: each (B, qualified, approved) training example gets weight 80/50 = 1.6; each (A, qualified, rejected) example gets weight > 1 too. The weighted dataset now shows no group-approval association, and the model trained on weights learns qualification, not group.

**Trade-offs.** Every mitigation trades some overall accuracy for fairness — that is the point. The choice of stage and strategy must be documented with rationale: what was measured, what was applied, what changed.

**What you will later ask an AI to do:** list plausible proxies for a sensitive attribute; explain reweighing weights for a small table; draft the mitigation section of a bias report.

## Slide Outline

1. **Title** — Measuring with sensitive data, training without bias.
2. **What counts as sensitive (SG/APAC)** — PDPA categories + proxies.
3. **The proxy problem** — deleting the column doesn't delete the information.
4. **Keep it to measure, exclude it to decide** — the dual role.
5. **Stage 1: pre-processing** — reweighing and resampling.
6. **Reweighing by hand** — the 80/50 → 1.6 weight example.
7. **Stage 2: in-processing** — fairness-aware training (conceptual).
8. **Stage 3: post-processing** — per-group thresholds; the controversy.
9. **The accuracy–fairness trade-off** — mitigations are not free.
10. **Document the decision** — strategy, rationale, measured effect.
11. **Recap + lab preview** — Lab 8 applies reweighing and resampling.

## Mini-Quiz

1. **MCQ:** Removing the race column guarantees a race-neutral model: (a) true (b) false — proxies can reconstruct it ✅ (c) true only for trees (d) true under PDPA.
2. **MCQ:** Reweighing is a: (a) post-processing technique (b) pre-processing technique ✅ (c) in-processing loss (d) deployment control.
3. **MCQ:** Post-processing threshold adjustment is controversial because: (a) it's inaccurate (b) it uses the sensitive attribute at decision time ✅ (c) it needs GPUs (d) it can't be documented.
4. **Short answer:** Why might you keep a sensitive attribute in the analysis pipeline but exclude it from model features? *(Answer: you need the attribute to compute fairness metrics and audit outcomes by group, but including it as a feature invites direct discrimination; measure with it, decide without it.)*
