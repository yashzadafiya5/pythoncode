
number1=int(input("enter a number:="))    
number2=int(input("enter a number:="))
proccess=input("enter a what process you do symbole:")
addition="+"
substraction="-"
division="/"
multiplication="*"
addition=number1+number2
if proccess=="+":
    print(f"addition: {number1} + {number2} = {addition}")
substraction=abs(number1-number2)
if proccess=="-":
    print(f"substraction: {number1} - {number2} = {substraction}")
division=number1/number2
if proccess=="/":
    print(f"division: {number1} / {number2} = {division}")
multiplication=abs(number1*number2)
if proccess=="*":
    print(f"multiplication: {number1} * {number2} = {multiplication}")
# "=========================================================================================================================="
# weight = float(input("enter your mass in kilogram (kg) : "))
# heightft = int(input("Enter your height (feet): "))    
# heightin = int(input("Enter your height (inches): "))

# foot=heightin/12
# foot_inch=heightft+foot
# mt=foot_inch/3.281
# bmi=weight/(mt*mt)
# print(bmi)
"===================================================================================================================="
