    # -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 03:29:06 2023

@author: Davis
"""
#using chatGPT: prompt - Write a Python function bisection that implements the 
#bisection method for finding the root of a given function. The function should 
#take the following arguments: myfunc (the function to find the root of), 
#xl (the lower bound of the interval), xu (the upper bound of the interval), 
#and reltol (the relative tolerance for convergence). The function should 
#return the estimated root given that its relative error does not exceed its tolerance.
# bisection.py
def bisection(myfunc, xl, xu, reltol):
    while True:
        xr = (xl + xu) / 2
        ea = abs((xr - xl) / xr) * 100
        if ea < reltol:
            return xr
        if myfunc(xl) * myfunc(xr) < 0:
            xu = xr
        else:
            xl = xr

