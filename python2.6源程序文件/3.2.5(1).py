import math 
def prime(n):
    i=2
    k=math.sqrt(n)
    flag=1
    while i>=2 and i<=int(k):
        if n%i==0:
            flag=0
            break
        i+=1
    if flag==1:
        return True
    #elif flag==0:
    else:
        return False
print(prime(2))
print(prime(4))
print(prime(5))
