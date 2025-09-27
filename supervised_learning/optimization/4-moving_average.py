#!/usr/bin/env python3
"""
calculates the weighted moving average of a data set
with bias correction
"""
import numpy as np


def moving_average(data, beta):
    """Calculate the weighted moving average of a
    data set with bias correction.

    Args:
        data (list): List of data points.
        beta (float): Weighting factor between 0 and 1.
    """
    v = 0
    moving_averages = []
    for x in range(len(data)):
        v = beta * v + (1 - beta) * data[x]
        v_corrected = 1 - (beta ** (x + 1))
        moving_averages.append(v / v_corrected)
    return moving_averages
