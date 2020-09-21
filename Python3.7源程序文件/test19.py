def func_test3(**kwargs):
    for key,val in kwargs.items():
        print("%s=%s"%(key,val))

print("====func_test3")
func_test3(myname='Tom',sep='comma',age=23)
