# 47. Password Authentication using Python 

import getpass
database = {"aman.kharwal": "123456", "yash": "123456"}
username = input("Enter Your Username : ")
password=getpass.getpass("enter a password")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
            break
print("Verified")