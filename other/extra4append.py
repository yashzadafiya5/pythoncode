#2) Write a program that appends the square of each number to a new list.

list=[12,25,30,5,10]
newlist=[]
for i in list:
    square=i*i
    newlist.append(square)

print(f'givin list :={list}')  
print(f'retuern newsquerlist :={newlist}')

