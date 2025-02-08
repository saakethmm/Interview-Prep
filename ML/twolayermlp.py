import numpy as np

class TwoLayerMLP:
    def __init__(self, input_dim, hidden_dim, output_dim, lr)
        # parameters
        self.W1 = np.random(input_dim, hidden_dim)
        self.b1 = np.random(hidden_dim)
        self.W2 = np.random(hidden_dim, output_dim)
        self.b2 = np.random(output_dim)

        # activations
        self.hidden = None
        self.X = None

        # hyperparameters
        self.activation_fn = "relu"
        self.dropout = False
        self.lr = lr 
    # forward pass
    def forward(self, X):
        self.X = X
        self.hidden = X @ self.W1 + self.b1
        # apply relu
        if self.activation_fn == "relu":
            self.hidden = self.hidden[self.hidden >= 0]
        return self.hidden @ self.W2 + self.b2
    # backward pass
    def backward(self, y_hat, y):
        # standard mse loss
        loss = np.mean(np.sum((y - y_hat) ** 2, axis=1))
        # compute backward pass
        dL_dZ = 2 / y_hat.shape[0] * (y_hat - y) # (N, C)
        dL_dW2 = self.hidden.T @ (dL_dZ) # (H, C)

        # X transposed, but zeros filled in where self.hidden < 0
        dZ_dW1 = np.zeros_like(self.X.T) # (D, N)
        grad_W1 = self.X.T @ dL_dZ @ self.W2.T # (D, H)

        # update weights
        self.W1 -= self.lr * grad_W1
        self.W2 -= self.lr * grad_W2

        return loss

        