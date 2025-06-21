#!/usr/bin/env python3
""" class Normal that represents a normal distribution """
import math


class Normal:
    """Represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the normal distribution """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        coeff = 1 / (self.stddev * math.sqrt(2 * math.pi))
        return coeff * math.exp(exponent)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""
        z = (x - self.mean) / (self.stddev * math.sqrt(2))
        return 0.5 * (1 + math.erf(z))
