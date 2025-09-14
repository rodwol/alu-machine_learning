#!/usr/bin/env python3
"""
Class that defines a single neuron performing binary classification
"""
import numpy as np


class Neuron:
    """
    Class that defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        if not nx isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ getter for weights"""
        return self.__W

    @property
    def b(self):
        """Getter for bias"""
        return self.__b

    @property
    def A(self):
        """Getter for activated output"""
        return self.__A
