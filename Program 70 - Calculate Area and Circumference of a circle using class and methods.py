
class Circle:
    pi = 3.14159
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        area= self.pi * self.radius**2
        return area

    def calculate_circumference(self):
        circumference= 2*self.pi*self.radius
        return circumference

radius = input("Enter radius of a circle : ")
if radius.replace('.','').isdigit() and float(radius)>0:
    radius = float(radius)
    circle1= Circle(radius)
    circle_area =round(circle1.calculate_area(),2)
    print(f"The Area of a circle is {circle_area}")
    circle_circumference= round(circle1.calculate_circumference(),2)
    print(f"The Circumference of a Circle is {circle_circumference}")
else:
    print("Invalid Input")

