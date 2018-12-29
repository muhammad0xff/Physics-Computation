# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:13:01 2018

@author: USER
"""

import numpy as np

def bvpMatriks(x,h,m):
    h2 = h*h
    d = np.ones(m+1)*(-2.0 + 4.0*h2)
    c = np.ones(m)
    e = np.ones(m)
    b = np.ones(m+1)*4.0*h2*x
    
    d[0] = 1.0
    e[0] = 0.0
    b[0] = 0.0
    c[m-1] = 2.0
    
    A = np.zeros([m+1,m+1])
    for k in range(0,m+1):
        A[k,k] = d[k]
    for k in range(0,m):
        A[k,k+1] = e[k]
    for k in range(1,m+1):
        A[k,k-1] = c[k-1]
    return A,b