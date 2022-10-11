#2) create function that count & return how many vowels are there in given string


def countvovel(string):
    count=0
    for i in string:
        if i == "a" :
            print(f"yes i found vovel :={i}") 
            count+=1
        elif i=="e":
            print(f"yes i found vovel :={i}")
            count+=1
        elif i=="i":
            print(f"yes i found vovel :={i}")
            count+=1
        elif i=="o":
            print(f"yes i found vovel :={i}")
            count+=1
        elif i=="u":
            print(f"yes i found vovel :={i}")
            count+=1
    print(count)   

    
string=input("enter a random string :")
countvovel(string)
