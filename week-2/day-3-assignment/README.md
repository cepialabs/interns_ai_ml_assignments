## Probability Distribution Analysis on Online Retail Data
Bodas karunanjali

INT2026-1462

 ## Introduction


This project focuses on applying probability distribution concepts to a real-world retail dataset. The objective is to analyze customer purchase behavior using statistical methods such as Normal Distribution, Probability Density Function (PDF), Cumulative Distribution Function (CDF), and Z-Score Standardization, which are fundamental in Machine Learning and Data Science.



## Dataset Information



Dataset Name: Online Retail Dataset



File: data.csv



Data Type: Transactional retail data



Key Columns Used



InvoiceNo – Transaction number



StockCode – Product code



Description – Product description



Quantity – Number of units purchased



InvoiceDate – Date of purchase



UnitPrice – Price per unit



CustomerID – Unique customer identifier



Country – Customer country



## Feature Engineering



Since the dataset does not directly contain purchase amount, a new feature was created:



Purchase Amount Calculation

PurchaseAmount= Quantity × UnitPrice

PurchaseAmount= Quantity ×UnitPrice



This derived column represents the total value of each transaction and is used for probability analysis.



## Data Preprocessing



The following preprocessing steps were performed:



Resolved CSV encoding issues during data loading



Removed records with:



Negative quantities (product returns)



Zero or negative purchase amounts



Ensured clean and valid data for statistical analysis



## Probability Distribution Concepts Covered

1️  Common Probability Distributions



Discrete Distributions



Binomial Distribution



Poisson Distribution



Continuous Distributions



Normal Distribution



Uniform Distribution



2️  Probability Density Function (PDF)



Used to visualize the likelihood of different purchase amounts



Represented using histograms and kernel density estimation



3️  Cumulative Distribution Function (CDF)



Used to compute probabilities such as:



Probability that a purchase amount exceeds a specified threshold



4️  Z-Score Standardization



Z-score standardization was applied to normalize the purchase amount values:



𝑧=𝑥−𝜇𝜎

z=σ

x−μ

&nbsp;	​





This technique is widely used in machine learning algorithms to scale features.



## Implementation Steps



The analysis was implemented in a Jupyter Notebook with the following steps:



Load dataset using appropriate encoding



Create PurchaseAmount feature



Perform data cleaning



Visualize data using histograms and normal distribution curves



Calculate probabilities using CDF



Apply Z-score standardization



Compare actual data with simulated normal distribution



## Tools and Libraries Used



Python



Pandas



NumPy



Matplotlib



Seaborn



SciPy



## Importance in Machine Learning



Probability distributions play a crucial role in machine learning by:



Helping understand data behavior



Supporting assumption-based models



Enabling probability-based predictions



Assisting in feature scaling and normalization



Detecting outliers



## Conclusion



This project demonstrates the practical application of probability distribution techniques on a real-world retail dataset. By analyzing customer purchase behavior through statistical methods, the assignment highlights the importance of probability concepts in data science and machine learning.

