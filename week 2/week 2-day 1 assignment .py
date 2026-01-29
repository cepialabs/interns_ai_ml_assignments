#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure display options for better viewing
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load the dataset
df = pd.read_csv('Marketing_Campaign_Data.csv')

print("Dataset Head:")
print(df.head())
print("\nDataset Info:")
df.info()
print("\nDataset Description:")
print(df.describe(include='all'))
print("\nMissing Values:")
print(df.isnull().sum())


# In[11]:


# Initial Data Cleaning and Exploration

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Check for duplicate rows
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")
if df.duplicated().any():
    df.drop_duplicates(inplace=True)
    print("Duplicate rows removed.")

# Check for missing values (already done in initial load, but good to re-confirm after cleaning)
print("\nMissing values after initial cleaning:")
print(df.isnull().sum())

print("\nDataFrame after initial cleaning steps:")
df.info()


# In[12]:


# Data Cleaning: Clean 'Cost (₹)' and 'Revenue (₹)' columns

# Remove '₹' symbol and commas, then convert to numeric
df['Cost'] = df['Cost (₹)'].str.replace('₹', '').str.replace(',', '').astype(float)
df['Revenue'] = df['Revenue (₹)'].str.replace('₹', '').str.replace(',', '').astype(float)

# Drop original currency columns if desired
df.drop(columns=['Cost (₹)', 'Revenue (₹)'], inplace=True)

print("\nDataFrame after cleaning Cost and Revenue columns:")
df.info()
print(df[['Cost', 'Revenue']].head())


# In[13]:


# Create EngagementRate column

# Calculate EngagementRate = (Clicks / Impressions) * 100
df['EngagementRate'] = (df['Clicks'] / df['Impressions']) * 100

# Handle potential NaN values from division by zero (if Impressions was 0)
df['EngagementRate'] = df['EngagementRate'].fillna(0)

print("\nDataFrame with new EngagementRate column:")
print(df[['Impressions', 'Clicks', 'EngagementRate']].head())


# In[14]:


# 1. Calculate average spending per customer

average_revenue = df['Revenue'].mean()
print(f"Average revenue per campaign: ${average_revenue:,.2f}")

# Visualization: Distribution of Revenue
plt.figure(figsize=(10, 6))
sns.histplot(df['Revenue'], kde=True, bins=30)
plt.title('Distribution of Revenue (Campaign Spend)')
plt.xlabel('Revenue ($)')
plt.ylabel('Frequency')
plt.show()


# In[15]:


# 2. Identify top 10% of spenders

# Assuming each row represents a customer or a campaign for simplicity.
# Sort by Revenue in descending order and get the top 10%
top_10_percent_spenders = df.sort_values(by='Revenue', ascending=False).head(int(len(df) * 0.10))

print("Top 10% Spenders (first 5 rows):")
print(top_10_percent_spenders.head())

# Visualization: Box plot of Revenue to show high spenders
plt.figure(figsize=(10, 6))
sns.boxplot(y=df['Revenue'])
plt.title('Box Plot of Revenue Distribution (Campaign Spend)')
plt.ylabel('Revenue ($)')
plt.show()


# In[16]:


# Visualization: Histograms to show skewness of Clicks and EngagementRate
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['Clicks'], kde=True, bins=30)
plt.title('Distribution of Clicks')
plt.xlabel('Clicks')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.histplot(df['EngagementRate'], kde=True, bins=30)
plt.title('Distribution of Engagement Rate')
plt.xlabel('Engagement Rate (%)')
plt.ylabel('Frequency')

plt.tight_layout()


# In[ ]:





# In[ ]:




