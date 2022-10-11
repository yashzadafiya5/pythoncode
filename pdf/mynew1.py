
# j=[]
# for i in range(1000):
#     j.append(i)    
# print(j,end='')

number=(i for i in range(1000))
print(number)

for l in number:
    m=l*l
    print(m)