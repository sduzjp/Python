def fib(x):
     '''assume x an int >=0
          return Fibonacci of x'''
     if x==0 or x==1:
          return 1
     else:
          return fib(x-1)+fib(x-2)
print(fib(5))
print(fib(10))

