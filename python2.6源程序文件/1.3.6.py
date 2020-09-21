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
    # Delete the pass statement below and insert your own code
    pass

#-----------------------------------------------------------------------------
import math 
class Polynomial:
    def __init__(self,coefficients):
        adict=dict()
        for i in coefficients[:]:
            for j in range(len(coefficients)):
                adict[j]=i
        p=0
        for i in range(len(coefficients)):
            p+=adict[i]*(z**i)
        print p
    def coeff(self,i):
        
    def quadraticRootsComplex(self):
        alist=list()
        if self.pa==0:                      #������ʽΪһ��ʱ
            if self.pb==0:                  #������ʽΪһ�����޽�ʱ������error�Ϳ��б�
                print('error')
                return alist
            else:
                x=-self.pc/float(self.pb)
                alist.append(x)
                return alist
        else:                               #������ʽΪ�����Ҹ�Ϊʵ��ʱ
            m=self.pb**2-4*self.pa*self.pc
            if m>=0:
                k=math.sqrt(m)
                p1=(-self.pb+k)/float((2*self.pa))
                p2=(-self.pb-k)/float((2*self.pa))
                alist.append(p1)
                alist.append(p2)
                return alist
            else:                           #������ʽΪ�����Ҹ�Ϊ����ʱ
                n=math.sqrt(-m)
                r1=-self.pb/float((2*self.pa))
                r2=n/float((2*self.pa))
                r=complex(r1,r2)
                t=complex(r1,-r2)
                alist.append(r)
                alist.append(t)
                return alist
P1=Polynomial(0,0,1)                        #���Դ���
P2=Polynomial(0,2,1)
P3=Polynomial(1,2,1)
P4=Polynomial(1,0,1)
print(P1.quadraticRootsComplex())
print(P2.quadraticRootsComplex())
print(P3.quadraticRootsComplex())
print(P4.quadraticRootsComplex())
