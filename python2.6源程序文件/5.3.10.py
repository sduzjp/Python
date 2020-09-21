# -*- coding: cp936 -*-
import math

def within(x,y,eps):
    if x>=(y-eps) and x<=y:
        return True
def piSeries(n,eps):
    sum=0
    for i in range(n):
        m=2*i+1
        p=(-1)**i
        t=p/m
        sum=sum+t
    if  within(sum,math.pi/4,eps)==True:
        return True
def numTerms(eps):
    #自己大约估计的n的最小值在100之内
    for j in range(100):
        if piSeries(j,eps)==True:
            return j
numTerms(0.1)
