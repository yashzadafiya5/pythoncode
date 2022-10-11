# 17. Match Sequences using Python 

i1=["yash","ram","lakum","param"]
i2=["nerav","modi","lakum","param","dhaivat"]

ranges=len(i1)
ranges2=len(i2)
if ranges>ranges2:
    r=ranges
else:
    r=ranges2

for i in range(0,r+1):
    if i1 in i2:
        print(i1)
    if i2 in i1:
        print(i2)