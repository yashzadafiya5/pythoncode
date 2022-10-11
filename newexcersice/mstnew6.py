# 7. Count Number of words in a Column **completed**

# from string import ascii_letters
# alphabets=ascii_letters
# i="hello how are you this is new"
# count=0
# for word in i:
#     if word in alphabets:
#         count=count+1
    
# print(count,end='')

from string import ascii_letters
alphabets=ascii_letters
i="hello how are you this is new"
k=i.split(' ')
print(len(k))



