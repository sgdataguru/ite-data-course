# Bias Assessment Report - HDB Resale Price Prep

## 1. Scope
data.gov.sg-style HDB resale transactions, 6,000 rows, 2017-2024. Sensitive-ish attributes: town, flat_type.

## 2. Bias risks identified
- Representation: towns range from 9.2% to 10.8% of the data.
- Historical: price levels embed past market conditions.
- Aggregation: one island-wide model hides town-level price behaviour (mean price gap ~18,625 SGD).

## 3. Metrics computed
Mean prediction error by flat type. Error gap: 2,965 SGD.

## 4. Mitigations applied
Inverse-share reweighing of towns. Error gap changed from 2,965 to 2,996 SGD (R2 cost 0.0000). Honest finding: the mitigation did NOT close the gap - it is driven by flat-type price structure, not town representation. A good report says what the mitigation did not fix.

## 5. Residual risks
Metric choice is a values decision; re-audit on new data before deployment.
