#!/usr/bin/env python3
""" class Poisson that represents a poisson distribution """


class Poisson:
    """ class Poisson that represents a poisson distribution """
    def __init__(self, data=None, lam=1.):
    """ initializes the poisson distribution """
    if data is None:
        if lam <= 0:
            raise ValueError("Lambda must be a positive value")
        self.lam = float(lam)
    else:
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.lam = float(sum(data) / len(data))
