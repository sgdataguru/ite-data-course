# Lab 1 — Exit ticket

**Task:** Commit your `cleaned_hdb.csv` to the LMS, plus one sentence:

> "The hardest bug I fixed was ___ because ___."

**Expected answer guidance (instructor):** Most learners struggle with either (a) the mixed date formats — the naive `pd.to_datetime` fails or silently mis-parses — or (b) the implausible floor-area values — imputing *before* removing 9999/-50 corrupts the median. Both answers indicate correct engagement with the lab's teaching points. Award the exit ticket if the CSV passes all 6 progress tests and the sentence names a *specific* bug (not "it was hard").
