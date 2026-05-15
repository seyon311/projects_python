class Dog:
    species = 'dog'

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

poodle = Dog('poodle', 6)
dashshund = Dog('dashshund', 3)

print(f"My dog is a {poodle.breed} and it's {poodle.age} years old!")
print(f"My dog is a {dashshund.breed} and it's {dashshund.age} years old!")