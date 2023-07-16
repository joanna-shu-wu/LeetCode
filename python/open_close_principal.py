"""
that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. 
In Python, this principle can be demonstrated using inheritance and polymorphism.
"""
class Shape:
    def calculate_area(self):
        pass

    def display(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def display(self):
        print(f"Rectangle: width={self.width}, height={self.height}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def display(self):
        print(f"Circle: radius={self.radius}")


"""
In the print_area() function, we take a shape parameter of type Shape. 
This allows us to pass objects of either Rectangle or Circle as arguments. 
We can see that the calculate_area() method is correctly called for each object, and we get the expected results.

This example demonstrates the Liskov substitution principle in Python, 
We can substitute the subclasses (Rectangle, Circle) in place of the superclass (Shape) without affecting the behavior or correctness of the program.
"""
def print_area(shapes):
    for shape in shapes:
        print(f"Area: {shape.calculate_area()}")


shapes = [Rectangle(4, 5), Circle(3)]
print_area(shapes)

"""
With this design, you can easily extend the functionality by adding new shapes without modifying the existing classes.
For example, you could add a Triangle class by creating a new class derived from Shape and implementing its specific behavior.
"""



"""
This is the anti Open/Close pattern example
"""
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def calculate_area(self):
        if self.shape_type == "rectangle":
            # Calculation logic for rectangle
            return self.width * self.height
        elif self.shape_type == "circle":
            # Calculation logic for circle
            return 3.14 * self.radius * self.radius
        else:
            raise ValueError("Unsupported shape type.")

# Usage example
rectangle = Shape("rectangle")
rectangle.width = 4
rectangle.height = 5
print(rectangle.calculate_area())  # Output: 20

circle = Shape("circle")
circle.radius = 3
print(circle.calculate_area())  # Output: 28.26
