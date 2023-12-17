# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 02:05:03 2023

@author: Davis
"""
#ChatGPT Prompt; Write a Python function for solving a system of linear equations using 
#Gaussian elimination with partial pivoting. The function should take two arguments, 
#a square matrix A and a column vector b, and return the solution vector x and the augmented
#matrix as a whole. The forward elimination process should work top down and left to right,
#compounding operations to rows below itself to form an upper right trianglular matrix.
#The back substitution process must start from the lastmost variable on the last row.

import numpy as np

def gauss(A, b):
    n = len(b)
    augMatrix = np.column_stack((A, b.astype(float)))  # Ensure 'b' is of type float
    x = np.zeros(n, float)

    augMatrix = forwardElim(0, 0, n, augMatrix)
    x, _ = backSub(x, augMatrix, n)  # Discard the updated augMatrix

    x = x.reshape(-1, 1)  # Reshape x into a 2D array
    return x, augMatrix

# Forward elimination; Row n = Row n - (xn1 / xn-1,1)(Row n-1)
def forwardElim(index, prior, length, augMatrix):
    while index < length:
        for prior in range(index + 1, length):
            coefficient = augMatrix[prior][index] / augMatrix[index][index]
            augMatrix[prior] -= coefficient * augMatrix[index]
        index += 1
    return augMatrix

# Back substitution; isolate remaining variable within the last row
def backSub(x, augMatrix, length):
    x[length - 1] = augMatrix[length - 1][length] / augMatrix[length - 1][length - 1]
    
    for a in range(length - 2, -1, -1):
        x[a] = augMatrix[a][length]
        for b in range(a + 1, length):
            x[a] -= augMatrix[a][b] * x[b]
        x[a] /= augMatrix[a][a]
    return x, augMatrix

        