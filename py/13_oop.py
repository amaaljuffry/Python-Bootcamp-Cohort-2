# Date: 2025-11-07
# Object-Oriented Programming in Python

# Object-Oriented Programming - A programming paradigm based on the concept of "objects", which can contain data and code to manipulate that data.

# Object - An instance of a class.
# Class - A blueprint for creating objects.
# Inheritance - A mechanism for creating new classes based on existing classes.

# Inheritance
class Shape: # Parent class
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0

class Circle(Shape): # Child class
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape): # Child class
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

def area(self): # Override parent method
    return self.side * self.side

# Both Circle and Square are Shape objects
circle = Circle(10)
square = Square(4)

print(circle.name)
print(square.name)


# Polymorphism - A mechanism for using the same interface for different data types.
# Encapsulation - A mechanism for hiding the internal details of an object.
# Abstraction - A mechanism for hiding the internal details of an object.

# Example 1:
# Polymorphism
def print_area(shape): # Takes any shape object
    print(f"{shape.name} area: {shape.area()}")

# Same method call, different implementations
print_area(circle) # "Circle area:78.5"
print_area(square) # "Square area:16"

# Or with a list
shapes = [Circle(3), Square(5), Circle(2)]
for shape in shapes:
    print_area(shape) # same code, different objects

# Exercise 1: 