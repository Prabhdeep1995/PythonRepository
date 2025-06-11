num = input("Enter a number: ")
first_sum = 0
total_sum = 0
for digit in num:
    first_sum += int(digit)
    print(first_sum)
    for total in str(first_sum):
        total_sum+=int(total)
        print("Sum of digits:", total_sum)