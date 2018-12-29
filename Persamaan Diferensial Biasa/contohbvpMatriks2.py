# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:21:52 2018

@author: USER
"""

import numpy as np
from NewtonRaphson2 import newtonRaphson2

def finDiff(y):
    fd = np.zeros(m+1)
    fd[0] = y[0]
    fd[m] = y[m] - 1.0
    for i in range(1,m):
        fd[i] = (y[i-1] - 2.0*y[i] + y[i+1]) - h*h*F(x[i],y[i],(y[i+1] - y[i-1])/(2.0*h))
    return fd

def F(x,y,dy):
    F = -3.0 * y * dy
    return F

def SolusiAwal(x):
    y = np.zeros(m+1)
    for i in range(m+1):
        y[i] = 0.5*x[i]
    return y

xi = 1.2
xf = 1.0
m = 10
h = (xf-xi)/m
x = np.arange(xi, xf+h, h)
y = newtonRaphson2(finDiff, SolusiAwal(x), akurasi= 1.0e-5)
print("\n       x                y")
for i in range(m+1):
    print("{:14.5f} {:14.5f}".format(x[i],y[i]))