import random

print("Lets play Rock Paper Scissors!\n")

def wincond(p1, p2):
    if p1 == p2:
        return "draw"
    elif p1 == "rock" and p2 == "paper":
        return "p2"
    elif p1 == "rock" and p2 == "scissors":
        return "p1"
    elif p1 == "paper" and p2 == "rock":
        return "p1"
    elif p1 == "paper" and p2 == "scissors":
        return "p2"
    elif p1 == "scissors" and p2 == "rock":
        return "p2"
    elif p1 == "scissors" and p2 == "paper":
        return "p1"
    else:
        "N/A"


while True:
    optionh = input("Type rock, paper or scissors and dont worry I will choose randomly : ").lower()
    optiona = random.randint(1, 3)

    if optiona == 1:
        optiona = "rock"
    elif optiona == 2:
        optiona = "paper"
    else:
        optiona = "scissors"

    result = wincond(optionh, optiona)

    if result == "draw":
        print("It's a draw!")
    elif result == "p1":
        print("You won!")
    elif result == "p2":
        print("You lost...")
    else:
        print("Sorry I could understand your option.")

    again = input("Would you like to play again? (yes/no) : \n")

    if again != "yes":
        print("Bye then!")
        break
