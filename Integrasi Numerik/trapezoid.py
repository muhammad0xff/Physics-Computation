# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:10:37 2018

@author: USER
"""
"""
metode integrasi trapezoid
"""

#integrasi data dengan 1 segmen
def trapz1Data(h,f0,f1):
    l = h*(f0+f1)/2
    return l

#integrasi data dengan n segmen
def trapznData(f,h,n):
    m = len(f) - 1
    sum = f[0]
    for i in range(1,m):
        sum += 2*f[i]
        sum = sum + f[m]
        l = sum*h/2
        return l

#integrasi fungsi dengan 1 segmen
def trapz1Fungsi(f,a,b):
    h = b-a
    l = h*(f(a) + (b))/2
    return l

#integrasi fungsi dengan n segmen
def trapznFungsi(f,n,a,b):
    h = (b-a) / n
    x = a
    sum = f(a)
    for i in range(n-1):
        x = x+h
        sum += 2*f(x)
    sum += f(b)
    l = (b-a)*sum/(2*n)
    return l