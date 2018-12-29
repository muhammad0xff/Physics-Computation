# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:19:06 2018

@author: Muhammad_Vadhel
"""

"""Modul Dekomposisi Doolittle
Selesaikan Ax = b dengan dekomposisi LU Doolittle
"""

import numpy as np

def DekomDoolittle(A):
    n = len(A)
    U = A.copy()
    L = np.identity(n)
    # proses dekomposisi
    for k in range(0,n-1):
        for i in range(k+1,n):
            if U[i,k] != 0.0:
                L[i,k] = U[i,k]/U[k,k]
                for j in range(k,n):
                    U[i,j] = U[i,j] - L[i,k]*U[k,j]
    return L,U

def SolusiDoolittle(L,U,b):
    n = len(b)
    # substitusi maju
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = b[0]
    for k in range(1,n):
        y[k] = b[k] - np.dot(L[k,0:k],y[0:k])
    # proses substitusi mundur
    x[n-1] = y[n-1]/U[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (y[k]-np.dot(U[k,k+1:n],x[k+1:n]))/U[k,k]
        return x
 
 #Contol Soal
 from LUDoolittle import DekomDoolittle
from LUDoolittle import SolusiDoolittle

A = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]], float)
b = np.array([11,-16,17], float)

L, U = DekomDoolittle(A)
print("Hasil Dekomposisi adalah:\n")
print("matriks L:\n ",L)
print("matriks U:\n ",U)

x = SolusiDoolittle(L,U,b)
print("Vektor y hasil substitusi maju adalah: \n", x,"\n")
print("solusinya adalah: \n")
for i in range(len(b)):
    print("x{:1d} = {:5.5f}".format(i+1,x[i]))
    
