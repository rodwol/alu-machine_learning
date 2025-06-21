#!/usr/bin/env python3
""" class Normal that represents a normal distribution """


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
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        return z * self.stddev + self.mean

    def pdf(self, x):
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        coeff = 1 / (self.stddev * self._sqrt(2 * self._pi()))
        return coeff * self._exp(exponent)

    def cdf(self, x):
        z = (x - self.mean) / (self.stddev * self._sqrt(2))
        return 0.5 * (1 + self._erf(z))

    def _sqrt(self, x, eps=1e-10):
        """Compute square root using the Babylonian method"""
        if x < 0:
            raise ValueError("Cannot compute sqrt of negative number")
        guess = x
        if guess == 0:
            return 0.0
        while True:
            next_guess = 0.5 * (guess + x / guess)
            if abs(next_guess - guess) < eps:
                return next_guess
            guess = next_guess

    def _exp(self, x, terms=20):
        """Approximate exp(x) using Taylor series"""
        result = 1.0
        numerator = 1.0
        denominator = 1.0
        for i in range(1, terms):
            numerator *= x
            denominator *= i
            result += numerator / denominator
        return result

    def _pi(self):
        """Return an approximation of pi"""
        pi_approx = 0.0
        for k in range(1000):
            pi_approx += ((-1) ** k) / (2 * k + 1)
        return 4 * pi_approx

    def _erf(self, x):
        """Approximate error function"""
        # constants
        a1 =  0.254829592
        a2 = -0.284496736
        a3 =  1.421413741
        a4 = -1.453152027
        a5 =  1.061405429
        p  =  0.3275911

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        t = 1.0 / (1.0 + p * x)
        y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2)\
            * t + a1) * t * self._exp(-x * x)

        return sign * y
