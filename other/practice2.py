# AddtoFile(FileName,Content) append content into given file
def AddtoFile(filename):
    filename=open('number1.txt','r')
    secondfile=open('file1.txt','r')
    content=open('appendfile_data.txt','a')
    for i in filename:
        content.write(i)
    for j in secondfile:
        content.write(j)
    filename.close()
    content.close()

filename=input('enter a filename')
AddtoFile(filename)