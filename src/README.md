# Lecture Content

Here we collect the content of lectures for the Recommender Systems course.

## 1. Filters and users vectors

We are going to define _item_ and _user_ vectors, their geometrical meaning, etc. We will define _distance metrics_, also by implementing some examples of those.

Finally, we will build the simplest recommendation model possible: the most popular recommendation.

## 2. KNN-based recommendations

In this lecture, we will implement a distance-based model. First, we put ourself in the non-personalised mode, after that we try to assign a _ranking score_ to user-item preference in order to encode the personalised ranking.

## 3. Collaborative filtering

The aim of this lecture is to built a model that exploits the collaborative filtering algorithm in order to predict the rating $y_{ij}$ a user $i$ gives to the movie $j$.

## 4. K-Means recommendations

The purpose here is to build a model that is based on the notorious $k$-means clustering algorithm.
There are several ways to approach the problem, here we choose to cluster users based on their preferences, and recommend the most popular items in each user cluster. We mention alternative approaches in the conclusions.

## 5. Matrix Factorisation

This lecture will play the role of an introduction to the big topic of Matrix Factorisation. Indeed, we are going to define the important quantities and to apply a first example of the matrix factorisation recommendation model, that is FunkSVD.

## 6. Alternating Least Squares

We will keep going on exploring matrix factorisation algorithms, presenting the famous ALS algorithm and facing the issue of coping with big data structures. We will introduce a new way of handle data, through spark dataframes.
