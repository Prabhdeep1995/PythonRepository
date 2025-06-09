# Armstrong number
'''
An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits
in the number.
Let's take the example of number 1634.
It has four digits, so we raise each digit to the power of 4: 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634.
'''

original_num = input("Enter any number : ")
num=original_num
if num.isdigit():
    original_num = int(original_num)
    sum= 0
    no_of_digits = len(num)
    num= int(num)
    while num>0:
        temp = num%10
        sum = sum + temp ** no_of_digits
        num = num//10
    print(sum)
    if sum==original_num:
        print(f"The entered number {original_num} is an Armstrong number")
    else:
        print(f"The entered number {original_num} is not an Armstrong number")
else:
    print("Invalid input")
