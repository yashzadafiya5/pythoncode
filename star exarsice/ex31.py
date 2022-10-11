#hollow inverted peramid
n=6
for i in range(n):
    for j in range(i,n):
        if  i==j or j==n-1 or i==0:
            print(j+1,end=' ')
        else:
            print(' ',end=' ')
    print()