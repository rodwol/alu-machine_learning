#!/usr/bin/env python3
""" class that represents a Multivariate Normal distribution """
import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Initializes the distribution with mean and covariance from the dataset.
        """
        # Input validation
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Compute the mean: shape (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data
        data_centered = data - self.mean

        # Compute covariance matrix: shape (d, d)
        self.cov = (data_centered @ data_centered.T) / (n - 1)


    def pdf(self, x):
        """
        Calculates the PDF at a given data point x.
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        if x.shape != (self.d, 1):
            raise ValueError(f"x must have the shape ({self.d}, 1)")

        # Constants
        det_cov = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        diff = x - self.mean

        norm_const = 1.0 / np.sqrt((2 * np.pi) ** self.d * det_cov)
        exponent = -0.5 * (diff.T @ inv_cov @ diff)

        return float(norm_const * np.exp(exponent))
