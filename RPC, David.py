import random
print("Welcome to rock paper scissors, the rules of the game are simple")
print("You pick between rock, peper or scissors, you're playing best out of three" + "\U0001F9CD")

# make the three options into a list
gameoptions = ["rock", "paper", "scissors"]

# define the player and computer score
playerscore = 0
opponentscore = 0

while True:
    # get player input
    player = input("Pick rock, paper, or scissors(choose wisely): ")

    # check if user input is valid
    if player not in gameoptions:
        print("Invalid input. Try again.")
        continue

    # get computer's choice
    computer = random.choice(gameoptions)

    # print choices
    print("You chose " + player)
    if player == "rock":
        print("   __")
        print(" /    \ ")
        print("|      |")
        print(" \____/")
    elif player == "scissors":
        print("   _    ")
        print("  | |   ")
        print("  | |__ ")
        print(" /  ___|")
        print("|  |___ ")
        print(" \____/ ")
    elif player == "paper":
        print("  _______")
        print(" /       \ ")
        print("/         \ ")
        print("\         / ")
        print(" \_______/")

    print("The computer chose " + computer)
    if computer == "rock":
        print("   __")
        print(" /    \ ")
        print("|      |")
        print(" \____/")
    elif computer == "scissors":
        print("   _    ")
        print("  | |   ")
        print("  | |__ ")
        print(" /  ___|")
        print("|  |___ ")
        print(" \____/ ")
    elif player =="paper":
        print("  _______")
        print(" /       \ ")
        print("/         \ ")
        print("\         / ")
        print(" \_______/")

     # determine the winner
    if player == computer:
        print("It's a tie, so go again")
        print("\U0001F604")

    elif (player == "rock" and computer == "scissors") or (
            player == "paper" and computer == "rock") or (
            player == "scissors" and computer == "paper"):
        print("You won, against an AI feel smart")
        print("\U0001F60E")
        # Add a point to player score
        playerscore += 1

    else:
        print("\U0001F641")
        print("Your opponent wins")
        # Add a point to opponent score
        opponentscore += 1

    # print scores
    print("Your score:", playerscore)
    print("Opponent score", opponentscore)

    # check if either score has reached 3
    if playerscore == 3 or opponentscore == 3:
        # print the winner
        if playerscore > opponentscore:
            print("You won best out of three")
            print("\U0001F60E")
        else:
            print("You lost best out of three")
            print("\U0001F641")
        break

    # Ask user to end game
    playagain = input("Do you want to play again? (yes or no) ")
    if playagain == "no":
        print("Thanks for playing")
        print("\U0001F604")
        break