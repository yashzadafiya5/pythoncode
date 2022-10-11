#write a program to findout octal number of given decimal number using recursion

def getoctal(number):
    if number>0:
       reminder=number%8
       number=number//8
       getoctal(number)
       print(reminder,end=' ')
        
number = int(input("Enter number"))
getoctal(number)
