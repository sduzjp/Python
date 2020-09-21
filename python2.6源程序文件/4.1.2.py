import math
def quadraticRootsComplex(a,b,c):
    if a==0:
        if b==0:
            print('error')
        else:
            print('x=%f'%(-c/b))
    else:
         m=b*b-4*a*c
         if m>=0:
            k=math.sqrt(m)
            p1=(-b+k)/(2*a)
            p2=(-b-k)/(2*a)
            print('x1=%f,x2=%f'%(p1,p2))
         else:
            n=math.sqrt(-m)
            r1=-b/(2*a)
            r2=n/(2*a)
            r=complex(r1,r2)
            t=complex(r1,-r2)
            print('x1=%s,x2=%s'%(r,t))
      
    
