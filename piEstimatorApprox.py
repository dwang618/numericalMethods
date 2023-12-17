# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 02:51:42 2023

@author: Davis
"""

def piEstimatorApprox(tolerance):
    estimate = 0
    relError = tolerance+1
    k = 1 
    copy = 0
    count = 0
    start = True

    while relError > tolerance:
        numerator = (-1) ** (k + 1)
        denominator = 2 * k - 1
        count += numerator / denominator
        estimate = count * 4
        k += 1
        
        if not start:
            relError = abs((estimate - copy) / estimate) * 100
    
        copy = estimate
        start = False
    return estimate, relError
        