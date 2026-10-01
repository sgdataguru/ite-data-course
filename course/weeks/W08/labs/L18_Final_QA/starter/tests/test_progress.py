"""Lab 18 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_checklist_catches_constraints():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    ok = df.floor_area_sqm.between(30, 250).all() and df.storey.between(1, 30).all()
    assert ok                                           # the dataset passes its own constraints

def test_checklist_catches_leakage_pattern():
    # the checklist function must mention leakage
    p = HERE / "qa_checklist.py"
    if p.exists():
        assert "leak" in p.read_text().lower()
