# 50. Merge Sort Algorithm 

Array = [70,50,30,10,20,40,60]
ok=[]
a=round(len(Array)/2)
b=0
while b<a:
    d=Array[b]
    ok.append(d)
    e=round(b/2)-1
    
    b+=1
print(ok[e])

'''c=a
while c<len(Array):
    print(Array[c])
    c+=1'''