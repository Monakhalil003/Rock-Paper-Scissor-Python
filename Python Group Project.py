import random

print("\n ****Welcome to the Game****")


print("\n You have to choose any of the following choices-->>> rock,paper or scissor")

print("\n Winning Rules:")
print("\n if \n rock vs paper \n than \n paper will win ")
print("\n if \n rock vs scissor \n than \n rock will win ")
print("\n if \n scissor vs paper \n than \n scissor will win ")
print("\n if \n same \n then \n tie <<< Try again dude~~")

while True:
    print("\n What would you like to play?")
    player= int(input("\n Press 1 for playing with computer and 2 for playing with your friend:"))
    if player == 1:
        print("\n ^^Okay...now make your choice^^")
        print("\n ~Enter 1 for Rock~")
        print("\n ~2 for Paper~")
        print("\n ~3 for Scissor~")

        userChoice = int(input("\nYour choice = "))

        if userChoice > 3 or userChoice < 1:
            print("\n Na Na .. choose number between 1-3")
            break

        compChoice = random.randint(1, 3)

        if compChoice == 1:
            compChoiceName = "rock"

        elif compChoice == 2:
            compChoiceName = "paper"

        else:
            compChoiceName = "scissor"

        if userChoice == 1:
            userChoiceName = "Rock"

        elif userChoice == 2:
            userChoiceName = "paper"

        else:
            userChoiceName = "scissor"

        print("\n User's choice is: ", userChoiceName)
        print("\n Computuer's choice is : ", compChoiceName)
        print(userChoiceName + " V/s " + compChoiceName)
        result = "a"
        if userChoice == compChoice:
            result = "draw"
            str(result)

        elif userChoiceName == "paper" and compChoiceName == "rock":
            result = "user win"
            str(result)

        elif userChoiceName == "paper" and compChoiceName == "scissor":
            result = "computer win"
            str(result)

        elif userChoiceName == "scissor" and compChoiceName == "rock":
            result = "computer win"
            str(result)

        elif userChoiceName == "scissor" and compChoiceName == "paper":
            result = "user win"
            str(result)

        elif userChoiceName == "rock" and compChoiceName == "paper":
            result = "computer win"
            str(result)

        elif userChoiceName == "rock" and compChoiceName == "scissor":
            result = "user win"
            str(result)

        if result == "draw":
            print("\n awww... its a tie .. try again")

        elif result == "computer win":
            print("\n o..ooooo!! You Lost ... Don't be sad *** Try Again ")

        else:
            print("\n Hurraaahhh !!!! You Won...")

        print("\n Do you want to play this game again ???")
        ans = int(input("Enter 0 to exit and enter any number to play again: "))
        if ans == 0:
            print("\n Thanks for Playing Game")
            break

    elif player == 2:

        print("Enter player names:")
        print("Player 1:")
        player1 = str(input())
        print("Player 2:")
        player2 = str(input())
        if player1 == player2:
            print("Players cannot have same names.Please choose a different name.")
            break

         
        print("Now Make choices:Enter any number from 1-3 ")
        

        player1Choice = int(input("\n{} Make your choice".format(player1)))
       

        if player1Choice == 1:
            player1ChoiceName = "rock"

        elif player1Choice == 2:
            player1ChoiceName = "paper"

        elif player1Choice == 3:
            player1ChoiceName = "scissor"
        else:
            print("You can only choose between 1-3")
            break
        
        player2Choice = int(input("\n{} Make your choice ".format(player2)))
        
        if player2Choice == 1:
            player2ChoiceName = "rock"

        elif player2Choice == 2:
            player2ChoiceName = "paper"

        elif player2Choice == 3:
            player2ChoiceName = "scissor"
        else:
            print("You can only choose between 1-3")
            break

        print(player1ChoiceName + " V/s " + player2ChoiceName)

        if player1Choice == player2Choice:
            result = "draw"
            str(result)

        elif player1ChoiceName == "paper" and player2ChoiceName == "rock":
            result = "player1 win"
            str(result)

        elif player1ChoiceName == "paper" and player2ChoiceName == "scissor":
            result = "player2 win"
            str(result)

        elif player1ChoiceName == "scissor" and player2ChoiceName == "rock":
            result = "player2 win"
            str(result)

        elif player1ChoiceName == "scissor" and player2ChoiceName == "paper":
            result = "player1 win"
            str(result)

        elif player1ChoiceName == "rock" and player2ChoiceName == "paper":
            result = "player2 win"
            str(result)

        elif player1ChoiceName == "rock" and player2ChoiceName == "scissor":
            result = "player1 win"
            str(result)

        if result == "draw":
            print("\n Awww... its a tie .. try again")

        elif result == "player2 win":
            print("\n Hurraaahh !!!!{} Won the game...".format(player2))

        else:
            print("\n Hurraaahhh !!!! {} Won the game...".format(player1))

        print("\n Do you want to play this game again ???")
        ans = int(input("Enter 0 to exit and enter any number to play again: "))
        if ans == 0:
            print("\n Thanks for playing the game.")
            break

    else:
        print("Choose only between 1 or 2")
        break
