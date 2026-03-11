# Simple Neural Network with One Hidden Layer

## Overview
This project demonstrates a **simple neural network with one hidden layer** built using Python and NumPy.  
The purpose of this project is to understand how data flows through a neural network during the training process.

The notebook shows:
- How input data enters the neural network
- How hidden layers process the data
- How predictions are generated at the output layer

## Technologies Used
- Python
- NumPy
- Jupyter Notebook

## Neural Network Architecture
The neural network used in this project has three layers:

1. **Input Layer**
2. **Hidden Layer**
3. **Output Layer**

Structure:

```
Input Layer (2 neurons)
        ↓
Hidden Layer (3 neurons)
        ↓
Output Layer (1 neuron)
```

## Dataset
A small example dataset similar to the **XOR problem** is used.

| Input 1 | Input 2 | Output |
|-------|-------|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Activation Function
The **Sigmoid activation function** is used in the hidden and output layers.

Sigmoid Formula:

```
sigmoid(x) = 1 / (1 + e^(-x))
```

## How Data Flows Through the Network

### 1. Input Layer
The neural network receives input data such as:

```
(0,0), (0,1), (1,0), (1,1)
```

### 2. Hidden Layer
Input values are multiplied with weights and passed to the hidden layer.

Formula:

```
H = sigmoid(X × W1)
```

Where:
- `X` = Input data
- `W1` = Weights between input and hidden layer

### 3. Output Layer
The hidden layer output is multiplied with another set of weights to generate the final output.

Formula:

```
Y = sigmoid(H × W2)
```

Where:
- `H` = Hidden layer output
- `W2` = Weights between hidden and output layer

### 4. Prediction
The output layer produces the **predicted result**.

### 5. Training Process
During training:
1. The predicted output is compared with the actual output.
2. The error is calculated.
3. The model adjusts the weights to reduce prediction error.

This process repeats for many iterations until the model learns the pattern in the data.

## Project Structure

```
week-6/
│
├── simple_neural_network_assignment.ipynb
├── README.md
```

## How to Run

1. Clone the repository

```
git clone <your-repo-link>
```

2. Open the notebook

```
jupyter notebook
```

3. Run all cells in the notebook to see the neural network training.

## Conclusion
This project demonstrates the basic working of a neural network and how data flows from the input layer through the hidden layer to produce predictions at the output layer.

Understanding this simple model helps build the foundation for more advanced deep learning models.

## Author
**Swati M Patil**
