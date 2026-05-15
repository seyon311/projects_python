class fruit:
    # class variable
    taste = 'sweet'

    def __init__(self, name, color):
        self.name = name
        self.color = color

apple = fruit('apple', 'red')
banana = fruit('banana', 'yellow')

print(apple.taste)
print(apple.name, apple.color)
print(banana.name, banana.color)