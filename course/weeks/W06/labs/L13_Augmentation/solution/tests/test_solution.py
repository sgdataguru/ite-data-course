"""Lab 13 solution tests."""
import pandas as pd, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_jitter_preserves_labels():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    rng = np.random.default_rng(42)
    aug = df.sample(frac=0.5, random_state=42).copy()
    aug["floor_area_sqm"] = aug.floor_area_sqm + rng.normal(0, 0.05 * df.floor_area_sqm.std(), len(aug))
    assert (aug.resale_price.values == df.loc[aug.index].resale_price.values).all()

def test_jitter_small():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    rng = np.random.default_rng(42)
    j = rng.normal(0, 0.05 * df.floor_area_sqm.std(), 1000)
    assert np.abs(j).max() < df.floor_area_sqm.std()  # jitter stays small vs feature scale
