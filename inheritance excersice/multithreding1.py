import threading


def getsum():
    num=3 
    sum=num*num
    print(sum)
    return num

def getsubs():
    num1=22
    num2=10
    subs=num1-num2
    print(subs)


  
t1=threading.Thread(target=getsum)
t2=threading.Thread(target=getsubs)

t1.start()
t2.start()
t1.join()
t2.join()

