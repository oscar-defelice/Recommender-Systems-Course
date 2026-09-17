import numpy as np
from utils.non_pers_rec import get_recent_liked_movie as correct_like_fn
from utils.non_pers_rec import get_genre as correct_genre_fn


def test_get_recent_liked_movie(target):
    usr_test = 3
    a = target(usr_test)
    atf = correct_like_fn(usr_test)

    assert a == atf, f"Wrong values. Expected {atf}, got {a}"

    usr_test = 74
    a = target(usr_test)
    atf = correct_like_fn(usr_test)

    assert a == atf, f"Wrong values. Expected {atf}, got {a}"

    print("\033[92m All tests passed.")


def test_get_movie_genre(target):
    usr_test = 2
    a = target(usr_test)
    atf = correct_genre_fn(usr_test)

    assert isinstance(a, list), f"Wrong type. Expected list, got {type(a)}"
    assert a == atf, f"Wrong values. Expected {atf}, got {a}"

    print("\033[92m All tests passed.")
