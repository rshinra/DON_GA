# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 10:52:43 2014

@author: normand2
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 21:14:48 2014

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
            T[i]=float(row[0])
            WR[i]=float(row[1])
        else:
            T.append(float(row[0]))
            WR.append(float(row[1]))
        i=i+1
 
def Calc_Curve(A,B,N):
    i = 0.
    p_start = 30.
    p_end = 13.9
    p = np.zeros(np.size(T))
    e = np.zeros(np.size(T))    
    p[0] = p_start
    e[0] = 0
    for i in range(np.size(T)-1):  #Calculating slope and moving to next coordinate (temp-march)
        dp_dT = -A * pow((p[i] - p_end),N) *exp(-B/T[i])/20.
        i=i+1        
        p[i]=p[i-1]+dp_dT*(T[i] - T[i-1])
        e[i]=(p[i]-WR[i])*(p[i]-WR[i])
    plt.plot(T,p,'b')
    plt.plot(T,WR,'k')
    error = np.sum(e)
    return error

# This is a brute force method to find A B and N (as well as to look at the error Contours)
#First TRYING A B N as constants, move later to tuples/lists and Tchanges
plt.clf()
print Calc_Curve(3000,5000,2)
            
            
