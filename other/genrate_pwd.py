#genrate password
import random
import string

def pwd(lenght=6):
    seeds=string.ascii_lowercase + string.ascii_uppercase + string.digits
    size=len(seeds)-1
    password=''
    for i in range(0,lenght+1):
        password+=seeds[random.randint(0,size)]
    return password
      
lenght=pwd(int(input('enter a number')))
print(lenght)
