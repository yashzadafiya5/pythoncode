#write a program to findout power of given number using given exponent

count=1
base=int(input("enter a base"))
exponent=int(input("enter a exponent"))
power=base
while count<8:
    count=count+1
    power= power*base
print(power,end="")
 
