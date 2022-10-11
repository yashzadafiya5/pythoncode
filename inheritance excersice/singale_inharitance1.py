# 1 create single level inheritance example which has two class 
#     1) kg class 
#         has constructor for grams 
#         has method getKg which return kg of grams 
#     2) Ton class  inherit kg class 
#         has constructor for grams which call parent class constructor
#         has method getTon() which return Ton of grams 

class Kg:
    def __init__(self,kg):
        self.kg=kg
    def returengram(self):
        gram=self.kg* 1000
        print(f"kg:{self.kg} convert gram is :{gram} gram")
        return gram
    
class Ton(Kg):
    # def __init__(self,kg):
    def returenton(self):
        super().__init__(kg)
        tons = (super().returengram() * 1.1023E-6)
        print(f"grams:{super().returengram()} convert ton is :{tons} ton")
        return tons
    # def sum(self):
    #     sum=super().returengram()+self.number
    #     print(sum)
    #     return sum

kg=int(input("enter a kg :"))       
b1=Kg(kg)
       
c1=Ton(Kg)
c1.returenton()

        