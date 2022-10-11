# 2. Group Anagrams using Python 

lists=['me','param','now','le','vishal','won','new']
new='new'
ok=[]
ele=[]
for p in lists:
    ok.append(list(p))
for i in range(0,len(lists)-1):
    listToStri = ''.join([str(param) for param in ok[i]])
    ele.append(listToStri)
    print(ele[i])
    # if new in ele[i]:
    #     print(new)
        # listToStri = ''.join([str(param) for param in ok[i]])
        # ele.append(listToStri)
# print(ele)
# print(ok[1])
