import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marketing_sales.csv")

correlation = df["ad_spend"].corr(df["sales"])

plt.scatter(df["ad_spend"], df["sales"])
plt.xlabel("Ad Spend")
plt.ylabel("Sales")
plt.title("Ad Spend vs Sales")
plt.tight_layout()
plt.show()

print("Correlation between ad spend and sales:", round(correlation, 3))
