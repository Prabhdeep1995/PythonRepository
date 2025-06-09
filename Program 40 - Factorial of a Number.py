# Factorial of a Number

num = input("Enter any number : ")
if num.isdigit():
    num=int(num)
    factorial=1
    for i in range(1,num+1):
            factorial = factorial *i
    print(f"The Factorial of an entered number {num} is {factorial}")
else:
    print("Invalid Input")