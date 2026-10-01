"""AI-generated prep script #2 — SMOTE applied BEFORE the split (silent correctness bug)."""
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score

df = pd.read_csv("data/fraud.csv")
X, y = df.drop(columns="is_fraud"), df.is_fraud
Xs, ys = SMOTE(random_state=42).fit_resample(X, y)   # BUG: resampling the FULL dataset
Xtr, Xte, ytr, yte = train_test_split(Xs, ys, test_size=0.3, random_state=42)
m = KNeighborsClassifier().fit(Xtr, ytr)
p = m.predict(Xte)
print(f"accuracy={accuracy_score(yte,p):.3f} recall={recall_score(yte,p):.3f}")  # beautiful lie
