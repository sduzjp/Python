def prime(n):
    i=2
    while i>=2 and i<n:
        if n%i==0:
            break
        i+=1
    if n==i:
        return True
    else:
        return False
print(prime(2))
print(prime(4))
print(prime(5))
