# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 02:05:48 2023

@author: Davis
"""

import numpy as np

def piEstimator(n):
    ret = 0
    for k in range(1,n):
            numerator = (-1)**(k+1)
            denominator = 2*k-1
            ret += numerator / denominator
    ret = ret*4
    error = abs(np.pi - ret) / np.pi
    return ret, error*100