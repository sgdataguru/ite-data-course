"""Lab 7 solution tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_metrics_in_range():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from fairlearn.metrics import MetricFrame
    X = pd.get_dummies(df.drop(columns="income_gt_50k"), drop_first=True)
    Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, df.income_gt_50k, df.group, test_size=0.3, random_state=42)
    pred = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr).predict(Xte)
    sr = MetricFrame(metrics=lambda y, p: (p == 1).mean(), y_true=yte, y_pred=pred, sensitive_features=gte)
    assert 0 <= sr.overall <= 1                        # selection rate is a valid rate
    assert sr.difference() > 0                         # a gap exists (planted bias)
