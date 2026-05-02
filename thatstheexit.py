from time import sleep

e = int(input("Enter a number between 4 and 20: "))

while e < 4 or e > 20: 
    print("Invalid input.")
    e = int(input("Please re-enter a number between 4 and 20: "))

for i in range(20):
    if i == e:
        print("Exiting the loop.")
        exit()
    print(i)    
    sleep(1) # Sleep for 20 ticks (1 second) before the next iteration
