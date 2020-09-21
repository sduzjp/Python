class Force:
     def __init__(self,x,y):
          self.fx=x
          self.fy=y   
     def __add__(self,force1,force2):
          x=force1.fx+force2.fx
          y=force1.fy+force2.fy
          return Force(x,y)
     def __str__(self):
          return "F<%s,%s>"%(self.fx,self.fy)
     def __mul__(self,n):
          x,y=self.fx*n,self.fy*n
          return Force(x,y)
     def __eq__(self,force2):
          return (self.fx==force2.fx) and (self.fy==force2.fy)
f1=Force(0,1)
f2=Force(3,4)
f3=Force(f1,f2)
print("f1=%s"%f1)
print("f2=%s"%f2)
print("f3=%s"%f3)

