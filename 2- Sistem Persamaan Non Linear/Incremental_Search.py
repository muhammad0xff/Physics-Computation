# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:54:37 2018

@author: Muhammad_Vadhel
"""
"""
akar persamaan dengan incremental search
"""

from numpy import sign

def cari_akar(f,a,b,dx):
    x1 = a
    f1 = f(x1)
    x2 = a + dx
    f2 = f(x2)
    while sign(f(1)) == sign(f(2)):
        if x1 >= b:
            return None, None
        x1 = x2
        f1 = f2
        x2 = x2 + dx
        f2 = f(x2)
    else:
        return x1,x2

#Contoh_Soal
from IncSearch import cari_akar

def f(x):
    return x**3 - 10.0*x**2 + 5.0

x1 = 0.0
x2 = 1.0

for i in range(4):
    dx = (x2 - x1)/10.0
    x1,x2 = cari_akar(f,x1,x2,dx)
    
x = (x1 + x2)/2.0
print('akar = {:6.5f}'.format(x))
