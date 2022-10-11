# 2) create class MathCalculator using constructor, instance variables for two numbers
# this class should have method following methods 

# addition
# substraction
# division
# multiplication 



class Mathcalculater:
    def __init__(self,number1,number2,process):
        self.number1=number1
        self.number2=number2
        self.proccess=process
    def displayMathcalculater(self):
        
        addition="+"
        substraction="-"
        division="/"
        multiplication="*"
        addition=number1+number2
        if self.proccess=="+":
            print(f"addition: {number1} + {number2} = {addition}")
        substraction=abs(number1-number2)
        if self.proccess=="-":
            print(f"substraction: {number1} - {number2} = {substraction}")
        division=number1/number2
        if self.proccess=="/":
            print(f"division: {number1} / {number2} = {division}")
        multiplication=abs(number1*number2)
        if self.proccess=="*":
            print(f"multiplication: {number1} * {number2} = {multiplication}")
        
        return addition,substraction,division,multiplication

number1=int(input("enter a number:="))    
number2=int(input("enter a number:="))
process=input("what process you get.ex(+,-,*,/):==")
    
b1=Mathcalculater(number1,number2,process)
b1.displayMathcalculater()

