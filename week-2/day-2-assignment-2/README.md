# Week 2-day-2 Email Marketing Campaign Analysis

# Assignment Overview
This project analyzes an **email marketing campaign dataset** to understand user behavior using **probability and conditional probability** concepts. The goal is to evaluate how user engagement (clicks) relates to conversions and to visualize these relationships.

# Dataset Description
The dataset contains customer demographics, purchase history, and campaign response information.

**Key columns used:**
- `AcceptedCmp1` to `AcceptedCmp5`: Indicates whether a user accepted (clicked) a campaign
- `Response`: Indicates whether the user converted
- Other columns include income, education, marital status, and spending details

⚠️ The dataset uses **semicolon (;)** as a separator.

# Objectives
1. Calculate the **probability that a user clicks an email**
2. Calculate the **probability that a user converts given they clicked**
3. Create **conditional probability tables**
4. Visualize probabilities using charts and heatmaps

# Methodology
# 1. Probability of Click
A user is considered to have **clicked** if they accepted at least one email campaign.

\[
P(Click) = \frac{\text{Number of users who clicked}}{\text{Total users}}
\]

# 2. Conditional Probability of Conversion Given Click
\[
P(Convert \mid Click) = \frac{\text{Users who converted and clicked}}{\text{Users who clicked}}
\]

# 3. Conditional Probability Table
A contingency table is created to analyze conversion behavior based on click status and is visualized using a heatmap.

#Visualizations
- Email click distribution
- Conditional probability heatmap for conversion vs click behavior

# Key Insights
- Only a subset of users click email campaigns, indicating selective engagement.
- Users who click emails have a **significantly higher probability of conversion**.
- Click behavior is a strong predictor of conversion.
- Improving click-through rates can directly improve campaign performance.

# Tools & Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

# Conclusion
This analysis demonstrates how **probability and conditional probability** can be applied to real-world marketing data to extract meaningful business insights and guide decision-making in email marketing strategies

#  Author
**Danish Shaikh**  
Week 2 – Internship Assignment

