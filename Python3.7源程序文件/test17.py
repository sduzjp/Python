def func_test(key1,key2,key3=23):
    print("k1=%s,k2=%s,k3=%s"%(key1,key2,key3))

print("====func_test")
func_test('v1','v2')
func_test('ab','cd',768)
func_test(key2='kk',key1='k')
