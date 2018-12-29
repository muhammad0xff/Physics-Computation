# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:25:17 2018

@author: Muhammad_Vadhel
"""

""" Menghitung determinan matriks dengan LUDoolittle Pivot
"""

import numpy as np 
from LUDoolittlePivot import DekomDoolittlePivot

# matriks yang akan dicari determinannya
A = np.array([[0,-1,1],[2,-1,0],[-1,2,-1]],float)
# simpan dulu sequence pivot aslinya 
pivot_asli = np.arange(len(A))
# dekompsosisi LU Doolittle+pivot 

L, U, pivot = DekomDoolittlePivot(A)
# kosmetik output 
print ("Hasil Dekomposisi adalah:\n")
print ("Matriks L:\n ",L)

print ("Matriks U:\n ",U) 
print ("Sequence pivot:\n",pivot)
if tuple( pivot_asli ) != tuple(pivot):
    print("Ada pertukaran baris. Hasil berikut harus dikalikan (−1)^q", \
          "dengan q adalah jumlah proses pertukaran baris")
# hitung determinan A
determinan = 1.0
for k in range(len(A)):
    determinan *= U[k,k]
    
print ("determinan A adalah: ",determinan)

import numpy.linalg as l

A=n.array([[2,1],[2,1.001]])

print('norm(A) adalah = {:12.3f}'.format(l.norm(A)))
print('determinan A adalah = {:12.3f}'.format(l.det(A)))
print('cond(A) adalah = {:12.3f}'.format(l.cond(A)))

for k in range(0,n-1):
    for i in range(k+1,n):
        if A[i,k] != 0:
            lam = A[i,k]/A[k,k]
            for i in range(k,n):
                A[i,i] = A[i,j] - lam * A[k,j]
            b[i] = b[i] - lam * b[k]
        

#menghitung invers matriks dengan LU Doolittle Pivot
from LUDoolittlePivot import DekomDoolittlePivot
from LUDoolittlePivot import SolusiDoolittlePivot

def InvMat(A):
    n = len(A[0])
    InvA = np.identity((n))
    
    L, U, Abaru, pivot = DekomDoolittlePivot(A)
    for k in range(n):
        y, InvA[:,k] = SolusiDoolittlePivot(L,U,InvA[:,k],pivot)
        
    return InvA
    
#Contol Soal mencari invers matrix
from InversMatriks import InvMat

A = np.array([[0.6, -0.4, 1.0],\
              [-0.3, 0.2, 0.5],\
              [0.6, -1.0, 0.5]], float)

# selamatkan dulu A
A_asli = A.copy()
# baru cari inversnya
A_inverse = InvMat(A)
print("invers matriks A adalah: \n",A_inverse,"\n")
print("Cek ulang A^-1 * A = I :\n",np.dot(A_inverse,A_asli))
