#3) write a program to findout lcd of given two number using loop
number1=int(input('enter a rendom number'))
number2=int(input("enter a rendom number"))

if number2>number1:
    mn=number1
else:
    mn=number2

for i in range(1,mn+1):
    if number1%i==0 and number2%i==0:
        gcd=i
        
lcm=int((number1*number2)/gcd)
print(lcm)