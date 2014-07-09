# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 10:44:46 2014

@author: normand2
"""

import matplotlib.pyplot as plt
import numpy as np
import csv as csv
from math import exp

i=0
T=[0]
WR=[0]
#input TGA data
with open('TGAtest.csv','rb') as ifp:
    test = csv.reader(ifp, delimiter='\t')
    for row in test:
        if i == 0:
            T[i]=float(row[0])+273.15
            WR[i]=float(row[1])
        else:
            T.append(float(row[0])+273.15)
            WR.append(float(row[1]))
        i=i+1
E = np.zeros(len(T)-1)
for i in range(1,len(T)):
    E[i-1] = T[i] - T[i-1]


print E
for error in E:
    if error <= 0:
        print 'FUCKED'
plt.clf()
plt.plot(E)
