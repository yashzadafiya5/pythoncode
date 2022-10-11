#write a program to findout all the perfect numbers between given range 


count=1
number=int(input('enter a rendom number'))
i=number

sum=0
while count<number:
    if i>1 and i<=number:
        perfect_number=(number%i==0)
        sum=sum+number

    count=count+1    
    if sum==number:
        print("the number is perfect number")
    else:
        print("the number is not a perfect number")
    