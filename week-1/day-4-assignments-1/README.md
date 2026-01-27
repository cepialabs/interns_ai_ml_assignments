# Student Performance Data Analysis 📊

## 📌 Project Overview

This repository contains a **data analysis and visualization project** using the **Student Performance dataset**.
The objective of this assignment is to **analyze academic performance patterns** using statistical summaries and visualizations.

The analysis focuses on understanding:

* Score distribution
* Gender-based performance differences
* Correlation between subject scores
* Impact of test preparation on student performance

The entire workflow is implemented using **Python**, **Pandas**, **Matplotlib**, and **Seaborn** in a Jupyter Notebook.

---

## 📁 Dataset

The dataset used in this project is the **Student Performance in Exams dataset**, which contains academic and demographic information of students.

### Key Columns:

* **gender**
* **race/ethnicity**
* **parental level of education**
* **lunch**
* **test preparation course**
* **math score**
* **reading score**
* **writing score**

📌 A derived column **`average_score`** is created by averaging math, reading, and writing scores for analysis.

---

## 🎯 Objectives

This project addresses the following analysis tasks:

1. **Score Distribution Analysis**
   Visualize the distribution of average student scores.

2. **Gender vs Performance Comparison**
   Analyze performance differences between male and female students.

3. **Correlation Analysis**
   Identify relationships between math, reading, and writing scores.

4. **Performance Trend Analysis**
   Study the impact of test preparation course on student performance.

---

## 📂 Folder Structure

```
INT2026-3908/
└── week-1/
    ├── day-4-assignment-1/
        ├── student_performance_analysis.ipynb
        ├── StudentsPerformance.csv
        └── README.md
```

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

  * Loaded dataset and checked structure, data types, and summary statistics.

* **Feature Engineering**

  * Created an `average_score` column for overall performance evaluation.

* **Score Distribution Visualization**

  * Used histogram and KDE plots to analyze score distribution.

* **Gender-Based Performance Analysis**

  * Used boxplots to compare performance across genders.

* **Correlation Heatmap**

  * Visualized correlations between math, reading, and writing scores.

* **Performance Trend Analysis**

  * Analyzed the effect of test preparation course on average scores.

---

## 📊 Visualizations

* Histogram of average student scores
* Boxplot for gender vs performance
* Correlation heatmap of subject scores
* Bar chart for test preparation course vs performance

📈 These visualizations help uncover meaningful insights from the dataset.

---

## 📌 How to Run the Notebook

1. Clone the repository:

```bash
git clone https://github.com/cepialabs/interns_ai_ml_assignments.git
```

2. Navigate to the assignment folder:

```bash
cd interns_ai_ml_assignments/week-1/day-1-assignment-2
```

3. Open Jupyter Notebook:

```bash
jupyter notebook student_performance_analysis.ipynb
```

4. Run all cells to generate visual insights.

---

## 🧠 What You Will Learn

* Data visualization techniques using Matplotlib and Seaborn
* Feature engineering for analysis
* Comparing categorical variables with numerical outcomes
* Correlation analysis using heatmaps
* Drawing insights from educational datasets

---

## ✨ Future Enhancements

Possible extensions of this project include:

* Exploratory Data Analysis (EDA)
* Predicting student performance using ML models
* Feature scaling and normalization
* Interactive dashboards (Streamlit / Power BI)
* Deeper demographic analysis

---

## 📌 Author

**Swati M Patil**
AI/ML Intern @ Cepia Labs
