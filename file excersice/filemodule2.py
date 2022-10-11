#AddtoFile(FileName,Content) append content into given file

def AddtoFile(files):
    files=open('file1.txt','r')
    thirdfile=open("newdata.txt",'w')

    for j in (files):
        print(j,end='')
        thirdfile.write(j)
    files.close()
    thirdfile.close()

AddtoFile('file2.txt')