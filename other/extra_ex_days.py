#how to find day using date

from datetime import datetime 
from calendar import day_name



def finddate(date):
    date = datetime.strptime(date, "%d %m %Y").weekday()
    return (day_name[date])

date="11 06 2001"
print("this is your day : ",finddate(date))

'''
date=int(input('enter a date'))
month=int(input('enter a month'))
year=int(input('enter a year'))
combine=finddate(date,month,year)
print(combine)
'''