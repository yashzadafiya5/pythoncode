# 28. Age Calculator using Python 

from datetime import date

def findage(birthdate):
    days_in_year = 365.2425  
    age = int((date.today() - birthdate).days / days_in_year)
    print((age),"years")

day=int(input("enter a day"))
month=int(input("enter a month"))
year=int(input("enter a year"))
birthdate=date(year,month,day)
findage(birthdate)
