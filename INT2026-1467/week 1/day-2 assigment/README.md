# Week 1 – Day 1 – Assignment 1  
## Netflix Data Analysis using Pandas & Matplotlib

### Author  
**Rawal Vipul**

---

## 📌 Assignment Objective
The objective of this assignment is to analyze Netflix content data to identify trends related to genres, content type, yearly additions, and top content-producing countries using Python data analysis libraries.

---

## 📂 Dataset Used
- **File Name:** `netflix_titles.csv`
- The dataset contains information about Netflix movies and TV shows including genre, country, type, and date added.

---

## 📝 Problem Analysis & Approach

### 1️⃣ Data Loading
- The dataset is loaded using **Pandas**.
- Basic inspection is performed to ensure correct loading.

### 2️⃣ Genre Analysis
- The `listed_in` column is split to extract individual genres.
- The dataset is exploded to count each genre separately.
- Top 10 most common genres are identified and visualized using a bar chart.

### 3️⃣ Movies vs TV Shows
- The `type` column is analyzed to compare the number of Movies and TV Shows.
- A pie chart is used to visualize the percentage distribution.

### 4️⃣ Content Added Per Year
- The `date_added` column is converted into datetime format.
- A new column `year_added` is extracted.
- The number of titles added each year is calculated and visualized using a line plot.

### 5️⃣ Top Content Producing Countries
- The `country` column is cleaned and exploded to handle multiple countries.
- The top 10 countries producing Netflix content are identified.
- A bar chart is used to visualize the result.
- The country producing the maximum content is displayed.

---

## 🛠️ Tools & Libraries Used
- Python  
- Pandas  
- Matplotlib  

---

## 📊 Key Outcomes
- Identified the **Top 10 Netflix genres**
- Compared **Movies vs TV Shows**
- Analyzed **year-wise content growth**
- Found **top content-producing countries**
- Determined the country with the highest Netflix content

---

## 📁 Folder Structure
```
week-1/
└── day-1-assignment-1/
    ├── netflix_analysis.py
    └── README.md
```

---

## ✅ Conclusion
This analysis provides insights into Netflix’s content strategy and distribution trends.  
It demonstrates practical usage of data cleaning, transformation, and visualization techniques, which are essential skills for data analysis and AI/ML workflows.

---

📅 **Week:** 1  
📌 **Assignment:** Day 1 – Assignment 1  
