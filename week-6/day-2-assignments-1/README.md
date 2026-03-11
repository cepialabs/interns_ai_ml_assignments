# Neural Network Training: ReLU vs Sigmoid Activation

## Overview
This project demonstrates training two simple neural network models using different activation functions:

- **Sigmoid Activation Function**
- **ReLU (Rectified Linear Unit) Activation Function**

The goal is to compare how these activation functions affect the **training performance of a neural network**.

## Technologies Used
- Python
- NumPy
- Matplotlib
- Jupyter Notebook

## Neural Network Architecture

The neural network used in this project consists of:

```
Input Layer (2 neurons)
        ↓
Hidden Layer (3 neurons)
        ↓
Output Layer (1 neuron)
```

Both models use the same architecture, but the **hidden layer activation function changes**.

## Dataset

A small dataset similar to the **XOR problem** is used for training.

| Input 1 | Input 2 | Output |
|-------|-------|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Activation Functions

### Sigmoid Function

The sigmoid activation function converts values between **0 and 1**.

Formula:

```
σ(x) = 1 / (1 + e^(-x))
```

### ReLU Function

ReLU outputs **0 for negative values** and the same value for positive inputs.

Formula:

```
ReLU(x) = max(0, x)
```

## Training Process

Both neural network models are trained using the same steps:

1. Initialize weights randomly
2. Perform forward propagation
3. Compute prediction
4. Calculate loss
5. Update weights
6. Repeat for multiple epochs

## Performance Comparison

| Feature | Sigmoid | ReLU |
|------|------|------|
| Output Range | 0 to 1 | 0 to ∞ |
| Training Speed | Slower | Faster |
| Gradient Issue | Vanishing gradient | Reduced gradient problem |
| Deep Networks | Less suitable | More suitable |

### Observation

- The **ReLU model trains faster** and converges more quickly.
- The **Sigmoid model may learn slower** because gradients become very small.
- ReLU is widely used in modern deep learning models.

## Project Structure

```
relu-vs-sigmoid-neural-network/
│
├── relu_vs_sigmoid_nn.ipynb
├── README.md
```

## How to Run the Project

1. Clone the repository

```
git clone <your-repository-link>
```

2. Navigate to the project folder

```
cd relu-vs-sigmoid-neural-network
```

3. Open the notebook

```
jupyter notebook
```

4. Run all cells to train both models and view the performance comparison graph.

## Conclusion

This project shows how different activation functions influence neural network training.  
The **ReLU activation function generally provides better training performance compared to Sigmoid**, especially in deeper neural networks.

Understanding activation functions is essential for building efficient deep learning models.

## Author
**Swati M Patil**
