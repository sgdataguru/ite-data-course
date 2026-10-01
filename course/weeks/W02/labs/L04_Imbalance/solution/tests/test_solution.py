"""Lab 4 solution tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_imbalance_present():
    df = pd.read_csv(HERE / "data" / "fraud.csv")
    ratio = df.is_fraud.value_counts(normalize=True)
    assert ratio[1] < 0.05                              # ~1% fraud

def test_smote_fold_safe():
    df = pd.read_csv(HERE / "data" / "fraud.csv")
    from sklearn.model_selection import train_test_split
    from imblearn.pipeline import Pipeline
    from imblearn.over_sampling import SMOTE
    from sklearn.neighbors import KNeighborsClassifier
    Xtr, Xte, ytr, yte = train_test_split(df.drop(columns="is_fraud"), df.is_fraud, test_size=0.3, random_state=42, stratify=df.is_fraud)
    pipe = Pipeline([("s", SMOTE(random_state=42)), ("m", KNeighborsClassifier())]).fit(Xtr, ytr)
    assert pipe.predict(Xte).shape == yte.shape        # test set untouched by SMOTE
