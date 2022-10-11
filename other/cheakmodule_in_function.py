'''from inspect import getmembers
import math
    
functions_list = getmembers(math, getmembers)

print(functions_list )'''

import math

def getmethods(modulename):
    print(modulename)
    list=dir(modulename)
    for i in list:
        print(i,end=' ')
        j=i.split(' ')
        print(j)

getmethods(math)

'''
def welcome(name):
    print(  ' hello to '+name+' analistic vidhya ' )

name=input('enter a name')
welcome(name)
'''