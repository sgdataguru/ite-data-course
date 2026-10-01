"""Lab 14 solution tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_smote_grows_minority():
    df = pd.read_csv(HERE / "data" / "minority_sample.csv")
    from imblearn.over_sampling import SMOTE
    Xs, ys = SMOTE(random_state=42, k_neighbors=3).fit_resample(df.drop(columns="label"), df.label)
    assert (ys == 1).sum() > (df.label == 1).sum()

def test_smote_stays_plausible():
    df = pd.read_csv(HERE / "data" / "minority_sample.csv")
    from imblearn.over_sampling import SMOTE
    Xs, _ = SMOTE(random_state=42, k_neighbors=3).fit_resample(df.drop(columns="label"), df.label)
    assert (Xs >= df.drop(columns="label").min()).all().all()  # no impossible values
