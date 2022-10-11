# 1. Write a python code to display numbers from 10 to 1 in reverse order without using any built methods

num=123456789
print(str(num)[::-1])

number=987654321

i=0
while number>0:
    last_number=number%10
    i=i*10+last_number
    number=number//10
print(i)

name=123456789

print(str(name)[::-1])


i="123 yash"
print(str(i)[::-1])