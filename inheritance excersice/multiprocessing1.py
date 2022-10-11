import multiprocessing
from datetime import datetime
def getSquare(start,stop):
    stop=stop+1
    for number in range(start,stop):
        square = number * number
        print(f"square of {number} = {square}")
    
if __name__ == '__main__':
    num1 = int(input("enter start value"))
    num2 = int(input("enter stop value"))
    first_start = num1
    first_end = int(num2/2)

    second_start = first_end + 1
    second_end = num2
    print(f"{first_start} {first_end} {second_start} {second_end}")
    process1 = multiprocessing.Process(target=getSquare,args=(first_start,first_end,))
    process2 = multiprocessing.Process(target=getSquare,args=(second_start,second_end,))
    start_time = datetime.now()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print("before function start",start_time)
    print("after function ends",datetime.now())