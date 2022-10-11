#6) write a program to findout whether given letter is value or not. 

value =(input("enter a rendom value"))

if((value >= 'a' and value<= 'z') or (value>= 'A' and value<= 'Z')): 
   print("The Given Character is an Alphabet ", value)
elif(value>= '0' and value<= '9'):
     print("The Given Character is a digit", value)
else:
    print("The Given Character is Not an Alphabet or a digit", value)