
1. [E] When building a neural network, should you overfit or underfit it first?


[E] Write the vanilla gradient update.
Neural network in simple Numpy.
[E] Write in plain NumPy the forward and backward pass for a two-layer feed-forward neural network with a ReLU layer in between.
[M] Implement vanilla dropout for the forward and backward pass in NumPy.
Activation functions.
[E] Draw the graphs for sigmoid, tanh, ReLU, and leaky ReLU.
[E] Pros and cons of each activation function.
[E] Is ReLU differentiable? What to do when it’s not differentiable?
[M] Derive derivatives for sigmoid function when is a vector.
[E] What’s the motivation for skip connection in neural works?
Vanishing and exploding gradients.
[E] How do we know that gradients are exploding? How do we prevent it?
[E] Why are RNNs especially susceptible to vanishing and exploding gradients?
[M] Weight normalization separates a weight vector’s norm from its gradient. How would it help with training?
[M] When training a large neural network, say a language model with a billion parameters, you evaluate your model on a validation set at the end of every epoch. You realize that your validation loss is often lower than your train loss. What might be happening?
[E] What criteria would you use for early stopping?
[E] Gradient descent vs SGD vs mini-batch SGD.
[H] It’s a common practice to train deep learning models using epochs: we sample batches from data without replacement. Why would we use epochs instead of just sampling data with replacement?
[M] Your model’ weights fluctuate a lot during training. How does that affect your model’s performance? What to do about it?
Learning rate.
[E] Draw a graph number of training epochs vs training error for when the learning rate is:
    too high
    too low
    acceptable.
[E] What’s learning rate warmup? Why do we need it?
[E] Compare batch norm and layer norm.
[M] Why is squared L2 norm sometimes preferred to L2 norm for regularizing neural networks?
[E] Some models use weight decay: after each gradient update, the weights are multiplied by a factor slightly less than 1. What is this useful for?
It’s a common practice for the learning rate to be reduced throughout the training.
[E] What’s the motivation?
[M] What might be the exceptions?
Batch size.
[E] What happens to your model training when you decrease the batch size to 1?
[E] What happens when you use the entire training data in a batch?
[M] How should we adjust the learning rate as we increase or decrease the batch size?
[M] Why is Adagrad sometimes favored in problems with sparse gradients?
Adam vs. SGD.
[M] What can you say about the ability to converge and generalize of Adam vs. SGD?
[M] What else can you say about the difference between these two optimizers?
[M] With model parallelism, you might update your model weights using the gradients from each machine asynchronously or synchronously. What are the pros and cons of asynchronous SGD vs. synchronous SGD?
[M] Why shouldn’t we have two consecutive linear layers in a neural network?
[M] Can a neural network with only RELU (non-linearity) act as a linear classifier?
[M] Design the smallest neural network that can function as an XOR gate.
[E] Why don’t we just initialize all weights in a neural network to zero?
Stochasticity.
[M] What are some sources of randomness in a neural network?
[M] Sometimes stochasticity is desirable when training neural networks. Why is that?
Dead neuron.
[E] What’s a dead neuron?
[E] How do we detect them in our neural network?
[M] How to prevent them?
Pruning.
[M] Pruning is a popular technique where certain weights of a neural network are set to 0. Why is it desirable?
[M] How do you choose what to prune from a neural network?
[H] Under what conditions would it be possible to recover training data from the weight checkpoints?
[H] Why do we try to reduce the size of a big trained model through techniques such as knowledge distillation instead of just training a small model from the beginning?
