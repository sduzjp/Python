def mod(m,n):
    sum=m
    while sum>=n:
        sum-=n
    return sum
print(mod(25,15))
print(mod(25,5))
