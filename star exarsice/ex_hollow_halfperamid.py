'''#hollow inverted half peramid
j=5
i=0

while i<=3:
    print("*",end='  ')
    i=i+1
   
i=0
while j>=0:
    number=0
    print("")
    print("*",end='')
    while number<=j:
        print(" ",end='')
        number=number+1
    print("*",end='')
    number=0
    
    j=j-1
print("")
print("*",end='')


'''
n=8
for i in range(n):
    for j in range(i,n):
        if  i==0 or j==0 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
            
    print()