# 📊 Customer Churn Prediction — BCG Data Science Virtual Experience Program

This repository contains my complete end-to-end data science workflow completed as part of:

**Boston Consulting Group (BCG) – Data Science & Advanced Analytics Virtual Experience Program (The Forage)**  

---

## 🚀 Project Objective

To analyze customer behavior and build a machine learning model that predicts **customer churn**, enabling the business to proactively retain customers and reduce revenue loss.

---

## 🛠️ Project Workflow

| Phase | Description |
|-------|-------------|
| **Task 1 — Exploratory Data Analysis (EDA)** | Loaded client and pricing datasets, visualized churn distribution using stacked bar charts & histograms. :contentReference[oaicite:2]{index=2} |
| **Task 2 — Feature Engineering** | Created new features such as: contract duration, off-peak price change (Dec–Jan), price variance, monthly breakdowns, etc. :contentReference[oaicite:3]{index=3} |
| **Task 3 — Modeling** | Prepared dataset (`X`, `y`), performed train/test split, trained Random Forest Classifier, evaluated using Accuracy, Precision, Recall, and Confusion Matrix. |
| **Task 4 — Executive Summary** | Converted insights into a concise PDF slide for leadership and stakeholders. |

---

## 🧠 Key Insights

- Churn rate ≈ **10%**
- Model accuracy: **90.36%**
- Precision (churn class): **82%** ✅
- Recall (churn class): **5%** ⚠️ *(model struggles to detect churners)*

> The model is excellent at predicting customers who **stay**,  
> but struggles to identify customers who **leave (churn)**.

---

## 📈 Model Performance Summary

| Metric | Result |
|--------|--------|
| ✅ Accuracy | **90.36%**
| ✅ Precision | **82%**
| ⚠️ Recall | **5%**
| 🔁 Confusion Matrix | TN: 3282, FP: 4, FN: 348, TP: 18 |

---
price_df["price_month"] = price_df["price_date"].dt.month

