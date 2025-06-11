# Calculate how many cans are required to paint a wall
# 1 can covers 7 sq m
# formula for number of cans = (h*w)/coverage
import math

def noOfCans(height,width,coverage):
    height = float(height)
    width = float(width)
    coverage = 7
    no_of_cans = math.ceil((height * width) / coverage)
    return no_of_cans


height = input("Enter height of a wall : ")
width = input("Enter width of a wall : ")
coverage= 7
if height.replace('.','').replace('-','').isdigit() and width.replace('.','').replace('-','').isdigit():
    total_cans =noOfCans(height,width,coverage)
    print(f"The total cans required to paint a wall is {total_cans}")
else:
    print("Invalid Input")