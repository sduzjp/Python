import datetime
today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=1)
print(yesterday)
hours=today-datetime.timedelta(hours=1)
print(hours)
