class Force:
    def __init__(self,x,y):
        self.fx=x
        self.fy=y
    def show(self):
        print("Force<%s,%s>"%(self.fx,self.fy))
    def add(self,force2):
        x=self.fx+force2.fx
        y=self.fy+force2.fy
        return Force(x,y)
f1=Force(0,1)
f1.show()
f2=Force(3,4)
f3=f1.add(f2)
f3.show()
"""f1=Force()
f2=Force()
f1.fx=0
f1.fy=1
f2.fx=3
f2.fy=4
f1.show()
f2.show()
f3=f1.add(f2)
f3.show()
"""
