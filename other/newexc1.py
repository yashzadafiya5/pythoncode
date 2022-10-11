# write a program to create to LOTRY three single numbers are three time same than you won a latry .

import random

def rendomnumber():
    
    
    first = random.randint(1,10)
    second=random.randint(1,10)
    third=random.randint(1,10)
    
    print(first)
    print(second)
    print(third)

    if first==second and second==third and third==first:
        print('you are a lucky person you have won a lotry')
rendomnumber()



