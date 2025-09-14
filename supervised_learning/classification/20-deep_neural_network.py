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

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network
        """
        self.__cache['A0'] = X
        A_prev = X

        for l in range(1, self.__L + 1):
            W = self.__weights['W' + str(l)]
            b = self.__weights['b' + str(l)]

            Z = np.matmul(W, A_prev) + b
            A = 1 / (1 + np.exp(-Z))  # Sigmoid activation
            self.__cache['A' + str(l)] = A
            A_prev = A

        return A, self.__cache

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        """
        m = Y.shape[1]
        cost = - (1 / m) * np.sum(
            Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        )
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neural network's predictions
        """
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost
