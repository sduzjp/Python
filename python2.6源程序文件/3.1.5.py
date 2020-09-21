def clip(lo,x,hi):
    m=min(lo,x,hi)
    n=max(lo,x,hi)
    a=list()
    a.append(lo)
    a.append(x)
    a.append(hi)
    a.remove(m)
    a.remove(n)
    return a[0]
print(clip(3,2,5))
print(clip(3,4,5))
print(clip(3,6,5))
