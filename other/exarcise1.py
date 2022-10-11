'''
Original List:
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]'''
'''
#(1)
list=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]


for i in list:
    i=list
i.sort()
print(i)
   ''' 
'''
#(2)get a current date time
import datetime


datetimes=datetime.datetime.now()
print(datetimes)
'''
'''
#3) circule
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2 ))
'''
'''
4.) Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
'''
'''
from datetime import date 
print("Enter first date month year")
firstdate=2
firstmonth=2
firstyear=2
firstdates=datetime(firstdate,firstmonth,firstyear)

print("Enter  second date month year")
seconddate=11
secondmonth=7
secondyear=2
seconddates=datetime(seconddate,secondmonth,secondyear)


print("start date",firstdates)
print("end date",seconddates)
dates= dates(2022,5,3)

firstdates = datetime.combine(date, firstdates)
seconddates = datetime.combine(date, seconddates)
#now substract old time(datetime1) from new time (datetime2)
gap = seconddates - firstdates
print('difference ',gap)
'''
'''
5) Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
'''
'''color_list = ["Red","Green","White" ,"Black"]
print(color_list[0::3])'''
'''
6) Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''
'''
date=(11,12.2014)
print("The examination will start from : %i / %i / %i"%date)
'''
'''
6). Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615

'''
'''number=int(input('enter a rendom number:'))
n1=int('%s'%number)
n2=int('%s%s'%(number,number))
n3=int('%s%s%s'%(number,number,number))

Result=n1+n2+n3
print(Result)'''

'''
7)calander

'''
'''import calendar
day=int(input('enter a day'))
month=int(input('enter a month'))
year=int(input('enter a year'))

print(calendar.month(year,month,day))
'''
'''
8)
'''
'''numbers = [386, 462, 47, 418, 907, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
958,743, 527]
numbers.sort(reverse=True)
print(numbers)'''
from datetime import datetime
now = datetime.now()
print(now)

indian_format_date = now.strftime("%d/%m/%Y %H:%M:%S")
print(indian_format_date)

just_time = now.strftime("%H:%M:%S")
print(just_time)

#how to display time in 12 hours format
hour = int(now.strftime("%H"))
minute = now.strftime("%M")
second = now.strftime("%S")
am_pm = "AM"
if hour>12:
    am_pm = "PM"
    hour = hour - 12
print(F"{hour}:{minute}:{second} {am_pm}")


#lcm 
'''number1=int(input('enter a number'))
number2=int(input('enter a number'))

if number2<number1:
    mx=number1
else:
    mx=number2
lcd=0
for i in range(i,mx+1):
    if mx%number1==0 and mx%number2==0:
        lcd=mx
print(lcd)
'''



