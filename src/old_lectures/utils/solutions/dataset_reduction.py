"""Solution module for the dataset reduction exercise."""

""" 
    What This Solution Does
    Filters out movies with fewer than 50 ratings
    Filters out users who rated fewer than 20 movies
    Compares dataset size before and after reduction
    Plots rating distributions to check if the dataset remains representative
    This method removes sparsity while keeping useful data, making it more efficient for training recommenders.
"""

import pandas as pd

# Load the dataset (MovieLens 100K)
ratings = pd.read_csv(
    "ml-100k/u.data", sep="\t", names=["UserId", "MovieId", "Rating", "Timestamp"]
)

# Step 1: Count how many ratings each movie received
movie_counts = ratings.groupby("MovieId").size()

# Step 2: Count how many ratings each user gave
user_counts = ratings.groupby("UserId").size()

# Step 3: Apply filters
min_movie_ratings = 50  # Keep movies with at least 50 ratings
min_user_ratings = 20  # Keep users who rated at least 20 movies

filtered_ratings = ratings[
    (ratings["MovieId"].isin(movie_counts[movie_counts >= min_movie_ratings].index))
    & (ratings["UserId"].isin(user_counts[user_counts >= min_user_ratings].index))
]

# Step 4: Compare dataset sizes before and after reduction
print(f"Original dataset size: {ratings.shape[0]}")
print(f"Reduced dataset size: {filtered_ratings.shape[0]}")
print(
    f"Reduction percentage: {(1 - filtered_ratings.shape[0] / ratings.shape[0]) * 100:.2f}%"
)

# Step 5: Show distribution of ratings before and after reduction
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.hist(ratings["Rating"], bins=5, alpha=0.5, label="Original", density=True)
plt.hist(filtered_ratings["Rating"], bins=5, alpha=0.5, label="Reduced", density=True)
plt.legend()
plt.xlabel("Rating")
plt.ylabel("Density")
plt.title("Distribution of Ratings Before and After Reduction")
plt.show()
