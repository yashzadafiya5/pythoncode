# 42. Internet Speed Test using Python 

import pyspeedtest

user=input("enter a you show a speed:")
test = pyspeedtest.SpeedTest(user)
 
print(test.ping())
print(test.download())


