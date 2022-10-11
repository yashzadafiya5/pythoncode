# create class BmiCalculator using constructor, instance variables 
# this class should have method getBMI() Which return BMI
class Bmi:
    def __init__(self,heightin,weight):
        self.weight=weight
        # self.foot=heightft
        self.hight=heightin
    def display(self):
        # foot=self.inch/12
        # inch=foot+self.foot
        # meter=inch/0.0254
        # BMI= self.weight/(meter*meter)
        BMI= self.weight/self.hight
        return BMI
name=input("Enter The Name")
print(f"Hello.. {name} welcome to bmi calculator")
weight=int(input("Enter The Weight In Kg."))
# heightft=int(input("enter a hight"))
Answer=int(input("Do You Know Your Height In Meter? if Yes Then Press 1 Else Press 2"))
if Answer==1:
    height=float(input("Enter Your Height"))
elif Answer==2:
    Height=float(input("Enter Your Height In ft."))
    heightin=Height/3.28084
    print(f"your Height In Meter Is= {heightin}")

b1=Bmi(weight,heightin)
bmi=b1.display()
print(f"BMi is = {bmi}")
if bmi<=18.5:
    print(f"Hello {name} You Are UnderWeight")
elif bmi<=24.9:
    print(f"Hello {name} You Have Normal Weight")
elif bmi<=29.9:
    print(f"Hello {name} You Are OverWeight")
elif bmi<=34.9:
    print(f"Hello {name} You Have Obesity Class 1")
elif bmi<=39.9:
    print(f"Hello {name} You Have Obesity Class 2")
elif bmi<=40:
    print(f"Hello {name} You Have Obesity Class 3")

print("Good Bye")