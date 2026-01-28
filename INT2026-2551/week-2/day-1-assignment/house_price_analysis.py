import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # for reproducibility
house_prices = np.random.normal(loc=50_00_000, scale=15_00_000, size=10000)

average_price = np.mean(house_prices)
print(f"Average house price: ₹{average_price:,.2f}")

Q1 = np.percentile(house_prices, 25)
Q3 = np.percentile(house_prices, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered_prices = house_prices[
    (house_prices >= lower_bound) & (house_prices <= upper_bound)
]

print(f"Original data size: {len(house_prices)}")
print(f"After removing outliers: {len(filtered_prices)}")

plt.figure()
plt.hist(filtered_prices, bins=50)
plt.xlabel("House Price (₹)")
plt.ylabel("Frequency")
plt.title("Distribution of House Prices (After Outlier Removal)")
plt.show()
