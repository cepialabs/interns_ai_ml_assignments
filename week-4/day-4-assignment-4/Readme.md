# Week 4 - Day 4 Assignment  
## Cross Validation on Housing Price Dataset

##  Objective

The objective of this assignment is to:

- Perform 5-fold / 10-fold Cross Validation
- Compare Linear Regression and Random Forest
- Analyze model stability and generalization

##  Dataset

Housing Price Dataset (`Housing.csv`)

Target Variable:
- price

Features include:
- area
- bedrooms
- bathrooms
- stories
- mainroad
- guestroom
- basement
- hotwaterheating
- airconditioning
- parking
- prefarea
- furnishingstatus

Categorical features were encoded before training.

## Cross Validation

Cross-validation helps evaluate how well a model generalizes to unseen data.

5-Fold Cross Validation was applied.

Each model was trained and validated 5 times on different splits of the dataset.

##  Models Used

###  Linear Regression  
- Baseline model  
- Assumes linear relationship  

###  Random Forest Regressor  
- Ensemble model  
- Captures non-linear relationships  
- More robust to variance  

##  Evaluation Metric

- R² Score

For each model:
- Mean R² across folds
- Standard deviation of R²

##  Observations

- Random Forest achieved higher average R².
- Random Forest showed lower variance in performance.
- Linear Regression had more variation across folds.
- Tree-based models generalize better for this dataset.

##  Insights on Model Stability

- Lower standard deviation indicates better stability.
- Random Forest demonstrated better generalization capability.
- Cross-validation provides more reliable performance estimation than a single train-test split.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

