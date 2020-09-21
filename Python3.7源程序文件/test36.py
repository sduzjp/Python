import shelve
d=shelve.open('filename')
d[key]='data'
del d[key]
flag=key in d
klist=list(d.keys())
d['xx']=[0,1,2]
d['xx'].append(3)
temp=d['xx']
temp.append(5)
d['xx']=temp
d.close()
