number=int(input('enter a number:'))
if number>0:
    reminder=number%16
    number=number//16
    print(reminder) 


word=input("enter a rendom word:")
try:
    a1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    a2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in word:
        if i in a1 or i in a2:
            if i == "a":
                print(61,end=' ')
            elif i == "b":
                print(62,end=' ')
            elif i == "c":
                print(63,end=' ')
            elif i == "d":
                print(64,end=' ')
            elif i == "e":
                print(65,end=' ')
            elif i == "f":
                print(66,end=' ')
            elif i == "g":
                print(67,end=' ')
            elif i == "h":
                print(68,end=' ')
            elif i == "i":
                print(69,end=' ')
            elif i == "j":
                print('6A',end=' ')
            elif i == "k":
                print('6B',end=' ')
            elif i == "l":
                print('6C',end=' ')
            elif i == "m":
                print('6D',end=' ')
            elif i == "n":
                print('6E',end=' ')
            elif i == "o":
                print('6F',end=' ')
            elif i == "p":
                print(70,end=' ')
            elif i == "q":
                print(71,end=' ')
            elif i == "r":
                print(72,end=' ')
            elif i == "s":
                print(73,end=' ')
            elif i == "t":
                print(74,end=' ')
            elif i == "u":
                print(75,end=' ')
            elif i == "v":
                print(76,end=' ')
            elif i == "w":
                print(77,end=' ')
            elif i == "x":
                print(78,end=' ')
            elif i == "y":
                print(79,end=' ')
            elif i == "z":
                print("7A",end=' ')
            if i == "A":
                print(41,end=' ')
            elif i == "B":
                print(42,end=' ')
            elif i == "C":
                print(43,end=' ')
            elif i == "D":
                print(44,end=' ')
            elif i == "E":
                print(45,end=' ')
            elif i == "F":
                print(46,end=' ')
            elif i == "G":
                print(47,end=' ')
            elif i == "H":
                print(48,end=' ')
            elif i == "I":
                print(49,end=' ')
            elif i == "G":
                print('4A',end=' ')
            elif i == "K":
                print('4B',end=' ')
            elif i == "L":
                print('4C',end=' ')
            elif i == "M":
                print('4D',end=' ')
            elif i == "N":
                print('4E',end=' ')
            elif i == "O":
                print('4F',end=' ')
            elif i == "P":
                print(50,end=' ')
            elif i == "Q":
                print(51,end=' ')
            elif i == "R":
                print(52,end=' ')
            elif i == "S":
                print(53,end=' ')
            elif i == "T":
                print(54,end=' ')
            elif i == "U":
                print(55,end=' ')
            elif i == "V":
                print(56,end=' ')
            elif i == "W":
                print(57,end=' ')
            elif i == "X":
                print(58,end=' ')
            elif i == "Y":
                print(59,end=' ')
            elif i == "Z":
                print("5A",end=' ')
except ValueError:
    print(f"invalid input{number}")   