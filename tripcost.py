print("Welcome to the Trip Cost Calculator!")
print("Please enter the following details about your trip in Pounds but dont use any currency symbols.")

def night(nights):
    return nights * 100
def citys(city):
    
    if city == "paris": return 200
    elif city == "london": return 150
    elif city == "new york": return 250
    elif city == "tokyo": return 300
    elif city == "new delhi": return 125
    else: return 145

def car(days):
    return days * 50
def ticket_on_flight(people):
    return people * 600


nights = int(input("How many nights will you be staying? "))
city = input("Which city are you visiting? ")
days = int(input("How many days will you be renting a car? "))
people = int(input("How many people are going on the trip? "))

def total_cost(nights, city, days, people):
    return night(nights) + citys(city) + car(days) + ticket_on_flight(people)

cost = total_cost(nights, citys, days, people)

print(f"The total cost of your trip is: £{cost}")




