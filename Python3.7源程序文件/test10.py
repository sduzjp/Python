for i in range(1,100):
    n=i
    step=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        step+=1
    else:
        print(i,"trapped!",step,"steps")
