'''print('1',end='\n')

print('1',end=' ')
print('2',end='\n')

print('1',end=' ')
print(' ',end=' ')
print('3',end='\n')

print('1',end=' ')
print(' ',end=' ')
print(' ',end=' ')
print('4',end='\n')

print('1',end=' ')
print('2',end=' ')
print('3',end=' ')
print('4',end=' ')
print('5',end=' ')
'''
'''n=6
for i in range(n):
    j=1
    while j<n:
        if  j==0 or i==n-1 or i==j:
            print(j,end=' ')
            
        else:
            print(' ',end=' ')
            
    print('')
    j=0
    n=n-1
    '''
j=3
i=0
while i<=5:
    print(i,end=' ')
    i=i+1
   
i=0
while j>=0:
    number=0
    print("")
    print(j,end=' ')
    while number<=j:
        print(" ",end=' ')
        number=number+1
    print(j,end='')
    number=0
    
    j=j-1
print("")
print(i,end='')

