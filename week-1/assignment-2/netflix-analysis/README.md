Netflix Titles Data Analysis 📊
📌 Project Overview
This repository contains a data analysis project using the Netflix Titles dataset to extract meaningful insights about the streaming content available on Netflix. The analysis was performed using Python, Pandas, and Matplotlib, and focuses on exploring content distribution, genres, trends over years, and country contributions.

📁 Dataset
The data used for this assignment is sourced from the netflix_titles.csv file (commonly available on Kaggle), which contains information about movies and TV shows such as:

title
show_id
type (Movie / TV Show)
director
cast
country
date_added
release_year
rating
duration
listed_in (Genres)
description
🎯 Objectives
This analysis answers the following key questions:

Top 10 Most Frequent Genres
Which genres appear most often in Netflix’s content library?

Movies vs TV Shows Distribution
How many movies versus TV shows are present on Netflix?

Content Added Per Year
What is the trend of content being added over the years?

Country Producing Most Content
Which countries contribute the most Netflix titles?

📂 Files in This Folder
INT-25-FS-2567/
└── week-1/
    ├── day-2-assignment-2/
        ├── netflix-analysis.ipynb
        └── README.md
🛠 Tools & Libraries
The analysis uses the following:

Python 3.x
Pandas
Matplotlib / Seaborn (optional)
🔍 Key Insights
Genre Analysis: Identified the most common genres present across Netflix titles.
Content Type: Compared the count of movies vs TV shows.
Yearly Trend: Visualized how many titles were added each year.
Top Countries: Found out which countries produced the highest number of titles.
📈 Use the included charts to visualize these insights clearly.

📌 How to Run the Notebook
Clone the repository:

git clone https://github.com/cepialabs/interns_ai_ml_assignments.git

2. Navigate to the assignment folder:

   ```bash
   cd interns_ai_ml_assignments/week-1/day-2-assignments-2
Open Jupyter Notebook:

jupyter notebook netflix_analysis.ipynb
Run all cells to generate insights and visualizations.

🧠 What You Will Learn
How to clean and preprocess real-world data
How to perform exploratory data analysis (EDA)
How to visualize data with charts
How to extract insights and answer analytical questions
✨ Future Enhancements
You can extend this analysis by adding:

More visualizations (Seaborn, Plotly)
Advanced metrics like content per genre over time
Filtering by country or type
Interactive dashboards with Streamlit or Dash
