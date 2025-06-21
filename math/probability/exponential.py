#!/usr/bin/env python3
""" class Exponential that represents an exponential distribution """


class Exponential:
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Initializes the Exponential distribution """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            self.lambtha = 1 / mean

    def pdf(self, x):
        if x < 0:
            return 0
        return self.lambtha * self._exp(-self.lambtha * x)

    def cdf(self, x):
        if x < 0:
            return 0
        return 1 - self._exp(-self.lambtha * x)

    def _exp(self, x, terms=20):
        """Approximate exp(x) using Taylor series expansion"""
        result = 1.0
        numerator = 1.0
        denominator = 1.0
        for i in range(1, terms):
            numerator *= x
            denominator *= i
            result += numerator / denominator
        return result
