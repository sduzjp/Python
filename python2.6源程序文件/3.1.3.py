def arithmeticIf(v,a,b,c):
    if v>0:
        return a
    elif v==0:
        return b
    elif v<0:
        return c
print(arithmeticIf(1,2,3,4))
print(arithmeticIf(0,1,'True',0))
print(arithmeticIf(-1,1,2,[0,1]))
