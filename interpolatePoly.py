# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:49:58 2023

@author: Davis
"""

# interpolatePoly.py
import numpy as np
def interpolatePoly(x,y,xi):
    matrix = np.vander(x, increasing=True)
    A = np.linalg.solve(matrix, y)
    revA = A[::-1]
    yi = np.polyval(revA, xi)
    return yi, A
