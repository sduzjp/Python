import math
def pointDist(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    m=(x1-x2)**2
    n=(y1-y2)**2
    p=math.sqrt(m+n)
    return p
print(pointDist((0,0),(3,4)))
