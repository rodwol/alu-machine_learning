#!/usr/bin/env python3
""" Gaussian Process """
import numpy as np


class GaussianProcess:
    """
    Gaussian Process class.
    """
    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        Initialize the GaussianProcess class.
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)  # Initial covariance matrix

    def kernel(self, X1, X2):
        """
        Calculate the covariance kernel matrix
        between two matrices
        using RBF kernel
        """
        # Compute the squared distances between each pair of points
        a = np.sum(X1**2, 1).reshape(-1, 1)
        b = np.sum(X2**2, 1)
        c = np.dot(X1, X2.T)
        sqdist = a + b - 2 * c
        # Compute the covariance kernel matrix using the RBF kernel formula
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)
    