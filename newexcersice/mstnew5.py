# 6. Calculate Execution Time of a Python Program 

import time

starttime=time.time()

i=0
for a in range(100000):
    i+=a
# time.sleep(3)
print(i)

endtime=time.time()
if endtime>12:
    endtime=endtime-24
    
finaltime=starttime-endtime
print(finaltime)


