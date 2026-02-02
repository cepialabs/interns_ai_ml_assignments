 # Week 2 Day 4 Assignment  
## Marketing and Sales Data Analysis  
  
**Date:** 02-02-2026  

---

## Assignment Description  

This assignment focuses on analyzing a **Marketing and Sales dataset** to understand the relationship between advertising spend and sales performance.  

The main objectives are:  
- To calculate the **correlation between ad spend and sales**  
- To understand the difference between **correlation and causal reasoning**  
- To identify and discuss **possible confounding variables**  

---

## Dataset  

**Source:** Kaggle  
**Dataset Type:** Marketing and Sales Dataset  
**Url:** https://www.kaggle.com/datasets/jacouchs/marketing-budget-and-actual-sales-dataset
**Columns used in this project:**  
- `marketing_budget(thousands)` – Advertising spend  
- `actual_sales(millions)` – Sales revenue  

---

## Tools & Technologies Used  

- Python  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Matplotlib  

---

## Steps Performed  

1. Loaded the dataset using Pandas  
2. Checked for missing values  
3. Calculated correlation between marketing budget and sales  
4. Implemented Pearson correlation manually  
5. Visualized data using scatter plots  
6. Drew regression line using NumPy  
7. Interpreted results  
8. Discussed correlation vs causation  
9. Listed possible confounding variables  

---

## Key Concepts  

### Correlation  
Correlation measures the **strength and direction** of the relationship between two variables.

### Correlation vs Causation  
Even if two variables are correlated, it does not mean one causes the other.  
There may be hidden factors influencing both.

---

## Possible Confounding Variables  

These factors may affect both marketing budget and sales:  
- Seasonality (festivals, holidays)  
- Discounts and offers  
- Brand reputation  
- Market demand  
- Competitor pricing  
- Product quality  

---

## Conclusion  

The analysis shows a **positive correlation** between marketing budget and sales.  
However, this does not guarantee that increasing ad spend alone will always increase sales.  
Other confounding factors must be considered before making business decisions.

---


## Learning Outcome  

This project helped in understanding:  
- How to perform correlation analysis  
- How to avoid common data errors  
- Why correlation is not equal to causation  
- How to implement statistics using only basic Python libraries
