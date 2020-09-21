# -*- coding: cp936 -*-
'''
def remove_dups(L1,L2):
     for e in L1:
          if e in L2:
               L1.remove(e)
L1=[1,2,3,4]
L2=[1,2,3,6]
remove_dups(L1,L2)
print(L1)
'''
'''
Python使用一个内部计数器来跟踪它所在循环中的索引
修改会改变列表长度，但Python不会更新计数器
loop从未见过元素2
'''
def remove_dups(L1,L2):
     L1_copy=L1[:]
     for e in L1_copy:
          if e in L2:
               L1.remove(e)
L1=[1,2,3,4]
L2=[1,2,3,6]
remove_dups(L1,L2)
print(L1)
