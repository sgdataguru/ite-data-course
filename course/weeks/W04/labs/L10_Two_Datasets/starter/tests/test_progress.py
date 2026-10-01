"""Lab 10 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_district_bias_exists():
    df = pd.read_csv(HERE / "data" / "lending.csv")
    rates = df.groupby("district").approved.mean()
    assert rates.max() - rates.min() > 0.05           # planted district gap
