# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:31:13 2018

@author: USER
"""

def deflPolin(a,r):
    n = len(a) - 1
    b = []
    b[n-1] = a[n]
    for i in range(n-2,-1,-1):
        b[i] = a[i+1] + r*b[i+1]