---
title: "Knowledge Discovery in Databases: 9 Steps to Success"
source: "https://blog.udemy.com/knowledge-discovery-in-databases/"
author:
  - "[[Udemy Editor]]"
published: 2014-04-01
created: 2026-05-28
description: "Knowledge discovery in databases (KDD) is the broad process of extracting meaningful patterns from large datasets, closely tied to data mining. This article covers KDD's nine iterative steps, from defining goals and cleansing data to selecting algorithms and applying discovered knowledge. You'll gain a clear understanding of how each phase builds toward actionable insight."
tags:
  - "clippings"
---
## Article Summary

Knowledge discovery in databases (KDD) is the broad process of extracting meaningful patterns from large datasets, closely tied to data mining. This article covers KDD's nine iterative steps, from defining goals and cleansing data to selecting algorithms and applying discovered knowledge. You'll gain a clear understanding of how each phase builds toward actionable insight.

[![knowledge discovery in databases](https://blog.udemy.com/wp-content/uploads/2014/04/shutterstock_104783216.jpg)](https://www.udemy.com/course/data-mining/?tc=blog.transcription_knowledgediscoveryindatabases) The term knowledge discovery in databases, or KDD for short, refers to the broad process of finding knowledge and data, and emphasizes the high level application of particular data minded methods. It is of interest to researchers in machine learning, pattern recognition, databases, statistics, artificial intelligence, knowledge acquisition for expert systems, and data visualization.

[Learn how to get started with your data](https://www.udemy.com/course/data-mining/?tc=blog.transcription_knowledgediscoveryindatabases)

The unifying goal of the KDD process is to extract knowledge from data in the context of large databases. The knowledge discovery process is repetitive, interactive, and consists of nine steps. Note that the process is repetitive at each step, meaning one might have to move back to the previous steps. The process has many artistic aspects in the sense that one cannot present one formula or technique to classify the right choices for each step and application type. Because of this it would be better to understand the process and the different needs and possibilities for each step.

The process starts with determining the KDD goals, and ends with the implementation of the discovered knowledge. Then the loop is closed. As a result, changes would have to be made in the application domain. This closes the loop, and the effects are then measured on the new data repositories, and the KDD process is launched again.

The following is a brief description of the nine step KDD process, starting with the managerial step.

## Step 1

Developing and understanding of the application domain. This is the preparatory step that sets the scene for understanding what should be done with transformation, algorithms, and representation. Those in charge of the KDD project need to understand and define the goals of the end user, then where the knowledge discovery process will take place, and other relevant prior knowledge.

[Work with SQL Server to store your data and create great reports](https://www.udemy.com/course/data-mining/?tc=blog.transcription_knowledgediscoveryindatabases)

As the KDD process proceeds, there may even be a revision of this step. Having understood the KDD goals, the pre-processing of the data starts defined in the next three steps. Note that some of the methods are similar to data mining algorithms, but are used in the pre-processing context.

## Step 2

Selecting and creating a data set on which discovery will be performed, based on goals. Determine what data will be used for the knowledge discovery, such as: what data is available, obtaining additional necessary data, and the integrating all the data for the knowledge discovery into one data set, including the attributes that will be considered for the process. This process is very important because the data mining learns and discovers from the available data. This is the evidence base for constructing the models. If some important attributes are missing, then the entire study may fail. From this respect, the more attributes considered, the better.

On the other hand, to collect, organize, and operate complex data repositories is expensive, and there is a trade off with the opportunity for best understanding the phenomenon. This trade off represents an aspect with the interactive, and iterative aspect of the KDD takes place.

This starts with the best available data set, and later expands and observes the effect in terms of knowledge discovery and modeling. The three primary sources include: a data warehouse, one or more transactional data, or one or more flat tables.

## Step 3

Pre-processing and cleansing. Data reliability is enhanced in this stage. It includes data clearing, such as handling missing values, and removing of outliers.

It may involve complex statistical methods, or using a data mining algorithm in this context. For example: If one suspects that a certain attribute is of insufficient reliability, or has many missing data, then this attribute could become the goal of a data mining supervised algorithm. A prediction model for this attribute will be developed, and then missing data can be predicted. The extent to which one pays attention to this level depends on many factors. In any case, studying the aspects is important, and often revealing by itself, regarding enterprise information systems.

[Get started with database design today](https://www.udemy.com/course/data-mining/?tc=blog.transcription_knowledgediscoveryindatabases)

## Step 4

Next is data transformation. In this stage, the generation of better data, for the data mining is prepared and developed. Methods here include dimension reduction, such as feature selection, and extraction, and record sampling, and attribute transformation such as discretization of numerical attributes and functional transformation.

This step can be crucial for the success of the entire KDD project, and it is usually very project specific. For example, in medical examinations, the quotient of attributes may often be the most important factor, and not each one by itself. In marketing we may need to consider facts beyond our control, as well as efforts and temporal issues, such as studying the effect of advertising accumulation. However, even if we do not use the right transformation at the beginning, we may obtain a surprising effect that gives a hint about the transformation needed in the next iteration.

Thus the KDD process reflects upon itself, and leads to an understanding of the transformation needed. Having completed the above four steps, the following four steps are related to data mining, where the focus is on the algorithmic aspects employed for each project.

## Step 5

Choosing the appropriate data mining task. We’re now ready to decide which type of data mining to use. For example: classification, regression, or clustering. This mostly depends on the KDD goals, and also on the previous steps. There are two major goals in data mining: prediction and description. Prediction is often referred to as supervised data mining, while descriptive data mining includes the unsupervised, and visualization aspects of data mining.

Most data mining techniques are based on inductive learning, where a model is constructed explicitly, or implicitly, by generalizing from a sufficient number of training examples. The underlying assumption of the inductive approach is that the trained model is applicable to future cases. The strategy also takes into account the level of meta learning for the particular set of available data.

## Step 6

Choosing the data mining algorithm. Now that you have the strategy, we can decide which tactics to use. This stage includes selecting the specific method for searching patterns, including multiple inducers. For example, when considering precision versus understandability, the former is better with neural networks, while the latter is better with decision trees.

For each strategy of meta learning, there are several possibilities for how it can be accomplished. Meta learning focuses on explaining what causes a data mining algorithm to be successful, or not in a particular problem. Thus, this approach attempts to understand the conditions under which a data mining is most appropriate. Each algorithm has parameters, and tactics of learning. Such as tenfold cross validation, or another division for training and testing.

## Step 7

Next is employing the data mining algorithm. Finally you can implement the appropriate data mining algorithm. In this step we might need to employ the algorithm several times until a satisfying the result is obtained. For instance, by tuning the algorithms control parameters, such as the minimum number of instances in a single leaf of a decision tree.

## Step 8

evaluation. In this stage we evaluate and interpret the mined patterns with respect to the goals defined in the first step. Here we consider the pre-processing steps with respect to their effect on the data mining algorithm results. This step focuses on the comprehensible nature and usefulness of the induced model. In this step, the discovered knowledge is also documented for further usage.

The last step is the usage, and overall feedback on the patterns and discovery results obtained by the data mining.

## Step 9

Using the discovered knowledge. We’re now ready to incorporate the knowledge into another system for further action. The knowledge becomes active in the sense that we may make changes to the system, and measure the effects. Actually, the success of this step determines the effectiveness of the entire KDD process.

There are many challenges in this step, such as losing laboratory conditions under which we have operated. For instance, the knowledge was discovered from a certain static snapshot, usually a sample of the data, but now the data becomes dynamic. Data structures may change, and the data domain may be modified.

Interested in learning more? [Enroll in this introductory course about understanding patterns, process, and tools of data today!](https://www.udemy.com/course/data-mining/?tc=blog.transcription_knowledgediscoveryindatabases)