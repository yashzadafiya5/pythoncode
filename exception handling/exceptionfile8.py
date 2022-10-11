#write a program to create, change directory as well as get current working directory and remove directory
import os 
while True:
    try:
        DirectoryName = input("Enter directory name") 
        print("Directory Created")


        
        CurrentWorkingDirectory = os.getcwd() 
        print(CurrentWorkingDirectory)

        os.chdir(DirectoryName) 
        CurrentWorkingDirectory = os.getcwd() 
        print(CurrentWorkingDirectory)

        os.mkdir("sub_directory1")
        os.mkdir("sub_directory2")
        os.mkdir("sub_directory3")

        print("sub directories created....")

        os.rmdir("sub_directory1")
        print("Directory removed....")
        break
    except FileExistsError:
        print(f'this file is already create :{DirectoryName}')
