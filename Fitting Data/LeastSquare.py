# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:49:25 2018

@author: Muhammad_Vadhel
"""

from warnings import warn
import numpy as np
from scipy.linalg.blas import dgemm
import matplotlib.pyplot as plt

def linear_least_squares(a, b, residuals=False):
    if type(a) != np.ndarray or not a.flags['C_CONTIGUOUS']:
        warn('Matrix a is not a C-contiguous numpy array. The solver will create a copy, which will result' + \
             ' in increased memory usage.')
        
    a = np.asarray(a, order='c')
    i = dgemm(alpha=1.0, a=a.T, b=a.T, trans_b=True)
    x = np.linalg.solve(i, dgemm(alpha=1.0, a=a.T, b=b)).flatten()

    if residuals:
        return x, np.linalg.norm(np.dot(a, x) - b)
    else:
        return x


if __name__ == "__main__":
    x = np.array([0.427,
0.465,
0.507,
0.556,
0.6])
    y = np.array([0.0025,
0.00425,
0.004,
0.00475,
0.004625
])
#    y2 = np.array([0.2889, 0.2525, 0.2377, 0.2093, 0.1936, 0.1871])
#   y3 = np.array([0.1314,0.1425,0.1482,0.162,0.1785,0.2048])
#    y4 = np.array([0.0946,0.104,0.0992,0.1173,0.1225,0.1541])
#    y5 = np.array([0.2943,0.077,0.0729,0.0961,0.0961,0.104])

    A = np.vstack([x, np.ones(len(x))]).T
    A = np.asarray(A, order='c')

m, c = linear_least_squares(A, y)
 #   m2, c2 = linear_least_squares(A, y2)
 #   m3, c3 = linear_least_squares(A,y3)
 #   m4, c4 = linear_least_squares(A,y4)
 #   m5, c5 = linear_least_squares(A,y5)

print(m, c)
#    print(m2, c2)
#    print(m3, c3)
#    print(m4, c4)
#    print(m5, c5)


plt.plot(x, y, '.', label='Perbandingan B dan ds', markersize=10)
plt.plot(x, m * x + c, 'r')
#plt.plot(x,y2,'o',label='1.2A',markersize=10)
#plt.plot(x, m2 * x + c2, 'b')
#plt.plot(x,y3,'o',label='1.4A',markersize=10)
#plt.plot(x, m3 * x + c3, 'green')
#plt.plot(x,y4,'o',label='1.6A',markersize=10)
#plt.plot(x, m4 * x + c4, 'yellow')
#plt.plot(x,y5,'o',label='1.8A',markersize=10)
#plt.plot(x, m5 * x + c5, 'black')
plt.legend(loc=0)

plt.ylabel('$ds$')
plt.xlabel('B')
plt.grid(True)
plt.show()
