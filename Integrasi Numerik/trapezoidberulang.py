# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:53:54 2018

@author: USER
"""

def trapznBerulang(f,a,b,akurasi,segmen=0):
    def trapznFungsiBerulang(f, a, b, k, Iseb=0.0):
        if k == 1:
            I = (f(a) + f(b))*(b-a)/2.0
        else:
            n = 2**(k-2) # jumlah titik baru
            h = (b-a)/n # rentang titik
            x = a+h/2.0
            sum = 0.0
            for i in range(n):
                sum = sum + f(x)
                x = x + h
            I = (Iseb + h*sum)/2.0
        return I
    
    Iseb = 0.0
    for k in range(1,50):
        Isdh = trapznFungsiBerulang(f,a,b,k,Iseb)
        if (k>1) and (abs(Isdh - Iseb))<akurasi:
            break
        Iseb = Isdh
    if segmen is not 0:
        print ("jumlah segmen=",2**(k-1))
    return Isdh