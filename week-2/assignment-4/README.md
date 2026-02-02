# Marketing & Sales Correlation Analysis

## 📌 Project Overview
This project analyzes the relationship between **advertising spend** and **sales revenue** using a Marketing & Sales dataset.  
The objective is to:
- Measure the **correlation** between ad spend and sales
- Understand the difference between **correlation and causation**
- Identify **possible confounding variables** that may affect the results

The analysis is performed using **Python** in a **Jupyter Notebook** environment.

---

## 📊 Dataset Description
The dataset used is `marketing_sales.csv`, which contains the following columns:

| Column Name        | Description |
|-------------------|-------------|
| TV                | TV advertising spend (in thousands) |
| Radio             | Radio advertising spend (in thousands) |
| Social_Media      | Social media advertising spend (in thousands) |
| Sales             | Sales revenue (in thousands) |

Each row represents advertising spend across different channels and the corresponding sales outcome.

---

## 🛠️ Tools & Libraries Used
- Python 3.x  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## 📈 Analysis Performed
The project includes the following steps:

1. **Data Loading & Exploration**
   - Reading the CSV file
   - Viewing dataset structure and summary statistics

2. **Correlation Analysis**
   - Computing a correlation matrix
   - Visualizing correlations using a heatmap
   - Calculating individual correlations between each ad channel and sales

3. **Data Visualization**
   - Scatter plots to visually inspect relationships
   - Regression line to show trend between ad spend and sales

4. **Linear Regression**
   - Simple linear regression model
   - Demonstrates association between ad spend and sales

---

## 🔍 Correlation vs Causation
While the analysis shows a positive correlation between advertising spend and sales, this **does not prove causation**.  
Correlation only indicates that two variables move together, not that one directly causes the other.

---

## ⚠️ Possible Confounding Variables
Several factors may influence both advertising spend and sales:
- Seasonality (festive or holiday periods)
- Market demand changes
- Pricing strategies and discounts
- Brand awareness
- Economic conditions

These confounders must be controlled to make causal claims.

---

## 📌 Conclusion
The project demonstrates that advertising spend is positively correlated with sales.  
However, further analysis such as controlled experiments, time-series analysis, or causal inference methods are required to establish causality.

---

## ▶️ How to Run the Project
1. Place `marketing_sales.csv` and the Jupyter notebook in the same folder
2. Open the notebook using Jupyter
3. Run cells sequentially from top to bottom

---

## 📁 Project Structure
├── marketing_sales.csv
├── marketing_sales_analysis.ipynb
├── README.md