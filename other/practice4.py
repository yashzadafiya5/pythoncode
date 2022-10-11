#one number are guess user for a 9 try 



i=0
while i<=9:
    number=int(input('enter a number'))
    if number==5:
        print('you won this game')
        break
    else:
        print(f'please try again your number is not correct :{number}')
    i=i+1