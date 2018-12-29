# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 08:10:43 2018

@author: USER
"""

from DeflatePolin import deflPolin
import numpy as np

a = np.array([12, -2, -48, -10, 3])
r = 6.0
deflate = deflPolin(a,r)
print('koef P(n-1) adalah:\n')
for i in range(len(deflate)):
    print('b{:1d} = {:12.5f}'.format(i,deflate[i]))