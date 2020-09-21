import time
from datetime import datetime,timedelta

print(time.time())

print(datetime.now())
print(datetime(2018,1,1))
print(datetime.strptime("2018/01/01","%Y/%m/%d"))
print(datetime.fromtimestamp(time.time()))
print(datetime.fromtimestamp(time.time()).strftime("%Y/%m"))

dt1=datetime(2018,1,1) + timedelta(days=1,seconds=1000)
dt2=datetime.now()
print(dt2-dt1)
dur=dt2-dt1
print(dur.days)
print(dur.seconds)
print(dur.total_seconds())