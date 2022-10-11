'''
    10) Write a Python program to calculate final electricity bill based upon below given criteria. take monthly electricity unit from user as input.
    units           price  per unit 
<100                 1
>100 & <200          2 
>200 & <300          3
>300 & <400          4
>400                 5

also calculate 5% percentage energy charge on total bill amount & display total amount  
'''
unit=int(input("enter a unit = "))

if (unit>0 and unit<100):
    print("bill rate =",unit*1 + unit/5)
elif (unit>=100 and unit<200):
    print("bill rate=",unit*2 + unit/5)
elif (unit>=200 and unit<300):
    print("bill rate=",unit*3 + unit/5)
elif (unit>=300 and unit<400):
    print("bill rate=",unit*4 + unit/5)
elif unit>=400:
    print("bill rate=",unit*5 + unit/5)
else:
    print(" your unit value is invalid ")



    
