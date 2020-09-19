import time

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())
# x=time.localtime()
# print("""
# Year : {0}
# Month: {1}
# Day : {2}
# """.format(x[0],x[1],x[2]))

import time
from time import time as timer
import random

input("Enter to start")

wait=random.randint(1,6)
time.sleep(wait)
start=timer()
input("Enter to stop")
end=timer()
print("started at " + time.strftime("%X",time.localtime(start)))
print("ended at " + time.strftime("%X",time.localtime(end)))
print("reaction time {}".format(end-start))








