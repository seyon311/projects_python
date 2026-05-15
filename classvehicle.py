class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

k = Vehicle('350 mph', '20000 miles')

print(f"\nKoenigsegg max speed: {k.max_speed}")
print(f"Keonigsegg mileage: {k.mileage}\n")