# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 03:14:28 2023

@author: Davis
"""

import numpy as np

def forwardDividedDifference(f,h):
    length = len(f)
    ret = []
    for x in range(length-1):
        ret.append((f[x+1] - f[x])/h)
    return ret