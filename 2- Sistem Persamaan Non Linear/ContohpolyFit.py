# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:28:56 2018

@author: USER
"""

import numpy as np
from polyFit import polyfit, stDev

xData = np.array([0.0, 11.1, 22.2, 33.3])
yData = np.array([0.55, 0.527778, 0.533333, 0.505556])

while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        coeff = polyfit(xData,yData,m)
        print("Coefficients are:\n",coeff) 
        print("Std. deviation =",stDev(coeff,xData,yData))
    except SyntaxError: break
input("Finished. Press return to exit")