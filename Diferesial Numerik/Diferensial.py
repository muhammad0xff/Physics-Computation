# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:55:24 2018

@author: Muhammad_Vadhel
"""

#modul turunan pertama

def err(DiffNum, HasilAnalitik):
    err = abs((DiffNum - HasilAnalitik)/HasilAnalitik)*100
    return err

def trn1Mundur(f,x,h):
    D = (3*f(x) - 4*f(x-2*h))/(2*h)
    return D

def trn1Maju(f,x,h):
    D = (-3*f(x) + 4*f(x+(2*h)))/(2*h)
    return D

def trn1Tengah(f,x,h):
    D = (f(x+h) - f(x-h))/(2*h)
    return D

def trn1Richardson(dh1,dh2,p):
    penyebut = 2**p - 1
    pembilang = 2**p * dh2 - dh1
    return pembilang/penyebut
    
#Contoh_Soal
import math
import numpy as np
from Diferensial import err, trn1Richardson, trn1Mundur, trn1Tengah, trn1Maju

def f(t):
    f = (((g*m)/cd)**0.5)*math.tanh(((g*cd)/m)**0.5)*t
    return f

g = 9.81
cd = 0.15
m = 60
h = 5000**4
t = np.arange(0,30,1)
#A = np.array([1.6,1.6,2.0,2.8])

#Di = trn1Mundur(f,t,h)
#error = err(Di,A)
#for i in range(len(Di)):
#    print('turunan 1 mundur x{:1d} = {:4f}'.format(i,Di[i]))
#    print('kesalahan relatif x{:1d} = {:4f}'.format(i,error[i]),'%\n')

#D2 = trn1Maju(f,t,h)
#error2 = err(D2,A)
#for i in range(len(D2)):
#    print('turunan 1 maju x{:1d} = {:4f}'.format(i,D2[i]))
#    print('kesalahan relatif x{:1d} = {:4f}'.format(i,error2[i]),'%\n')

#D3 = trn1Tengah(f,t,h)
#error3 = err(D3,A)
#for i in range(len(D3)):
#    print('turunan 1 tengah x{:1d} = {:4f}'.format(i,D3[i]))
#    print('kesalahan relatif x{:1d} = {:4f}'.format(i,error3[i]),'%\n')

dh1 = trn1Tengah(f,t,h)
dh2 = trn1Tengah(f,t,h/2)
D = trn1Richardson(dh1, dh2, 2)
print("turunan1 Richardson=",D)
#print("Kesalahan relatif=",err(D,A),"%\n")
