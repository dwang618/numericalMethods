# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 02:21:34 2023

@author: Davis
"""

import numpy as np

def piEstimatorTrue(tolerance):
    error = tolerance + 1
    k = 1
    ret = 0
    
    while error > tolerance:
        numerator = (-1) ** (k + 1)
        denominator = 2 * k - 1
        ret += numerator / denominator
        k += 1

        estimate = ret * 4
        
        error = abs(np.pi - estimate) / np.pi * 100

    return ret * 4, error


