# Write a Python code to segregate 0's and 1's (All 0's on left side and 1's on right side) from the given list.
List = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
left=[]
right=[]
for i in List:
    if i==0:
        left.append(i)
    else:
        right.append(i)

print(List)
print(left+right)
  