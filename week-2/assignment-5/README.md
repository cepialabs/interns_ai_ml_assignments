# Customer Retention Analysis – t-Test

## Objective
To test the hypothesis:

**“Customers who received a discount are more likely to return.”**

We use an independent two-sample t-test to compare customer return rates between:
- Customers who received a discount
- Customers who did not receive a discount

---

## Dataset Description
The dataset contains customer-level information with the following key variables:

- `discount_received`
  - 1 = Customer received a discount
  - 0 = Customer did not receive a discount
- `returned`
  - 1 = Customer returned
  - 0 = Customer did not return

---

## Methodology
1. Split customers into two groups based on discount status.
2. Calculate the average return rate for each group.
3. Perform Welch’s two-sample t-test to compare the means.
4. Use a significance level (α) of 0.05.

---

## Hypotheses
- **Null Hypothesis (H₀):** There is no difference in return rates between customers who received a discount and those who did not.
- **Alternative Hypothesis (H₁):** Customers who received a discount are more likely to return.

---

## Results Interpretation
- If the p-value < 0.05, the difference is statistically significant.
- If the p-value ≥ 0.05, the difference is not statistically significant.

---

## Conclusion (Plain English)
If the test is significant, we conclude that offering discounts is associated with higher customer return rates.
If the test is not significant, we conclude that discounts do not have a statistically meaningful impact on customer retention based on this data.

---

## Notes
- Since the outcome variable is binary, this analysis treats return behavior as a mean proportion.
- For more advanced analysis, logistic regression could also be considered.
