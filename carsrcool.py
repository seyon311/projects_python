class BMW:
    def __init__(self, year):
        self.year = year

    def intro(self, year):
        print("This is a BWM from the year", year)

class Ferrari:
    def __init__(self, year):
        self.year = year

    def intro(self, year):
        print("This is a Ferrari from the year", year)

bmw = BMW(2026)
ferrari = Ferrari(2025)

for car in (bmw, ferrari):
    car.intro(car.year)