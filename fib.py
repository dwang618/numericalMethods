# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 03:25:30 2023

@author: Davis (using ChatGPT tool)
Prompt: Create an algorithm that produces the nth value of the fibonacci sequence in python 
starting with series 0,1 and then proceeded with series F(n) = f(n-1) + f(n-2)...
"""

def fib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


    
    