
def clip(lo,x,hi):
    if x<lo:
        return lo
    if x>hi:
        return hi
    if x>=lo and x<=hi:
        return x
print(clip(3,4,5))
print(clip(3,2,5))
print(clip(3,7,5))
