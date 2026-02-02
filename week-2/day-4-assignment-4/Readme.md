# Dataset Description
The dataset contains sales and marketing-related metrics across different products and campaigns.

**Key columns used:**
- `Sessions` – Number of user visits (marketing exposure proxy)
- `Views` – Content or product views
- `Conversion Rate (%)` – Percentage of conversions
- `Sales Amount (USD)` – Total sales revenue

Since there is no explicit advertising spend column, marketing exposure metrics are used as **proxies for advertising activity**.

# Objectives
1. Analyze the **correlation** between marketing exposure and sales
2. Compare **correlation with causal reasoning**
3. Discuss **possible confounding factors** influencing sales
4. Explain why correlation does not imply causation

# Methodology

# 1. Correlation Analysis
- Scatter plots are used to visualize relationships between marketing metrics and sales.
- Correlation coefficients are calculated to measure the strength of association.

# 2. Correlation vs Causal Reasoning
- Correlation identifies statistical association between variables.
- Causal reasoning evaluates whether one variable directly causes changes in another.
- Since the dataset is observational, causation cannot be conclusively established.

# 3. Confounding Variables
Potential confounders are discussed conceptually, as they may influence both marketing exposure and sales.

Examples include:
- Product type
- Seasonality
- Pricing and discounts
- Customer plans
- Sales channel
- Sales representative performance

# Visualizations
- Scatter plots of marketing metrics vs sales
- Correlation matrix heatmap

# Key Insights
- Marketing exposure metrics show a positive correlation with sales.
- Correlation alone does not establish a cause-and-effect relationship.
- Sales outcomes are influenced by multiple external and internal factors.
- Causal conclusions require controlled experiments or additional context.

# Tools & Libraries Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Statsmodels (for supporting analysis)

# Conclusion
This analysis highlights the importance of distinguishing between **statistical correlation** and **true causation** in business decision-making. While marketing activity is associated with sales, causal conclusions must be drawn carefully, considering confounding factors and experimental validation.

# Author
**Mohammed Danish**  
Week 2 – Internship Assignment
