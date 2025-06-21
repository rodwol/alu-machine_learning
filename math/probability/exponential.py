#!/usr/bin/env python3
""" class Exponential that represents an exponential distribution """
import math


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
        """Calculates the PDF at a given time period x"""
        if x < 0:
            return 0
        return self.lambtha * math.exp(-self.lambtha * x)

    def cdf(self, x):
        """Calculates the CDF at a given time period x"""
        if x < 0:
            return 0
        return 1 - math.exp(-self.lambtha * x)
