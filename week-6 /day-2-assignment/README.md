Neural Network Comparison: ReLU vs Sigmoid Activation Functions

Week 6 - Day 2

Date: 16-03-2026

---

Project Overview

This project demonstrates the implementation and comparison of two neural network models using different activation functions: ReLU (Rectified Linear Unit) and Sigmoid.

Activation functions play an important role in neural networks because they control how the model learns patterns from the data. In this assignment, two neural networks are trained on the same dataset and their training performance is compared.

The models are implemented using TensorFlow/Keras in Jupyter Notebook.

---

Objectives

- Understand the importance of activation functions in neural networks
- Implement neural networks using ReLU and Sigmoid activation functions
- Train and evaluate both models on the same dataset
- Compare model performance using accuracy and training results
- Visualize the learning performance using graphs

---

Technologies Used

- Python
- Jupyter Notebook
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

Dataset

This project uses the Breast Cancer Wisconsin Dataset from the Scikit-learn library.

The dataset is used to classify tumors as:

- Benign (Non-Cancerous)
- Malignant (Cancerous)

Dataset Information

- Total Samples: 569
- Features: 30 numerical features
- Target Classes: 2

Example features include:

- Radius mean
- Texture mean
- Perimeter mean
- Area mean
- Smoothness mean

---

Project Workflow

1. Import Libraries

Import required libraries for data processing, machine learning, and visualization.

2. Load Dataset

Load the Breast Cancer dataset and separate it into feature variables and target variables.

3. Train-Test Split

Split the dataset into training and testing sets.

- 80% Training Data
- 20% Testing Data

4. Feature Scaling

Standardize the dataset using StandardScaler to improve neural network performance.

5. Build Neural Network using ReLU

Create a neural network model with:

- Input Layer
- Hidden Layer with ReLU activation
- Second Hidden Layer with ReLU
- Output Layer with Sigmoid

ReLU helps reduce the vanishing gradient problem.

6. Build Neural Network using Sigmoid

Create another neural network using Sigmoid activation function in the hidden layers.

Sigmoid outputs values between 0 and 1, which is useful for binary classification problems.

7. Model Training

Train both models using:

- Adam optimizer
- Binary cross-entropy loss
- Multiple training epochs

8. Model Evaluation

Evaluate the trained models using test data and measure:

- Accuracy
- Loss

9. Visualization

Plot training accuracy to compare both models.

---

Results

ReLU Model

- Faster training
- Better convergence
- Higher accuracy

Sigmoid Model

- Slower learning
- Can suffer from vanishing gradient problem
- Slightly lower accuracy

---

Comparison Summary

Feature| ReLU| Sigmoid
Training Speed| Faster| Slower
Gradient Problem| Less| More
Accuracy| Higher| Lower
Output Range| 0 to Infinity| 0 to 1

---

Conclusion

Activation functions significantly affect neural network performance.

From this experiment:

- ReLU provided faster training and better performance
- Sigmoid worked correctly but trained slower

Therefore, ReLU is generally preferred for hidden layers in deep learning models.

---

Future Improvements

- Test additional activation functions (Tanh, Leaky ReLU)
- Use larger datasets
- Implement deeper neural networks
- Add confusion matrix evaluation
- Perform hyperparameter tuning
