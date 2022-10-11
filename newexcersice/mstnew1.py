# 1. Number Guessing Game ***completed***
i=0
while i<9:
    print("guess any number between 1 to 100")
    number=int(input("enter a your choice"))
    if number==5:
        print("you are lucky you won the game....")
        break
    else:
        print("please try again....")
        i=i+1
print("thanks for playning better luck next time")



