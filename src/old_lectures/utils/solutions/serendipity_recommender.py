"""Solution script for serendipity recommender"""

import pandas as pd

# Load datasets
df_ratings = pd.read_csv("ratings.csv")  # Ensure this file is in the working directory
df_movies = pd.read_csv("movies.csv", index_col="MovieId")  # MovieId as index

# Step 1: Compute Movie Popularity (Number of Ratings)
movie_popularity = df_ratings.groupby("MovieId").size().reset_index(name="NumRatings")

# Step 2: Compute Average Rating for Each Movie
movie_avg_rating = (
    df_ratings.groupby("MovieId")["Rating"].mean().reset_index(name="AvgRating")
)

# Step 3: Merge Popularity and Ratings with Movie Titles
movies_stats = movie_popularity.merge(movie_avg_rating, on="MovieId")
movies_stats = movies_stats.merge(
    df_movies[["Title"]], left_on="MovieId", right_index=True
)

# Step 4: Define Serendipity Criteria
# Popular Movies: High number of ratings (e.g., top 10% most rated)
popularity_threshold = movies_stats["NumRatings"].quantile(0.90)
popular_movies = movies_stats[movies_stats["NumRatings"] >= popularity_threshold]

# Hidden Gems: High rating but low number of ratings (e.g., bottom 50% in popularity)
hidden_gems = movies_stats[
    (movies_stats["NumRatings"] <= movies_stats["NumRatings"].median())
    & (movies_stats["AvgRating"] >= movies_stats["AvgRating"].quantile(0.75))
]

# Step 5: Mix Popular and Serendipitous Movies
num_recommendations = 10  # Set the number of final recommendations
popular_sample = popular_movies.sample(
    min(len(popular_movies), num_recommendations // 2)
)
hidden_gems_sample = hidden_gems.sample(min(len(hidden_gems), num_recommendations // 2))

serendipity_recommendations = (
    pd.concat([popular_sample, hidden_gems_sample])
    .sample(frac=1)
    .reset_index(drop=True)
)

# Step 6: Display Recommendations
print("🎬 Serendipity-Based Movie Recommendations 🎬")
print(serendipity_recommendations[["Title", "NumRatings", "AvgRating"]])
