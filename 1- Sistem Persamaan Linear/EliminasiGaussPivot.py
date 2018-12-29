# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:40:37 2018

@author: Muhammad_Vadhel
"""

"""
### module eliminasi gauss dengan pivot

x = ElimGaussPivot(A,b)
    Selesaikan Ax = b dengan eliminasi gauss dengan pivoting
"""

import sys
import numpy as np
import TukarElemen

def ElimGaussPivot(A,b,eps=1.0e-12):
    n = len(b)
    
    # cari faktor skala dulu
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(A[i ,:]))
    
    #proses tukar elemen baris
    #cari baris dengan elemen A[k,k] terbesar
    for k in range(0,n-1):
        p = np.argmax(abs(A[k:n,k])/s[k:n]) + k
        
    #uji singularitas
        if abs(A[p,k]) < eps:
            print("matirks singular\n")
            sys.exit("kelar kuliah lo :-D")
            
    #mulai proses tukar baris p dan k
        if p != k:
            TukarElemen.TukarBaris(b,k,p)
            TukarElemen.TukarBaris(s,k,p)
            TukarElemen.TukarBaris(A,k,p)
            
    # Hasil setelah pertukaran baris
    print("setelah proses pertukaran baris, maka\n")
    print("matriks A menjadi:\n",A)
    print("vektor b menjadi:\n",b)
    print("dan vektor s menjadi:\n",s)
    input("tekan enter untuk lanjut ke proses eliminasi.")

    # proses eliminasi
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                lam = A[i,k]/A[k,k]
                for j in range(k,n):
                    A[i,j] = A[i,j] - lam*A[k,j]
                b[i] = b[i] - lam*b[k]
                print("setelah eliminasi, matriks A menjadi:\n",A)
                print("dan b menjadi: \n",b)
                input("tekan enter untuk lanjut")
                
    # proses substitusi mundur\
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (b[k]-np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]
        return x
        
   #Contoh Soal
   from EliminasiGaussPivot import ElimGaussPivot

A = np.array([[1,3,0],\
              [-1,2,1],\
              [0,1,4]],float)
b = np.array([-1,1,19],float)

x = ElimGaussPivot(A,b)
print("solusinya adalah: \n")
for i in range(len(b)):
    print("x{:1d} = {:5.5f}".format(i+1,x[i]))
