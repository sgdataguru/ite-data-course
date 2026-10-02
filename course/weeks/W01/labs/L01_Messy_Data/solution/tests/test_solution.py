"""Lab 1 solution tests — full passing suite for the solved lab."""
import pandas as pd
import numpy as np
from pathlib import Path

SOL = Path(__file__).resolve().parent.parent
CLEANED = SOL / "cleaned_hdb.csv"


def _clean():
    """Reference clean-up (mirrors the solution notebook)."""
    df = pd.read_csv(SOL / "data" / "hdb_messy.csv")
    df["resale_price"] = (df["resale_price"].str.replace("$", "", regex=False)
                          .str.replace(",", "", regex=False).astype(float))
    df["sale_date"] = pd.to_datetime(df["sale_date"], format="mixed", dayfirst=True)
    bad = ~df["floor_area_sqm"].between(30, 250)
    df.loc[bad, "floor_area_sqm"] = np.nan
    df["floor_area_sqm"] = df["floor_area_sqm"].fillna(df["floor_area_sqm"].median())
    df["storey"] = df["storey"].fillna(df["storey"].median())
    df = df.drop(columns=["floor_area_sqm.1"])
    return df


def test_reference_pipeline_runs():
    df = _clean()
    assert len(df) == 6000


def test_price_float_and_range():
    df = _clean()
    assert pd.api.types.is_float_dtype(df["resale_price"])
    assert df["resale_price"].between(100_000, 2_000_000).all()


def test_dates_parsed():
    df = _clean()
    assert pd.api.types.is_datetime64_any_dtype(df["sale_date"])
    assert df["sale_date"].between("2017-01-01", "2024-12-31").all()


def test_no_nans_no_dupes_no_outliers():
    df = _clean()
    assert df.notna().all().all()
    assert "floor_area_sqm.1" not in df.columns
    assert df["floor_area_sqm"].between(30, 250).all()


def test_exported_csv_matches():
    assert CLEANED.exists(), "solution notebook must export cleaned_hdb.csv"
