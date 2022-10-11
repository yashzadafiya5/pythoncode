'''write a program to print following series (hexagonal number)
1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231 .. 1000'''

number=1

while number<24:
    value=int((2*number*(2*number-1)/2))
    print(value,end=' ')
    number=number+1
