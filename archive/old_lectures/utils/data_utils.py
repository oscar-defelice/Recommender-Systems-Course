import numpy as np
import pandas as pd


def load_data():
    df_rating = pd.read_csv(
        "http://files.grouplens.org/datasets/movielens/ml-100k/u1.base",
        sep="\t",
        engine="python",
        header=None,
    )
    df_rating.columns = ["UserId", "MovieId", "Rating", "Timestamp"]
    df_rating_test = pd.read_csv(
        "http://files.grouplens.org/datasets/movielens/ml-100k/u1.test",
        sep="\t",
        engine="python",
        header=None,
    )

    df_users = pd.read_csv(
        "http://files.grouplens.org/datasets/movielens/ml-100k/u.user",
        sep="|",
        engine="python",
        header=None,
    )
    df_users.columns = ["UserId", "Age", "Gender", "Occupation", "ZipCode"]
    df_users.set_index("UserId", inplace=True)
    df_items = pd.read_csv(
        "http://files.grouplens.org/datasets/movielens/ml-100k/u.item",
        sep="|",
        engine="python",
        encoding="ISO-8859-1",
        header=None,
    )
    df_items.columns = [
        "MovieId",
        "Title",
        "Date",
        "VideoReleaseDate",
        "Url",
        "unknown",
        "Action",
        "Adventure",
        "Animation",
        "Children",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ]
    df_items.set_index("MovieId", inplace=True)

    # Pivot rating table in order to get rating matrix
    df_matrix = df_rating.pivot(index="MovieId", columns="UserId", values="Rating")

    n_users = len(df_users)
    n_items = len(df_items)

    return df_rating, df_rating_test, df_users, df_items, df_matrix, n_users, n_items
