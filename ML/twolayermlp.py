import numpy as np
from jaxtyping import Int, Float
from numpy import ndarray

class TwoLayerMLP:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, lr):
        # parameters
        self.W1 = np.random(input_dim, hidden_dim)
        self.b1 = np.random(hidden_dim)
        self.W2 = np.random(hidden_dim, output_dim)
        self.b2 = np.random(output_dim)

        # hyperparameters
        self.activation_fn = "relu"
        self.dropout = False
        self.lr = lr 
    # forward pass
    def forward(self, X):
        self.X = X
        self.Z = X @ self.W1 + self.b1
        # apply relu
        if self.activation_fn == "relu":
            self.A1 = self.Z[self.Z >= 0]
        return self.A1 @ self.W2 + self.b2
        
    # backward pass
    def backward(self, y_hat, y):
        # standard mse loss
        loss = np.mean(np.sum((y - y_hat) ** 2, axis=1))
        
        # compute backward pass for second layer
        dL_dZ2 = 2 / y_hat.shape[0] * (y_hat - y) # (N, C)
        dL_dW2 = self.hidden.T @ (dL_dZ2) # (H, C)
        dL_db2 = np.sum(dL_dZ2, axis=0)

        # backward pass for first layer
        dL_dA1 = dL_dZ2 @ self.W2.T
        dA1_dZ1 =  self.Z >= 0
        dL_dW1 = self.X.T @ dL_dA1 * dA1_dZ1 
        dL_db1 = np.sum(dL_dA1 * dA1_dZ1, axis=0)

        # update weights
        self.W1 -= self.lr * dL_dW1
        self.b1 -= self.lr * dL_db1 
        self.W2 -= self.lr * dL_dW2
        self.b2 -= self.lr * dL_db2

        return loss

        