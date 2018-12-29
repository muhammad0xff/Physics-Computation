# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 10:27:45 2018

@author: USER
"""

def htgNewton(dataX, a, xx):
    n = len(dataX) - 1
    p = a[n]
    for k in range(1, n+1):
        p = a[n-k] + (xx - dataX[n-k])*p
    return p

def koefNewton(dataX, dataY):
    import sys
    if len(dataX) != len(dataY):
        sys.exit('data x dan data y tidak sama')
    m = len(dataX)
    a = dataY.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(dataX[k:m] - dataX[k-1])
    return a

def poliNewton(dataX,a):
    import sympy as sym
    x = sym.symbols('x')
    n = len(dataX) - 1
    p = a[n]
    for k in range(1, n+1):
        p = a[n-k] + (x - dataX[n-k])*p
    return sym.cancel(p).evalf(n=4)