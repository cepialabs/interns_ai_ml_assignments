## Customer Retention Analysis Using T-Test
Bodasu karunanjali

INT2026-1462

## Project Overview

This project analyzes a Customer Retention (Telco Churn) dataset to understand the factors influencing customer retention and churn. The primary objective is to conduct an independent t-test to determine whether there is a statistically significant difference in monthly charges between retained and churned customers.

The findings are reported in plain English, as required in the assignment.

## Dataset Description

The dataset used in this project contains information about 7,043 customers with 33 attributes, including:

CustomerID – Unique customer identifier

Tenure Months – Number of months the customer stayed

Monthly Charges – Amount paid per month

Total Charges – Total amount paid

Contract Type – Month-to-month / 1-year / 2-year

Churn Label – Whether the customer left (Yes/No)

Churn Value – 1 for churned, 0 for retained

This dataset is based on the IBM Telco Customer Churn dataset.

## Objective

The main goals of this assignment were to:

Perform data cleaning and preprocessing

Conduct exploratory data analysis (EDA)

Apply an independent t-test

Report findings in plain, human-readable English

## Hypothesis
Null Hypothesis (H₀):

There is no significant difference in average monthly charges between retained and churned customers.

Alternative Hypothesis (H₁):

There is a significant difference in average monthly charges between retained and churned customers.

## Data Cleaning Steps

Checked for missing values using df.isnull().sum()

Filled missing values in Churn Reason with "Not Churned"

Converted Total Charges from object to numeric

Filled missing values in Total Charges using median

## Exploratory Data Analysis (EDA)

Key insights from EDA:

Most customers were retained, but a significant portion churned.

Retained customers had much longer tenure than churned customers.

Churned customers were paying higher monthly charges on average.

## Statistical Test

An independent t-test was conducted to compare monthly charges between the two groups.

Result:

p-value < 0.05

Therefore, we reject the null hypothesis.

## Final Findings (Plain English)

“An independent t-test was conducted to compare the monthly charges of customers who stayed with the company and those who left. The results showed a statistically significant difference between the two groups (p < 0.05). On average, customers who churned were paying higher monthly charges than retained customers.

In addition, exploratory analysis showed that customers who stayed with the company had much longer tenure than those who left. This indicates that customers who remain loyal tend to build longer relationships with the company, while those paying higher prices are more likely to churn. Overall, the findings suggest that pricing strategy and customer relationship duration both play important roles in customer retention.”

