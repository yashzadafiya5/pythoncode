#5) write a program to findout whether given number is odd or even

value=int(input("enter a rendom value"))
reminder=value%2
if  reminder==0:
    print(value," is even number")
else:
    print(value,"is odd number")