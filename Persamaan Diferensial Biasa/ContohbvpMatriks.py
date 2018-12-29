# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:16:46 2018

@author: USER
"""

from bvpMatriks import bvpMatriks
from EliminasiGaussPivot import ElimGaussPivot
import numpy as np
import math

xi = 0.0
xf = 1.44
m = 16
h = (xf-xi)/m
x = np.arange(xi,xf+h,h)
A,b = bvpMatriks(x,h,m)
y = ElimGaussPivot(A,b)
print("\tx\t\ty")
for i in range(m+1):
    print("{:13.5f}".format(x[i]),end="\t")
    print("{:13.5f}".format(y[i]))
    print("\n")