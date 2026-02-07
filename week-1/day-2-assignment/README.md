# Netflix Titles Data Analysis  
**Week 1 – Day 2 – Assignment 1**  
**Date:** 20 January 2026  

---

## 📌 Dataset
**Netflix Titles Dataset**  
The dataset contains information about movies and TV shows available on Netflix, including:
- Type (Movie / TV Show)
- Title
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genres (`listed_in`)

---

## 🎯 Objective
The goal of this assignment is to perform **basic exploratory data analysis** using **Pandas only**.

---

## 🛠️ Tasks Performed

### 1️⃣ Identify Top 10 Most Frequent Genres
- Split multiple genres from the `listed_in` column
- Count frequency of each genre
- Display top 10 genres

### 2️⃣ Compare Movies vs TV Shows Distribution
- Use the `type` column
- Count number of Movies and TV Shows

### 3️⃣ Analyze Content Added Per Year
- Convert `date_added` to datetime
- Extract year
- Count number of titles added each year

### 4️⃣ Identify Country Producing Most Content
- Handle multiple countries per title
- Split and explode country column
- Identify top producing country

---

## 🧑‍💻 Technologies Used
- **Python**
- **Pandas**
- No NumPy
- No Matplotlib / Seaborn

✔ Analysis is done strictly using **Pandas only**.

---
## 📁 Dataset Note
The dataset `netflix_titles.csv` is not uploaded due to size limits.

Dataset Source:
Netflix Movies and TV Shows – Kaggle  
https://www.kaggle.com/datasets/shivamb/netflix-shows

---

## ▶️ How to Run the Project

1. Install Pandas:
```bash
pip install pandas
python assignment1.py

