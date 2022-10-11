#write a program to delete all files and directories of given directory and then also delete directory itself.
import os
import shutil

def delete(path):
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
        print('your data will be deleting sucessfully:')
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print('your data will be deleting sucessfully:')
    else:
        raise ValueError(f" your path is not file or not link or not a directory {path}")
        

path=input("enter a file path & directory's path")
delete(path)

new_dir=input('enter a name of directory:=')    
os.mkdir(new_dir)
print(os.getcwd())

