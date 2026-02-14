
# Feature Scaling and Model Performance

This Assignment demonstrates the effect of **feature scaling** on machine learning models using 
**House Prices Dataset** – Regression task  

We train models **with and without scaling**, then compare their performance.

---

## 2. Feature Scaling

We apply **StandardScaler** to normalize numerical features so that they have:
- Mean = 0
- Standard deviation = 1

Scaling is performed using a **Pipeline** to avoid data leakage.

---

## 3. Models Used

### Regression
- Linear Regression

Each model is trained:
- Without feature scaling
- With feature scaling

---

## 4. Evaluation Metrics

### Regression
- Mean Squared Error (MSE)
- R² Score


## 5. Key Observations

- Linear Regression shows minimal performance change after scaling.
- Feature scaling is critical for distance-based and gradient-based algorithms.

---

## 6. How to Run

```bash
pip install numpy pandas scikit-learn
python your_script.py
```

---

## 7. Conclusion

Feature scaling is an essential preprocessing step that improves model stability, convergence, and performance for many machine learning algorithms.
