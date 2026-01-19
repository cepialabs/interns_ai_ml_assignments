import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# 1. Generate 10,000 random house prices
# We use a normal distribution (Mean: $500k, Std Dev: $150k)
prices = np.random.normal(loc=500000, scale=150000, size=10000)

# Ensure no negative prices (floor at $50k)
prices = np.clip(prices, 50000, None)

# Calculate original average
avg_original = np.mean(prices)
print(f"Original Average Price: ${avg_original:,.2f}")

# 2. Remove outliers using the IQR Method
Q1 = np.percentile(prices, 25)
Q3 = np.percentile(prices, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned_prices = prices[(prices >= lower_bound) & (prices <= upper_bound)]
avg_cleaned = np.mean(cleaned_prices)

print(f"Cleaned Average Price: ${avg_cleaned:,.2f}")
print(f"Outliers removed: {len(prices) - len(cleaned_prices)}")

# 3. Visualize price distribution
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=50, color='skyblue', edgecolor='black', alpha=0.7, label='Original Data')
plt.hist(cleaned_prices, bins=50, color='orange', edgecolor='black', alpha=0.5, label='Cleaned Data')

# Add mean lines
plt.axvline(avg_original, color='red', linestyle='dashed', label=f'Original Mean')
plt.axvline(avg_cleaned, color='green', linestyle='dashed', label=f'Cleaned Mean')

plt.title('House Price Distribution & Outlier Removal')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()