# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 21:14:48 2014

@author: normand2
"""

import matplotlib.pyplot as plt
import numpy as np
import csv as csv

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
print WR            
            

