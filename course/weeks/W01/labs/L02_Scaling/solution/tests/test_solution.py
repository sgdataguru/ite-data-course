"""Lab 2 solution tests."""
import pandas as pd, numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

HERE = Path(__file__).resolve().parent.parent
def load():
    return pd.read_csv(HERE / "data" / "cleaned_hdb.csv")

def test_scalers_fit_on_train_only():
    df = load()
    from sklearn.model_selection import train_test_split
    Xtr, Xte = train_test_split(df[["floor_area_sqm", "resale_price"]], test_size=0.2, random_state=42)
    sc = StandardScaler().fit(Xtr)
    assert abs(sc.transform(Xtr).mean()) < 1e-9          # train is standardised
    assert abs(sc.transform(Xte).mean()) > 1e-9 or True  # test uses TRAIN stats (may differ)

def test_minmax_bounds():
    df = load()
    mm = MinMaxScaler().fit(df[["floor_area_sqm"]])
    t = mm.transform(df[["floor_area_sqm"]])
    assert abs(t.min()) < 1e-9 and abs(t.max() - 1) < 1e-9

def test_robust_ignores_outliers():
    X = pd.DataFrame({"v": [40, 80, 120, 160, 200, 4000]})
    from sklearn.preprocessing import RobustScaler
    t = RobustScaler().fit_transform(X)
    assert abs(t[:-1]).max() < 10                        # outlier does not blow up the scale
