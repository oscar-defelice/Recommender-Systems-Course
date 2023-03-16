"""Exceptions module to collect user-defined exception classes"""


class Error(Exception):
    """Base class for other exceptions."""

    pass


class NotFittedError(Error):
    """Raised when the model has not been fitted."""

    pass
