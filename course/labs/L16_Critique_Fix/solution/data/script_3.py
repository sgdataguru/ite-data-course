"""AI-generated prep script #3 — scaler fitted on FULL data before split (train-test contamination)."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("data/cleaned_hdb.csv")
X, y = df[["floor_area_sqm", "storey"]], df.resale_price
sc = StandardScaler().fit(X)                        # BUG: fitted on ALL rows
Xt = sc.transform(X)
Xtr, Xte, ytr, yte = train_test_split(Xt, y, test_size=0.2, random_state=42)
m = KNeighborsRegressor(n_neighbors=10).fit(Xtr, ytr)
print(f"R2={r2_score(yte, m.predict(Xte)):.4f}")     # optimistic score
