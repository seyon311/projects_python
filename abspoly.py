from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk")

class Snake(Animal):
    def move(self):
        print("I can slither")

class Arachnid(Animal):
    def move(self):
        print("I can crawl")

class Lion(Animal):
    def move(self):
        print("I can roar")

h = Human()
s = Snake()
a = Arachnid()
l = Lion()

for animal in (h, s, a, l):
    animal.move()
