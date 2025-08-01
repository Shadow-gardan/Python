# operator overloading
# In python can be overloading using dunder method, these methods are called when a given operator is used on the objects


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Use the Operator Overloading

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  


