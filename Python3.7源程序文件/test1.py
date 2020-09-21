import datetime

dtstr=input('Enter the datetime :(20170228):')
dt=datetime.datetime.strptime(dtstr,"%Y%m%d")
another_dtstr=dtstr[:4]+'0101'
another_dt=datetime.datetime.strptime(another_dtstr,"%Y%m%d")
print(int((dt-another_dt).days)+1)
