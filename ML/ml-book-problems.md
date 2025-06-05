# Chapter 5: Math

## Algebra & Calculus

### Vectors

#### Dot Product

1. [E] What’s the geometric interpretation of the dot product of two vectors?
   * The dot product of two vectors $$p = \bf{a} \cdot \bf{b} = \|a\|\|b\| \cos(\theta_{ab})$$, which means that:
     * the more positive the dot product is, the more aligned the two vectors are in direction
     * the more negative it is, the more they point in opposite directions
     * the closer it is to 0, the more orthogonal they are 

2. [E] Given a vector *u*, find vector *v* of unit length such that the dot product of *u* and *v* is maximum.
   * $$v = \frac{\bf{u}}{\|\bf{u}\|}$$, or the unit vector in the direction of $$\bf{u}$$, which means the dot product is exactly $$\bf{u}$$ 

#### Outer Product

1. [E] Given two vectors *a*=[3,2,1] and  *b*=[−1,0,1]. Calculate the outer product $$a b^\top$$?
   * $$\begin{bmatrix}
     -3 & 0 & 3 \\
     -2 & 0 & 2 \\
     -1 & 0 & 1
     \end{bmatrix}$$
2. [M] Give an example of how the outer product can be useful in ML.
   * Computing **covariance matrix** $$xx^\top$$, useful in determining correlations between elements of vector 
     * *Whitening* data
   * Computing **Fisher Information matrix**, useful for natural gradient descent (approximation of curvature)
   * Cross/Self-Attention: $$QK^\top$$ computation is an outer product over each batch/head

#### General 

1. [E] What does it mean for two vectors to be linearly independent?
   * Two vectors are linearly independent $$\iff$$ $$\alpha_1 \bf{a} + \alpha_2 \bf{b} = 0$$ for  $$\alpha_1 = \alpha_2 = 0$$ 

2. [M] Given two sets of vectors *A*=*a*1,*a*2,*a*3,...,*an* and *B*=*b*1,*b*2,*b*3,...,*bm*. How do you check that they share the same basis?
   * Determine $$\text{rank}({A})$$, $$\text{rank}({B})$$ 
   * If both are equal, then they both span the same subspace $\rightarrow$ same basis 
   * Else, they have different basis vectors 
3. [M] Given *n* vectors, each of *d* dimensions. What is the dimension of their span?
   * It would be upper bounded by $$\min(n, d)$$ 
   * Linearly dependent vectors would reduce max dimension beyond upper bound 

#### Norms 

1. 





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



