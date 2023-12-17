# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 23:50:10 2023

@author: Davis
"""
#using chatgpt; used prompt:
#create a python function that performs a 4th order runge-kutta method that solves both 
#singular ODEs and a system of ODEs, given the same parameters of the previous function. 
#it should follow this template # rungekutta4.py
#import numpy as np
#def rungakutta4(ODEfunc,tspan,y0,h):
#return t,y   the formatting follows this setup   def ODEfuncSingle(t,y): return  -0.5*y
#tspan = np.array([0, 10])
#y0 = [10]
#h = 0.1
#t, y = rungakutta4(ODEfuncSingle,tspan,y0,h)
#plt.plot(t,y.T)
#assert(np.abs(y.T[-1]- 0.06737949)<1e-4)
#print('Test 1 completed')
#rungakutta4.py
import numpy as np
def rungekutta4(ODEfunc, tspan, y0, h):
    """
    4th Order Runge-Kutta method for solving ordinary differential equations (ODEs).

    Parameters:
        ODEfunc (function): The ODE function to solve.
        tspan (numpy array): Time span [t_initial, t_final].
        y0 (numpy array): Initial value(s) for the dependent variable(s).
        h (float): Step size.

    Returns:
        t (numpy array): Time points.
        y (numpy array): Corresponding values of the dependent variable.
    """
    # Initialize arrays to store time points and solution values
    t = np.arange(tspan[0], tspan[1] + h, h)
    y = np.zeros((len(y0), len(t)))

    # Set initial values
    y[:, 0] = y0

    # Perform 4th Order Runge-Kutta method
    for i in range(1, len(t)):
        k1 = h * ODEfunc(t[i - 1], y[:, i - 1])
        k2 = h * ODEfunc(t[i - 1] + 0.5 * h, y[:, i - 1] + 0.5 * k1)
        k3 = h * ODEfunc(t[i - 1] + 0.5 * h, y[:, i - 1] + 0.5 * k2)
        k4 = h * ODEfunc(t[i - 1] + h, y[:, i - 1] + k3)

        y[:, i] = y[:, i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, y