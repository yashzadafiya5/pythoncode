# 32. Find the Number of Capital Letters in a File 

import string 


file=open("new.txt","r")

for i in file:
    ok=i.split()
    # if ok in string.ascii_uppercase:
    #     print(ok)

# print(ok)
for c in ok:
    if string.ascii_uppercase in c :
        print(c)