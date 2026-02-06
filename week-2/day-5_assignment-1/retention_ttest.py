import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("customer_retention.csv")

discount_group = df[df["received_discount"] == 1]["return_days"]
no_discount_group = df[df["received_discount"] == 0]["return_days"]

t_stat, p_value = ttest_ind(discount_group, no_discount_group)

print("Average return days (discount):", round(discount_group.mean(), 2))
print("Average return days (no discount):", round(no_discount_group.mean(), 2))
print("T-statistic:", round(t_stat, 3))
print("P-value:", round(p_value, 4))
