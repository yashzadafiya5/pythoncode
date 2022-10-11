'''write a program to print following series (Lucas series)/
    2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 300
'''
def lucas(n):

    a=2
    b=1
    if (n==0):
        return a
    for i in range(2,n+1):
        print(b, end = ' ')
        c = a+b
        a=b
        b=c
    return b
n=int(input('enter a number'))
print(lucas(n))

    
