class Bird:
    
    species = 'bird'

    def __init__(self, name, age):
        self.name = name
        self.age = age

ParrotX2 = Bird("ParrotX2", 20)
Theobald = Bird('Theobald', 22)        

print("ParrotX2 is a {}".format(ParrotX2.species))
print("Theobald is also a {}".format(Theobald.species))

print("{} is {} years old".format( ParrotX2.name, ParrotX2.age))
print("{} is {} years old".format( Theobald.name, Theobald.age))