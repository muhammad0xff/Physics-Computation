# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:57:19 2018

@author: Muhammad_Vadhel
"""

""" Module dekomposisi LU Doolittle dengan Pivot
Selesaikan Ax = b dengan dekomposisi LU Doolittle plus pivoting
"""

import sys
import numpy as np
import TukarElemen

def DekomDoolittlePivot(A,eps=1.0e-12):
    n = len(A[0])
    pivot = np.array(range(n))
    
    # cari faktor skala dulu
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(A[i,:]))
        
    # proses tukar elemen baris
    # cari baris dengan elemen A[k,k] terbesar
    for k in range(0,n-1):
        p = np.argmax(abs(A[k:n,k])/s[k:n]) + k
        
    # uji singularitas
    if abs(A[p,k]) < eps:
        print("matriks singular\n")
        sys.exit("kelar kuliah lo :-D")
    
    # mulai proses tukar baris p dan k
        if p != k:
            TukarElemen.TukarBaris(s,k,p)
            TukarElemen.TukarBaris(A,k,p)
            TukarElemen.TukarBaris(pivot,k,p)
            
    # inisialisasi proses dekomposisi
    U = A.copy()
    L = np.identity(n)
    
    # proses dekomposisi
    for k in range(0,n-1):
        for i in range(k+1,n):
            if U[i,k] != 0.0:
                L[i,k] = U[i,k]/U[k,k]
                for j in range(k,n):
                    U[i,j] = U[i,j] - L[i,k]*U[k,j]
    return L,U,pivot

def SolusiDoolittlePivot(L,U,b,pivot):
    n = len(b)
    #susun ulang vektor b dan simpan dalam z
    z = b.copy()
    
    for i in range(n):
        z[i] = b[pivot[i]]
    
    # substitusi maju
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = z[0]
    
    for k in range(1,n):
        y[k] = z[k] - np.dot(L[k,0:k],y[0:k])
        
    # proses substitusi mundur
    x[n-1] = y[n-1]/U[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (y[k]-np.dot(U[k,k+1:n],x[k+1:n]))/U[k,k]
        
    return x
 
 #Contol Soal
 from LUDoolittlePivot import DekomDoolittlePivot
from LUDoolittlePivot import SolusiDoolittlePivot

A = np.array([[6,0,-1,0,0],\
              [3,-3,0,0,0],\
              [0,-1,9,0,0],\
              [0,1,8,-11,2],\
              [3,1,0,0,-4]],float)
b = np.array([[50],\
             [0],\
             [160],\
             [0],\
             [0]],float)

L, U, pivot = DekomDoolittlePivot(A)
print("hasil dekomposisi adalah:\n")
print("matriks L:\n ",L,"\n")
print("matriks U:\n ",U,"\n")
print("vektor pivot:\n ",pivot,"\n")

x = SolusiDoolittlePivot(L,U,b,pivot)
print("Solusinya adalah: \n")
for i in range(len(b)):
    print("x{:1d} = {:5.5f}".format(i+1,x[i]))
