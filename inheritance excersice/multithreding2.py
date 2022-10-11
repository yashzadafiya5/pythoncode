import threading

def getBin(number):
    if number>0:
        reminder=number%2
        number=number//2
        getBin(number)
        print(reminder,end=' ')



def getoctal(number):
    if number>0:
        reminder=number%8
        number=number//8
        getoctal(number)    
        print(reminder,end=' ')

def gethexa(number):
    if number>0:
        reminder=number%16
        number=number//16
        gethexa(number)
        print(reminder,end=' ') 
    
i=0
number=int(input("enter a number"))
while i<1:
    binary = getBin(number)
    print('')
    octal = getoctal(number)
    print('')
    hexa = gethexa(number)
    i=i+1

t1=threading.Thread(target=getBin,args=(number))
t2=threading.Thread(target=getoctal,args=(number))
t3=threading.Thread(target=gethexa,args=(number))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
