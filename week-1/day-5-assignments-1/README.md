# Student Performance Data Analysis 📊

## 📌 Project Overview

This repository contains an **Exploratory Data Analysis (EDA) project** based on the **Student Performance in Exams dataset**.  
The objective of this assignment is to **analyze academic performance patterns** using data cleaning, statistical analysis, and visualizations.

The analysis focuses on understanding how **demographic, socio-economic, and academic factors** influence student performance across different subjects.

All analysis is implemented using **Python** in a **Jupyter Notebook**.

---

## 📁 Dataset Information

The dataset used in this project is the **Student Performance in Exams dataset**, which contains academic scores along with student background information.

### Key Features

- **gender**
- **race/ethnicity**
- **parental level of education**
- **lunch**
- **test preparation course**
- **math score**
- **reading score**
- **writing score**

📌 A derived feature **`average_score`** is created by averaging math, reading, and writing scores to represent overall academic performance.

---

## 🎯 Project Objectives

This project aims to:

1. Load and understand the dataset structure and statistics  
2. Clean and preprocess the data  
3. Perform meaningful exploratory data analysis  
4. Create multiple visualizations to uncover patterns  
5. Extract key insights from the data  

---

## 📂 Project Structure

INT2026-3908/
└── week-1/
    ├── day-5-assignment-1/
        ├── student_performance_analysis.ipynb
        ├── StudentsPerformance.csv
        └── README.md

---

## 🛠 Tools & Technologies Used

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## 🔍 Analysis Workflow

- **Data Loading & Inspection**
  - Checked dataset shape, column names, data types, and summary statistics.

- **Data Cleaning & Feature Engineering**
  - Renamed columns for consistency.
  - Created an `average_score` column for overall performance evaluation.

- **Exploratory Data Analysis**
  - Analyzed score distributions.
  - Compared performance across gender and test preparation categories.
  - Studied relationships between subject scores.

- **Correlation Analysis**
  - Used heatmaps to identify correlations between math, reading, and writing scores.

---

## 📊 Visualizations Included

- Histogram showing distribution of average student scores  
- Boxplot comparing gender vs academic performance  
- Correlation heatmap of subject scores  
- Bar chart showing the impact of test preparation course  

📈 These visualizations help identify meaningful trends and patterns in student performance.

---

## 🧠 Key Insights

- Students who completed the test preparation course scored higher on average.  
- Reading and writing scores show a strong positive correlation.  
- Gender-based performance differences are observable across subjects.  
- Parental level of education has an impact on overall student performance.  
- Socio-economic factors such as lunch type influence academic outcomes.  

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

## 🚀 Learning Outcomes

Practical experience with Exploratory Data Analysis

Data visualization using Matplotlib and Seaborn

Feature engineering techniques

Correlation and comparative analysis

Drawing insights from real-world educational data

---

## 🔮 Future Enhancements

Build predictive models for student performance

Perform deeper demographic and socio-economic analysis

Create interactive dashboards using Streamlit or Power BI

Apply feature scaling and normalization techniques

---

## 👩‍💻 Author

**Swati M Patil**
AI/ML Intern @ Cepia Labs
