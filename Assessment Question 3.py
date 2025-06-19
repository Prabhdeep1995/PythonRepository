# Construct an array of numbers by taking input from the user and finally build an array with unique number

num1 = [1,5,6,2,1,5,3,2,1]
num2 = []
for i in num1:
    for j in num1:
        if i==j and i not in num2:
            num2.append(i)
print(f"The unique number is {num2}")