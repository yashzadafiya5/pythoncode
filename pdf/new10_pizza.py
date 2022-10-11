# # 10)  create function that calculate & return Per Inch Cost of a Round Pizza from given size and price
import math
import time

def pizz_per_inch(inch,price):
    radius=inch/2
    area=math.pi*(radius*radius)
    print(area)
    perinch=price/area
    perinchprice=perinch/price
    print(perinchprice)
    print(f"Your cost per square inch = {perinch}")
print("hello welcome to dominis'pizza.......")
time.sleep(4)
print("please select your pizza .......")
name=input("enter your name:")
inch=int(input("enter a pizz inch:="))
price=int(input("enter a pizz price:="))
pizz_per_inch(inch,price)
time.sleep(2)
print(f" {name} please wait your order will be ready in few minutes :)")
