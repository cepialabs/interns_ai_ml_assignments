# Week 2 – Day 4 Assignment  
## Date: 2 February 2026  

## Title  
Correlation Analysis between Marketing Budget and Sales  

---

## Objective  
The objective of this assignment is to analyze the relationship between marketing expenditure and sales performance. The study focuses on identifying correlation, understanding the difference between correlation and causation, and discussing possible confounding variables that may influence sales.

---

## Dataset Description  
The dataset used in this assignment is a Marketing & Sales dataset containing the following columns:

- **marketing_budget(thousands):** Marketing expenditure in thousands  
- **actual_sales(millions):** Actual sales achieved in millions  

---

## Step 1: Data Loading  
The dataset was loaded using the Pandas library. Initial inspection was performed to understand the structure, data types, and presence of missing values.

---

## Step 2: Data Cleaning  
- Checked for missing values  
- Ensured both columns were numeric  
- Removed null or invalid entries if present  

This step ensures reliable correlation results.

---

## Step 3: Correlation between Marketing Budget and Sales  
Pearson correlation was calculated to measure the linear relationship between marketing budget and actual sales.

### Interpretation:
- A **positive correlation** indicates that higher marketing spend is associated with higher sales  
- A **negative correlation** indicates an inverse relationship  
- A correlation value close to **0** indicates a weak or no linear relationship  

---

## Step 4: Visualization  
A scatter plot was used to visually examine the relationship between marketing budget and sales.

- X-axis: Marketing Budget (Thousands)  
- Y-axis: Actual Sales (Millions)  

The visualization helps confirm the trend suggested by the correlation value.

---

## Step 5: Correlation vs Causal Reasoning  

### Correlation  
- Measures the strength and direction of association  
- Does not imply cause-and-effect  
- Two variables may be correlated due to external factors  

### Causation  
- Indicates that one variable directly affects another  
- Requires controlled experiments, time precedence, and elimination of confounders  

**Conclusion:**  
Correlation alone cannot prove that increased marketing budget causes higher sales.

---

## Step 6: Possible Confounders  
Confounding variables are factors that influence both marketing budget and sales, leading to misleading correlations.

### Possible Confounders Not Present in the Dataset:
1. Seasonal demand  
2. Discounts and promotional offers  
3. Brand popularity and reputation  
4. Market competition  
5. Economic conditions  

These variables may increase sales independently of marketing expenditure.

---

## Step 7: Key Findings  
- Marketing budget and sales show a measurable correlation  
- Correlation does not establish causation  
- External confounding factors may influence the observed relationship  

---

## Conclusion  
The analysis shows that while marketing budget and sales are correlated, the relationship does not guarantee causality. To establish causal impact, additional variables, controlled experiments, or advanced statistical models are required.

---

## Tools & Libraries Used  
- Python  
- Pandas  
- Matplotlib  
- NumPy  

---


