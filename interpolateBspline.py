# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:04:21 2023

@author: Davis
"""
#ChatGPT: Prompt - write a Python function that performs linear interpolation for a 
#given list of data points. The function should take three arguments; x, a list of 
#x-values; y, a list of corresponding y-values; and xi - a list of points at which to 
#perform interpolation. make sure that the function handles cases where the interpolation 
#points may fall outside the range defined by the x-values. the function should return a 
#list of interpolated y-values for each point in xi
def interpolateBspline(x,y,xi):
    A = y  
    yi = []

    for point in xi:
        # Check if the point falls within the range defined by x[0] and x[-1]
        if point == x[-1] or x[0] <= point <= x[-1]:
            # Find the index where x[idx] is the smallest value greater than or equal to the current point
            idx = 0
            while x[idx] < point:
                idx += 1

            if x[idx] == point:
                # If the point matches an x-value exactly, append the corresponding y-value
                yi.append(y[idx])
            else:
                # Perform linear interpolation
                x0, x1 = x[idx - 1], x[idx]
                y0, y1 = y[idx - 1], y[idx]
                interpolated_value = y0 + (point - x0) * (y1 - y0) / (x1 - x0)
                yi.append(interpolated_value)
    return yi, A
