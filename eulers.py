# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 23:39:31 2023

@author: Davis
"""
#using chatgpt; used prompt:
#create a python function that performs eulers method when given parameters for an ode 
#function, the interval of the method denoted as tspan, the initial point denoted as y0, 
#and the step size denoted as h.  use this template: import numpy as np
#def eulers(ODEfunc,tspan,y0,h):
#    return t,y     it should pass this test #%%
#def ODEfuncSingle(t,y): return -0.5*y
#tspan = np.array([0, 10])
#y0 = [10]
#h = 0.1
#t, y = eulers(ODEfuncSingle,tspan,y0,h)
#plt.plot(t,y.T)
#assert(np.abs(y.T[-1]- 0.05920529)<1e-4)
#print('Test 1 completed') 

# eulers.py
import numpy as np

def eulers(ODEfunc, tspan, y0, h):
    """
    Euler's method for solving ordinary differential equations (ODEs).

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

    # Perform Euler's method
    for i in range(1, len(t)):
        y[:, i] = y[:, i - 1] + h * ODEfunc(t[i - 1], y[:, i - 1])

    return t, y
