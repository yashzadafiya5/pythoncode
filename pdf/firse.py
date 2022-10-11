addition=0
class das:
    def __init__(self,num1,num2):
        print("constructor called....")
        self.num1=num1
        self.num2=num2
    def sum(self):
        global addition
        addition=self.num1+self.num2
        # global addition
        return addition
    def display(self):
        print(addition)
num1=10
num2=20
m1=das(num1,num2)
sum=m1.display()
print(sum)

        