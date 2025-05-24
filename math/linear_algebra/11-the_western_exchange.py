#!/usr/bin/env python3
""" function that transposes a matrix using NumPy """


def np_transpose(matrix):
    """ function that transposes a matrix using NumPy """
    return list(map(list, zip(*matrix)))
