# -*- coding: cp936 -*-

#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------

def fib(n):
    # Delete the pass statement below and insert your own code
    pass

#-----------------------------------------------------------------------------

class V2:
    def __init__(self,x,y):
        self.vx=x
        self.vy=y
        print("V2[%s,%s]"%(self.vx,self.vy))
    def getX(self):
        print self.vx
    def getY(self):
        print self.vy
    def add(self,v2):
        x=self.vx+v2.vx
        y=self.vy+v2.vy
        return V2(x,y)
    def mul(self,n):
        x=self.vx*n
        y=self.vy*n
        return V2(x,y)
    def __add__(self,v):
        return self.add(v)
'''
a=V2(1.0,2.0)                   #测试程序
b=V2(2.2,3.3)
a.add(b)
a.mul(2)
a.add(b).mul(-1)
V2(1.1,2.2)+V2(3.3,4.4)
'''

#-----------------------------------------------------------------------------

class Polynomial:
    # Delete the pass statement below and insert your own code
    pass
