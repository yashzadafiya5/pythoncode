# full peramid

n=5
for i in range(1,n):
    for j in range(1,2*n):
        if  j==n and j%2!=0 or j+i==n+1 or i-j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()