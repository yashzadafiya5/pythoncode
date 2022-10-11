# 4) create function that findout & return GCD from given two number 

def getgcd(num1,num2):
    if num1>num2:
        minimum= num2
    else:
        minimum= num1
    for i in range(1,minimum+1):
        if num1%i==0 and num2%i==0 :
            gcd=i
    print(gcd)       
            

num1=int(input('enter a rendom number'))
num2=int(input("enter a rendom number"))

getgcd(num1,num2)