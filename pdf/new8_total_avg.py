# 8) create function that calculate & return Find total,average from given arguments 
# def total_avg(n):
ok=[]  
def totl_avg(ok):
    total=(sum(ok))
    print(f"total={total}")
    avrage=sum(ok)/len(ok)
    print(f"avrage={avrage}")

n1=int(input("enter a n:"))
n2=int(input("enter a n1:"))
n3=int(input("enter a n2:"))
n4=int(input("enter a n3:"))
ok.append(n1)
ok.append(n2)
ok.append(n3)
ok.append(n4)
totl_avg(ok)