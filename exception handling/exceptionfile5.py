#write a program to read numbers from file if particular number is odd number then write that number into odd.txt file otherwise write that number into even.txt
try:
    NumberFile = open("number.txt","r")
    EvenFile = open("even.txt","a")
    OddFile = open("odd.txt","a")
    for line in NumberFile: #outerloop
        #print(line,end='')
        #first convert line into list 
        list = line.split("\t")
        try:
            for number in list: #inner loop
            
                number = int(number)
                if number%2==0: #even number
                    EvenFile.write(str(number) + '\t')
                else:
                    OddFile.write(str(number) + '\t') 
        except ValueError:
            print("skipped a string data")
    NumberFile.close()
    EvenFile.close()
    OddFile.close()
except FileNotFoundError as error:
    print(error)
    print("enter a valid filename")
    