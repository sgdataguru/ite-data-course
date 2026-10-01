"""Lab 11 solution tests."""
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
HERE = Path(__file__).resolve().parent.parent

def test_split_disjoint():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    Xtr, Xtmp = train_test_split(df, test_size=0.30, random_state=42)
    Xval, Xte = train_test_split(Xtmp, test_size=0.33, random_state=42)
    assert set(Xtr.index) & set(Xte.index) == set()   # no overlap
    assert len(Xtr) + len(Xval) + len(Xte) == len(df)

def test_scaler_uses_train_stats():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    from sklearn.preprocessing import StandardScaler
    Xtr, Xte = train_test_split(df[["floor_area_sqm"]], test_size=0.2, random_state=42)
    sc = StandardScaler().fit(Xtr)
    assert sc.mean_[0] == Xtr.floor_area_sqm.mean()   # train stats, not full-data stats
