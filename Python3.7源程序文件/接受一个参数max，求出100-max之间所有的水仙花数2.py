def issxhs(n,m):
    t=0
    temp=n
    while n>0:
        m1=n%10
        t=t+m1**m
        n=n//10#循环结束后n已经不是开始时的n！
    else:
        if temp==t:
            return True
        else:
            return False
def printf_sxhs(max):
    s=[]
    for i in range(100,max):
        temp=i
        cnt=0
        while temp>0:
            cnt+=1
            temp=temp//10
        if issxhs(i,cnt)==True:
            s.append(i)
    print(s)
max=2000
printf_sxhs(max)

        
