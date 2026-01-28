# Marketing Campaign Data Analysis 📈

## 📌 Project Overview

This repository contains a **data analysis and visualization project** using a **Marketing Campaign dataset**.
The objective of this assignment is to **analyze customer spending behavior and engagement patterns** to derive meaningful business insights.

The analysis focuses on understanding:

* Customer spending behavior
* High-value (top 10%) customers
* Engagement patterns across different channels
* Distribution and skewness of engagement metrics

The entire workflow is implemented using **Python**, **Pandas**, **Matplotlib**, and **Seaborn** in a **Jupyter Notebook**.

---

## 📁 Dataset

The dataset used in this project is the **Marketing Campaign dataset**, which contains demographic, spending, and engagement information for customers.

### Key Columns:

* **ID** – Unique customer identifier  
* **Income** – Customer income  
* **Recency** – Days since last purchase  
* **MntWines** – Spending on wine products  
* **MntFruits** – Spending on fruits  
* **MntMeatProducts** – Spending on meat products  
* **MntFishProducts** – Spending on fish products  
* **MntSweetProducts** – Spending on sweet products  
* **MntGoldProds** – Spending on gold products  
* **NumWebVisitsMonth** – Number of website visits per month  
* **NumWebPurchases** – Number of online purchases  
* **NumStorePurchases** – Number of in-store purchases  

📌 A derived column **`Total_Spend`** is created by summing spending across all product categories.

---

## 🎯 Objectives

This project addresses the following analysis tasks:

1. **Average Spending Analysis**  
   Calculate the average total spending per customer.

2. **Top 10% Customer Identification**  
   Identify high-value customers based on total spending.

3. **Customer Engagement Analysis**  
   Analyze customer interaction across web and store channels.

4. **Skewness Detection**  
   Detect skewness in engagement metrics to understand customer behavior distribution.

---

## 📂 Folder Structure

```

INT2026-3908/
└── week-2/
    ├── day-1-assignment-1/
        ├── marketing_campaign_analysis.ipynb
        ├── marketing_campaign.csv
        └── README.md

````

---

## 🛠 Tools & Libraries

The following tools and libraries were used:

* Python 3.x  
* Pandas  
* NumPy  
* Matplotlib  
* Seaborn  
* Jupyter Notebook  

---

## 🔍 Analysis Steps Performed

* **Data Loading & Inspection**
  * Loaded the dataset and reviewed its structure, data types, and summary statistics.

* **Feature Engineering**
  * Created a `Total_Spend` column to represent overall customer spending.

* **Average Spending Calculation**
  * Computed the mean total spending per customer.

* **Top 10% Spender Identification**
  * Identified the top 10% of customers using quantile-based filtering.

* **Engagement Analysis**
  * Analyzed customer activity using web visits, web purchases, and store purchases.

* **Skewness Detection**
  * Calculated and visualized skewness in engagement-related features.

---

## 📊 Visualizations

* Histogram of total customer spending  
* Distribution of website visits per month  
* Distribution of web and store purchases  
* Engagement metric skewness plots  

📈 These visualizations help uncover **customer behavior trends** and **marketing insights**.

---

## 📌 How to Run the Notebook

1. Clone the repository:

```bash
git clone https://github.com/cepialabs/interns_ai_ml_assignments.git
````

2. Navigate to the assignment folder:

```bash
cd interns_ai_ml_assignments/week-1/day-5-assignment-1
```

3. Open the Jupyter Notebook:

```bash
jupyter notebook marketing_campaign_analysis.ipynb
```

4. Run all cells to reproduce the analysis and visualizations.

---

## 🧠 What You Will Learn

* Customer spending analysis techniques
* Identifying high-value customers using quantiles
* Understanding engagement behavior through skewness analysis
* Feature engineering for business analytics
* Visual storytelling using Python

---

## ✨ Future Enhancements

Possible extensions of this project include:

* Customer segmentation using clustering algorithms
* Predictive modeling for campaign response
* Revenue contribution analysis by customer segment
* Interactive dashboards using Streamlit or Power BI
* Campaign effectiveness evaluation

---

## 📌 Author

**Swati M Patil**
AI/ML Intern @ Cepia Labs

```