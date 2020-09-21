def p2(x):
    m=1
    if x<=1:
        return 0
    while x>1:
        m*=2
        if m>=x:
            break
    return m/2
print(p2(1))
print(p2(2))
print(p2(5))

        
