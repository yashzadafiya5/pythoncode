
'''
create a half peramid 
* 
*   *
*   *   *
*   *   *   *
'''
'''
number=0
while number<6:
    i=0
    while i<=number:
        if number==6 or number==2  or number==1:
            print(' ',end=' ')
        elif i<=5 and i<number:
            print('*',end=' ')
        i=i+1
    print(" ")
    number=number+1
'''

'''
create a inverted half peramid
*   *   *   *   *
*   *   *   *
*   *   *
*   *
*
number=6
while number>=0:
    i=0
    while i<number:
        print('*',end=' ')
        i=i+1
    print(" ")
    number=number-1
'''
'''
create a hollow inverted peramind 
*   *   *   *   *   *
*               *
*           *
*       *
*   *
*    
number=6
while number>=0:
    i=1
    while i<=number:
        if number==6 or number==1 or number==2:
            print('*',end=' ')
        elif  i>=2 and i<number:
            print(' ',end=' ')
        else:
            print('*',end=' ')
        i=i+1
    print(' ')
    number=number-1           
'''
n=5
for i in range(n):
    for k in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print('')
'''
 
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
n=5
for i in range(n):
    for k in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print('')
''' 