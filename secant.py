# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 03:38:52 2023

@author: Davis
"""
#Usage of chatGPT: prompt - Write a Python function secant that implements 
#the secant method for finding the root of a given function. The function should 
#take the following arguments: myfunc (the function to find the root of), xr_old 
#(the initial guess for the root), xr (another initial guess for the root), and 
#reltol (the relative tolerance for convergence). The function should return the 
#estimated root given that its relative error falls within the defined tolerance.
#secant.py
def secant(myfunc,xr_old,xr,reltol):
    while(True):
        xr, xr_old = xr - (myfunc(xr) * (xr - xr_old)) / (myfunc(xr) - myfunc(xr_old)), xr
        ea = abs((xr - xr_old) / xr) * 100
        if ea < reltol:
            return xr
