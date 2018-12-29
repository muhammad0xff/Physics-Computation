# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:07:26 2018

@author: Muhammad_vadhel
"""

import numpy as np
from LUDoolittlePivot import DekomDoolittlePivot
from LUDoolittlePivot import SolusiDoolittlePivot

resistansi = np.array([5,10,15,20,25],float)
V = np.array([110,220,124])

for R in resistansi:
    A = np.array([[50+R, -R, -30*R],\
                  [-R, 65+R, -15],\
                  [-30, -15, 45]], float)
    B = np.array([[0,0,V[0]],\
                  [0,0,V[1]],\
                  [0,0,V[2]]], float)
    print("matriks A sebelum eliminasi adalah:\n",A)
    
    # Dekomposisi
    L, U, pivot = DekomDoolittlePivot(A)
    # Solusi
    for k in range(len(B)):
        x = SolusiDoolittlePivot(L,U,B[k],pivot)
        print("solusi untuk R = {:.1f} Ohm dan V = {:.1f} adalah: \n".format(R,V[k]))
        for i in range(len(B)):
            print("i{:1d} = {:5.5f}".format(i+1,x[i]))
        input("tekan enter untuk lanjut.\n")
