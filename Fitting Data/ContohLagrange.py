# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 10:09:43 2018

@author: USER
"""

import numpy as np
from Lagrange import KoefLagrange, HitungLagrange, PoliLagrange

datax = np.array([1.00, 1.01, 1.02, 1.03, 1.10])
datay = np.array([3.10, 3.12, 3.14, 3.18, 3.24])

c = KoefLagrange(datax,datay)
print("koef lagrange:")
for i in range(len(c)):
    print ("c{:1d} = {:.4f}".format(i,c[i]))
    
Pn = PoliLagrange(datax,c)
print ("polinomial Pn(x) = ",Pn)

# hitung lagrange
xx = np.array([np.pi/3])
p = HitungLagrange(datax,c,xx)
for i in range(len(xx)):
    print ("nilai Pn({:.4f}) = {:>4f}".format(xx[i],p[i]))

# plot lagrange
from matplotlib import pyplot as plt
x = np.arange(datax[0], datax[len(datax) - 1], 1.0e-3)
p = HitungLagrange(datax,c,x)
plt.plot(datax,datay, 'o', x, p, '-', x, np.cos(x), '--')
plt.legend(('data', 'lagarange', 'cos(x)'), loc = 0)
plt.xlabel("x")
plt.ylabel("Pn(x) dari cos(x)")
plt.grid(True)
plt.show()