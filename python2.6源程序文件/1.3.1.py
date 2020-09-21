# -*- coding: cp936 -*-

# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------

'''def fib(n):
    a=list()
    a.append(1)
    a.append(1)
    i=2
    while i<n:
       t=a[i-1]+a[i-2]
       a.append(t)
       i+=1
    for m in range(n):
        print(a[m])                 #第一种定义方法
'''
'''def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)    #第二种定义方法
'''
def fib(n):
    d={1:1,2:2}
    if n in d:
        return d[n]
    else:
        t=fib(n-1)+fib(n-2)
        d[n]=t
        return t
                                    #第三种方法
#-----------------------------------------------------------------------------

class V2:
    # Delete the pass statement below and insert your own code
    pass

#-----------------------------------------------------------------------------

class Polynomial:
    # Delete the pass statement below and insert your own code
    pass
