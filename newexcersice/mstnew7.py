import random

while True:
    print("press 1 for rock,press 2 for paper,press 3 for scissor")

    user=int(input("enter your choice:"))
    if user==1:
        choice="rock"
    elif user==2:
        choice="paper"
    elif user==3:
        choice="scissor"
    else:
        print("invalid input ")
    print("user choice is: " + choice)

    computerchoice=random.randint(1,3)
    if computerchoice==1:
        computerchoice="rock"
    elif computerchoice==2:
        computerchoice="paper"
    elif computerchoice==3:
        computerchoice="scissor"
    else:
        print("invalid input ")
    print("computerchoice choice is: " + computerchoice)

    if((choice == 1 and computerchoice == 2) or (choice == 2 and computerchoice ==1 )):
        result = "paper"
    elif((choice == 1 and computerchoice == 3) or (choice == 3 and computerchoice == 1)):
        result = "Rock"
    else:
        result = "scissor"
    if choice==computerchoice:
        print("<== it's a tie==>")
    elif result == choice:
        print("<== you are wins ==>")
    elif result == computerchoice:
        print("<== Computer wins ==>")       
    print("Do you want to play again? (Y/N)")
    ans=input("enter your choice (Y/N):")
    if ans=="n" or ans=="N":
        break
print("Thanks for playing")

