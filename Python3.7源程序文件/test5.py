mylist=[1,2,3,4]
A=[mylist]*3
print(A)
mylist[2]=45
print(A)
print(id(mylist))
print(id(A))
