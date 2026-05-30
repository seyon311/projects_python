class Reverse:
    def __init__(self, str):
        self.str = str

    def reverse(self):
        str = self.str
        str1 = ""
        for i in str:
            str1 = i + str1
        return str1

str = input("Enter a string: ")
rev = Reverse(str)
print("The reversed string is: ", rev.reverse())