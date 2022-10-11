#5) create function that findout & return LCD from given two number 

def getlcd(num1,num2):
    if num1>num2:
        mn= num2
    else:
        mn= num1
    for i in range(1,mn+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    lcd=(num1*num2)/gcd
    print(round(lcd))     

num1=int(input('enter a rendom number'))
num2=int(input("enter a rendom number"))

getlcd(num1,num2)