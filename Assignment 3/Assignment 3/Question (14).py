class StringMethod:

    def __init__(self):
        self.string_1 = ""

    def getstring(self):
        self.string_1 = input("Enter a string: ")

    def printstring(self):
        print(f"{self.string_1.upper()}")


str1 = StringMethod()
str1.getstring()
str1.printstring()
