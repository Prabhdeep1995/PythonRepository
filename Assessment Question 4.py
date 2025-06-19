# Using oops concept, calculate the area of a given figure, it could be a circle,triangle, square,rectangle

class Figure:
    def __init__(self,radius,base,height,side,length,breadth):
        self.radius = radius
        self.base = base
        self.height = height
        self.side = side
        self.length = length
        self.breadth = breadth

    def area_of_circle(self):
        pi=3.14
        area = pi * (self.radius**2)
        return area

    def area_of_triangle(self):
        area = 1/2 * self.base * self.height
        return area

    def area_of_square(self):
        area = self.side**2
        return area

    def area_of_rectangle(self):
            area = self.length*self.breadth
            return area

figure1 = Figure(radius=2,base=3,height=5,side=4,length=5,breadth=7)
area_of_circle = figure1.area_of_circle()
area_of_triangle = figure1.area_of_triangle()
area_of_square= figure1.area_of_square()
area_of_rectangle = figure1.area_of_rectangle()

print(f"The area of circle is {area_of_circle}")
print(f"The area of triangle is {area_of_triangle}")
print(f"The area of square is {area_of_square}")
print(f"The area of rectangle is {area_of_rectangle}")



