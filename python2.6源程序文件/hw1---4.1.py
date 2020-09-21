def apply(opList,arg):
     if len(opList)==0:
          return arg
     else:
          return apply(opList[1:],opList[0](arg))

def increment(n):
     return n+1
def square(n):
     return n**2
print apply([],7)
print apply([increment],7)
print apply([square],7)
print apply([increment,square],7)
