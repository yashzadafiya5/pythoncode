# 3) create function that count & return how many words are there in given string

# def countvovel(string):
#     count=0
#     for i in string:
#         if i == "a" :
#             print() 
#         elif i=="e":
#             print()
#         elif i=="i":
#             print()
#         elif i=="o":
#             print()
#         elif i=="u":
#             print()
#         else:
#             print(f"word is constants :{i}")
#             count+=1
#     print(count)  
    

    
# string=input("enter a random string :")
# countvovel(string)

from string import ascii_letters

def countwords(string):
    count=0
    for i in string:
        if i in ascii_letters:
            print("yes i found word ")
            count+=1
        else:
            print("word is intiger")
    print(count)

string=" hello this is  12 20 30"
countwords(string)