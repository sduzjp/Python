# -*- coding: cp936 -*-
import math
class Polynomial:
     def __init__(self,coefficients):
          self.adict=dict()
          self.coefficients_=coefficients

     def __repr__(self):
          for i in self.coefficients_[:]:
               for j in range(len(self.coefficients_)):
                    if self.coefficients_[j]==i:
                         self.adict[j]=i
          alist=list()
          for i in range(len(self.coefficients_)):
               alist.append(str("%d*(z**%d)"%(self.adict[i],len(self.coefficients_)-1-i)))
          p='+'.join(alist)
          return p

     def coeff(self,i):
          for j in range(len(self.coefficients_)):
               if len(self.coefficients_)-1-j==i:
                    print self.adict[j]

     def add(self,other):
          if len(self.coefficients_)>=len(other.coefficients_):
               for i in range(len(other.coefficients_)):
                    self.coefficients_[len(self.coefficients_)-len(other.coefficients_)+i]+=other.coefficients_[i]
               return Polynomial(self.coefficients_)
          else:
               for i in range(len(self.coefficients_)):
                    other.coefficients_[len(other.coefficients_)-len(self.coefficients_)+i]+=self.coefficients_[i]
               return Polynomial(other.coefficients_)         

     def mul(self,other):
          alist=[]
          if len(self.coefficients_)<len(other.coefficients_):
               t=self.coefficients_
               self.coefficients_=other.coefficients_
               other.coefficients_=t
          for i in range(len(self.coefficients_)):
               blist=[]
               for j in range(len(other.coefficients_)):
                    blist.append(self.coefficients_[i]*other.coefficients_[j])
               alist.append(blist)
          for i in range(len(self.coefficients_)):
               m=0
               while m<(len(self.coefficients_)-1-i):
                    alist[i].append(0)       
                    m+=1
          P=list()
          for i in range(len(self.coefficients_)):
               p1=Polynomial(alist[i])
               P.append(p1)
          for i in range(len(self.coefficients_)-1):
               P[i+1]=P[i].add(P[i+1])
          print P[len(self.coefficients_)-1]
          
     def str(self):
          p=Polynomial(self.coefficients_)
          print('"%s"'%str(p))

     def val(self,v):
          value=0
          for i in range(len(self.coefficients_)):
               value+=self.coefficients_[i]*(v**(len(self.coefficients_)-1-i))
          print value

     def roots(self):
        alist=list()
        self.pa=self.coefficients_[0]
        self.pb=self.coefficients_[1]
        self.pc=self.coefficients_[2]
        if self.pa==0:                                 #当多项式为一阶时
            if self.pb==0:                             #当多项式为一阶且无解时，返回error和空列表
                print('error')
                return alist
            else:
                x=-self.pc/float(self.pb)
                alist.append(x)
                return alist
        else:                                          #当多项式为二阶且根为实根时
            m=self.pb**2-4*self.pa*self.pc
            if m>=0:
                k=math.sqrt(m)
                p1=(-self.pb+k)/float((2*self.pa))
                p2=(-self.pb-k)/float((2*self.pa))
                alist.append(p1)
                alist.append(p2)
                return alist
            else:                                      #当多项式为二阶且根为复根时
                n=math.sqrt(-m)
                r1=-self.pb/float((2*self.pa))
                r2=n/float((2*self.pa))
                r=complex(r1,r2)
                t=complex(r1,-r2)
                alist.append(r)
                alist.append(t)
                return alist
