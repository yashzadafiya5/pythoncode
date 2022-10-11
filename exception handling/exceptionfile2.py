#write a program to create new given file and write given content into it 
try:
    FileName = input("Enter new File name to write content in it")

    file = open(FileName,"w") # r = read mode 
    print("File created successfully")
    Content = input("Enter some content to write in file")
    file.write(Content)
    file.close()
    print("File closed successfully")
except PermissionError:
    print("you have not a access this file")