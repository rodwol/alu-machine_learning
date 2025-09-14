#!/usr/bin/env python3
"""
Deep Neural Network class for binary classification
"""
import numpy as np


class DeepNeuralNetwork:
    """Defines a deep neural network performing binary classification"""

    def __init__(self, nx, layers):
        """
        Constructor for DeepNeuralNetwork
        """

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        if not all(isinstance(x, int) and x > 0 for x in layers):
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for l in range(1, self.L + 1):
            if l == 1:
                self.weights['W1'] = np.random.randn(layers[l - 1], nx) * \
                                     np.sqrt(2 / nx)
            else:
                self.weights['W' + str(l)] = np.random.randn(
                    layers[l - 1], layers[l - 2]) * np.sqrt(2 / layers[l - 2])

            self.weights['b' + str(l)] = np.zeros((layers[l - 1], 1))

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights
