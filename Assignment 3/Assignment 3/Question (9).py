class Circle:

    def __init__(self, center,radius):
        self.center = center
        self.radius = radius

a = int(input("Enter a coordinate of center: "))
b = int(input("Enter b coordinate of center: "))
rad = int(input("Enter radius: "))
circ_1 = Circle((a,b),rad)
print(circ_1.center)
print(circ_1.radius)
