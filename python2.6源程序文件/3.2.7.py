import math
def perfectSquare(n):
    m=math.sqrt(n)
    p=int(m)
    if p*p==n:
        return True
    else:
        return False
print(perfectSquare(1))
print(perfectSquare(0))
print(perfectSquare(4))
print(perfectSquare(3))
