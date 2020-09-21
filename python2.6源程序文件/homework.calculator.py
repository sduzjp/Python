

#input("% (%s=%s)"%(key,value))
def calc():
     env=dict()
     while 1:
          input_=raw_input()
          t=input_.split('=')
          a=list(t[0])
          b=list(t[1])
          del a[0]
          del b[len(b)-1]
          env[a[0]]=b[0]
          print env
calc()
class Statement:
     def __init__(self,

                  
     
