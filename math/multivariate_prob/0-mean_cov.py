#!/usr/bin/env python3
""" calculates the mean and covariance of a data set """
import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set X.
    """
    # Input validation
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate mean
    mean = np.mean(X, axis=0, keepdims=True)  # shape (1, d)

    # Center data
    X_centered = X - mean

    # Compute covariance matrix
    cov = (X_centered.T @ X_centered) / (n - 1)  # shape (d, d)

    return mean, cov
