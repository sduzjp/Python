def multIA(m,n):
    sum=0
    for i in range(n):
        sum+=m
    return sum
def multIAgen(m,n):
    if n>=0:
        return multIA(m,n)
    elif n<0 and m>=0:
        return  -multIA(m,-n)
    #elif n<0 and m<0:
    else:
        return multIA(-m,-n)
print(multIAgen(4,5))
print(multIAgen(4,-3))
print(multIAgen(4,0))
print(multIAgen(0,4))
print(multIAgen(-1,5))
print(multIAgen(-1,-4))
