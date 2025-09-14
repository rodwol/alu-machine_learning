#!/usr/bin/env python3
"""
class Neuron that defines a single neuron performing binary classification
"""
import numpy as np


class Neuron:
    """Class that defines a single neuron performing binary classification"""

    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)  # Weights
        self.__b = 0                       # Bias
        self.__A = 0                       # Activated output

    # Getter methods
    @property
    def W(self):
        """Getter for weights"""
        return self.__W

    @property
    def b(self):
        """Getter for bias"""
        return self.__b

    @property
    def A(self):
        """Getter for activated output"""
        return self.__A

    def forward_prop(self, X):
        """ Calculates forward propagation of the neuron """
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))  # Sigmoid activation
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        """
        m = Y.shape[1]
        cost = -(1 / m) * np.sum(
            Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        )
        return cost

    def evaluate(self, X, Y):
        """ Evaluates the neuron's predictions """
        A = self.forward_prop(X)  # forward propagation
        cost = self.cost(Y, A)    # compute cost
        prediction = np.where(A >= 0.5, 1, 0)  # threshold at 0.5
        return prediction, cost
