"""AI-generated prep script #1 — contains a HALLUCINATED API."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import SmartEncoder  # BUG: hallucinated — no such class exists

df = pd.read_csv("data/cleaned_hdb.csv")
X, y = df.drop(columns="resale_price"), df.resale_price
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
enc = SmartEncoder()
Xtr_t = enc.fit_transform(Xtr[["town"]], ytr)
print("encoded", Xtr_t.shape)
