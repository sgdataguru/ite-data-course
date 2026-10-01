"""DE5002FP — Master dataset generator.

Deterministically generates every synthetic dataset used across the labs.
Run:  python generate_all.py
Output: labs/data/*.csv  (byte-identical across runs — fixed seeds, sorted output)
"""
import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parent / "data"
OUT.mkdir(parents=True, exist_ok=True)

def save(df: pd.DataFrame, name: str):
    df.to_csv(OUT / name, index=False)
    print(f"wrote {name}: {df.shape[0]} rows x {df.shape[1]} cols")

# ---------------------------------------------------------------- Lab 1 / 5 / 11 / 13 / 15
def gen_hdb_messy(n=6000, seed=42):
    """HDB-style resale data with deliberate mess: '$' strings, mixed dates,
    NaNs, a duplicate column, and implausible outliers."""
    rng = np.random.default_rng(seed)
    towns = ["ANG MO KIO", "BEDOK", "CLEMENTI", "JURONG WEST", "TAMPINES",
             "WOODLANDS", "YISHUN", "PUNGGOL", "HOUGANG", "GEYLANG"]
    flat_types = ["3-ROOM", "4-ROOM", "5-ROOM", "EXECUTIVE"]
    df = pd.DataFrame({
        "town": rng.choice(towns, n),
        "flat_type": rng.choice(flat_types, n, p=[.3, .35, .25, .1]),
        "floor_area_sqm": rng.normal(95, 22, n).clip(40, 200).round(1),
        "storey": rng.integers(1, 30, n),
        "lease_commence": rng.integers(1975, 2015, n),
    })
    base = (df.floor_area_sqm * 4500
            + df.storey * 3000
            + (2024 - df.lease_commence) * -1500
            + rng.normal(0, 40000, n))
    df["resale_price"] = base.clip(150000, 1500000).round(-3)
    # mess 1: price as "$530,000" strings
    df["resale_price"] = df.resale_price.map(lambda v: f"${v:,.0f}")
    # mess 2: mixed date formats
    dates = pd.to_datetime("2017-01-01") + pd.to_timedelta(rng.integers(0, 2555, n), "D")
    df["sale_date"] = [d.strftime("%Y-%m-%d") if i % 2 == 0 else d.strftime("%d/%m/%Y")
                        for i, d in enumerate(dates)]
    # mess 3: NaNs in floor_area (47-ish) and a few in storey
    na_idx = rng.choice(n, 52, replace=False)
    df.loc[na_idx[:47], "floor_area_sqm"] = np.nan
    df.loc[na_idx[47:], "storey"] = np.nan
    # mess 4: duplicate column
    df["floor_area_sqm.1"] = df.floor_area_sqm
    # mess 5: a few implausible outliers pre-corruption
    out_idx = rng.choice(n, 5, replace=False)
    df.loc[out_idx, "floor_area_sqm"] = [9999.0, -50.0, 0.0, 400.0, 250.0]
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)  # shuffle deterministically
    save(df, "hdb_messy.csv")

# ---------------------------------------------------------------- Lab 4 / 12
def gen_fraud(n=1000, seed=7):
    """990:10 imbalanced fraud dataset."""
    rng = np.random.default_rng(seed)
    n_fraud = n // 100
    x_legit = rng.normal([50, 12000, 3.5], [10, 4000, 1.0], (n - n_fraud, 3))
    x_fraud = rng.normal([85, 3000, 7.5], [8, 1500, 0.8], (n_fraud, 3))
    X = np.vstack([x_legit, x_fraud])
    y = np.array([0] * (n - n_fraud) + [1] * n_fraud)
    df = pd.DataFrame(X, columns=["txn_amount", "txn_distance_km", "txn_hour_dev"]) \
        .round(2).assign(is_fraud=y)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    save(df, "fraud.csv")

# ---------------------------------------------------------------- Labs 6-10 (C2)
def gen_adult_like(n=8000, seed=11):
    """Adult-income-style dataset with representation + measurement bias baked in."""
    rng = np.random.default_rng(seed)
    # representation bias: 70/30 group split
    group = rng.choice(["A", "B"], n, p=[0.7, 0.3])
    # historical bias: group B gets systematically lower income
    edu = rng.integers(6, 20, n)
    hours = rng.normal(40, 8, n).clip(10, 90).round(1)
    noise = rng.normal(0, 1, n)
    logit = (0.5 * (edu - 12) + 0.04 * (hours - 40) + noise
             + np.where(group == "B", -0.9, 0.0))          # historical bias
    income50k = (logit > 0).astype(int)
    # measurement bias: hours self-reported (noisy) for group B, verified for A
    hours_obs = hours + np.where(group == "B", rng.normal(0, 6, n), 0)
    df = pd.DataFrame({
        "age": rng.integers(18, 70, n),
        "education_years": edu,
        "hours_per_week": hours_obs.round(1),
        "workclass": rng.choice(["Private", "Govt", "Self-emp"], n, p=[.7, .2, .1]),
        "group": group,
        "income_gt_50k": income50k,
    })
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    save(df, "adult_like.csv")

def gen_lending(n=5000, seed=13):
    """Lending dataset: approval imbalance 92:8 + district proxy bias."""
    rng = np.random.default_rng(seed)
    district = rng.choice(["CENTRAL", "EAST", "WEST", "NORTH", "NORTH-EAST"], n)
    score = rng.normal(650, 80, n).clip(300, 900).round(0)
    income = rng.normal(4500, 1500, n).clip(800, 20000).round(0)
    # district-based historical bias
    d_pen = {"CENTRAL": 0.0, "EAST": -0.2, "WEST": -0.5, "NORTH": -0.8, "NORTH-EAST": -0.7}
    logit = (score - 650) / 120 + (income - 4500) / 2000 + np.array([d_pen[d] for d in district])
    approved = (logit + rng.normal(0, 1, n) > 1.4).astype(int)
    df = pd.DataFrame({"district": district, "credit_score": score,
                       "monthly_income": income, "approved": approved})
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    save(df, "lending.csv")

# ---------------------------------------------------------------- Lab 12 (time series)
def gen_energy(days=730, seed=17):
    """Daily energy demand: trend + weekly + yearly seasonality + noise."""
    rng = np.random.default_rng(seed)
    t = pd.date_range("2022-01-01", periods=days, freq="D")
    doy = np.arange(days)
    demand = (120 + 8 * (doy / 365)                       # trend
              + 25 * np.sin(2 * np.pi * doy / 365 - np.pi / 2)   # yearly
              + 6 * np.sin(2 * np.pi * (doy % 7) / 7)     # weekly
              + rng.normal(0, 5, days)).round(1)
    df = pd.DataFrame({"date": t.strftime("%Y-%m-%d"), "demand_mw": demand})
    save(df, "energy_demand.csv")

# ---------------------------------------------------------------- Lab 14 / 25 (synthetic)
def gen_minority_sample(n=200, seed=19):
    """Small minority-class sample for SMOTE vs GenAI comparison."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "feature_a": rng.normal(10, 2, n).round(2),
        "feature_b": rng.normal(5, 1, n).round(2),
        "feature_c": rng.normal(50, 10, n).round(1),
        "label": rng.choice([0, 1], n, p=[0.95, 0.05]),
    })
    save(df, "minority_sample.csv")

# ---------------------------------------------------------------- Mock/test-style (Lab 16 planted bugs use fraud.csv)
if __name__ == "__main__":
    gen_hdb_messy()
    gen_fraud()
    gen_adult_like()
    gen_lending()
    gen_energy()
    gen_minority_sample()
    print("All datasets generated deterministically.")
