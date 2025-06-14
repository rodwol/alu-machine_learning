#!/usr/bin/env python3
""" function that calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ function that calculates the derivative of a polynomial """
    if not isinstance(poly, list):
        return None
    if not poly:
        return None

    derivative = []
    for power in range(1, len(poly)):
        derivative.append(power * poly[power])
    if not derivative:
        return [0]

    return derivative
