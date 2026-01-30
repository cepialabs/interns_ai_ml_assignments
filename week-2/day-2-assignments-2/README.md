# Marketing Campaign Data Analysis 📈

## 📌 Project Overview

This repository contains a **data analysis and visualization project** based on a **Marketing Campaign dataset**.
The objective of this assignment is to **analyze customer spending behavior and engagement patterns** to derive meaningful business insights.

The analysis focuses on:
- Customer spending behavior across product categories
- Identification of high-value (top 10%) customers
- Engagement patterns across different purchase channels
- Distribution and skewness of engagement metrics

The entire workflow is implemented using **Python**, **Pandas**, **Matplotlib**, and **Seaborn** in a **Jupyter Notebook**.

---

## 📁 Dataset

The dataset used in this project is the **Marketing Campaign dataset**, containing demographic, spending, and engagement information.

### Key Columns

- **ID** – Unique customer identifier  
- **Income** – Customer income  
- **Recency** – Days since last purchase  
- **MntWines** – Spending on wine products  
- **MntFruits** – Spending on fruit products  
- **MntMeatProducts** – Spending on meat products  
- **MntFishProducts** – Spending on fish products  
- **MntSweetProducts** – Spending on sweet products  
- **MntGoldProds** – Spending on gold products  
- **NumWebVisitsMonth** – Number of website visits per month  
- **NumWebPurchases** – Number of online purchases  
- **NumStorePurchases** – Number of in-store purchases  

📌 A derived column **`Total_Spend`** is created by summing spending across all product categories.

---

## 🎯 Objectives

1. Calculate the **average total spending** per customer  
2. Identify **top 10% high-value customers** based on total spending  
3. Analyze **customer engagement** across web and store channels  
4. Detect **skewness** in engagement metrics  

---

## 📂 Folder Structure
INT2026-3908/
└── week-2/
    └── day-2-assignment-1/
        ├── marketing_campaign_analysis.ipynb
        ├── marketing_campaign.csv
        └── README.md


---

## 🛠 Tools & Libraries

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## 🔍 Analysis Steps

- Loaded and inspected the dataset  
- Created `Total_Spend` using feature engineering  
- Calculated average customer spending  
- Identified top 10% spenders using quantiles  
- Analyzed customer engagement metrics  
- Visualized skewness in engagement data  

---

## 📊 Visualizations

- Total customer spending distribution  
- Monthly website visits distribution  
- Web vs store purchase distribution  
- Engagement skewness plots  

---

## How to Run the Notebook

1. Clone the repository:

```bash
git clone https://github.com/cepialabs/interns_ai_ml_assignments.git
````

2. Navigate to the assignment folder:

```bash
cd interns_ai_ml_assignments/week-2/day-2-assignment-1
```

3. Open the Jupyter Notebook:

```bash
jupyter notebook marketing_campaign_analysis.ipynb
```

4. Run all cells to reproduce the analysis and visualizations.

---

## 🧠 What You Will Learn

Customer spending analysis
High-value customer identification
Engagement behavior analysis
Feature engineering for marketing analytics
Data visualization with Python

---

## ✨ Future Enhancements

Possible extensions of this project include:

Customer segmentation using clustering
Campaign response prediction
Revenue contribution analysis
Interactive dashboards

---

## 📌 Author

**Swati M Patil**
AI/ML Intern @ Cepia Labs

```