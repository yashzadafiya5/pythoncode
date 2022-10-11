'''
write a program to read content from one file and write all the words in reverse into reverse_words.txt file 
friends.txt => param ronak vishal
reverse_words.txt = > marap kanor lahsip
'''     
myfile=open('file5.txt','r')
    
for i in myfile:
    lists = i.split('\n')
print(lists)
for j in lists:
    j=list(j)
    
    j.reverse()
    print(f'your reversed value={j}')

f1=open('file6.txt','w')
for item  in j:
    f1.write(str(item)+"\t")
myfile.close()
f1.close()