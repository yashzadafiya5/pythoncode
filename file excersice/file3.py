#write a program to read numbers from numbers.txt and store all numbers into aseconding order into sorted_number.txt 

numberfile=open('number1.txt','r')
numbers = []
for i in numberfile:
    list = i.split("\t")
    for item in list:
        numbers.insert(0,item)
numbers.sort()
sortedfile=open('sorted_number.txt','w')
for j  in numbers:
    sortedfile.write(str(j)+"\t")
    
sortedfile.close()
numberfile.close()

