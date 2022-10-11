# Reversing a String using Python

# i="this is new car"[::-1]

# print((i))
def riverse(string):
    i=""
    for k in string:
        i=k+i
    print(f"The reversed string(using loops) is :{i} ")


# print(reverse(s))
string=input("enter a any random word")
riverse(string)
