#write a program to merge two given file into third file 


filename=open('number1.txt','r')
secondfile=open('file1.txt','r')
thirdfile=open("file2.txt",'w')

for i in filename:
    print(i,end='')
    thirdfile.write(i)
for j in secondfile:
    print(j,end=' ')
    thirdfile.write(j)


filename.close()
secondfile.close()
thirdfile.close()

