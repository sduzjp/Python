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
Pythonʹ��һ���ڲ�������������������ѭ���е�����
�޸Ļ�ı��б��ȣ���Python������¼�����
loop��δ����Ԫ��2
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
