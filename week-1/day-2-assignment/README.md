# Day 2 Assignment

**Date:** January 20, 2026

## Assignment Description

Dataset: Netflix Titles

Tasks:
1. Identify top 10 most frequent genres
2. Compare Movies vs TV Shows distribution
3. Analyze content added per year
4. Identify country producing most content

## Data Source

https://www.kaggle.com/datasets/mahmoudtaya/netflix-titles
https://www.kaggle.com/datasets/sonalshinde123/student-academic-performance-dataset

## How to Pull the Dataset from Kaggle

```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("mahmoudtaya/netflix-titles")
print("Path to dataset files:", path)

# Load the dataset CSV
csv_path = f"{path}/netflix_titles.csv"

df = pd.read_csv(csv_path)
print(df.head())
print(df.shape)
```

---

## Instructions

Complete the tasks in the `assignment-1.ipynb` notebook file.
