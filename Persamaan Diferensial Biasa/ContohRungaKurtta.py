# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 06:13:02 2018

@author: USER
"""

import numpy as np
from RungaKutta import modEuler, printSoln
import matplotlib.pyplot as plt
from math import exp

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1] - x
    return F

x = 0.0                     #start of integration
xAkhir = 2.0                #End of integration
y = np.array([0.0, 1.0])    #initial values of {y}
h = 0.05                    #step size

X,Y = modEuler(F,x,y,xAkhir,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('numericalmodEULER','exactmodEULER'),loc=0)
plt.show()


def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1] - x
    return F

x = 0.0                     #start of integration
xAkhir = 2.0                #End of integration
y = np.array([0.0, 1.0])    #initial values of {y}
h = 0.2                    #step size

X,Y = modEuler(F,x,y,xAkhir,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('numericalROKUT4','exactROKUT4'),loc=0)
plt.show()


#def F(x,y):
#    F = np.zeros(4)
#    F[0] = y[1]
#    F[1] = y[0]*(y[3]**2)- 3.9860e14/(y[0]**2)
#    F[2] = y[3]
#    F[3] = -2.0*y[1]*y[3]/y[0]
#    return F

#x = 0.0                                                   #start of integration
#xAkhir = 1200.0                                           #End of integration
#y = np.array([7.15014e16, 0.0, 0.0, 0.937045e-3])         #initial values of {y}
#h = 50.0                                                  #step size
#freq = 2                                                  #printout frequency

#X,Y = Euler(F,x,y,xAkhir,h)
#printSoln(X,Y,freq)