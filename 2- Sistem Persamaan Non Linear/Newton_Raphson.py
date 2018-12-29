# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:44:25 2018

@author: Muhammad_Vadhel
"""

def newtonRaphson(f,df,x,akurasi=1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < akurasi:
            return x,i
    print('terlalu banyak iterasi\n')

import numpy as np
from EliminasiGaussPivot import ElimGaussPivot
import math

def newtonRaphson2(f,x,akurasi=1.0e-9):
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
        jac, f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < akurasi:
            return x
        dx = ElimGaussPivot(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < akurasi*max(max(abs(x)),1.0):
            return x
    print('terlalu banyak iterasi')
   
   #Contoh_Soal_1
   from newtonRaphson import newtonRaphson


def f (x):
    return x**3 - 10.0*x**2 + 5.0

def df(x):
    return 3.0*x**2 - 20.0*x

akar, iterasi = newtonRaphson(f,df,2.0)
print('akar = {:5.4f}'.format(akar))
print('jumlah iterasi =', iterasi)

#Contoh_Soal_2
from NewtonRaphson2 import newtonRaphson2

def f(a):
    return (x-a)**2 + (x-y)**2 - 320000**2

x = np.array([8.21, 0.34, 5.96])
y = np.array([0.01, 6.62, -1.12])
solusi = newtonRaphson2(f,x)
print('solusinye:/n')
for i in range(len(solusi)):
    print('x{:1d}={:5.4f}'.format(i, solusi[i]))
