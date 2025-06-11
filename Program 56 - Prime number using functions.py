# Prime number using function

# Logic 1
# def primeCheck(num):
#     count = 0
#     for i in range(1, num + 1):
#         if (num % i == 0):
#             count += 1
#     if count == 2:
#         isPrime = True
#         return isPrime
#     else:
#         isPrime = False
#         return isPrime
#
#
# num =int(input("Enter any number : "))
# checkPrime= primeCheck(num)
# if checkPrime :
#     print(f"The entered number {num} is a Prime Number")
# else:
#     print(f"The entered number {num} is not a Prime Number")


# Logic 2


def primeCheck(num):
    sqt = num ** 0.5
    for i in range(2, int(sqt) + 1):
        if (num % i == 0):
            return False
    else:
        return True

num =int(input("Enter any number : "))
checkPrime= primeCheck(num)
print(bool(checkPrime))
if bool(checkPrime):
    print(f"The entered number {num} is a Prime Number")
else:
    print(f"The entered number {num} is not a Prime Number")
