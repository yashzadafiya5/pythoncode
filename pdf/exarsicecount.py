user=input("enter a value:")
o=""
word=user[0]
count=0

for i in user:
    if word==user:
        count+=1
    else:
        result=o+str(i)+count
        count=1
        result=user
result=o+str(i)
print(result)