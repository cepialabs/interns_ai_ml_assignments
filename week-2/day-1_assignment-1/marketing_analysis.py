import pandas as pd
import numpy as np
from scipy.stats import skew

df = pd.read_csv("marketing_campaign.csv")

average_spend = df["spend"].mean()

threshold = np.percentile(df["spend"], 90)
top_spenders = df[df["spend"] >= threshold]

engagement_skewness = skew(df["engagement_score"])

print("Average spending per customer:", round(average_spend, 2))
print("\nTop 10% spenders:")
print(top_spenders[["customer_id", "spend"]])
print("\nEngagement skewness:", round(engagement_skewness, 3))
