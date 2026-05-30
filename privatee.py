class MyClass:
    __PrivateVar = 27

    def __PrivateMeth(self):
        print("This is a private method ", self.__PrivateVar)

    def PublicMeth(self):
        print("This is a public method")
        self.__PrivateMeth()

obj = MyClass()
obj.PublicMeth()

# obj.__PrivateMeth()  # This will raise an AttributeError