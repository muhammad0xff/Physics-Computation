# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 04:31:19 2018

@author: USER
"""

import numpy as np
import math
from trapezoidberulang import trapznBerulang

def f(t):
    f = (((g*m)/cd)**0.5)*math.tanh(((g*cd)/m)**0.5)*t
    return f

g = 9.81
cd = 0.15
m = 60
h = 5000
t = np.arange(0,30,1)


Iseb = 1.0
for k in range(1,30):
    Isdh = trapznBerulang(f,0.0,30.0,0.001,Iseb)
    if (k>1) and (abs(Isdh-Iseb)) < 1.0e-6: break
    Iseb = Isdh
print("integral =",Isdh)
print("nPanels =",2**(k-1))