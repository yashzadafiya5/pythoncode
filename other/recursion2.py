#write a program to findout octal number of given  hexadecimal number using recursion
def gethexa(number):
    if number>0:
        reminder=number%16
        number=number//16
        gethexa(number)
        print(reminder,end=' ')

hexadecimal=int(input('enter a number'))
hexa=gethexa(hexadecimal)
