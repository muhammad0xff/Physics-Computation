# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 10:35:58 2018

@author: USER
"""

import numpy as np
from InterpolasiNewton import htgNewton, koefNewton, poliNewton

datax = np.array([0.0, 1.525, 3.050, 4.575, 6.100, 7.625, 9.150])
datay = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])

c = koefNewton(datax,datay)
print("koefisien: ",c)
Pn = poliNewton(datax,c)
print("Pn(x) = ", Pn)
xx = np.pi/3
yy = htgNewton(datax,c,xx)
print("y = {:.4f}".format(yy))