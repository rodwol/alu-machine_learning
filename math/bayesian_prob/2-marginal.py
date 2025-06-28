#!/usr/bin/env python3
""" calculates the marginal probability of obtaining the data """
import numpy as np


def likelihood(x, n, P):
    """
    Helper function to calculate the likelihood of observing x successes
    in n trials given an array of hypothetical probabilities P.
    """
    def factorial(k):
        return np.math.factorial(k)

    binom_coeff = factorial(n) / (factorial(x) * factorial(n - x))
    return binom_coeff * (P ** x) * ((1 - P) ** (n - x))


def marginal(x, n, P, Pr):
    """
    Calculates the marginal probability of obtaining the data (x and n)
    across the various hypothetical probabilities weighted by prior beliefs
    """
    # Input validations
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater "
                         "than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Compute likelihood
    L = likelihood(x, n, P)

    # Marginal = sum of likelihood * prior
    return np.sum(L * Pr)
