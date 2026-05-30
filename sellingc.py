class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

# Will work, sells for 900

msi = Computer()
msi.sell()

# Will change the price and sell for 1000

msi.setMaxPrice(1000)
msi.sell()

# Won't work, will raise an AttributeError as __maxprice is private

# msi.__maxprice = 1000
# msi.sell()