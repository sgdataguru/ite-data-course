"""Lab 3 solution tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_onehot_shape():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    from sklearn.preprocessing import OneHotEncoder
    ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore").fit(df[["town"]])
    assert ohe.transform(df[["town"]]).shape[1] == df.town.nunique()

def test_ordinal_order():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    from sklearn.preprocessing import OrdinalEncoder
    oe = OrdinalEncoder(categories=[["3-ROOM", "4-ROOM", "5-ROOM", "EXECUTIVE"]]).fit(df[["flat_type"]])
    codes = oe.transform(pd.DataFrame({"flat_type": ["3-ROOM", "EXECUTIVE"]}))
    assert codes[0][0] == 0 and codes[1][0] == 3        # order preserved, not alphabetical
