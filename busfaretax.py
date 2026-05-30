class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)


    def bus_fare(self):
        og = self.capacity * 100
        final_fare = og * 1.1
        return final_fare

School_bus = Bus(50)
print("The bus fare is: ", School_bus.bus_fare())    


