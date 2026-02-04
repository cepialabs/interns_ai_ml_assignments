# Customer Retention Analysis using t-test

## Project Overview
This project analyzes customer retention using a statistical t-test.
The goal is to determine whether customers with different account types
return at different rates.

## Dataset
- File: customer_time_series (1).csv
- Each row represents a customer activity record.
- Customers may appear multiple times in the dataset.

## Definition of Customer Retention
Customer retention is defined as the number of times a customer appears
in the dataset. A higher count indicates that the customer has returned
multiple times.

## Methodology
1. Load the dataset using pandas.
2. Group data by Customer_ID and Account_Type.
3. Calculate retention as the count of records per customer.
4. Split data into account type groups.
5. Perform an independent t-test to compare mean retention.

## Hypothesis
- Null Hypothesis (H₀): There is no difference in retention between account types.
- Alternative Hypothesis (H₁): There is a significant difference in retention.

## Statistical Test Used
- Independent t-test (Welch’s t-test)
- Significance level: 0.05

## Results
The p-value obtained from the t-test determines whether the observed
difference in customer retention is statistically significant.

## Conclusion
Based on the statistical results, we conclude that account type
(has / does not have) a significant effect on customer retention.

## Tools Used
- Python
- Pandas
- SciPy
- Jupyter Notebook (VS Code)
