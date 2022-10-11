'''
create module which has following methods 
    ReadFile(FileName) return text content of given file 
'''
lists=['number1.txt','file1.txt','file2.txt']
    
def getfile(lists):
    
    for i in (lists):
        filename=open(i,'r')
        for number in filename:
            print(number)


getfile(lists)

    


