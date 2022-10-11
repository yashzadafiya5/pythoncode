# 4. Group Elements of Same Indices 

io=([12,25,30],[20,35,40],[10,45,50],[30,50,60])
lol=[]
ok=0
while ok<3:
        int = [i[ok] for i in io]
        lol.append(int)
        ok=ok+1
print(lol)

