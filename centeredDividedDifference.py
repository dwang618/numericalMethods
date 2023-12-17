# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 03:23:51 2023

@author: Davis
"""

import numpy as np

def centeredDividedDifference(f,h):
    length = len(f)
    ret = []
    for x in range(1,length-1):
        ret.append((f[x+1] - f[x-1]) / (2*h))
    return ret