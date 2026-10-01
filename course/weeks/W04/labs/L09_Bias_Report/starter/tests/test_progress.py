"""Lab 9 progress tests."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_report_has_five_sections():
    p = HERE / "bias_report.md"
    assert p.exists(), "bias_report.md not written yet"
    text = p.read_text()
    for s in ["Scope", "Bias risks", "Metrics", "Mitigations", "Residual"]:
        assert s in text, f"missing section: {s}"
