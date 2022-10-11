import random
# from PyDictionary import PyDictionary

lists=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0
names=[]
while i<26:
    list=lists[i]
    i=i+1
    name=random.choices(lists,k=4)
    string= ''.join([str(new) for new in name])
    print(string)
    names.append(string)
    
# # print(names)
# dictionary=PyDictionary()
# cheakname=input('enter a name')
# mining=PyDictionary.meaning(cheakname)
# print(mining)

    