#write a program to create new given file(if not exists) otherwise open and write/append given content into it 
while True:
    try:
        FileName = input("Enter new File name to write content in it")
        file = open(FileName,"a") # r = read mode 
        print("File created successfully")
        Content = input("Enter some content to write in file")
        Content = '\n' + Content
        file.write(Content)
        file.close()
        print("File closed successfully")
        break
    except PermissionError as error:
        print(error)
        print(f"you have not access this file={FileName}")
    except OSError:
        print('this is invalid input')