# 3. Find Missing Number 

# numbers=[1,2,4,5,6,7,8,9,10]
# i=[1,2,3,4,5,6,7,8,9,10]

# userlist=sum(numbers)
# lists=sum(i)

# missingnumber=lists-userlist
# print(missingnumber)

########################################################

numbers=[1,2,5,6,7,9,10,12]

maxnumber=max(numbers)

for row in range(1,maxnumber+1):   
    if row not in numbers:
        print(row,end=' ')
        
    
