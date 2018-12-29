# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:14:44 2018

@author: USER
"""

import numpy as np
import math
from EliminasiGaussPivot import ElimGaussPivot
import matplotlib.pyplot as plt

def polyfit(xData,yData,m):
    a = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        temp = 1.0
        
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
        
        for i in range(m+1):
            for j in range(m+1):
                a[i,j] = s[i+j]
        return ElimGaussPivot(a,b)
    
def stDev(c,xData,yData):
    
    def evalPoly(c,x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p*x + c[m-j-1]
        return p
    
    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c,xData[i])
        sigma = sigma + (yData[i] - p)**2
    sigma = math.sqrt(sigma/(n-m))
    return sigma

def plotPoly(xData,yData,coeff,xlab='x',ylab='y'):
    m = len(coeff)
    x1 = min(xData)
    x2 = max(xData)
    dx = (x2-x1)/20.0
    x = np.arange(x1,x2 + dx/10.0,dx)
    y = np.zeros((len(x)))*1.0
    for i in range(m):
        y = y + coeff[i]*x**i
    plt.plot(xData,yData,'o',x,y,'-')
    plt.xlabel(xlab); plt.ylabel(ylab)
    plt.grid(True)
    plt.show()