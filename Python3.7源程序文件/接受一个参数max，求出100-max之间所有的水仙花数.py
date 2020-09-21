def printf_sxhs(max):
    s=[]
    for i in range(100,max):
        temp=i
        cnt=0
        while temp>0:
            cnt+=1
            temp=temp//10
        t = 0
        temp1 = i
        while temp1 > 0:
            m1 = temp1 % 10
            t += m1 ** cnt
            temp1 //= 10
        if i == t:
            s.append(i)
    print(s)
max=2000
printf_sxhs(max)

