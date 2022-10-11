# 31. Find the Most Frequent Words in a File 

# fname=input("enter file name")
fname="new.txt"             

filename=open(fname,'r')
for i in filename:
    words=i.split()
print(max(set(words), key = words.count))

# c=[]
# for a in range(0,len(words)):
#     for b in range(0,len(words)):
#         if words[a]==words[b]:
#             if words[a] not in c:
#                 c.append(words[a])
#             else:
                
#                 e=words[a].count(words[a])
#                 print(set(words[a]))

                