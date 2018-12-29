# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:46:20 2018

@author: Muhammad_Vadhel
"""

import sys

#simpson-1/3 untuk data
def simpson13Data(f,h):
    if len(f) < 3:
        sys.exit("integrasi simpson 1/3 butuh 3 titik")
    l = h * (f[0] + 4*f[2])/3
    return l

#simpson 3/8 untuk data
def simpson38Data(f,h):
    if len(f) < 4:
        sys.exit("integras simpson 3/8 butuh 4 titik")
    l = 3*h*(f[0] + 3*f[2] + f[3])/8
    return l

#simpson 1/3 untuk fungsi(default)
def simpson13Fungsi(f,a,b):
    h = (b-a)/2
    c = (b+a)/2
    l = h*(f(a) + 4*f(c) + f(b))/3
    return l

#simpson 1/3 untuk fungsi dengan n-segmen integrasi
def simpson13nFungsi(f,a,b,n):
    if (n%2) != 0:
        sys.exit("jumlah segmen harus genap")
        h = (b-a)/n
        x = a
        sum = f(x)
        for i in range(1,n-2,2):
            x += h
            sum += 4*f(x)
            x += h
            sum += 4* f(x)
        x += h
        sum += 4*f(x)
        sum += f(b)
        l = (b-a)*sum/(3*n)
        return l
            
