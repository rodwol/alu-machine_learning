#!/usr/bin/env python3
""" class Binomial that represents a binomial distribution """


class Binomial:
    """Represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the binomial distribution """
        if data is None:
            if not isinstance(n, int) or n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p = 1 - (variance / mean)
            n = round(mean / p)
            p = mean / n

            self.n = n
            self.p = p

    def _comb(self, n, k):
        """Calculates combination n choose k without using math.comb"""
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        k = min(k, n - k)  # symmetry property
        c = 1
        for i in range(k):
            c = c * (n - i) // (i + 1)
        return c

    def pmf(self, k):
        """ calculates the pmf """
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        nCk = self._comb(self.n, k)
        return nCk * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """ calculates the cdf """
        k = int(k)
        if k < 0:
            return 0
        if k >= self.n:
            k = self.n
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
