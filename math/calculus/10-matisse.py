#!/usr/bin/env python3
""" function that calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ function that calculates the derivative of a polynomial """
    if not isinstance(poly, list) or not all(isinstance(c, int, float)) for c in poly):
        return None

    if len(poly) <= 1:
        return [0]

    derivative = [poly[i]* i for i in range(1, len(poly))]
    if all(c == 0 for c in derivative):
        return [0]

    return derivative
