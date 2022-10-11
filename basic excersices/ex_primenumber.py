#write a program to findout all the prime number between given range 

lower=int(input("enter a lower value"))
upper=int(input("enter uper value"))


for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)