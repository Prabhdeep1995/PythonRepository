# Print all numbers between 1 to 100 that are divisible by both 3 and 5 but not 30
# Output: [15, 45, 75]

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 and i % 30 != 0:
            print(i, end=" ")