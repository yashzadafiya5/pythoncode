#write a program to print all files and directories name of given directory name ,'new1','vegitables'
import os as yash

directoryname=input('enter a exicits directory name')
directories=yash.listdir(directoryname)
for i in directories:
        print(i)

