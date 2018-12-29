# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:44:22 2018

@author: USER
"""

import math
from romberg import romberg

def f(t):
    f = 5*(1+2*t*math.exp(2*t/5))
    return f


I,n = romberg(f,47,48)
print("Integral =",I)
print("numEvals =",n)   