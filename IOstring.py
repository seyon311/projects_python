# class creation

class IOstring():

    # Constuctor

    def __init__(self):
        self.str1 = ""

    # Method 1 : Inputing string

    def input_string(self):
        self.str1 = input("Enter string : ")

    # Method 2 : Outputing string

    def output_string(self):
        print("The string you typed in 'Uppercased' is as follows :", self.str1.upper())

# Object :

str1 = IOstring()

# call the methods

str1.input_string()
str1.output_string()