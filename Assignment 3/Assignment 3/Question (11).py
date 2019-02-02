class Numbers:
    MULTIPLIER = 5

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def multiply(self, x):
        return x*self.MULTIPLIER

    @staticmethod
    def subtractor(y, z):
        return y - z

    @property
    def value(self):
        tup = (self.a, self.b)
        return tup

    def setter(self):
        self.a = int(input("Set value of a: "))
        self.b = int(input("Set value of b: "))

    def deleter(self):
        self.a = 0
        self.b = 0


num = Numbers(3, 4)
print(num.add())
print(num.multiply(2))
print(num.value)
num.setter()
print(num.value)
num.deleter()
print(num.value)
