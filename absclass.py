from abc import ABC, abstractmethod

class AbsClass(ABC):
    
    def print(self, x):
        print("Passed Value is: ", x)

    @abstractmethod

    def task(self):
        print("We are in an abstract class")

class Subclass(AbsClass):
    def task(self):
        print("We are in a subclass")

obj = Subclass()
obj.task()
obj.print("100")        