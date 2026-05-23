class Person():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Name: ", self.name ,", Id number: ", self.id)

class Employee(Person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, id)

Test1 = Employee("Mark", 101832, 1000000, "Intern")

Test1.display()