#1) create function that convert return given ceilcius into farenheit

def farenhit(ceilcius):
    farenheit= (ceilcius * 1.8) + 32
    return farenheit

ceilcius=float(input("enter a ceilcius :="))
print(f" ceilciusfarenhit:={round(farenhit(ceilcius))} F")
