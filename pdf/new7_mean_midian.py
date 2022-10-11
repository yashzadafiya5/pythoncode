# 7) create function that calculate & return Find Mean, Median, and Mode from given arguments 


def getmean(i):
    mean=round(sum(i)/len(i))
    print(f"mean is ={mean}")
i={10,20,30}
getmean(i)
def getmedian(i):
    
        if len(i)%2!=0:
            median=(len(i)+1)/2
            print(i[round(median)])
        else:
            median=((len(i)/2)+((len(i)/2) + 1))/2
            print(f"median:{i[round(median)]}")
i=[10,20,30,40,50]
i.sort()
getmedian(i)

def mode(mode, n,  k):
    for i in range(0,  n):
        mode[mode[i]%k] += k
    max = mode[0]
    result = 0
    for i in range(1, n):
        if mode[i] > max:
            max = mode[i]
            result = i
    return result
mode=[10,20,30,20,40,30,10,20]
n = len(mode)
k = 8
print(mode(mode,n,k))



