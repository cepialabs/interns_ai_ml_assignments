📊 Customer Retention Analysis

Week 2 – Day 5 Assignment
Date: 03-02-2026

📁 Dataset Description

The dataset contains customer purchase and behavioral information such as discount usage, purchase history, and other demographic attributes. The goal of this analysis is to examine whether offering discounts improves customer retention.

🎯 Objective

To test whether customers who received a discount are more likely to return compared to customers who did not receive a discount.

🧠 Hypothesis Formulation

Null Hypothesis (H₀):
There is no significant difference in customer retention between customers who received a discount and those who did not.

Alternative Hypothesis (H₁):
Customers who received a discount are more likely to return than customers who did not receive a discount.

📌 Key Columns Used
Column Name	Description
Discount Applied	Indicates whether a discount was applied (Yes/No)
Previous Purchases	Number of past purchases (used as a proxy for retention)
🧪 Statistical Method Used

Independent Samples t-test (Welch’s t-test)

This test is appropriate because:

Two independent groups are being compared

The outcome variable (Previous Purchases) is numerical

Group sizes and variances may differ
