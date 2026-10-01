"""Lab 1 progress tests — run with: pytest tests/ -v
These test the learner's work-in-progress notebook output (cleaned_hdb.csv
in the starter folder). They pass only when the lab is correctly completed."""
import pandas as pd
import numpy as np
from pathlib import Path

CLEANED = Path(__file__).resolve().parent.parent / "cleaned_hdb.csv"


def test_cleaned_file_exists():
    assert CLEANED.exists(), "cleaned_hdb.csv not found — complete the lab and export it."


def test_price_is_float():
    df = pd.read_csv(CLEANED)
    assert pd.api.types.is_float_dtype(df["resale_price"]), "resale_price must be float"


def test_price_range_plausible():
    df = pd.read_csv(CLEANED)
    assert df["resale_price"].between(100_000, 2_000_000).all(), \
        "implausible resale prices remain — check your conversion"


def test_no_duplicate_column():
    df = pd.read_csv(CLEANED)
    assert "floor_area_sqm.1" not in df.columns, "duplicate column not dropped"


def test_no_missing_values():
    df = pd.read_csv(CLEANED)
    assert df["floor_area_sqm"].notna().all(), "floor_area_sqm still has NaNs"
    assert df["storey"].notna().all(), "storey still has NaNs"


def test_floor_area_plausible():
    df = pd.read_csv(CLEANED)
    assert df["floor_area_sqm"].between(30, 250).all(), \
        "implausible floor areas remain (9999 / -50 / 0 bugs not fixed)"
