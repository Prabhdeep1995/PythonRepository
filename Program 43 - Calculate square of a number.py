# Calculate square of a number

num = input("Enter any number : ")
if num.replace('-','').isdigit():
    num=int(num)
    square = num**2
    print(f"The Square of entered digit {num} is {square}")
else:
    print("Invalid input")