# -*- coding: cp936 -*-
def is_even(i):
     '''Input:i,a positive int
          return True if i is even ,otherwise False
     '''
     print("inside is_even")
     #return i%2==0
     if i%2!=1:          #python�У�û��ȡ������˼��
          return True
     else:
          return False
print(is_even(3))
print(is_even(2))
