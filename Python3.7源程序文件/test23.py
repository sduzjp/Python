import time,datetime
today=datetime.date.today()
print(today.timetuple())
d=time.mktime(today.timetuple())
print(d)
m=datetime.date.fromtimestamp(d)
print(m)
