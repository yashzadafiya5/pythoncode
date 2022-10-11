#rename existing file 
import os 
while True:
    try:
        CurrentFileName = input("Enter Current File Name")
        NewFileName = input("Enter new file name")
        os.rename(CurrentFileName,NewFileName)
        print("file renamed successfully")
        break
    except FileNotFoundError:
        print(f"enter a excist file:{CurrentFileName} ")