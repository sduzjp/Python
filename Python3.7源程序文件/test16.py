num=[10,20,40,80,160]
lst=[2,4,6,8,10]
def mul3(a):
    return a*3
print(list(map(mul3,num)))
def atob(a,b):
    return a+1.0/b
print(list(map(atob,num,lst)))
print(list(map(lambda a:a*3,num)))
print(list(map(lambda a,b:a+1.0/b,num,lst)))
