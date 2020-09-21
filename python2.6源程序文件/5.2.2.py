import math
def perpDist(p,l):
    px=p[0]
    py=p[1]
    a=l[0]
    b=l[1]
    c=l[2]
    m=a**2
    n=b**2
    p=math.sqrt(m+n)
    t=a*px+b*py+c
    q=t/float(p)
    return q
print(perpDist((0,0),(3,4,1)))
