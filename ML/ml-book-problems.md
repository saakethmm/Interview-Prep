# Chapter 5: Math

## Algebra & Calculus



### Calculus & Convex Optimization

#### **Differentiable functions**

1. [E] What does it mean when a function is differentiable?
   * A function $f$ is differentiable when it is
     * continuous (limit from right and left sides for all points in domain are equal), and 
     * smooth (no jumps or jagged points)
       * i.e., the left and right derivatives are equal
2. [E] Give an example of when a function doesn’t have a derivative at a point.
   * A good example is the step function $f(x) = u(x) = \begin{cases} 0 \quad x\le 0 \\ 1 \quad x > 0 \end{cases}$

3. [M] Give an example of non-differentiable functions that are frequently used in machine learning. How do we do backpropagation if those functions aren’t differentiable?
   * A good example is the $f(\cdot) = \text{ReLU}(\cdot)$ activation function, which has a jagged point at $x=0$, where the left derivative is $f^\prime(x) = 0$ and right derivative is $f^\prime(x) = 1$ 
     * It is not smooth (though continuous), so it is non-differentiable at $x=0$ 
   * For the forward pass in an MLP, it appears as $h^{(i)} = \text{ReLU}(W^{(i)}h^{(i-1)})$ 
     * During backpropagation, we simply use the chain rule
     * Hence, $\frac{dh^{(i)}}{dW^{(i)}} = \frac{d}{da^{(i)}}(\sigma(a^{(i)}))\frac{d a^{(i)}}{dW^{(i)}}$ where the first derivative can be represented consistently via cases: $\sigma^\prime(a^{(i)}) = \begin{cases} 1 \quad a^{(i)} > 0 \\ 0 \quad else \end{cases}$

#### **Convexity**

1. [E] What does it mean for a function to be convex or concave? Draw it.
   * Function $f$ is convex if $f(\theta a + (1-\theta) b) \leq \theta f(a) + (1-\theta) f(b) \quad \forall \theta \in [0, 1] \quad \forall a, b \in \text{dom}(f)$ 
     * In other words, secant line is always above the value of the function at any point in between 
   * Similarly, $f$ is concave if $f(\theta a + (1-\theta) b) \geq \theta f(a) + (1-\theta) f(b) \quad \forall \theta \in [0, 1] \quad \forall a, b \in \text{dom}(f)$ 
     * In other words, secant line is always below the value of the function at any point in between 
2. [E] Why is convexity desirable in an optimization problem?
   * Convexity is useful since that means there exists only a single global minimum (i.e., any local minimum we find via some optimization algorithm such as gradient descent will ALWAYS find the optimal solution)

3. [M] Show that the cross-entropy loss function is convex.
   * Cross entropy loss is given by $\ell_{ce} = -\sum_{i=1}^n q_i \log p_i$ where $q_i$ is the ground-truth label for the $i$th component (e.g., GT class) of the output and $p_i$ is the predicted probability of the $i$th component (e.g., predicted class)
   * Note that $\ell_{ce}$ is a non-negative weighted sum of $-\log$ terms. Since $\log(x)$ is a concave function (second derivative is negative semi definite) at all points in the domain $x > 0$, CE loss must be convex!



# Chapter 6: Computer Science





# Chapter 7: ML Workflows





# Chapter 8: ML Algorithms 

* Check out [Data Science Glossary on Kaggle](https://www.kaggle.com/code/shivamb/data-science-glossary-on-kaggle) for ideas on different ML algorithms and data science tools that might be useful in projects/questions



