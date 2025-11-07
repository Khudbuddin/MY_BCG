# 🔍 Customer Churn Prediction | BCG Data Science Virtual Experience Program

This repository contains the end-to-end work completed as part of the  
**Boston Consulting Group (BCG) – Data Science & Advanced Analytics Virtual Experience (The Forage)**.

The objective of the project was to predict *customer churn* using machine learning techniques and deliver actionable insights to the business stakeholders.

---

## 📂 Project Overview

| Task | Description |
|------|-------------|
| **Task 1: Exploratory Data Analysis (EDA)** | Identified trends and insights regarding customer churn. |
| **Task 2: Feature Engineering** | Created meaningful new features such as consumption behavior, price differences, contract duration, etc. |
| **Task 3: Modeling** | Built a Random Forest Classifier and evaluated model performance using accuracy, precision, recall, and confusion matrix. |
| **Task 4: Executive Summary** | Presented insights and recommendations to stakeholders in a slide format. |

---

## 🧠 Key Insights

- Churn rate in the dataset is approximately **10%**.
- The model had a **high accuracy (90.36%)** but struggled to detect churners.
- Recall score for churn prediction was **5%**, indicating more feature engineering or better model tuning is required.
- Precision was **82%**, meaning predictions of churn were mostly correct.

---

## 📊 Model Performance Summary

| Metric | Score |
|--------|-------|
| **Accuracy** | 90.36% |
| **Precision** | 82% |
| **Recall** | 5% |
| **Confusion Matrix** | TP: 18, FP: 4, TN: 3282, FN: 348 |

➡️ The model is excellent at predicting non-churn customers,  
but struggles to correctly identify churners.

---

## 📌 Business Recommendation

> **Prioritize feature engineering and model tuning to improve recall**,  
> so the business can proactively retain customers likely to churn  
> and reduce revenue loss.

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn (Visualization)
- Scikit-learn (Modeling)
- Jupyter Notebook

---

## 📁 Repository Contents

