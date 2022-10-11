# 9) create function that calculate & return day of the week from the given date


import calendar
from calendar import day_name
def findDay(day,month,year):
    date = calendar.weekday(year, month, day)
    
    return (day_name[date])
 
day=int(input("enter a day:"))
month=int(input("enter a month:"))
year=int(input("enter a year:"))
print("this is your day : ",findDay(day,month,year))

# from calendar import day_name
# from datetime import datetime
 

# def getday(date):
    
#     date=datetime.strptime(date, "%d %m %Y").weekday()
#     return(day_name[date])

# date="10 01 2002"
# print(getday(date))