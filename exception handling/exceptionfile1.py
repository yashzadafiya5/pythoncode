#write a program to read given file and display its content on screen
while 1:
    try:
        FileName = input("Enter Existing File name to read its content")
        file = open(FileName,"r") # r = read mode 
        count=0
        for line in file:
            print(line,end='')
            count=count+1
        file.close()
        print("")
        print(f"total lines in file = {count}")
        break
    except FileNotFoundError as error:
        print(error)
        print(f" does not exictes this file={FileName}")
    except PermissionError:
            print('you do not have a permission access file ')