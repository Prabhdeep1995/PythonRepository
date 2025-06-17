# Create a class Rectangle with attributes length and breadth.
# Write methods to calculate and return the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area_of_rectangle(self):
        area = self.length * self.breadth
        return area

    def perimeter(self):
        perimeter = 2 *(self.length + self.breadth)
        return perimeter

length = input("Enter Length of a Rectangle : ")
breadth = input("Enter Breadth of a Rectangle : ")

if length.replace('.','').isdigit() and breadth.replace('.','').isdigit():
    length = float(length)
    breadth = float(breadth)
    if length > 0 and breadth > 0:
        rectangle_1 = Rectangle(length,breadth)
        area = rectangle_1.area_of_rectangle()
        print(f"The Area of Rectangle is {area}")
        perimeter = rectangle_1.perimeter()
        print(f"The perimeter of Rectangle is {perimeter}")
    else:
        print("Length and Breath should be greater than 0")
else:
    print("Invalid Input")

