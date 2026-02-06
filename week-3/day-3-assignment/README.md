## 📧 Spam Email Classification using Machine Learning  
Boads karunanjali

INT2026-1462

date:06-02-2026

## Project Overview  
This project builds a Spam Detection System using two supervised machine learning algorithms:  

- K-Nearest Neighbors (KNN)  
- Decision Tree Classifier  

The model classifies SMS messages as **Spam (1)** or **Ham (0)** based on their text content.

## Objective  
The main goals of this assignment are:  

- To clean and preprocess text data  
- To convert text into numerical features using TF-IDF  
- To train and compare two machine learning models  
- To evaluate performance using accuracy, precision, recall, and F1-score  

## Dataset  
The dataset used is the **SMS Spam Collection Dataset**, which contains:  

| Column | Description |
|--------|-------------|
| v1 | Label (`ham` or `spam`) |
| v2 | SMS message text |

After preprocessing, columns were renamed to:  
- `label`  
- `message`

## Data Preprocessing Steps  

1. Loaded dataset using Pandas  
2. Removed unnecessary columns (`Unnamed: 2, 3, 4`)  
3. Renamed columns to `label` and `message`  
4. Converted labels:  
   - `ham → 0`  
   - `spam → 1`  
5. Removed rows with missing values  
6. Converted text to numbers using **TF-IDF Vectorization**  
7. Split data into:  
   - 80% training  
   - 20% testing  

## Task 1 — KNN Classifier  

- Model: K-Nearest Neighbors  
- Parameter: `n_neighbors = 5`  
- Metrics used: Accuracy, Precision, Recall, F1-score  

**Finding:**  
KNN performed well in detecting spam messages using TF-IDF features but is slower on very large datasets.

## Task 2 — Decision Tree Classifier  

- Model: Decision Tree  
- Parameter: `max_depth = 10`  
- The decision tree was visualized for better understanding  

**Finding:**  
Decision Tree was slightly less accurate than KNN but easier to interpret.

## Model Comparison  

| Model | Advantage | Limitation |
|-------|------------|------------|
| KNN | Higher accuracy | Slow on large data |
| Decision Tree | Easy to interpret | Slightly lower accuracy |

**Final Conclusion:**  
Use **KNN** when accuracy matters most.  
Use **Decision Tree** when explainability is required.

## Tools and Libraries Used  

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- TF-IDF Vectorizer  
- Jupyter Notebook  
