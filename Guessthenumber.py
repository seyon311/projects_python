import random
playing = True
while playing:
    number = random.randint(1, 10)
    guess = int(input("I am thinking of a number between 1 and 10. Can you guess it? "))
    if guess == number:
        print("You won!")
        print("The number was", number)
        break
    else:
        print(guess, "is not the correct number. Try again!")
