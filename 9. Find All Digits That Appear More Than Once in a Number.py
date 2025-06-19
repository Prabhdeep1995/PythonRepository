# Find All Digits That Appear More Than Once in a Number
# Input: a number like 1234557611
# Output: Digits repeated = 1, 5


num = 1234557611
num1 =''

for i in str(num):
    c = 0
    for j in str(num):
        if int(i) == int(j):
            c = c+1
            # print(j)
        if c>1 and i not in num1:
            num1+=i+" "
print(num1)