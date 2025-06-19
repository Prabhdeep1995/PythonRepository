# Find the GCD (Greatest Common Divisor) of two numbers

num1 = 18
num2 = 42
list1 = []
list2 = []
list3 = []

for i in range(1,num1+1):
    if num1%i == 0:
        list1.append(i)
# print(list1)

for i in range(1,num2+1):
    if num2%i == 0:
        list2.append(i)
# print(list2)

for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print(max(list3))

