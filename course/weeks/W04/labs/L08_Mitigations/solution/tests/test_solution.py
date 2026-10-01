"""Lab 8 solution tests."""
import pandas as pd, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_reweighing_weights_sum():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    g, y = df.group, df.income_gt_50k
    w = np.ones(len(df))
    for grp in ["A", "B"]:
        for out in [0, 1]:
            mask = (g == grp) & (y == out)
            w[mask.values] = (g == grp).mean() * (y == out).mean() / mask.mean()
    assert abs(w.sum() - len(df)) < 1e-6               # reweighing preserves total weight
