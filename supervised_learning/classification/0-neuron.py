#!/usr/bin/env python3
""" class that defines a single neuron performing
binary classification """
import numpy as np


class Neuron:
    """
    class that defines a single neuron performing
    binary classification """
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
