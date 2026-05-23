class Vehicle:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)

print("Vehicle name: ", School_bus.name, "Speed: ", School_bus.max_speed, "Milage: ", School_bus.milage)