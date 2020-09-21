import time
t1=time.time()
a=0
for i in range(100):
    a+=i
print(a)
t2=time.time()
print(t2-t1)
