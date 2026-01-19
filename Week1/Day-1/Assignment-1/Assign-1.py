import numpy as np
import matplotlib.pyplot as plt

# 1. Generate 10,000 random house prices
# Assume prices follow a normal distribution
np.random.seed(42)
prices = np.random.normal(loc=500000, scale=100000, size=10000)

# 2. Calculate average price
average_price = np.mean(prices)
print("Average house price (before outlier removal):", average_price)

# 3. Remove outliers using IQR method
Q1 = np.percentile(prices, 25)
Q3 = np.percentile(prices, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered_prices = prices[(prices >= lower_bound) & (prices <= upper_bound)]

print("Average house price (after outlier removal):", np.mean(filtered_prices))
print("Total prices after removing outliers:", len(filtered_prices))

# 4. Visualize price distribution
plt.figure(figsize=(10, 6))
plt.hist(filtered_prices, bins=50, color='skyblue', edgecolor='black')
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.title("House Price Distribution (Outliers Removed)")
plt.show()
