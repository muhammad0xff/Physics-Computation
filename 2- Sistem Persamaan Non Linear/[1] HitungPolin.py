# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 07:49:29 2018

@author: USER
"""

"""
Hitung nilai polinomial P = a[0] + a[1]*x^1 + a[2]*x^2 + ....
"""

def HitungPolin(a,x):
    n = len(a) - 1
    p = a[n]
    dp = 0.0 + 0.0j
    ddp = 0.0 + 0.0j
    for i in range(1,n+1):
        ddp = ddp*x + 2.0*dp
        dp = dp*x + p
        p = p*x + a[n-i]
    return p,dp,ddp