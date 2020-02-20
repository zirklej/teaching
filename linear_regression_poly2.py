# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:23:03 2020

@author: zirklej
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from random import gauss
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# generate random points about the curve y=x^2+1
num=100

x=np.linspace(-1,1,num)
y=x**2+1

x_rand=np.array([gauss(0.,0.1) for i in range(num)])
y_rand=np.array([gauss(0.,0.2) for i in range(num)])

xrand=x+x_rand
yrand=y+y_rand

def mine(xrand,yrand,num):
    # create coefficient matrix
    coef=np.array([[num,np.sum(xrand),np.sum(xrand**2)],
                    [np.sum(xrand),np.sum(xrand**2),np.sum(xrand**3)],
                    [np.sum(xrand**2),np.sum(xrand**3),np.sum(xrand**4)]])
    # create constant vector
    const=np.array([np.sum(yrand),np.sum(xrand*yrand),np.sum(yrand*xrand**2)])
    # solve linear system
    soln=np.linalg.solve(coef,const)
    return soln

def sklearn(xrand,yrand):
    xrand=xrand.reshape((-1,1))
    # include column for x^2
    transformer=PolynomialFeatures(degree=2,include_bias=False)
    transformer.fit(xrand)
    xrand_=transformer.transform(xrand) # this includes a second col, which is the square of the first col
    
    model=LinearRegression().fit(xrand_,yrand)
    a=model.intercept_
    b=model.coef_[0]
    c=model.coef_[1]
    print(a,b,c)
    return a,b,c

ymine=mine(xrand,yrand,num)
a,b,c=sklearn(xrand,yrand)

fig1=plt.figure(figsize=(12,6))
ax1=fig1.add_subplot(1,1,1)
ax1.plot(x,a+b*x+c*x**2)
ax1.scatter(xrand,yrand)
ax1.plot(x,ymine[0]+ymine[1]*x+ymine[2]*x**2,color='r')

print("ours:  a = {}\n b = {}\n c = {}".format(ymine[0],ymine[1],ymine[2]))
print("scikit-learn:  a = {}\n b = {}\n c = {}".format(a,b,c))
