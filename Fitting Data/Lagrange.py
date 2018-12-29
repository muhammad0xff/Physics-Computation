# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:58:40 2018

@author: USER
"""

import numpy as np
import sys
import sympy as sym

def KoefLagrange(datax,datay):
    # mencari koef interpolasi Lagrange
    if len(datax) != len(datay):
        sys.exit('data x dan data y tidak sama')
    
    n = len(datax)
    d = np.ones(n)
    c = np.ones(n)
    for j in range(n):
        for k in range(n):
            if k!= j:
                d[j] *= (datax[j] - datax[k])
            c[j] = datay[j] / d[j]
    return c

def HitungLagrange(datax,c,xx):
    n = len(datax)
    m = len(xx)
    p = np.zeros(m)
    t = np.zeros(n)
    for i in range(m):
        for j in range(n):
            t[j] = 1
            for k in range(n):
                if j != k:
                    t[j] *= (xx[i] - datax[k])
            p[i] += t[j]*c[j]
    return p

def PoliLagrange(datax,c):
    n = len(datax)
    x = sym.symbols('X')
    P = 0
    for j in range(n):
        t = 1
        for k in range(n):
            if j != k:
                t *= (x-datax[k])
        P += c[j]*t
    return (sym.cancel(P)).evalf(n=4)