'''
    3) write a program to accept month number from user. display message "this month has 28 or 29 days" if month if 
'''

month=int(input("enter a valid month"))

if month==1:
    print("this month is january")
elif month==2:
    print("this month is february,february month in 28 & 29 day ")
elif month==3:
    print("this month is march  ")
elif month==4:
    print("this month is april ")
elif month==5:
    print("this month is may  ")
elif month==6:
    print("this month is june  ")
elif month==7:
    print("this month is julay  ")
elif month==8:
    print("this month is augest ")
elif month==9:
    print("this month is september")
elif month==10:
    print("this month is october")
elif month==11:
    print("this month is navember")
elif month==12:
    print("this month is december")
else:
    print("invalid input")