Day 1 : Assignment 1

# House Price Analysis using NumPy

This project demonstrates how to generate synthetic house price data, calculate summary statistics, remove outliers, and visualize price distributions using Python and NumPy.

---

## Overview

The goal of this project is to:

* Simulate real-world house price data
* Compute the average house price
* Remove outliers using a robust statistical method
* Visualize the cleaned price distribution

This is useful for beginners learning **NumPy**, **data cleaning**, and **basic data visualization**.

---

## Features

* Generate 10,000 random house prices
* Calculate mean house price
* Detect and remove outliers using the IQR method
* Visualize data using a histogram

---

## Technologies Used

* Python 3.x
* NumPy
* Matplotlib

---

## Methodology

### Data Generation

House prices are generated using a normal distribution with:

* Mean: $300,000
* Standard deviation: $50,000

### Outlier Removal

Outliers are removed using the **Interquartile Range (IQR)** method:

* Values below Q1 − 1.5 × IQR
* Values above Q3 + 1.5 × IQR

This helps eliminate extreme values that could skew the analysis.

---

## Output

* Average house price statistics
* Histogram showing the distribution of filtered house prices

---

## Author

Your Name
Gunjan Damade