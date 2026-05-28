---
title: "The Kernel Trick in Machine Learning"
source: "https://medium.com/@oelmofty/the-kernel-trick-in-machine-learning-aaa597032bb4"
author:
  - "[[Omar Elmofty]]"
published: 2025-04-06
created: 2026-05-27
description: "More"
tags:
  - "clippings"
---
It is sometimes easy to overlook some of the cleverness in early machine learning algorithms, such as support vector machines. Pioneers of these algorithms had to deal with limited resources and computing power, which forced them to innovate and come up with clever ways to make machines learn. One such innovation is the so-called “Kernel Trick”, so let’s talk about that!

## Classification via Linear Separability

To understand the idea of linear separability in classification problems, let’s start with an example. Consider the problem in which you’re trying to classify whether a vehicle is a “Truck” or a “Supercar.” The information you have for each vehicle is the “Weight” of the vehicle in kg and the “Top speed” in km/h. In machine learning literature, these pieces of information (weight and top speed) are called features.

We can then plot the Weight vs. Top Speed graph below. This plot is called the feature space (a combination of all possible features). Now, let’s say you have a dataset with lots of examples of trucks and supercars, where for each example, we have the features (weight and top speed) and the class label (whether it’s a car or a truck). We can plot the dataset in the feature space below, where red points represent trucks and green points represent supercars.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JiiNQMH0nm-0DaTaX5X63w.png)

Figure 1: Example of a classification problem where different classes can be separated by a linear decision boundary.

Now, notice that most trucks are heavy and slow, and most supercars are light and fast. Hence, we have this nice separation between the data in the feature space. Now, the question becomes: How can we create a machine learning model that, given some input features (weight and top speed), outputs the class label (whether the vehicle is a car or a truck)?

The simplest and most intuitive model we could create to answer this question is a linear model, where we fit a straight line between the data, as shown in Figure 1. The straight line splits the feature space into two regions, where above the line are vehicles that are trucks, and below the line are vehicles that are cars. This type of separation, where the data can be split by a straight line, is referred to as **Linear Separability**.

The boundary between the two classes in the feature space (the straight line in our example) is typically called the **decision boundary**. Linear decision boundaries are lines in 2D, planes in 3D, and hyperplanes in higher dimensions.

The final linear model f(**x**), which is responsible for classifying data using a linear decision boundary, takes the following form (this is the model we fit in Support vector machines):

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*CBxeKPO8Mj5h1rfa0o7cFA.png)

Equation 1: Formulation of the linear model

Where:

- f(**x**) = 0, on the desicion boundary
- f(**x**) > 0, classify as class A
- f(**x**) < 0, classify as class B

So why is linear separability good? That’s because when the decision boundary is linear, a multitude of convex optimization tools can be used to find the optimal boundary that separates the data classes, with guarantees on convergence, optimality, etc. In short, linear decision boundaries are practical and easy to solve.

However, one could ask, what if I could not fit a linear decision boundary between the data points? How could that be fixed? Consider Figure 2 below, showing a feature space with points for two classes. These features cannot be split by a linear boundary and require a complex nonlinear boundary to separate the two regions in the feature space.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eptaO0i9b340VZVyuGVckw.png)

Figure 2: Example of a problem where the decision boundary is not linear.

There are two options to solve this in two ways:

1. Try to fit a complex curve in the feature space that will provide the needed decision boundary. However, picking the right curve and optimizing it to form the decision boundary is a challenging task, especially if the feature space has high dimensionality (i.e., too many features). Additionally, you lose all guarantees of optimality when you abandon the linear decision boundary.
2. Try to transform the feature space somehow into a higher-dimensional space where a linear decision boundary could be fit. See the diagram below for an example. With this approach, we don’t lose the nice properties that linearity brings to the problem.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LdPQ6tEdoTD4SeQDZTQuMQ.png)

Figure 3: Illustration showing how a transformation of the feature space into a higher dimension could make linear separability possible.

Option 2 is the obvious winner in this scenario, since as long as we can find the transformation of the feature space that enables linear separability, the rest is easy. But finding this transformation is tricky and can impact the effectiveness of the solution. That’s where the “Kernel Trick” comes to the rescue.

## The Kernel Trick

To understand the Kernel Trick, let’s define ϕ(x) as the transformation function that will transform the feature space to a higher dimension where linear separability can be achieved. We could write the formulation as:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*JLr4RUkl8DSdQXCLiy-W3A.png)

Equation 2: Transforming features to a higher dimension such that linear separability can be achieved.

Now, let’s take the linear model we defined in Equation 1 and tweak it a bit:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ocWDenjqH_uKqAu0hnLWhA.png)

Equation 3: Re-formulation of the linear model as a function of the training examples.

So, what have we done in the above re-formulation? We have made the linear decision boundary a function of the training examples, where, for each training example, we perform a dot product between the input **x** and the training example **x(i)**, then multiply by the coefficient ai.

Now, let’s substitute in the transformation ϕ(x) to get the final model:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Q-N8LNaebRao-Ps_PrxMBw.png)

Equation 4: Linear model with the transformation substituted in.

The final model now has a dot product of the transformed features in a higher dimension. Let’s break this down:

1. We are first transforming the space into a higher-dimensional one.
2. We are then computing the dot product in the higher dimension.
3. The final result of the dot product is a scalar, we multiply that by the coefficient ai.

Now, imagine the amount of computation involved in performing the above steps. If the transformation function ϕ(x) increases the dimensionality of the space by a significant factor, then computing the dot product in this higher-dimensional space will involve many multiplication and addition operations, which could be very expensive, if not impossible.

So, what if I told you we could skip steps 1 and 2 and directly compute the scalar in step 3 without having to compute dot products in higher dimensions? That’s exactly what the Kernel Trick is. The Kernel Trick is simply the following reformulation:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*x1ixwZ6M_VJF5I0TQsW9PA.png)

Equation 5: The definition of the kernel function

Where *k* is the kernel function. It directly computes a scalar, which is the resultant dot product of the features transformed into a higher dimension where linear separability is possible. It’s a short circuit, as it avoids having to perform the transformation and dot product in the higher dimension. This makes solving for the linear model computationally efficient. Some kernel functions also support underlying transformations that map the features into an infinite-dimensional space, where it would be impossible to fit a linear model without the Kernel Trick.

So now the final linear model can be expressed as:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*PHRLqwba5MhnRe_9x6rmmA.png)

Equation 5: Final linear model.

## Examples of Kernel Function

Without going into too much detail, here are a couple of examples of popular kernel functions. I’ll let you do your own reading if you want to understand them in depth.

### Polynomial Kernel

The polynomial kernel can be expressed as:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*Sock_Jftx1tiiwkCrkooaw.png)

Where d is the degree of the polynomial. If d = 1 we get the linear kernel, which is equivalent to no tranformation.

The underlying ϕ(**x**) can be shown to be (full derivation can be found in [wikipedia](https://en.wikipedia.org/wiki/Polynomial_kernel)):

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YpAs2Q2a4McTTIJ_D5KCeg.png)

### Radial Basis Function (RBF) / Guassisan Kernel

One of the most popular kernels used in machine learning.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*SjyNzozmNBhdSRi04KqJBQ.png)

The underlying feature space is infinite dimensional and can be expressed as (see [wikipedia](https://en.wikipedia.org/wiki/Radial_basis_function_kernel)):

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UcE-Rm6UtBqXnHoTgNRlFg.png)

## Some final remarks

The kernel trick is a powerful concept, and it is most popularly used in Support Vector Machines (SVMs), where the property of linear separability is utilized to fit a linear model to classify the data as explained above. However, it extends beyond that. For example, Gaussian Processes use the kernel function (often called the covariance function) to embed data into a higher-dimensional space and use that to define the similarity of data in this higher-dimensional space. Other similar and useful use cases of the kernel trick exist in the machine learning literature.