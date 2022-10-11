#delete given file from disk
import os
while True:
    try:
        FileName = input("Enter file name to delete")
        os.remove(FileName)
        print("File deleted from disk")
        break
    except FileNotFoundError:
        print(f"enter a valid filename :{FileName}")
