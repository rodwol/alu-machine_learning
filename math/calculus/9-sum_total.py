#!/usr/bin/env python3
""" fun that calculates the sum of squares from 1^2 to n^2"""


def summation_i_squared(n):
    """ fun that calculates the sum of squares from 1^2 to n^2 """
    if isinstance(n, int) and n >= 1:
        return n * (n+1) * (2*n+1) // 6
    return None
