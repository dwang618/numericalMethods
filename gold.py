# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 06:29:45 2023

@author: Davis
"""
#chatgpt - 10/31: Prompt - Implement the Golden Section Search algorithm in Python. 
#The Golden Section Search is used to find the local minimum of a function within a 
#specified interval with a given relative tolerance. The algorithm should take the 
#following parameters: f, the function for which you want to find the local minimum, xL. 
#rhe lower bound of the interval, xU, the upper bound of the interval, reltol, the relative 
#tolerance. your function should return the value of x that corresponds to the local minimum 
#of the function f within the interval [xL, xU] with a relative tolerance not exceeding reltol.
#use the function signature def gold(myfunc, xL, xU, reltol): 
# gold.py
# implements golden section search
import numpy as np
def gold(myfunc,xL,xU,reltol):
    phi = (5 ** 0.5 -1) / 2
    x1, x2 = xL + ((xU - xL) * phi), xU - ((xU - xL) * phi)
    f1, f2 = myfunc(x1), myfunc(x2)  

    while (1-phi)*abs((xU - xL)/max(x1,x2))*100 > reltol:
        if f1 < f2:
           xU, x1, f1 = x1, x2, f2 
           x2 = xU - ((xU - xL) * phi)
           f2 = myfunc(x2)
          
        else:
            xL, x2, f2 = x2, x1, f1
            x1 = xL + ((xU - xL) * phi)
            f1, f2 = myfunc(x1), myfunc(x2)            
    return x1 if f1 > f2 else x2
 
