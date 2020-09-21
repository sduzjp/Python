#import math
n=2
j=0
while True:
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    if flag==1:
        print("%d"%n)
        j+=1
        if j==5:
            print("\n")
    n+=1
    if j==10:
        break

    
