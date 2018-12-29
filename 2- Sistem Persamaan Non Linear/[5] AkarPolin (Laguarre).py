# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:06:58 2018

@author: USER
"""
    
import math
import error
import numpy as np
import bayu_algebra as alg

def bisection(fungsi,a,b,toleransi=1.0e-6):
    iterasi = 0
    while True:
        h = (a + b)/2
        tol = abs(b-a)/2
        if tol < toleransi:
            break
        elif fungsi(h) == 0.0:
            break
        elif fungsi(a)*fungsi(h) < 0.0:
            b = h
        else:
            a = h
        iterasi += 1
    return h, iterasi

"""
    x1,x2 = rootsearch(f,a,b,dx).
    Searches the interval (a,b) in increments dx for
    the bounds (x1,x2) of the smallest root of f(x).
    Returns x1 = x2 = None if no roots were detected.
"""

def rootsearch(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx
    f2 = f(x2)
    while np.sign(f1) == np.sign(f2):
        if x1 >= b: 
            return None,None
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)
    else:
        return x1,x2

def bisectioninc(f,x1,x2,switch=1,tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    if np.sign(f1) == np.sign(f2):
        error.err('Root is not bracketed')
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))
    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) \
            and (abs(f3) > abs(f2)):
                return None
        if f3 == 0.0: return x3
        if np.sign(f2)!= np.sign(f3): x1 = x3; f1 = f3
        else: x2 = x3; f2 = f3
    return (x1 + x2)/2.0

def newtonRaphson2(f,x,tol=1.0e-9):
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol: return x
        dx = alg.gaussPivot(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0):
            return x
    print('Too many iterations')

