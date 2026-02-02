# Week 2 – Day 3 Assignment  
**Date:** 30 January 2026  

## 📌 Title  
Customer Purchase Amount Analysis Using Probability Distribution

---

## 📂 Dataset Description  
The dataset contains customer purchase information with the following columns:

- Customer Reference ID  
- Item Purchased  
- Purchase Amount (USD)  
- Date Purchase  
- Review Rating  
- Payment Method  

For this assignment, the **Purchase Amount (USD)** column is used for statistical analysis.

---

## 🎯 Objectives  
1. Plot a histogram of customer purchase amounts  
2. Fit a normal distribution to the purchase data  
3. Calculate the probability of a customer spending above a given threshold  
4. Simulate random sales data using a theoretical normal distribution  
5. Compare actual purchase data with simulated data  

---

## 🛠️ Tools & Libraries Used  
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- SciPy  

---

## 🧪 Step-Wise Approach  

### Step 1: Data Loading  
The dataset is loaded using Pandas and basic inspection is performed.

### Step 2: Data Cleaning  
- Converted purchase amounts to numeric values  
- Removed missing (`NaN`) and non-finite values  
This ensures the data is suitable for statistical analysis.

### Step 3: Histogram Plot  
A histogram is plotted to visualize the distribution of customer purchase amounts.

### Step 4: Normal Distribution Fitting  
Mean (μ) and standard deviation (σ) are calculated and used to fit a normal distribution.

### Step 5: Probability Calculation  
The probability that a customer spends more than a specified threshold amount is computed using the cumulative distribution function (CDF).

### Step 6: Sales Data Simulation  
Random sales data is generated using the fitted normal distribution parameters.

### Step 7: Comparison  
Actual purchase data and simulated data are compared visually using histograms.

---

## 📊 Key Observations  
- Customer purchase behavior follows an approximately normal distribution  
- High-value customer spending probability can be estimated statistically  
- Simulated data closely matches the theoretical distribution  

---

## ✅ Conclusion  
This analysis demonstrates how probability distributions can be applied to real-world customer purchase data to understand spending patterns, estimate probabilities, and validate assumptions through simulation.

---

  
