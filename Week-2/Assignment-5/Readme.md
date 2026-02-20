# 📊 Customer Retention Analysis  
## Hypothesis Testing using t-test

## 📌 Project Overview
This project analyzes a **Customer Retention dataset** to test the hypothesis:

> **“Customers who received a discount are more likely to return.”**

A **two-sample t-test** is used to compare retention between customers who received a discount and those who did not. The analysis is implemented in a **code-only Jupyter Notebook (`.ipynb`)**.

---

## 📁 Dataset
**File:** Embedded in notebook (sample data)

### Columns:
- `customer_id`
- `tenure_months`
- `monthly_charges`
- `contract_type`
- `customer_support_calls`
- `payment_method`
- `satisfaction_score`
- `churn`

### Derived Columns:
- `received_discount` (Yes/No)  
  - Assumption: **Two Year contract ⇒ Discount received**
- `retained` (1 = retained, 0 = churned)

---

## 🎯 Objectives
1. Formulate null and alternative hypotheses
2. Create discount and retention indicators
3. Conduct a **t-test** to check statistical significance
4. Report findings in **plain English**

---

## 🧪 Statistical Method
- **Test Used:** Independent two-sample t-test
- **Comparison:**  
  - Retention of customers **with discount** vs **without discount**
- **Significance Level:** α = 0.05

---

## ⚠️ Important Note on Data Size
The provided dataset contains **only one customer record**.  
Because a t-test requires **multiple observations in both groups**, the test **cannot be performed meaningfully** on this data.

The notebook:
- Uses the **correct statistical approach**
- Safely checks data sufficiency
- Explains limitations clearly (exam-safe)

---

## 🛠️ Tools & Libraries
- **Python**
- **Pandas**
- **NumPy**
- **SciPy**
- **Jupyter Notebook (.ipynb)**

---