#write a program to print following pattern 
#1 8 27 64 .... 10000

count=1

while count<=100:
    squer=count * count * count
    print(squer,end = ' ')
    count=count+1
