# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:06:43 2023

@author: Davis
"""
import math as m
import numpy as np
def linInterp(n1, n2):
        x0=n1
        x1=n2
        yCol = np.array([[m.exp(x0*-3)],[m.exp(x1*-3)]])
        T = np.array([[1,x0],[1,x1]])
        a1a2 = np.linalg.solve(T, yCol)
        print(a1a2)
def quadInterp(n1, n2, n3):
    x0=n1
    x1=n2
    x2 =n3
    yCol = np.array([[m.exp(x0*-3)],[m.exp(x1*-3)],[m.exp(x2*-3)]])
    T = np.array([[1,x0, x0*x0],[1,x1,x1*x1],[1,x2,x2*x2]])
    a1a2a3 = np.linalg.solve(T, yCol)
    print(a1a2a3)
        

        
