# Week 2 Day 5 Assignment  
## Customer Retention Analysis using T-Test  
**Date:** 03-02-2026  

---

## Assignment Description  

This assignment focuses on analyzing a **Customer Retention dataset** to determine whether there is a statistically significant difference between retained and non-retained customers.

The main objectives of this assignment are:

- To perform a **t-test** to check significance  
- To compare customer behavior across two groups  
- To interpret results in simple English  

---

## Dataset Resource : kaggle
**URL** https://www.kaggle.com/datasets?search=customer+retention

**Dataset Type:** Customer Retention Dataset  

### Columns used in this Assignment:

- `custid` – Unique customer ID  
- `retained` – Customer retained or not (1 = Yes, 0 = No)  
- `created` – Account creation date  
- `firstodr` – First order date  
- `lastodr` – Last order date  
- `esent` – Emails sent  
- `eopenrate` – Email open rate  
- `eclickrate` – Email click rate  
- `avgorder` – Average order value  
- `ordfreq` – Order frequency  
- `paperless` – Paperless billing  
- `refill` – Refill service  
- `doorstep` – Doorstep delivery  
- `favday` – Favorite purchase day  

---

## Tools & Technologies Used  

- Python  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Matplotlib 

---

## Steps Performed  

- Loaded dataset using Pandas  
- Checked for missing values  
- Divided customers into two groups:
  - Retained customers  
  - Non-retained customers  
- Calculated mean and standard deviation  
- Implemented **Independent T-Test manually**  
- Visualized data using box plots  
- Compared t-value with critical value  
- Interpreted results in plain English  

---

## Key Concepts  

### T-Test  
T-test is a statistical method used to determine whether the difference between two group means is significant or not.

### Null Hypothesis (H₀)  
There is no significant difference between retained and non-retained customers.

### Alternative Hypothesis (H₁)  
There is a significant difference between retained and non-retained customers.

---

## Conclusion  

The analysis helps in understanding whether customer retention is influenced by behavioral metrics like order value and engagement.

If the **p-value < 0.05**, the difference is statistically significant.  
If the **p-value > 0.05**, the difference is not significant.

---

## Learning Outcome  

This project helped in learning:

- Real-world application of t-test  
- Manual statistical computation  
- Business interpretation of statistical results  
- Importance of customer retention analysis  

---

## Final Note  

Customer retention analysis helps companies design better marketing strategies and improve customer experience using data-driven insights.
