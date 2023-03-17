import numpy as np
import pandas as pd
from typing import Tuple


def normalizeRatings(Y: np.ndarray, R: np.ndarray, axis: int = 1) -> Tuple:
    """
    Preprocess data by subtracting mean rating for every movie (every row).
    Only include real ratings: R(i,j)=1.

    [Ynorm, Ymean] = normalizeRatings(Y, R) normalized Y so that each movie
    has a rating of 0 on average. Unrated moves then have a mean rating (0)
    Returns the mean rating in Ymean.

    Parameters
    ----------
    Y : np.ndarray
        The rating array to normalise.
    R : np.ndarray
        The array indicating whether a user rated a movie.
    axis : int
        The numpy axis to use for taking the average rating.

    Returns
    -------
    Tuple
        The normalised array of ratings and the mean rating.

    """
    Ymean = (np.sum(Y * R, axis=axis) / (np.sum(R, axis=axis) + 1e-12)).reshape(-1, 1)

    if axis == 0:
        Ynorm = Y.T - np.multiply(Ymean, R.T)
    else:
        Y_norm = Y - np.multiply(Y_mean, R)

    return (Ynorm, Ymean)


def minmaxNormalise(Y: np.ndarray) -> Tuple:
    """Preprocess data by normalising rating for every movie (every row).
    It rescale ratings in the range [0,1]

    Parameters
    ----------
    Y : np.ndarray
        The rating array to normalise.

    Returns
    -------
    Tuple
        The normalised array of ratings and the max rating.
    """
    Y_scaled = Y / Y.max()
    return Y_scaled, Y.max()


def load_precalc_params_small() -> Tuple:
    file = open("../data/small_movies_X.csv", "rb")
    X = np.loadtxt(file, delimiter=",")

    file = open("../data/small_movies_W.csv", "rb")
    W = np.loadtxt(file, delimiter=",")

    file = open("../data/small_movies_b.csv", "rb")
    b = np.loadtxt(file, delimiter=",")
    b = b.reshape(1, -1)
    num_movies, num_features = X.shape
    num_users, _ = W.shape
    return (X, W, b, num_movies, num_features, num_users)


def load_ratings_small() -> Tuple:
    file = open("../data/small_movies_Y.csv", "rb")
    Y = np.loadtxt(file, delimiter=",")

    file = open("../data/small_movies_R.csv", "rb")
    R = np.loadtxt(file, delimiter=",")
    return (Y, R)


def load_Movie_List_pd() -> Tuple[list, pd.DataFrame]:
    """returns df with and index of movies in the order they are in in the Y matrix"""
    df = pd.read_csv(
        "../data/small_movie_list.csv",
        header=0,
        index_col=0,
        delimiter=",",
        quotechar='"',
    )
    mlist = df["title"].to_list()
    return (mlist, df)
