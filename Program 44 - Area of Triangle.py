# Calculate Area of Triangle
# Formula = 1/2 * base * height

base = input("Enter Base of a Triangle : ")
height = input("Enter Height of a Triangle : ")

if base.replace('.','').isdigit() and height.replace('.','').isdigit():
    base = float(base)
    height = float(height)
    area = 1/2 * base*height
    print(f"The area of Triangle is {area}")
else:
    print("Invalid Input")