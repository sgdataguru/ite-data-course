# S23 — AI-Based Data Augmentation & Synthetic Data (C3, 1 hr)

## Concept Note

**Augmentation vs synthesis.** *Augmentation* transforms existing examples (rotate an image, jitter a number, swap a word). *Synthesis* creates new examples from a learned distribution (SMOTE interpolation, GAN samples, LLM-generated rows). Augmentation says "the same data, viewed differently"; synthesis says "new data, statistically plausible".

**An augmentation taxonomy.**
- **Image:** rotation, flip, crop, brightness, noise.
- **Tabular numeric:** adding small Gaussian noise, binning + jitter, scaling within feature range.
- **Tabular categorical:** rare-category swapping, back-translation of text fields.
- **Text:** paraphrase, back-translation, synonym replacement.

**Synthetic data — three approaches (conceptual):**
1. **SMOTE** — interpolation between minority neighbours (from C1). Simple, fast, no new "shapes" of data.
2. **GANs** — two networks compete: a generator forges samples, a discriminator detects forgeries; the generator gets good. Powerful for images and complex tabular distributions; hard to train, risk of mode collapse.
3. **LLM-generated** — prompt a model: "generate 50 realistic rows matching this schema and distribution." Fast and flexible; risks: hallucinated values, subtle distribution drift, leakage of real records the LLM memorised.

**Worked example by hand.** Tabular augmentation: a customer's `age = 34`, `income = 4500`. Gaussian jitter: age → 34.7, income → 4480 (noise σ = 5% of feature std). The label stays the same — augmentation must not change the truth.

**The verification duty.** Synthetic/augmented data must be checked: does the class balance improve? Does the distribution still resemble the original? Did we accidentally create impossible rows (negative age, 999-room flats)? QA of generated data is a C3 performance criterion.

**What you will later ask an AI to do:** generate synthetic rows from a schema; critique its own generated data for plausibility; write a distribution-comparison check between real and synthetic data.

## Slide Outline

1. **Title** — More data without collecting more data.
2. **Augmentation vs synthesis** — transform vs create.
3. **The taxonomy** — image / numeric / categorical / text techniques.
4. **The jitter example** — age 34 → 34.7; label unchanged.
5. **SMOTE recap** — interpolation; no new shapes.
6. **GANs** — generator vs discriminator; power and pitfalls.
7. **LLM-generated rows** — fast, flexible, hallucination-prone.
8. **The verification duty** — balance, distribution, plausibility.
9. **Impossible rows** — negative ages and 999-room flats.
10. **Recap + lab preview** — Labs 13–14: augmentation and synthesis hands-on.

## Mini-Quiz

1. **MCQ:** Adding Gaussian noise to `income` while keeping the label is: (a) synthesis (b) augmentation ✅ (c) leakage (d) encoding.
2. **MCQ:** A GAN's generator learns by: (a) copying training rows (b) fooling the discriminator ✅ (c) interpolating neighbours (d) averaging classes.
3. **MCQ:** The biggest risk of LLM-generated tabular data is: (a) speed (b) hallucinated or drifting values ✅ (c) file size (d) licensing of pandas.
4. **Short answer:** Give two checks you would run on a synthetic dataset before using it. *(Answer: e.g., compare feature distributions/descriptive stats against the real data; validate domain constraints (no negative ages); check class balance and that no real-record duplicates leaked in.)*
