# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 15:05:27 2014

@author: normand2
"""
import time
import matplotlib.pyplot as plt
import random
""" 
Hard coded for one dimensional 3 unkown 2 parameter search 
A x*x + B x + C = y; xy parameters, ABC unknowns
"""
#-------------------------------
def calc_fit(A,B,C,f,x,y,n):
    for i in range(0,n):
      f[i] = 0
      for j in range(0,31):
          f[i] = f[i] + abs(y[j] - (A[i]*x[j]*x[j] + B[i]*x[j] + C[i]))
    return(i)
#-------------------------------
def sort(f,len):        # heapsort
    #-------------------------------
    def sink(f,i,n):
        mc = i*2+1
        if(mc < n):
            oc = mc+1
            if(f[oc]>f[mc]):
                mc = oc
        else:
            if(mc>n):
                return
        if(f[i] >= f[mc]):
            return
        swap(f,i,mc)
        sink(f,mc,n)
        return
    #-------------------------------
    def swap(f,a,b):
        temp = f[b]
        f[b] = f[a]
        f[a] = temp
        temp = A_pop[b]
        A_pop[b]=A_pop[a]
        A_pop[a] = temp
        temp = B_pop[b]
        B_pop[b]=B_pop[a]
        B_pop[a] = temp
        temp = C_pop[b]
        C_pop[b]=C_pop[a]
        C_pop[a] = temp
        return
    #-------------------------------
    for i in range(len/2,-1,-1):
        sink(f,i,len-1)
    for i in range(len-1,-1,-1):
        swap(f,0,i);
        sink(f,0,i-1)
    return(0)
#-------------------------------
def hump(f,n,c):
    kid = n
#   each mates with each
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,c):
                if(i != j):     # cant mate with self
                    bit = random.randint(1,7)   # Random 1-7, with bit for inheritance, if 1, inherit from parent 1, else parent 2
#                    for k in range(0,3):
#                        if(bit/pow(2,k)%2 == 1):
                    #A
                    if((bit/4)%2 == 1):
                        A_pop[kid]=A_pop[i]
                    else:
                        A_pop[kid]=A_pop[j]
                    #B
                    if((bit/2)%2 == 1):
                        B_pop[kid]=B_pop[i]
                    else:
                        B_pop[kid]=B_pop[j]
                    #C                       
                    if(bit%2 == 1):
                        C_pop[kid]=C_pop[i]
                    else:
                        C_pop[kid]=C_pop[j]
                    kid = kid + 1
    return
#-------------------------------
def MC(f,n,c,m,currgen):
    mut = n+c*(n*(n-1))
#rand(7)   bitwise mutation.  4 mutate A 2 Mutate B 1 Mutate C
    for i in range(0,n):
        for j in range(0,m):
            bit = random.randint(1,7)   # Random 1-7, with bit for inheritance, if 1, inherit from parent 1, else parent 2
            #A
            if((bit/4)%2 == 1):
#                A_pop[mut]=A_pop[i]+random.uniform(-10/(currgen+1),10/(currgen+1))
                A_pop[mut]=A_pop[i]+random.uniform(-10,10)
            else:
                A_pop[mut]=A_pop[i]
            #B
            if((bit/2)%2 == 1):
#                B_pop[mut]=B_pop[i]+random.uniform(-10/(currgen+1),10/(currgen+1))
                B_pop[mut]=B_pop[i]+random.uniform(-10,10)
            else:
                B_pop[mut]=B_pop[i]
            #C                       
            if(bit%2 == 1):
#                C_pop[mut]=C_pop[i]+random.uniform(-10/(currgen+1),10/(currgen+1))
                C_pop[mut]=C_pop[i]+random.uniform(-10,10)
            else:
                C_pop[mut]=C_pop[i]
            mut = mut + 1
    return
#-------------------------------
n = 50 # Fitness cull
m = 50 # mutants
c = 2*3 # children
gens = 10
max = n + n*m + c*(n*(n-1))
A_pop=[]
B_pop=[]
C_pop=[]
pop_fit=[]
data_x = range(-15,16)
data_y = [2*x*x-17*x-3 for x in range(-15,16)]
#populate
for i in range(0,max):
    A_pop.append(random.uniform(-10,10))
    B_pop.append(random.uniform(-10,10))
    C_pop.append(random.uniform(-10,10))
    pop_fit.append(0)
calc_fit(A_pop,B_pop,C_pop,pop_fit,data_x,data_y,max)
#
fig, (ax0, ax1) = plt.subplots(nrows=2)

#ax0.plot(pop_fit)
#-------------------------------

sort(pop_fit,max)
ax1.plot(pop_fit)
ax1.draw
ax0.hold(False)
ax1.hold(False)
for i in range(0,gens):
    time.sleep(0.5)
    print 'current gen = ', i
    sort(pop_fit,max)
    test_x = [x/10. for x in range(-200,201)]
    test_y = [A_pop[0]*x*x+B_pop[0]*x+C_pop[0] for x in test_x]
    ax0.plot(data_x,data_y,'ro',test_x,test_y)
    ax0.draw
    ax1.plot(pop_fit)
    ax1.draw
    plt.pause(.0001)
    hump(pop_fit,n,c)
    MC(pop_fit,n,c,m,i)
    calc_fit(A_pop,B_pop,C_pop,pop_fit,data_x,data_y,max)
sort(pop_fit,max)
ax1.plot(pop_fit)
for i in range(0,10):
    print A_pop[i],"* x^2 +",B_pop[i],"* x +",C_pop[i],"   fitness:",pop_fit[i]
test_x = [x/10. for x in range(-200,201)]
test_y = [A_pop[0]*x*x+B_pop[0]*x+C_pop[0] for x in test_x]
ax0.plot(data_x,data_y,'ro',test_x,test_y)
plt.ylabel('what the f?')
