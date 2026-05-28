---
title: "A Gentle Introduction to Bayes Theorem for Machine Learning"
source: "https://machinelearningmastery.com/bayes-theorem-for-machine-learning/"
author:
  - "[[Jason Brownlee]]"
published: 2019-10-03
created: 2026-05-27
description: "Bayes Theorem provides a principled way for calculating a conditional probability. It is a deceptively simple calculation, although it can be used to easily calculate the conditional probability of events where intuition often fails. Although it is a powerful tool in the field of probability, Bayes Theorem is also widely used in the field of […]"
tags:
  - "clippings"
---
Bayes Theorem provides a principled way for calculating a conditional probability.

It is a deceptively simple calculation, although it can be used to easily calculate the conditional probability of events where intuition often fails.

Although it is a powerful tool in the field of probability, Bayes Theorem is also widely used in the field of machine learning. Including its use in a probability framework for fitting a model to a training dataset, referred to as maximum a posteriori or MAP for short, and in developing models for classification predictive modeling problems such as the Bayes Optimal Classifier and Naive Bayes.

In this post, you will discover Bayes Theorem for calculating conditional probabilities and how it is used in machine learning.

After reading this post, you will know:

- What Bayes Theorem is and how to work through the calculation on a real scenario.
- What the terms in the Bayes theorem calculation mean and the intuitions behind them.
- Examples of how Bayes theorem is used in classifiers, optimization and causal models.

**Kick-start your project** with my new book [Probability for Machine Learning](https://machinelearningmastery.com/probability-for-machine-learning/), including *step-by-step tutorials* and the *Python source code* files for all examples.

Let’s get started.

- **Update Oct/2019**: Join the discussion about this tutorial on [HackerNews](https://news.ycombinator.com/item?id=21151032).
- **Update Oct/2019**: Expanded to add more examples and uses of Bayes Theorem.
![A Gentle Introduction to Bayes Theorem for Machine Learning](https://machinelearningmastery.com/wp-content/uploads/2019/10/A-Gentle-Introduction-to-Bayes-Theorem-for-Machine-Learning.jpg)

A Gentle Introduction to Bayes Theorem for Machine Learning  
Photo by [Marco Verch](https://www.flickr.com/photos/160866001@N07/46679370454/), some rights reserved.

## Overview

This tutorial is divided into six parts; they are:

1. Bayes Theorem of Conditional Probability
2. Naming the Terms in the Theorem
3. Worked Example for Calculating Bayes Theorem
	1. Diagnostic Test Scenario
		2. Manual Calculation
		3. Python Code Calculation
		4. Binary Classifier Terminology
4. Bayes Theorem for Modeling Hypotheses
5. Bayes Theorem for Classification
	1. Naive Bayes Classifier
		2. Bayes Optimal Classifier
6. More Uses of Bayes Theorem in Machine Learning
	1. Bayesian Optimization
		2. Bayesian Belief Networks

## Bayes Theorem of Conditional Probability

Before we dive into Bayes theorem, let’s review marginal, joint, and conditional probability.

Recall that marginal probability is the probability of an event, irrespective of other random variables. If the random variable is independent, then it is the probability of the event directly, otherwise, if the variable is dependent upon other variables, then the marginal probability is the probability of the event summed over all outcomes for the dependent variables, called the sum rule.

- **Marginal Probability**: The probability of an event irrespective of the outcomes of other random variables, e.g. P(A).

The joint probability is the probability of two (or more) simultaneous events, often described in terms of events A and B from two dependent random variables, e.g. X and Y. The joint probability is often summarized as just the outcomes, e.g. A and B.

- **Joint Probability**: Probability of two (or more) simultaneous events, e.g. P(A and B) or P(A, B).

The conditional probability is the probability of one event given the occurrence of another event, often described in terms of events A and B from two dependent random variables e.g. X and Y.

- **Conditional Probability**: Probability of one (or more) event given the occurrence of another event, e.g. P(A given B) or P(A | B).

The joint probability can be calculated using the conditional probability; for example:

- P(A, B) = P(A | B) \* P(B)

This is called the product rule. Importantly, the joint probability is symmetrical, meaning that:

- P(A, B) = P(B, A)

The conditional probability can be calculated using the joint probability; for example:

- P(A | B) = P(A, B) / P(B)

The conditional probability is not symmetrical; for example:

- P(A | B)!= P(B | A)

We are now up to speed with marginal, joint and conditional probability. If you would like more background on these fundamentals, see the tutorial:

- [A Gentle Introduction to Joint, Marginal, and Conditional Probability](https://machinelearningmastery.com/joint-marginal-and-conditional-probability-for-machine-learning/)

### An Alternate Way To Calculate Conditional Probability

Now, there is another way to calculate the conditional probability.

Specifically, one conditional probability can be calculated using the other conditional probability; for example:

- P(A|B) = P(B|A) \* P(A) / P(B)

The reverse is also true; for example:

- P(B|A) = P(A|B) \* P(B) / P(A)

This alternate approach of calculating the conditional probability is useful either when the joint probability is challenging to calculate (which is most of the time), or when the reverse conditional probability is available or easy to calculate.

This alternate calculation of the conditional probability is referred to as Bayes Rule or [Bayes Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem), named for [Reverend Thomas Bayes](https://en.wikipedia.org/wiki/Thomas_Bayes), who is credited with first describing it. It is grammatically correct to refer to it as Bayes’ Theorem (with the apostrophe), but it is common to omit the apostrophe for simplicity.

- **Bayes Theorem**: Principled way of calculating a conditional probability without the joint probability.

It is often the case that we do not have access to the denominator directly, e.g. P(B).

We can calculate it an alternative way; for example:

- P(B) = P(B|A) \* P(A) + P(B|not A) \* P(not A)

This gives a formulation of Bayes Theorem that we can use that uses the alternate calculation of P(B), described below:

- P(A|B) = P(B|A) \* P(A) / P(B|A) \* P(A) + P(B|not A) \* P(not A)

Or with brackets around the denominator for clarity:

- P(A|B) = P(B|A) \* P(A) / (P(B|A) \* P(A) + P(B|not A) \* P(not A))

**Note**: the denominator is simply the expansion we gave above.

As such, if we have P(A), then we can calculate P(not A) as its complement; for example:

- P(not A) = 1 – P(A)

Additionally, if we have P(not B|not A), then we can calculate P(B|not A) as its complement; for example:

- P(B|not A) = 1 – P(not B|not A)

Now that we are familiar with the calculation of Bayes Theorem, let’s take a closer look at the meaning of the terms in the equation.

### Want to Learn Probability for Machine Learning

Take my free 7-day email crash course now (with sample code).

Click to sign-up and also get a free PDF Ebook version of the course.

## Naming the Terms in the Theorem

The terms in the Bayes Theorem equation are given names depending on the context where the equation is used.

It can be helpful to think about the calculation from these different perspectives and help to map your problem onto the equation.

Firstly, in general, the result P(A|B) is referred to as the **posterior probability** and P(A) is referred to as the **prior probability**.

- P(A|B): Posterior probability.
- P(A): Prior probability.

Sometimes P(B|A) is referred to as the **likelihood** and P(B) is referred to as the **evidence**.

- P(B|A): Likelihood.
- P(B): Evidence.

This allows Bayes Theorem to be restated as:

- Posterior = Likelihood \* Prior / Evidence

We can make this clear with a smoke and fire case.

**What is the probability that there is fire given that there is smoke?**

Where P(Fire) is the Prior, P(Smoke|Fire) is the Likelihood, and P(Smoke) is the evidence:

- P(Fire|Smoke) = P(Smoke|Fire) \* P(Fire) / P(Smoke)

You can imagine the same situation with rain and clouds.

Now that we are familiar with Bayes Theorem and the meaning of the terms, let’s look at a scenario where we can calculate it.

## Worked Example for Calculating Bayes Theorem

Bayes theorem is best understood with a real-life worked example with real numbers to demonstrate the calculations.

First we will define a scenario then work through a manual calculation, a calculation in Python, and a calculation using the terms that may be familiar to you from the field of binary classification.

1. Diagnostic Test Scenario
2. Manual Calculation
3. Python Code Calculation
4. Binary Classifier Terminology

Let’s go.

### Diagnostic Test Scenario

An excellent and widely used example of the benefit of Bayes Theorem is in the analysis of a medical diagnostic test.

**Scenario**: Consider a human population that may or may not have cancer (Cancer is True or False) and a medical test that returns positive or negative for detecting cancer (Test is Positive or Negative), e.g. like a mammogram for detecting breast cancer.

> **Problem**: If a randomly selected patient has the test and it comes back positive, what is the probability that the patient has cancer?

### Manual Calculation

Medical diagnostic tests are not perfect; they have error.

Sometimes a patient will have cancer, but the test will not detect it. This capability of the test to detect cancer is referred to as the **sensitivity**, or the true positive rate.

In this case, we will contrive a sensitivity value for the test. The test is good, but not great, with a true positive rate or sensitivity of 85%. That is, of all the people who have cancer and are tested, 85% of them will get a positive result from the test.

- P(Test=Positive | Cancer=True) = 0.85

Given this information, our intuition would suggest that there is an 85% probability that the patient has cancer.

**Our intuitions of probability are wrong.**

This type of error in interpreting probabilities is so common that it has its own name; it is referred to as the [base rate fallacy](https://en.wikipedia.org/wiki/Base_rate_fallacy).

It has this name because the error in estimating the probability of an event is caused by ignoring the base rate. That is, it ignores the probability of a randomly selected person having cancer, regardless of the results of a diagnostic test.

In this case, we can assume the probability of breast cancer is low, and use a contrived base rate value of one person in 5,000, or (0.0002) 0.02%.

- P(Cancer=True) = 0.02%.

We can correctly calculate the probability of a patient having cancer given a positive test result using Bayes Theorem.

Let’s map our scenario onto the equation:

- P(A|B) = P(B|A) \* P(A) / P(B)
- P(Cancer=True | Test=Positive) = P(Test=Positive|Cancer=True) \* P(Cancer=True) / P(Test=Positive)

We know the probability of the test being positive given that the patient has cancer is 85%, and we know the base rate or the prior probability of a given patient having cancer is 0.02%; we can plug these values in:

- P(Cancer=True | Test=Positive) = 0.85 \* 0.0002 / P(Test=Positive)

We don’t know P(Test=Positive), it’s not given directly.

Instead, we can estimate it using:

- P(B) = P(B|A) \* P(A) + P(B|not A) \* P(not A)
- P(Test=Positive) = P(Test=Positive|Cancer=True) \* P(Cancer=True) + P(Test=Positive|Cancer=False) \* P(Cancer=False)

Firstly, we can calculate P(Cancer=False) as the complement of P(Cancer=True), which we already know

- P(Cancer=False) = 1 – P(Cancer=True)
- \= 1 – 0.0002
- \= 0.9998

Let’s plugin what we have:

We can plug in our known values as follows:

- P(Test=Positive) = 0.85 \* 0.0002 + P(Test=Positive|Cancer=False) \* 0.9998

We still do not know the probability of a positive test result given no cancer.

This requires additional information.

Specifically, we need to know how good the test is at correctly identifying people that do not have cancer. That is, testing negative result (Test=Negative) when the patient does not have cancer (Cancer=False), called the true negative rate or the **specificity**.

We will use a contrived specificity value of 95%.

- P(Test=Negative | Cancer=False) = 0.95

With this final piece of information, we can calculate the false positive or false alarm rate as the complement of the true negative rate.

- P(Test=Positive|Cancer=False) = 1 – P(Test=Negative | Cancer=False)
- \= 1 – 0.95
- \= 0.05

We can plug this false alarm rate into our calculation of P(Test=Positive) as follows:

- P(Test=Positive) = 0.85 \* 0.0002 + 0.05 \* 0.9998
- P(Test=Positive) = 0.00017 + 0.04999
- P(Test=Positive) = 0.05016

Excellent, so the probability of the test returning a positive result, regardless of whether the person has cancer or not is about 5%.

We now have enough information to calculate Bayes Theorem and estimate the probability of a randomly selected person having cancer if they get a positive test result.

- P(Cancer=True | Test=Positive) = P(Test=Positive|Cancer=True) \* P(Cancer=True) / P(Test=Positive)
- P(Cancer=True | Test=Positive) = 0.85 \* 0.0002 / 0.05016
- P(Cancer=True | Test=Positive) = 0.00017 / 0.05016
- P(Cancer=True | Test=Positive) = 0.003389154704944

The calculation suggests that if the patient is informed they have cancer with this test, then there is only 0.33% chance that they have cancer.

**It is a terrible diagnostic test!**

The example also shows that the calculation of the conditional probability requires *enough* information.

For example, if we have the values used in Bayes Theorem already, we can use them directly.

This is rarely the case, and we typically have to calculate the bits we need and plug them in, as we did in this case. In our scenario we were given 3 pieces of information, the the **base rate**, the **sensitivity** (or true positive rate), and the **specificity** (or true negative rate).

- **Sensitivity**: 85% of people with cancer will get a positive test result.
- **Base Rate**: 0.02% of people have cancer.
- **Specificity**: 95% of people without cancer will get a negative test result.

We did not have the P(Test=Positive), but we calculated it given what we already had available.

We might imagine that Bayes Theorem allows us to be even more precise about a given scenario. For example, if we had more information about the patient (e.g. their age) and about the domain (e.g. cancer rates for age ranges), and in turn we could offer an even more accurate probability estimate.

That was a lot of work.

Let’s look at how we can calculate this exact scenario using a few lines of Python code.

<iframe frameborder="0" src="https://166c3c03bd34b6f2770d8f13bd8e51c6.safeframe.googlesyndication.com/safeframe/1-0-45/html/container.html" title="Conteúdo de anúncios de terceiros" width="1" height="1" allow="private-state-token-redemption;attribution-reporting" aria-label="Publicidade"></iframe>

### Python Code Calculation

To make this example concrete, we can perform the calculation in Python.

The example below performs the same calculation in vanilla Python (no libraries), allowing you to play with the parameters and test different scenarios.

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | \# calculate the probability of cancer patient and diagnostic test  \# calculate P(A\|B) given P(A), P(B\|A), P(B\|not A)  def bayes\_theorem(p\_a, p\_b\_given\_a, p\_b\_given\_not\_a):  \# calculate P(not A)  not\_a = 1 - p\_a  \# calculate P(B)  p\_b = p\_b\_given\_a \* p\_a + p\_b\_given\_not\_a \* not\_a  \# calculate P(A\|B)  p\_a\_given\_b = (p\_b\_given\_a \* p\_a) / p\_b  return p\_a\_given\_b  \# P(A)  p\_a = 0.0002  \# P(B\|A)  p\_b\_given\_a = 0.85  \# P(B\|not A)  p\_b\_given\_not\_a = 0.05  \# calculate P(A\|B)  result = bayes\_theorem(p\_a, p\_b\_given\_a, p\_b\_given\_not\_a)  \# summarize  print('P(A\|B) = %.3f%%' % (result \* 100)) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Running the example calculates the probability that a patient has cancer given the test returns a positive result, matching our manual calculation.

| 1 | P(A\|B) = 0.339% |
| --- | --- | --- |

This is a helpful little script that you may want to adapt to new scenarios.

Now, it is common to describe the calculation of Bayes Theorem for a scenario using the terms from binary classification. It provides a very intuitive way for thinking about a problem. In the next section we will review these terms and see how they map onto the probabilities in the theorem and how they relate to our scenario.

### Binary Classifier Terminology

It may be helpful to think about the cancer test example in terms of the common terms from [binary (two-class) classification](https://en.wikipedia.org/wiki/Sensitivity_and_specificity), i.e. where notions of specificity and sensitivity come from.

Personally, I find these terms help everything to make sense.

Firstly, let’s define a [confusion matrix](https://machinelearningmastery.com/confusion-matrix-machine-learning/):

| 1  2  3 | \| Positive Class \| Negative Class  Positive Prediction \| True Positive (TP) \| False Positive (FP)  Negative Prediction \| False Negative (FN) \| True Negative (TN) |
| --- | --- | --- | --- | --- | --- | --- | --- |

We can then define some rates from the confusion matrix:

- True Positive Rate (TPR) = TP / (TP + FN)
- False Positive Rate (FPR) = FP / (FP + TN)
- True Negative Rate (TNR) = TN / (TN + FP)
- False Negative Rate (FNR) = FN / (FN + TP)

These terms are called rates, but they can also be interpreted as probabilities.

Also, it might help to notice:

- TPR + FNR = 1.0, or:
	- FNR = 1.0 – TPR
		- TPR = 1.0 – FNR
- TNR + FPR = 1.0, or:
	- TNR = 1.0 – FPR
		- FPR = 1.0 – TNR

Recall that in a previous section that we calculated the false positive rate given the complement of true negative rate, or FPR = 1.0 – TNR.

Some of these rates have special names, for example:

- Sensitivity = TPR
- Specificity = TNR

We can map these rates onto familiar terms from Bayes Theorem:

- **P(B|A)**: True Positive Rate (TPR).
- **P(not B|not A)**: True Negative Rate (TNR).
- **P(B|not A)**: False Positive Rate (FPR).
- **P(not B|A)**: False Negative Rate (FNR).

We can also map the base rates for the condition (class) and the treatment (prediction) on familiar terms from Bayes Theorem:

- **P(A)**: Probability of a Positive Class (PC).
- **P(not A)**: Probability of a Negative Class (NC).
- **P(B)**: Probability of a Positive Prediction (PP).
- **P(not B)**: Probability of a Negative Prediction (NP).

Now, let’s consider Bayes Theorem using these terms:

- P(A|B) = P(B|A) \* P(A) / P(B)
- P(A|B) = (TPR \* PC) / PP

Where we often cannot calculate P(B), so we use an alternative:

- P(B) = P(B|A) \* P(A) + P(B|not A) \* P(not A)
- P(B) = TPR \* PC + FPR \* NC

Now, let’s look at our scenario of cancer and a cancer detection test.

The class or condition would be “ *Cancer* ” and the treatment or prediction would the “ *Test* “.

First, let’s review all of the rates:

- True Positive Rate (TPR): 85%
- False Positive Rate (FPR): 5%
- True Negative Rate (TNR): 95%
- False Negative Rate (FNR): 15%

Let’s also review what we know about base rates:

- Positive Class (PC): 0.02%
- Negative Class (NC): 99.98%
- Positive Prediction (PP): 5.016%
- Negative Prediction (NP): 94.984%

Plugging things in, we can calculate the probability of a positive test result (a positive prediction) as the probability of a positive test result given cancer (the true positive rate) multiplied by the base rate for having cancer (the positive class), plus the probability if a positive test result given no cancer (the false positive rate) plus the probability of not having cancer (the negative class).

The calculation with these terms is as follows:

- P(B) = P(B|A) \* P(A) + P(B|not A) \* P(not A)
- P(B) = TPR \* PC + FPR \* NC
- P(B) = 85% \* 0.02% + 5% \* 99.98%
- P(B) = 5.016%

We can then calculate Bayes Theorem for the scenario, namely the probability of cancer given a positive test result (the posterior) is the probability of a positive test result given cancer (the true positive rate) multiplied by the probability of having cancer (the positive class rate), divided by the probability of a positive test result (a positive prediction).

The calculation with these terms is as follows:

- P(A|B) = P(B|A) \* P(A) / P(B)
- P(A|B) = TPR \* PC / PP
- P(A|B) = 85% \* 0.02% / 5.016%
- P(A|B) = 0.339%

It turns out that in this case, the [posterior probability](https://en.wikipedia.org/wiki/Posterior_probability) that we are calculating with the Bayes theorem is equivalent to the [precision](https://en.wikipedia.org/wiki/Precision_and_recall), also called the Positive Predictive Value (PPV) of the confusion matrix:

- PPV = TP / (TP + FP)

Or, stated in our classifier terms:

- P(A|B) = PPV
- PPV = TPR \* PC / PP

**So why do we go to all of the trouble of calculating the posterior probability?**

Because we don’t have the confusion matrix for a population of people both with and without cancer that have been tested and have been not tested. Instead, all we have is some priors and probabilities about our population and our test.

This highlights when we might choose to use the calculation in practice.

Specifically, when we have beliefs about the events involved, but we cannot perform the calculation by counting examples in the real world.

<iframe frameborder="0" src="https://166c3c03bd34b6f2770d8f13bd8e51c6.safeframe.googlesyndication.com/safeframe/1-0-45/html/container.html" title="Conteúdo de anúncios de terceiros" width="1" height="1" allow="private-state-token-redemption;attribution-reporting" aria-label="Publicidade"></iframe>

## Bayes Theorem for Modeling Hypotheses

Bayes Theorem is a useful tool in applied machine learning.

It provides a way of thinking about the relationship between data and a model.

A machine learning algorithm or model is a specific way of thinking about the structured relationships in the data. In this way, a model can be thought of as a hypothesis about the relationships in the data, such as the relationship between input (*X*) and output (*y*). The practice of applied machine learning is the testing and analysis of different hypotheses (models) on a given dataset.

If this idea of thinking of a model as a hypothesis is new to you, see this tutorial on the topic:

- [What is a Hypothesis in Machine Learning?](https://machinelearningmastery.com/what-is-a-hypothesis-in-machine-learning/)

Bayes Theorem provides a probabilistic model to describe the relationship between data (*D*) and a hypothesis (h); for example:

- P(h|D) = P(D|h) \* P(h) / P(D)

Breaking this down, it says that the probability of a given hypothesis holding or being true given some observed data can be calculated as the probability of observing the data given the hypothesis multiplied by the probability of the hypothesis being true regardless of the data, divided by the probability of observing the data regardless of the hypothesis.

> Bayes theorem provides a way to calculate the probability of a hypothesis based on its prior probability, the probabilities of observing various data given the hypothesis, and the observed data itself.

— Page 156, [Machine Learning](https://amzn.to/2jWd51p), 1997.

Under this framework, each piece of the calculation has a specific name; for example:

- P(h|D): Posterior probability of the hypothesis (the thing we want to calculate).
- P(h): Prior probability of the hypothesis.

This gives a useful framework for thinking about and modeling a machine learning problem.

If we have some prior domain knowledge about the hypothesis, this is captured in the prior probability. If we don’t, then all hypotheses may have the same prior probability.

If the probability of observing the data P(D) increases, then the probability of the hypothesis holding given the data P(h|D) decreases. Conversely, if the probability of the hypothesis P(h) and the probability of observing the data given hypothesis increases, the probability of the hypothesis holding given the data P(h|D) increases.

The notion of testing different models on a dataset in applied machine learning can be thought of as estimating the probability of each hypothesis (h1, h2, h3, … in H) being true given the observed data.

The optimization or seeking the hypothesis with the maximum posterior probability in modeling is called [maximum a posteriori](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation) or MAP for short.

> Any such maximally probable hypothesis is called a maximum a posteriori (MAP) hypothesis. We can determine the MAP hypotheses by using Bayes theorem to calculate the posterior probability of each candidate hypothesis.

— Page 157, [Machine Learning](https://amzn.to/2jWd51p), 1997.

Under this framework, the probability of the data (D) is constant as it is used in the assessment of each hypothesis. Therefore, it can be removed from the calculation to give the simplified unnormalized estimate as follows:

- max h in H P(h|D) = P(D|h) \* P(h)

If we do not have any prior information about the hypothesis being tested, they can be assigned a uniform probability, and this term too will be a constant and can be removed from the calculation to give the following:

- max h in H P(h|D) = P(D|h)

That is, the goal is to locate a hypothesis that best explains the observed data.

Fitting models like linear regression for predicting a numerical value, and logistic regression for binary classification can be framed and solved under the MAP probabilistic framework. This provides an alternative to the more common maximum likelihood estimation (MLE) framework.

## Bayes Theorem for Classification

Classification is a predictive modeling problem that involves assigning a label to a given input data sample.

The problem of classification predictive modeling can be framed as calculating the conditional probability of a class label given a data sample, for example:

- P(class|data) = (P(data|class) \* P(class)) / P(data)

Where P(class|data) is the probability of class given the provided data.

This calculation can be performed for each class in the problem and the class that is assigned the largest probability can be selected and assigned to the input data.

In practice, it is very challenging to calculate full Bayes Theorem for classification.

The priors for the class and the data are easy to estimate from a training dataset, if the dataset is suitability representative of the broader problem.

The conditional probability of the observation based on the class P(data|class) is not feasible unless the number of examples is extraordinarily large, e.g. large enough to effectively estimate the probability distribution for all different possible combinations of values. This is almost never the case, we will not have sufficient coverage of the domain.

As such, the direct application of Bayes Theorem also becomes intractable, especially as the number of variables or features (n) increases.

### Naive Bayes Classifier

The solution to using Bayes Theorem for a conditional probability classification model is to simplify the calculation.

The Bayes Theorem assumes that each input variable is dependent upon all other variables. This is a cause of complexity in the calculation. We can remove this assumption and consider each input variable as being independent from each other.

This changes the model from a dependent conditional probability model to an independent conditional probability model and dramatically simplifies the calculation.

This means that we calculate P(data|class) for each input variable separately and multiple the results together, for example:

- P(class | X1, X2, …, Xn) = P(X1|class) \* P(X2|class) \* … \* P(Xn|class) \* P(class) / P(data)

We can also drop the probability of observing the data as it is a constant for all calculations, for example:

- P(class | X1, X2, …, Xn) = P(X1|class) \* P(X2|class) \* … \* P(Xn|class) \* P(class)

This simplification of Bayes Theorem is common and widely used for classification predictive modeling problems and is generally referred to as [Naive Bayes](https://machinelearningmastery.com/classification-as-conditional-probability-and-the-naive-bayes-algorithm/).

The word “ *naive* ” is French and typically has a diaeresis (umlaut) over the “i”, which is commonly left out for simplicity, and “Bayes” is capitalized as it is named for Reverend Thomas Bayes.

For tutorials on how to implement Naive Bayes from scratch in Python see:

- [How to Develop a Naive Bayes Classifier from Scratch in Python](https://machinelearningmastery.com/classification-as-conditional-probability-and-the-naive-bayes-algorithm/)
- [Naive Bayes Classifier From Scratch in Python](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)

### Bayes Optimal Classifier

The Bayes optimal classifier is a probabilistic model that makes the most likley prediction for a new example, given the training dataset.

This model is also referred to as the Bayes optimal learner, the Bayes classifier, Bayes optimal decision boundary, or the Bayes optimal discriminant function.

- **Bayes Classifier**: Probabilistic model that makes the most probable prediction for new examples.

Specifically, the Bayes optimal classifier answers the question:

> What is the most probable classification of the new instance given the training data?

This is different from the MAP framework that seeks the most probable hypothesis (model). Instead, we are interested in making a specific prediction.

The equation below demonstrates how to calculate the conditional probability for a new instance (*vi*) given the training data (*D*), given a space of hypotheses (*H*).

- P(vj | D) = sum {h in H} P(vj | hi) \* P(hi | D)

Where *vj* is a new instance to be classified, *H* is the set of hypotheses for classifying the instance, *hi* is a given hypothesis, *P(vj | hi)* is the posterior probability for *vi* given hypothesis *hi*, and *P(hi | D)* is the posterior probability of the hypothesis *hi* given the data *D*.

Selecting the outcome with the maximum probability is an example of a Bayes optimal classification.

Any model that classifies examples using this equation is a Bayes optimal classifier and no other model can outperform this technique, on average.

We have to let that sink in. It is a big deal.

Because the Bayes classifier is optimal, the Bayes error is the minimum possible error that can be made.

- **Bayes Error**: The minimum possible error that can be made when making predictions.

It is a theoretical model, but it is held up as an ideal that we may wish to pursue.

The Naive Bayes classifier is an example of a classifier that adds some simplifying assumptions and attempts to approximate the Bayes Optimal Classifier.

- [A Gentle Introduction to the Bayes Optimal Classifier](https://machinelearningmastery.com/bayes-optimal-classifier/)

## More Uses of Bayes Theorem in Machine Learning

Developing classifier models may be the most common application on Bayes Theorem in machine learning.

Nevertheless, there are many other applications. Two important examples are optimization and causal models.

### Bayesian Optimization

Global optimization is a challenging problem of finding an input that results in the minimum or maximum cost of a given objective function.

Typically, the form of the objective function is complex and intractable to analyze and is often non-convex, nonlinear, high dimension, noisy, and computationally expensive to evaluate.

Bayesian Optimization provides a principled technique based on Bayes Theorem to direct a search of a global optimization problem that is efficient and effective. It works by building a probabilistic model of the objective function, called the surrogate function, that is then searched efficiently with an acquisition function before candidate samples are chosen for evaluation on the real objective function.

Bayesian Optimization is often used in applied machine learning to tune the hyperparameters of a given well-performing model on a validation dataset.

- [How to Implement Bayesian Optimization from Scratch in Python](https://machinelearningmastery.com/what-is-bayesian-optimization/)

### Bayesian Belief Networks

Probabilistic models can define relationships between variables and be used to calculate probabilities.

Fully conditional models may require an enormous amount of data to cover all possible cases, and probabilities may be intractable to calculate in practice. Simplifying assumptions such as the conditional independence of all random variables can be effective, such as in the case of Naive Bayes, although it is a drastically simplifying step.

An alternative is to develop a model that preserves known conditional dependence between random variables and conditional independence in all other cases. Bayesian networks are a probabilistic graphical model that explicitly capture the known conditional dependence with directed edges in a graph model. All missing connections define the conditional independencies in the model.

As such Bayesian Networks provide a useful tool to visualize the probabilistic model for a domain, review all of the relationships between the random variables, and reason about causal probabilities for scenarios given available evidence.

The networks are not exactly Bayesian by definition, although given that both the probability distributions for the random variables (nodes) and the relationships between the random variables (edges) are specified subjectively, the model can be thought to capture the “belief” about a complex domain.

- [A Gentle Introduction to Bayesian Belief Networks](https://machinelearningmastery.com/introduction-to-bayesian-belief-networks/)

## Further Reading

This section provides more resources on the topic if you are looking to go deeper.

### Related Tutorials

- [A Gentle Introduction to Joint, Marginal, and Conditional Probability](https://machinelearningmastery.com/joint-marginal-and-conditional-probability-for-machine-learning/)
- [What is a Hypothesis in Machine Learning?](https://machinelearningmastery.com/what-is-a-hypothesis-in-machine-learning/)
- [How to Develop a Naive Bayes Classifier from Scratch in Python](https://machinelearningmastery.com/classification-as-conditional-probability-and-the-naive-bayes-algorithm/)
- [Naive Bayes Classifier From Scratch in Python](https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/)
- [How to Implement Bayesian Optimization from Scratch in Python](https://machinelearningmastery.com/what-is-bayesian-optimization/)
- [A Gentle Introduction to Bayesian Belief Networks](https://machinelearningmastery.com/introduction-to-bayesian-belief-networks/)

### Books

- [Pattern Recognition and Machine Learning](https://amzn.to/2JwHE7I), 2006.
- [Machine Learning](https://amzn.to/2jWd51p), 1997.
- [Pattern Classification, 2nd Edition](https://amzn.to/2xVBI1n), 2001.
- [Machine Learning: A Probabilistic Perspective](https://amzn.to/2xKSTCP), 2012.

### Articles

- [Conditional probability, Wikipedia](https://en.wikipedia.org/wiki/Conditional_probability).
- [Bayes’ theorem, Wikipedia](https://en.wikipedia.org/wiki/Bayes%27_theorem).
- [Maximum a posteriori estimation, Wikipedia](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation).
- [False positives and false negatives, Wikipedia](https://en.wikipedia.org/wiki/False_positives_and_false_negatives).
- [Base rate fallacy, Wikipedia](https://en.wikipedia.org/wiki/Base_rate_fallacy).
- [Sensitivity and specificity, Wikipedia](https://en.wikipedia.org/wiki/Sensitivity_and_specificity).
- [Taking the Confusion out of the Confusion Matrix](https://lucdemortier.github.io/articles/16/PerformanceMetrics), 2016.

## Summary

In this post, you discovered Bayes Theorem for calculating conditional probabilities and how it is used in machine learning.

Specifically, you learned:

- What Bayes Theorem is and how to work through the calculation on a real scenario.
- What the terms in the Bayes theorem calculation mean and the intuitions behind them.
- Examples of how Bayes theorem is used in classifiers, optimization and causal models.

**Do you have any questions?**  
Ask your questions in the comments below and I will do my best to answer.

## Get a Handle on Probability for Machine Learning!

[![Probability for Machine Learning](https://machinelearningmastery.com/wp-content/uploads/2022/11/P4ML-220.png)](https://machinelearningmastery.com/probability-for-machine-learning/)

#### Develop Your Understanding of Probability

...with just a few lines of python code

Discover how in my new Ebook:  
[Probability for Machine Learning](https://machinelearningmastery.com/probability-for-machine-learning/)

It provides **self-study tutorials** and **end-to-end projects** on:  
*Bayes Theorem*, *Bayesian Optimization*, *Distributions*, *Maximum Likelihood*, *Cross-Entropy*, *Calibrating Models*  
and much more...

#### Finally Harness Uncertainty in Your Projects

Skip the Academics. Just Results.

[See What's Inside](https://machinelearningmastery.com/probability-for-machine-learning/)