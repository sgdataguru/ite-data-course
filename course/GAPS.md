# GAPS.md — Agent 6 sidecar

Missing from upstream agents (not fabricated in the portal):

1. **Full slide decks & speaker notes** — Agent 2 delivered concept notes with embedded slide outlines and quizzes per session; the portal summarises. Full `S##_slides.md` / `S##_quiz.md` as separate files were consolidated into the concept notes to keep the pack deliverable — regenerate as separate files if the LMS requires per-file uploads.
2. **Starter/solution notebooks as .ipynb** — Agent 3 delivered notebook *outlines* in the lab pack; actual .ipynb files need to be authored by the instructor (or a follow-up pass) from the outlines.
3. **Actual dataset files** — `loan_prep_test.csv`, `telecom_churn_prep_mock.csv`, and the synthetic fraud/hospital datasets are described but not generated. A prep script must be run before Week 1.
4. **fairlearn/AIF360 version pinning** — library versions change; instructor should pin and verify before Week 4.
5. **Official SS v2.0 performance-criterion IDs** — rubric criteria are traced to criterion *text* from the official docx; formal PC reference codes were not present in the extracted spec.
