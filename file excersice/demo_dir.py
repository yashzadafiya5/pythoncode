#demo for dir method in python 
import math 
import os 
import random 
def ListMethods(ModuleName):
    print("-"*100)
    print(f"list of methods & contant in {ModuleName}")
    print("-"*100)
    list = dir(ModuleName)
    for item in list:
        print(item)
    print("-"*100)
ListMethods(os)
ListMethods(math)
ListMethods(random)