# Week 2 – Day 1 Assignment  
📅 Date: 28 January 2026  

## Dataset: Marketing Campaign Dataset  
(Customer Spend, Engagement, Clicks)

---

## 📌 Objective
The objective of this assignment is to perform Exploratory Data Analysis (EDA) on a marketing campaign dataset to:
1. Calculate average spending per customer
2. Identify the top 10% of spenders
3. Detect skewness in customer engagement metrics

---

## 📂 Dataset Description
The dataset contains information about various marketing campaigns, including spending, engagement, and performance metrics.

### Columns Used:
- **CampaignID** – Unique identifier for each campaign  
- **Cost (₹)** – Money spent on the campaign (used as customer spend)  
- **Revenue (₹)** – Revenue generated  
- **Impressions** – Number of times the campaign was shown  
- **Clicks** – Number of clicks received  
- **Leads / Applications / Enrollments** – Engagement outcomes  

---

## 🛠 Tools & Libraries Used
- Python  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 🔍 Step-wise Analysis

### Step 1: Load the Dataset
The dataset is loaded using Pandas after extracting it from the archive and placing it in the same directory as the notebook.

```python
import pandas as pd
df = pd.read_excel("Marketing_Campaign_Data.csv")
