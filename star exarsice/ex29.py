#print hollow full peramid pattern using a stars

r=5
for i in range(1,r+1):
    for j in range(1,2*r):
        if (i==r and j%2!=0) or i+j==r+1 or j-i==r-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()