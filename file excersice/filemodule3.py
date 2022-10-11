# WriteFile(FileName,Content) create new file and write content into it. 

def getAddtoFile():
    filename=open('number1.txt','r')
    content=open('newfile1.txt','w')
    for i in filename:
        content.write(i)
    filename.close()
    content.close()

new=getAddtoFile()
print(new)

