# Dataset Description
The dataset contains customer purchase records from a Walmart-like retail system.

**Key columns used:**
- `Purchase_Amount` – Amount spent by a customer on a purchase

Other columns include customer demographics, product category, payment method, and repeat customer information, but they are not required for this analysis.

# Objectives
1. Plot a **histogram of customer purchase amounts**
2. Fit a **normal distribution** to the data
3. Calculate the **probability of a customer spending above a threshold**
4. Simulate random sales data
5. Compare simulated data with the **theoretical normal distribution**

#  Methodology

# 1. Histogram & Normal Distribution
- A histogram is plotted to visualize the distribution of purchase amounts.
- A normal distribution curve is fitted using the calculated mean and standard deviation.

# Probability Above a Threshold
The probability that a customer spends more than a given threshold (e.g., ₹300) is calculated using the **Cumulative Distribution Function (CDF)**:

\[
P(X > x) = 1 - F(x)
\]

# 3. Simulation of Sales Data
- Random sales data is generated using a normal distribution with the same mean and standard deviation.
- The simulated distribution is compared with the actual data and the theoretical curve.

# Visualizations
- Histogram of purchase amounts
- Normal distribution fit
- Probability threshold visualization
- Comparison of actual, simulated, and theoretical distributions

# Key Insights
- Customer purchase amounts approximately follow a normal distribution.
- A small proportion of customers spend significantly more than the average.
- The fitted normal distribution closely matches the real purchase data.
- Simulated sales data behaves similarly to actual customer purchases.
- Normal distribution is a reasonable model for customer spending behavior.

# Tools & Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib
- SciPy

# Conclusion
This analysis demonstrates how probability theory and normal distributions can be applied to real-world retail data to model customer spending patterns and estimate high-spending behavior.

# Author
**Danish Shaikh**  
Week 2 – Internship Assignment
