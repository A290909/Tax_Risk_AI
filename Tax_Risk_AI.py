# TaxRiskScan: simple anomaly detector for tax compliance

import numpy as np

def anomaly_score(turnover, profit, tax_paid, employees):
    """
    A simple heuristic anomaly score:
    - Very low effective tax rate increases risk
    - Very high profit per employee increases risk
    - Negative profits combined with zero tax increases risk
    """
    if employees == 0:
        employees = 1

    etr = tax_paid / max(profit, 1)  # effective tax rate
    profit_per_employee = profit / employees

    score = 0

    # Low effective tax rate
    if etr < 0.10:
        score += 2
    elif etr < 0.15:
        score += 1

    # Unusual productivity
    if profit_per_employee > 300000:
        score += 2
    elif profit_per_employee > 100000:
        score += 1

    # Loss-making but no tax paid
    if profit < 0 and tax_paid == 0:
        score += 1

    return score, etr, profit_per_employee


# Example dataset
example = [
    ("Ireland", 5000000, 1000000, 120000, 20),
    ("Bermuda", 8000000, 3000000, 0, 5),
    ("Germany", 10000000, 2000000, 450000, 50),
]

for country, turnover, profit, tax_paid, emps in example:
    score, etr, ppe = anomaly_score(turnover, profit, tax_paid, emps)
    print(f"{country}: Risk={score}, ETR={etr:.2f}, Profit/Employee={ppe:.0f}")