# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 01:15:59 2018

@author: Muhammad_Vadhel
"""

import numpy as np

def Euler(F,x,y,xAkhir,h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xAkhir:
        h = min(h,xAkhir - x)
        y = y + h*F(x,y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)


def printSoln(X,Y,freq):
    def printHead(n):
        print("\n x ",end=" ")
        for i in range (n):
            print("y[",i,"]",end=" ")
        print()
        
    def printLine(x,y,n):
        print("{:13.4e}".format(x),end=" ")
        for i in range (n):
            print("{13.4e}".format(y[1]),end=" ")
        print()
    m = len(Y)
    try: n = len(Y[0])
    except TypeError: n = 1
    if freq == 0: freq = m
    printHead(n)
    for i in range(0,m,freq):
        printLine(X[i],Y[i],n)
    if i != m - 1: printLine(X[m-1],Y[m-1],n)

        
def modEuler(F,x,y,xAkhir,h):
    def rk2_euler(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x +h/2.0, y + K0)
        return K1
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xAkhir:
        h = min(h,xAkhir - x)
        y = y + rk2_euler(F,x,y,h)
        x = x + h
    X.append(x)
    Y.append(y)
    return np.array(X), np.array(Y)

def ruKut4(F,x,y,xAkhir,h):
    def rk4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xAkhir:
        h = min(h,xAkhir - x)
        y = y + rk4(F,x,y,h)
        x = x + h
    X.append(x)
    Y.append(y)
    return np.array(X), np.array(Y)

def ruKut3(F,x,y,xAkhir,h):
    def rk3(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h, y - K0*h + 2*K1*h)
        return (K0 + 4.0*K1 + K2)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xAkhir:
        h = min(h,xAkhir - x)
        y = y + rk3(F,x,y,h)
        x = x + h
    X.append(x)
    Y.append(y)
    return np.array(X), np.array(Y)
