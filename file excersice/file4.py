#write a program to findout whether given word exist in given file or not

filename=open('file1.txt','r')
serchword=input('enter a word :')

for i in filename:
    lists =i.split(' ')

if serchword in lists:
    print(f'your word found :={serchword}')
else:
    print(f'your word is not found :={serchword}')
