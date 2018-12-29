# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:23:41 2018

@author: Muhammad_Vadhel
"""

"""
module bisection
"""

import math
import sys
from numpy import sign

def bisect(f,x1,x2,cm=0,eps=1.0e-4):
    f1 = f(x1)
    if f1 == 0.0:
        return f1
    f2 = f(x2)
    if f2 == 0.0:
        return f2
    if sign(f1) == sign(f2):
        sys.exit('akar tidak diapit x1 dan x2')
    n = int(math.ceil(math.log(abs(x2-x1)/eps/math.log(2.0))))
    
    for i in range(n):
        xm = 0.5*(x1+x2)
        fm = f(xm)
        if (cm == 1) and (abs(fm) > abs(f1)) and (abs(fm > abs(f2))):
            return None
        if fm == 0:
            return fm
        if sign(f2) != sign(fm):
            x1 = xm
            f1 = fm
            return (x1+x2)/2.0
            
#Contoh_Soal_1
from bisection import bisect

def f(x):
    return x**3 - 10.0*x**2 + 5.0

x1 = 0.0
x2 = 1.0
x = bisect(f,x1,x2)
print('{:6.5f}'.format(x))

#Contoh_Soal_2
import math
from IncSearch import cari_akar
from bisection import bisect


def f(x):
    return x - math.tan(x)

a,b,dx = (0.0, 20.0, 0.01)
print('akar f(x) adalah: \n')

while True:
    x1,x2 = cari_akar(f,a,b,dx)
    if x1 != None:
        a = x2
        akar = bisect(f,x1,x2,1)
        if akar != None:
            print(akar)
    else:
        print("\nSelesai")
        break
 
 
