# Shape → Polygon → Rectangle
# Shape: Base class with color
# Polygon: Inherits from Shape, adds sides
# Rectangle: Inherits from Polygon, adds length, breadth, area() method
# Use multilevel inheritance to show how rectangle is a polygon and shape. Add a method to calculate area and print all properties.

class Shape :
    def __init__(self,color):
        self.color = color
    def display_color(self):
        print(f"Color is : {self.color}")

class Polygon(Shape):
    def __init__(self,color,sides):
        super().__init__(color)
        self.sides = sides
    def display_sides(self):
        print(f"Sides is : {self.sides}")

class Rectangle(Polygon):
    def __init__(self, color, sides,length, breadth):
        super().__init__(color,sides)
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area

rectangle1 = Rectangle('blue',4,11,15)
rectangle1.display_color()
rectangle1.display_sides()
area = rectangle1.area()
print(f"The area is {area}")


