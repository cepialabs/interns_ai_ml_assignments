
# Customer Retention Analysis using t-Test

📅 **Date:** 03-02-2026

---

## 📌 Project Overview

This project analyzes **customer retention behavior** using statistical hypothesis testing.
An **independent two-sample t-test** is conducted to determine whether there is a **statistically significant difference** between customers who **returned** and those who **did not return** based on a numeric business metric.

The goal is to understand whether customer return behavior is associated with measurable differences in customer characteristics.

---

## 📂 Dataset Description

**Dataset Name:** PwC Customer Retention Dashboard
**Data Source:** Kaggle
🔗 [https://www.kaggle.com/datasets/rithikmurali/pwc-customer-retention-dashboard]

The dataset represents customer data from a telecom-like business and includes:

* Customer churn / retention status
* Billing and subscription information
* Service usage details
* Customer tenure and charges

---

## 🧪 Problem Statement

**Research Question:**
Is there a statistically significant difference between returned and non-returned customers?

To answer this question, a **t-test** is used to compare the average value of a numeric variable between two independent groups.

---

## 📊 Methodology

1. Load and clean the dataset
2. Divide customers into two groups:

   * **Returned customers** (Churn = No)
   * **Not returned customers** (Churn = Yes)
3. Select a numeric variable (e.g., Monthly Charges)
4. Conduct an **independent two-sample t-test**
5. Interpret results using a **5% significance level (α = 0.05)**

---

## 📐 Hypotheses

* **Null Hypothesis (H₀):**
  There is no significant difference between returned and non-returned customers.

* **Alternative Hypothesis (H₁):**
  There is a significant difference between returned and non-returned customers.

---

## 📈 Statistical Test Used

* **Test:** Independent Two-Sample t-Test
* **Library:** `scipy.stats`
* **Significance Level:** 0.05

This test is appropriate because:

* Two independent groups are compared
* The variable of interest is numeric
* The objective is to compare group means

---

## 📝 Key Findings

The t-test results indicate that the difference in the selected numeric variable between returned and non-returned customers is **statistically significant** (p < 0.05).

This suggests that customer return behavior is associated with measurable differences in customer characteristics rather than occurring by random chance.

---

## 💼 Business Interpretation

* The identified metric may help predict customer retention
* Businesses can use this insight to:

  * Improve pricing strategies
  * Enhance customer experience
  * Reduce churn rates

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* SciPy
* Jupyter Notebook / VS Code

---

## 📌 Conclusion

This project demonstrates how **statistical hypothesis testing** can be applied to real-world customer data to gain actionable insights into **customer retention behavior**.

---


