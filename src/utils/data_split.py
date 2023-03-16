"""Module to handle data splitting"""

import numpy as np
import random
from typing import Tuple, Union


def split_ratings(
    ratings: np.ndarray, val_size: Union[float, int]
) -> Tuple[np.ndarray, np.ndarray]:
    """Function to create a validation set of ratings out of a sparse matrix

    Parameters
    ----------
    ratings : np.ndarray
        The matrix of ratings, can be sparse, full of zeros or nan values.
    val_size : float or int
        The size of the validation set.
        If float, the size is expressed in percentage of total size of the ratings array.
        if int, the size is expressed in raw number ratings in the validation set.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        The tuple of training and validation ratings.
    """
    # Get the couples of indices with significant values
    rows, cols = np.where(ratings > 0)
    val_ratings = np.zeros(ratings.shape)
    train_ratings = ratings.copy()

    if val_size < 1:  # Hence it is a percentage
        val_size = int(rows * val_size)

    val_ids = random.sample(range(len(rows)), val_size)

    for row, col in zip(rows[val_ids], cols[val_ids]):
        train_ratings[row, col] = 0
        val_ratings[row, col] = ratings[row, col]

    return train_ratings, val_ratings
