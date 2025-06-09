
def checkEvenOdd(x):
    if(x%2==0):
        return True
    else:
        return False

x = int(input("Enter a number: "))

is_even = checkEvenOdd(x)
if (is_even==True):
    print("The number is even")
else:
    print("The number is odd")


