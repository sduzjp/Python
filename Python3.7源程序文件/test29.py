import time
for i in range(3):
    print(i)
    t1=time.time()
    time.sleep(1)
    t2=time.time()
    print(t2-t1)
