import collections
n=9
ar=[10,12,25,21,45,12,23,45,11,21]
now=[]
for i in ar:
    final=([item for item, count in collections.Counter(ar).items() if count > 1])
    o=len(final)
print(o)
    # if i not in final:
    #     now.append(i)
    