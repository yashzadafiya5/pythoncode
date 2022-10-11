'''
create module which has following methods 
    getBinary() return binary of given number 
    getOctal() return octal of given number 
    getHexa() return hexadecimal of given number 
'''
def getBin(number):
    if number>0:
        reminder=number%2
        number=number//2
        getBin(number)
        print(reminder,end='')



def getoctal(number):
    if number>0:
        reminder=number%8
        number=number//8
        getoctal(number)    
        print(reminder,end='')

def gethexa(number):
    if number>0:
        reminder=number%16
        number=number//16
        gethexa(number)
        print(reminder,end='') 
        


