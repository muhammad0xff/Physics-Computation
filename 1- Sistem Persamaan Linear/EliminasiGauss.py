# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:16:17 2018

@author: Muhammad_Vadhel
"""

""" x = ElimGauss(A,b)
    Selesaikan Ax = b dengan eliminasi gauss
"""

import numpy as np

def ElimGauss(A,b):
    n = len(b)
    # proses eliminasi
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                lam = A[i,k]/A[k,k]
                for j in range(k,n):
                    A[i,j] = A[i,j] - lam*A[k,j]
                b[i] = b[i] - lam*b[k]
                print("Setelah eliminasi, Matriks A menjadi:\n",A)
                print("dan b menjadi: \n",b)
                input("tekan enter untuk lanjut")
                
    # proses substitusi mundur
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (b[k]-np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]
        return x
