# TaxRiskScan: AI System for Detecting High-Risk Tax Jurisdictions

Building AI course project

## Summary

TaxRiskScan is an AI-based tool that analyzes multinational company data and automatically flags jurisdictions with potential tax avoidance, low-tax risk, or aggressive profit-shifting patterns. It uses basic financial inputs and machine learning techniques to generate easy-to-understand compliance alerts.

## Background

Multinational companies often operate across many countries with different tax rates and reporting obligations. Regulators (OECD, EU, UN) have introduced new frameworks such as Pillar Two and Country-by-Country Reporting (CbCR), but interpreting the data remains hard.

Problems addressed:
* Difficulty detecting unusual profit patterns  
* Manual analysis of CbCR spreadsheets  
* Identifying jurisdictions with very low effective tax rates  
* Difficulty assessing where further audit or documentation is needed  

My motivation is to make tax transparency accessible and to reduce illicit profit shifting while supporting companies that want to comply proactively.

## How is it used?

1. User uploads a simple dataset (turnover, profit, number of employees, tax paid).
2. The system computes effective tax rates and productivity indicators.
3. Machine learning detects anomalies suggesting:
   * Very low taxation  
   * Mismatch between profits and economic activity  
   * High-risk jurisdictions (e.g., known tax havens)  
4. User receives:
   * A heatmap of risk scores  
   * A summary table  
   * Recommendations for documentation or review  

Primary users: auditors, financial analysts, tax officers, compliance teams.

## Data sources and AI methods

### Data

* OECD CbCR public dataset  
* EU Tax Observatory statistics  
* Manually created example datasets  
* Lists of harmful tax jurisdictions (EU/OECD)

### AI Methods

* Logistic regression for risk classification  
* Clustering (k-means) for anomaly detection  
* Rule-based scoring (ETR < 10%, profit/employee unusually high)  
* Simple data preprocessing & normalization  

## Challenges

* Does not provide legal conclusions – only risk indicators  
* Risk of misinterpretation if data quality is low  
* Anomalies may be legitimate, requiring human review  
* Data availability differs across jurisdictions  

## What next?

* Add neural-network-based risk detection  
* Integrate web scraping for real-time regulatory updates  
* Build a dashboard interface  
* Extend to UTPR, IIR, and QDMTT simulation  
* Automatic report generator for auditors  

## Acknowledgments

* Building AI course by Reaktor & University of Helsinki  
* OECD, EU Tax Observatory (open data)  
* Research inspiration from academic literature on tax transparency