# Project Assignment: Movie Pairing Recommender System

## Objective

Develop a recommender system that pairs two movies based on complementary genres, themes, or viewer preferences, similar to the concept used on [Date Night Movies](https://datenightmovies.com/spider-man-no-way-home+mona-lisa-smile).

## Dataset

You can use the following datasets:

- **MovieLens Dataset**: [MovieLens](https://grouplens.org/datasets/movielens/)
- **IMDb Dataset**: [IMDb Datasets](https://www.imdb.com/interfaces/)

## Tasks

1. **Data Collection and Preprocessing**
   - Download the MovieLens and IMDb datasets.
   - Merge datasets to include movie ratings, genres, and metadata.

2. **Feature Engineering**
   - Extract relevant features, you can choose the basic ones or create composite ones. A few examples are genres, directors, cast, and ratings.
   - Create a user-item interaction matrix for collaborative filtering.
   - Understand how to combine user data to get data for the couple of users.

3. **Model Development**
   - Implement a recommender system algorithm (e.g., matrix factorization) to predict the rating of a movie by a couple of users.

4. **Recommendation Algorithm**
   - Develop an algorithm to suggest one movie that might be liked by the couple of users. You can use the criteria you prefer to create a "couple score" for each movie and then sort the movies by the score.

5. **Evaluation**
   - Split the data into training and testing sets.
   - Evaluate the model, choose the metric you prefer.

**Important note**: There are quite few free choices in the project. This is intentional, it is expected the different developers might have different approaches. The important thing is to *always* be able to explain your approach and why you chose the specific tools/frameworks/methodologies.

## Deliverables

- **Code**: Well-documented code in a GitHub repository. I expect for each of you a *link* to a GitHub repository.
- **Report**: A detailed report explaining the methodology, experiments, results, and conclusions. (This can be included in the GitHub repository README.md)

## Evaluation Criteria

- **Functionality**: Does the system provide relevant and complementary movie recommendations?
- **Accuracy**: How well does the system perform in terms of the chose metric? Was the metric a good measure of the quality of the recommendations?
- **Documentation**: Quality and clarity of the code documentation and report.

This project will give you practical experience in building a real-world recommender system, integrating data from multiple sources. Good luck!
