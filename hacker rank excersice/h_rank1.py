def getvalue(number):
    for i in range(number+1):
        if  i%2 !=0:
            print(f"Weird:{i}")
        # else:
        #     print(f"Not Weird:{i}")
        if int(i)in range(2,5+1):
            if i%2==0:
                print(f"Not Weird:{i}")
            # else:
            #     print(f"Weird:{i}")
        if int(i)in range(6,20+1):
            if i%2==0:
                print(f"Weird:{i}") 
            # else:
            #     print(f"Not Weird:{i}")
        if int(i)>20: 
            if int(i)%2==0:
                print(f"Not Weird{i}") 
            # else:
            #     print(f"Weird:{i}")      
if __name__=="__main__":     
    number=22
    getvalue(number)