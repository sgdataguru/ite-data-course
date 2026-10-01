"""Lab 6 solution tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_representation_gap_exists():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    props = df.group.value_counts(normalize=True)
    assert abs(props["A"] - props["B"]) > 0.2          # planted 70/30 gap

def test_income_gap_exists():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    rates = df.groupby("group").income_gt_50k.mean()
    assert abs(rates["A"] - rates["B"]) > 0.05         # planted historical bias
