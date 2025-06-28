#!/usr/bin/env python3
""" calculates a correlation matrix """
import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix from a covariance matrix.
    """
    # Input validation
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Standard deviations on the diagonal
    std_dev = np.sqrt(np.diag(C))  # shape (d,)

    # Avoid division by zero
    if np.any(std_dev == 0):
        raise ValueError("Covariance matrix has zero variance along "
                         "at least one dimension")

    # Outer product of standard deviations
    denom = np.outer(std_dev, std_dev)  # shape (d, d)

    # Element-wise division to compute correlation matrix
    corr_matrix = C / denom

    return corr_matrix
