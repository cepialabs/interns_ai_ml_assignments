import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
prices = np.random.normal(500000, 100000, 10000)

# Average price
avg_price = np.mean(prices)
print("Average house price:", avg_price)

# Visualization
plt.hist(prices, bins=50, color='blue', edgecolor='black')
plt.axvline(avg_price, color='red', linestyle='--', label='Average')
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.title("House Prices with Average")
plt.legend()
plt.show()
