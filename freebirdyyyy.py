class Bird:
    def __init__(self):
        print("Bird is built")
    def WhoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim!")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is built")
    def WhoisThis(self):
        print("Penguin")
    def run(self):
        print("Run!")

Pengu = Penguin()
Pengu.WhoisThis()
Pengu.swim()
Pengu.run()
