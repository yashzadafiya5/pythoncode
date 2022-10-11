  
n=5
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=" ")
    print()
 
 
n=6
for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or j==i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
     

n=5
for i in range(n):
    for j in range(i,n):
        if i==0 or j==i or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
   
'''
                *
            *       *
        *               *
    *                       *
*   *   *   *   *   *    *     *   
      

'''
n= int(input('enter a number'))
for i in range(n):
    for j in range(i+1):
        if i==n-1 or i+j==n-1 or i==j :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

 

n=5
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()    
    