#!/usr/bin/env python3
""" class Poisson that represents a poisson distribution """
import math


class Poisson:
    """ class Poisson that represents a poisson distribution """

    def __init__(self, data=None, lambtha=1.):
        """ initializes the poisson distribution """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the PMF for a given number of 'successes' k."""
        k = int(k)
        if k < 0:
            return 0

        e_term = math.exp(-self.lambtha)
        lambtha_power_k = self.lambtha ** k
        factorial_k = math.factorial(k)

        pmf_value = (e_term * lambtha_power_k) / factorial_k
        return pmf_value

    def cdf(self, k):
        """Calculates the CDF for a given number of 'successes' k."""
        k = int(k)
        if k < 0:
            return 0

        cdf_value = 0
        for i in range(0, k + 1):
            e_term = math.exp(-self.lambtha)
            lambtha_power_i = self.lambtha ** i
            factorial_i = math.factorial(i)
            cdf_value += (e_term * lambtha_power_i) / factorial_i

        return cdf_value
