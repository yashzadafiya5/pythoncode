'''write a program to print following series (triangular numbers)
    0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... 1000
'''

value=1

while value<45:
    result=int(value*(value+1)/2)
    print(result,end=' ')
    value=value+1