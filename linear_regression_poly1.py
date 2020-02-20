# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:53:04 2020

@author: zirklej
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from random import gauss
from sklearn.linear_model import LinearRegression

# generate random data points about line y=2x+0.5
num=100

x=np.linspace(0,5.,num)
y=2*x+0.5

x_rand=np.array([gauss(0.,1.) for i in range(num)])
y_rand=np.array([gauss(0.,1.) for i in range(num)])

xrand=x+x_rand
yrand=y+y_rand

def mine(xrand,yrand):
    
    xbar=np.mean(xrand)
    ybar=np.mean(yrand)
    m=np.sum((x-xbar)*(y-ybar))/np.sum((x-xbar)**2)
    
    b0=ybar-m*xbar
    yline=m*xrand+b0
    
    return yline,m,b0

def scpy(xrand,yrand):
    
    slope, intercept, r_value, p_value, std_err=linregress(xrand,yrand)
    yreg=slope*xrand+intercept
    
    return yreg,slope,intercept

def sklearn(xrand,yrand):
    
    xsk=xrand.reshape((-1,1)) # make x a col vector
    model=LinearRegression().fit(xsk,yrand)
    b0=model.intercept_
    m=model.coef_[0]
    ysk=xrand*m+b0
    return ysk,m,b0

yline,mline,b0line=mine(x,y)
yreg,mreg,b0reg=scpy(x,y)
ysk,msk,b0sk=sklearn(x,y)

print("slope, intercept: ")
print("ours:  " ,mline,b0line)
print("scipy:  " ,mreg,b0reg)
print("scikit-learn:  " ,msk,b0sk)

fig1=plt.figure(figsize=(12,6))
ax1=fig1.add_subplot(1,1,1)
ax1.scatter(xrand,yrand)
xgraph=np.linspace(-1,5.5,num)
ax1.plot(xgraph,yline,color='b')
ax1.plot(xgraph,yreg,color='r')
ax1.plot(xgraph,ysk,color='g')
