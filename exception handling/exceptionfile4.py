#write a program to read content from one file and write it into another file  
while 1:
    try:   
        ReadFileName = input("enter file name to read content from it")
        WriteFileName = input("enter file name to write content in it")
        FileReader = open(ReadFileName,"r")
        FileWriter = open(WriteFileName,"w")
        for line in FileReader:
            print(line,end='')
            FileWriter.write(line)    
        FileWriter.close()
        FileReader.close()
        print()
        print("File copied successfully")
        break
    except FileNotFoundError :
        print(f"enter a valid file this file is not erxcist={ReadFileName}")
    except PermissionError:
        print(f"you do not have a access this file :{ReadFileName}")