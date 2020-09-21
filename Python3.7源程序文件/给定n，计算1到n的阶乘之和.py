n=10
m=1
i=2
sum=0
while i<=n+1:
    for a in range(1,i):
        m*=a
    else:
        sum+=m
        m=1
        i+=1
else:
    print(sum)
