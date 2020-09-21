def issxhs(n,m):
    t=0
    temp=n
    while n>0:
        m1=n%10
        t=t+m1**m
        n=n//10#循环结束后n已经不是开始时的n！
    else:
        if temp==t:
            print("True")
        else:
            print("False")
issxhs(153,3)
issxhs(1634,4)
