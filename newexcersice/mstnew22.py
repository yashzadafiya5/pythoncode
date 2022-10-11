# 22. Find Duplicate Values using Python # Finding Duplicate Items in a Python List
# numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]

# duplicates = [number for number in numbers if numbers.count(number) > 1]
# unique_duplicates = list(set(duplicates))

# print(unique_duplicates)
items = [{'name':'Nik'}, {'name': 'Kate'}, {'name':'James'}, {'name':'Nik'}, {'name': 'Kate'}]
unique_items = [{'name':'Nik'}]

ok=[]
for i in items:
    if i not in unique_items:
        ok.append(i)
    
print(ok)
