'''write a program to print following series (pentagonal  number)
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176 ... 300'''

number=1
while number<15:
    result = int((3*number*number-number)/2)
    number=number+1
    print(result,end=' ')