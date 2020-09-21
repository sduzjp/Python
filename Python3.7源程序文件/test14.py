def addnum():
    global num1,num2
    num1,num2=2,3
    return(num1+num2)
num1=1
num2=2
addnum()
print("%d %d %d"%(num1,num2,addnum()))
