# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 03:27:09 2023

@author: Davis
"""
#used chatgpt agent 9/19
#prompt; "Generate a Python function called multiTrapezoidal that takes two input arrays x and y as arguments. 
#Implement the trapezoidal rule to calculate the integral of a function represented by x and y. 
#The function should return the calculated integral value."
import numpy as np

def multiTrapezoidal(x, y):
    n = len(x)
    I = 0
    for i in range(1, n):
        I += (y[i-1] + y[i]) * (x[i] - x[i-1]) / 2
    return I