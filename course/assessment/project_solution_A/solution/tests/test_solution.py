"""Option A solution tests — verify the worked solution's key outputs.
Run: pytest tests/ -v"""
import pandas as pd
import numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def _clean():
    df = pd.read_csv(HERE / "data" / "hdb_messy.csv")
    df["resale_price"] = (df["resale_price"].str.replace("$", "", regex=False)
                          .str.replace(",", "", regex=False).astype(float))
    df["sale_date"] = pd.to_datetime(df["sale_date"], format="mixed", dayfirst=True)
    bad = ~df["floor_area_sqm"].between(30, 250)
    df.loc[bad, "floor_area_sqm"] = np.nan
    df["floor_area_sqm"] = df["floor_area_sqm"].fillna(df["floor_area_sqm"].median())
    df["storey"] = df["storey"].fillna(df["storey"].median())
    return df.drop(columns=["floor_area_sqm.1"])


def test_m1_clean_pipeline():
    df = _clean()
    assert len(df) == 6000
    assert pd.api.types.is_float_dtype(df["resale_price"])
    assert df.notna().all().all()


def test_m2_representation_gap_exists():
    df = _clean()
    rep = df["town"].value_counts(normalize=True)
    # towns are not exactly equally represented; the gap is small on this
    # synthetic stand-in (real data.gov.sg data shows a much larger gap)
    assert rep.max() - rep.min() > 0.005


def test_m3_splits_disjoint():
    df = _clean()
    from sklearn.model_selection import train_test_split
    Xtr, Xtmp = train_test_split(df, test_size=0.30, random_state=42)
    Xval, Xte = train_test_split(Xtmp, test_size=0.33, random_state=42)
    assert set(Xtr.index) & set(Xte.index) == set()
    assert len(Xtr) + len(Xval) + len(Xte) == len(df)


def test_m4_readiness_checks_pass():
    df = _clean()
    assert df["resale_price"].between(100_000, 2_000_000).all()
    assert df["floor_area_sqm"].between(30, 250).all()
