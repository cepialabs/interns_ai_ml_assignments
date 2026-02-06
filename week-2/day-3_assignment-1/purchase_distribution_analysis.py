import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df = pd.read_csv("customer_purchases.csv")

data = df["purchase_amount"]

mean = data.mean()
std = data.std()

threshold = 700
prob_above_threshold = 1 - norm.cdf(threshold, mean, std)

simulated_data = np.random.normal(mean, std, 10000)

x = np.linspace(min(data), max(data), 100)
pdf = norm.pdf(x, mean, std)

plt.hist(data, bins=8, density=True, alpha=0.6)
plt.plot(x, pdf)
plt.xlabel("Purchase Amount")
plt.ylabel("Density")
plt.title("Purchase Amount Distribution with Normal Fit")
plt.tight_layout()
plt.show()

plt.hist(simulated_data, bins=30, density=True, alpha=0.6)
plt.plot(x, pdf)
plt.xlabel("Purchase Amount")
plt.ylabel("Density")
plt.title("Simulated vs Theoretical Distribution")
plt.tight_layout()
plt.show()

print("Mean purchase amount:", round(mean, 2))
print("Standard deviation:", round(std, 2))
print("Probability spending above", threshold, ":", round(prob_above_threshold, 3))
