y=2100
m=2
adict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if m!=2:
    print(adict[m])
else:
    if y%4==0 and y%100!=0 or y%400==0:
        print(adict[m]+1)
    else:
        print(adict[m])
