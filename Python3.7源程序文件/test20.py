def issxhs(n,m):
    t=0
    temp=n
    while temp>0:
        m1=temp%10
        t=t+m1**m
        temp=temp//10
    else:
        if n==t:
            print("True")
        else:
            print("False")
issxhs(153,3)
issxhs(1634,4)
