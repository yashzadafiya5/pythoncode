class Reminder:
    def __init__(self,number):
        self.number=number
    def reminder(self):
        reminder=self.number%16
        return reminder
    
class Flordivision:
    def __init__(self,num):
        self.num=num
    def division(self):
        division=self.num//16
        return division
class Hexa(Reminder,Flordivision):
    def __init__(self,number,num):
        super().__init__(num)
        super().__init__(number)
    def gethexa(number):
        if number>0:
            re=super().reminder()
            se=super().division()
            print(re,end=' ')
        return se
number=int(input("enter a number:"))
num=int(input("enter a num:"))
h1=Hexa(Reminder,Flordivision)
h1.reminder()
h1.division()
h1.gethexa()
