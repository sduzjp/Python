def div(m,n):
    cnt=0
    sum=m
    while sum>=n:
        sum-=n
        cnt+=1
    return cnt
print(div(25,15))
print(div(100,15))
print(div(25,5))
