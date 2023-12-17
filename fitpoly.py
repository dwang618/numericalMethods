# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 02:05:38 2023

@author: Davis
"""

# fitpoly.py
#using chatgpt; used prompt:
#Write a Python function fitpoly(x, y, order) that takes two arrays x and y representing 
#input data points and their corresponding output values, and an integer order representing 
#the degree of the polynomial. Implement the function to fit a polynomial of the specified 
#order to the data using the method of least squares. Return the coefficients of the fitted 
#polynomial and the sum of squared errors 

#Returned output with code extended below
#Combined the creation of the Vandermonde matrix and calculation of coefficients in a 
#single line. Eliminated the intermediate variable y_fit and directly used it in the sum 
#of squared errors calculation.
import numpy as np

def fitpoly(x,y,order):
    # Create the Vandermonde matrix and calculate the coefficients
    X = np.column_stack([x**i for i in range(order + 1)])
    A = np.linalg.inv(X.T @ X) @ X.T @ y

    # Calculate the fitted values, sum of squared errors, and return
    return A, np.sum((y - X @ A)**2)