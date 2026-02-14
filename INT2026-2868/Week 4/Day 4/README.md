# Spam Email Classifier – Cross-Validation Study

This project implements a **spam email classification system** using **Logistic Regression** and **Random Forest**, evaluated with **5-fold and 10-fold cross-validation**.

The goal is to compare model performance, stability, and generalization behavior using standard classification metrics.

---

## Project Structure

```
├── spam_dataset.csv        # Input dataset (text, label)
├── spam_cv.py              # Main training & evaluation script
├── README.md               # Project documentation
```

---

## Dataset

- **text**: Raw email content  
- **label**:  
  - `1` → Spam  
  - `0` → Ham (not spam)

The dataset should be stored as a CSV file named `spam_dataset.csv`.

---

## Models Used

### Logistic Regression
- Linear classifier with regularization
- Stable and interpretable
- Strong baseline for text classification

### Random Forest
- Ensemble of decision trees
- Captures non-linear feature interactions
- Higher performance but higher variance and cost

---

## Feature Engineering

- **TF-IDF Vectorization**
  - Stop-word removal
  - Maximum document frequency filtering
- Implemented using `sklearn.pipeline.Pipeline`

---

## Cross-Validation Setup

- **Stratified K-Fold Cross-Validation**
  - Preserves spam/ham class distribution
- Experiments conducted with:
  - **5-fold CV**
  - **10-fold CV**

---

## Evaluation Metrics

The following metrics are computed for each fold and reported as **mean ± standard deviation**:

- Accuracy
- Precision (Spam)
- Recall (Spam)
- F1-score (Spam)
- ROC-AUC

> Recall and F1-score are emphasized due to the cost of missed spam emails.

---

## Results Interpretation

- **10-fold CV**
  - Lower variance across folds
  - More reliable generalization estimates
  - Higher computational cost

- **5-fold CV**
  - Faster evaluation
  - Slightly higher variance
  - Suitable for rapid experimentation

---

## Requirements

Install dependencies using:

```bash
pip install numpy pandas scikit-learn
```

---

## Running the Experiment

```bash
python spam_cv.py
```

The script will output performance metrics for:
- Logistic Regression (5-fold & 10-fold)
- Random Forest (5-fold & 10-fold)

---

## Key Findings

- Random Forest generally achieves higher recall and ROC-AUC.
- Logistic Regression is more stable and interpretable.
- 10-fold CV is recommended for final model evaluation.

---

## Future Improvements

- Hyperparameter tuning with `GridSearchCV`
- Class imbalance handling
- ROC and precision-recall curve visualization
- Deployment-ready inference pipeline

---

## Author

Spam Classification CV Study  
