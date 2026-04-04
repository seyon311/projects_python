import random

userchoice = input("Do you choose rock, paper or scissors? [ R/P/S ] ").upper().strip()
Aichoice = random.choice(['R', 'P', 'S'])

if userchoice == Aichoice:
    print("It's a tie! Both you and the AI chose", userchoice)
elif userchoice == 'R' and Aichoice == 'S' or userchoice == 'P' and Aichoice == 'R' or userchoice == 'S' and Aichoice == 'P':
    print("You win! You chose", userchoice, "and the AI chose", Aichoice)
elif userchoice == 'R' and Aichoice == 'P' or userchoice == 'P' and Aichoice == 'S' or userchoice == 'S' and Aichoice == 'R':
    print("You lose! You chose", userchoice, "and the AI chose", Aichoice)
else:
    print("Invalid input. Please choose R, P, or S.")
    
            