# Email Marketing Probability Model

## 📌 Project Overview

This project models an **email marketing campaign funnel** using probability theory.  
It focuses on two key user behaviors:

1. **Clicking an email**
2. **Converting after clicking**

Using conditional probability tables (CPTs), the project shows how engagement (clicks) and intent (conversions) interact, and how to compute overall conversion rates from these components.

The project is designed to be:
- Easy to understand
- Statistically sound
- Extendable to real-world datasets

---

## 🎯 Problem Statement

In email marketing, conversion does not happen randomly — it depends strongly on whether a user clicks the email.

This project answers:
- What is the probability a user clicks an email?
- What is the probability a user converts *given* they clicked?
- What is the overall conversion rate?
- How can this relationship be represented using conditional probabilities?

---

## 🧠 Modeling Assumptions

We model the funnel using two binary random variables:

- **C (Click)**: {Yes, No}
- **V (Conversion)**: {Yes, No}

Key assumption:
> Conversion is conditionally dependent on clicking the email.

---

## 📊 Probabilistic Structure

### Base Probabilities

- P(Click = Yes) = 0.30
- P(Click = No) = 0.70

### Conditional Probabilities

- P(Convert = Yes | Click = Yes) = 0.20
- P(Convert = Yes | Click = No) = 0.01

These values are assumed for demonstration purposes and would normally be calculated from real campaign data.

---

## 📋 Conditional Probability Tables (CPTs)

### Click Probability Table

| Click | Probability |
|------|------------|
| Yes  | 0.30       |
| No   | 0.70       |

### Conversion Probability Table (Conditional)

| Click | Convert | Probability |
|------|--------|------------|
| Yes  | Yes    | 0.20       |
| Yes  | No     | 0.80       |
| No   | Yes    | 0.01       |
| No   | No     | 0.99       |

---

## 🔗 Joint Probabilities

Joint probabilities are computed using:

P(Click, Convert) = P(Click) × P(Convert | Click)

| Click | Convert | Joint Probability |
|------|--------|------------------|
| Yes  | Yes    | 0.06             |
| Yes  | No     | 0.24             |
| No   | Yes    | 0.007            |
| No   | No     | 0.693            |

---

## 📈 Overall Conversion Rate

The total probability of conversion is:

