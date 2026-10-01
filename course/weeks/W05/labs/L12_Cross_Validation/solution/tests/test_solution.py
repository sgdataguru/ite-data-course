"""Lab 12 solution tests."""
import pandas as pd, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_timeseries_no_time_travel():
    df = pd.read_csv(HERE / "data" / "energy_demand.csv").sort_values("date").reset_index(drop=True)
    from sklearn.model_selection import TimeSeriesSplit
    for tr, te in TimeSeriesSplit(n_splits=5).split(df):
        assert tr.max() < te.min()                    # train strictly before test

def test_stratified_preserves_ratio():
    df = pd.read_csv(HERE / "data" / "fraud.csv")
    from sklearn.model_selection import StratifiedKFold
    y = df.is_fraud
    for _, te in StratifiedKFold(5, shuffle=True, random_state=42).split(df, y):
        assert abs(y.iloc[te].mean() - y.mean()) < 0.02
