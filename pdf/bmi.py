#1) create class BmiCalculator using constructor, instance variables this class should have method getBMI() Which return BMI.

class Bmi:
    def __init__(self,weight,heightft,heightin):
        print("constructor called....")
        self.hightft=heightft
        self.heightin=heightin
        self.weight=weight
    def getdisplay(self):
        foot=self.heightin/12
        total_foot=foot+self.hightft
        meter=total_foot/3.281
        BMI = self.weight/(meter*meter)
        print(f"You BMI is {BMI}")
        if BMI <= 18.4:
            print("You are underweight.")
        elif BMI <= 24.9:
            print("You are healthy.")
        elif BMI <= 29.9:
            print("You are over weight.")
        elif BMI <= 34.9:
            print("You are severely over weight.")
        elif BMI <= 39.9:
            print("You are obese.")
        else:
            print("You are severely obese.")
        return BMI

weight = int(input("Enter your weight in kg: "))
heightft = int(input("Enter your height (feet): "))    
heightin = int(input("Enter your height (inches): "))   
b1=Bmi(weight,heightft,heightin)
b1.getdisplay()        
