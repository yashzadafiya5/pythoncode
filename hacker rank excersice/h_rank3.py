
def getfizzfuzz(number):
    for i in range(number):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        
if __name__=="__main__":
    number=int(input("enter a  number:"))
    getfizzfuzz(number)