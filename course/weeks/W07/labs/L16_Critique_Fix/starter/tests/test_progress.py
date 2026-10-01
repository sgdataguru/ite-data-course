"""Lab 16 progress tests — the planted bugs must be FIXED in the learner's fixed scripts."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_fixed_scripts_exist():
    for i in [1, 2, 3]:
        assert (HERE / f"fixed_script_{i}.py").exists(), f"fixed_script_{i}.py not written"

def test_fixed_2_resamples_train_only():
    text = (HERE / "fixed_script_2.py").read_text()
    assert "Pipeline" in text or "pipeline" in text      # fold-safe structure
    assert text.find("fit_resample") > text.find("train_test_split") or "Pipeline" in text
