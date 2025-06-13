# Multiple return add 2 numbers and return None if both are 0

def add(a,b):
    if a==0 and b==0:
        return
    else:
        return a+b

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

sum= add(num1,num2)
print(sum)