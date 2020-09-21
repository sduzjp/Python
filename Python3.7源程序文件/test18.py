def func_test2(*args):
    for arg,i in zip(args,range(len(args))):
        print("arg%d=%s"%(i,arg))
print("====func_test2")
func_test2(12,34,"abcd",True)
