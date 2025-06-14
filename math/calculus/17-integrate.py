#!/usr/bin/env python3
""" function that calculates integral of polynomial """


def poly_integral(poly, C=0):
    """ function that calculates integral of polynomial """
    if not isinstance(poly, list) or not isinstance(C, int):
        return None
    if not poly:
        return None

    integral = []
    integral.append(C)

    for power, coeff in enumerate(poly):
        new_power = power + 1
        if coeff == 0:
            new_coeff = 0
        else:
            new_coeff = coeff / new_power
            if new_coeff.is_integer():
                new_coeff = int(new_coeff)
        integral.append(new_coeff)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
