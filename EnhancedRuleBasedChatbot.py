import colorama
from colorama import Fore
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import random
import os

colorama.init()

num = 1

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def dice_rolling(number):
    global num
    num = number

    if number == 1:
        print("______")
        print("|    |")
        print("|  o |")
        print("|____|")
        num = 1
    elif number == 2:
        print("______")
        print("|o   |")
        print("|    |")
        print("|___o|")
        num = 2
    elif number == 3:
        print("______")
        print("|o   |")
        print("|  o |")
        print("|___o|")
        num = 3
    elif number == 4:
        print("______")
        print("|o  o|")
        print("|    |")
        print("|o__o|")
        num = 4
    elif number == 5:
        print("______")
        print("|o  o|")
        print("|  o |")
        print("|o__o|")
        num = 5
    elif number == 6:
        print("______")
        print("|o  o|")
        print("|o  o|")
        print("|o__o|")
        num = 6

print(Fore.CYAN + "Hello this is Enchanced chatbot!")
print(Fore.CYAN + "I can tell you :\n")
print(Fore.MAGENTA + "The time in different cities, [TYPE TIME]")
print(Fore.MAGENTA + "I can roll a dice for you, [TYPE DICE]")
print(Fore.MAGENTA + "Or I can flip a coin [TYPE COIN]")
print(Fore.LIGHTGREEN_EX)

while True:
    print(Fore.CYAN)
    ask = input("What would you like to do? [TYPE EXIT IF YOU WANT TO STOP AND TYPE OPTIONS IF YOU WANT TO SEE THE OPTIONS AGAIN] >> ").strip().lower()

    if ask == "exit":
        print(Fore.CYAN + "Goodbye then!")
        break

    elif ask == "dice":
        print(Fore.CYAN + "Ok I'll roll the dice for you!" + Fore.WHITE)
        time.sleep(0.7)
        cls()
        for i in range(19):
            dice_rolling(random.randint(1, 6))
            time.sleep(0.1)
            cls()
        dice_rolling(random.randint(1, 6))

        if num == 1:
            print(Fore.CYAN + "\nYou got an one!")
        else:
            print(Fore.CYAN + "\nYou got a " + str(num))

    elif ask == "coin":
            print(Fore.CYAN + "Ok I'll flip the coin for you!\n")
            cls()
            time.sleep(1)
            if random.randint(1, 2) == 1:
                print(Fore.CYAN + "You got a heads!")
            else:
                print(Fore.CYAN + "You got a tails!")

    elif ask == "time":
        print(Fore.CYAN + "Would you to the time at Tokyo, New delhi or London?")
        area = input(Fore.LIGHTGREEN_EX + " >> ").strip().lower()

        if area == "tokyo":
            tokyo_time = datetime.now(ZoneInfo("Asia/Tokyo"))
            print(Fore.CYAN + "Time in Tokyo:", tokyo_time.strftime("%Y-%m-%d %H:%M:%S"))
        elif area == "newdelhi" or area == "new delhi":
            delhi_time = datetime.now(ZoneInfo("Asia/Kolkata"))
            print(Fore.CYAN + "Time in New Delhi:", delhi_time.strftime("%Y-%m-%d %H:%M:%S"))
        elif area == "london":
            london_time = datetime.now(ZoneInfo("Europe/London"))
            print(Fore.CYAN + "Time in London:", london_time.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            print(Fore.RED + "Sorry, I couldn't quite understand that.")
            continue
    elif ask == "option" or ask == "options":
        print(Fore.CYAN + "I can tell you :\n")
        print(Fore.MAGENTA + "The time in different cities, [TYPE TIME]")
        print(Fore.MAGENTA + "I can roll a dice for you, [TYPE DICE]")
        print(Fore.MAGENTA + "Or I can flip a coin [TYPE COIN]\n")
    
    else:
        print(Fore.RED + "Sorry I could quite understand that.")
        continue