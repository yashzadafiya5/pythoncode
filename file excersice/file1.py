# write a program to create list which has 5 files. print content of each and every file on screen 

list=['number1.txt','file2.txt','file1.txt','file3.txt','file4.txt ','file5.txt']
for i in list:
    filename=open(i,'r')
    for number in filename:
        print(number)

    
    

