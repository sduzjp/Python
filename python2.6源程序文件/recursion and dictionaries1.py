'''
a*b
'''
def mult(a,b):
     if b==1:
          return a
     else:
          return a+mult(a,b-1)
a=100
b=100
print(mult(100,100))
