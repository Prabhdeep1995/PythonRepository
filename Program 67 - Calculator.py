def add(first_number,second_number):
    result= first_number+second_number
    return result

def subtract(first_number,second_number):
    result= first_number - second_number
    return result

def multiply(first_number,second_number):
    result= first_number*second_number
    return result

def division(first_number,second_number):
    result= first_number / second_number
    return result



def calculator(first_number,operand,second_number):
    first_number=int(first_number)
    second_number=int(second_number)
    if operand=='+':
        finalResult =add(first_number,second_number)
    elif operand=='-':
        finalResult = subtract(first_number, second_number)
    elif operand=='*':
        finalResult = multiply(first_number, second_number)
    elif operand=='/':
        finalResult = division(first_number, second_number)
    else:
        print("Invalid Operand")
        exit()
    print(finalResult)
    newInput =input(f"Enter 'y' to continue calculation with {finalResult} or enter 'n' to start new calculation or 'x' to exit ").lower()
    if newInput=='y':
        first_number = finalResult
        operand = input("+\n-\n*\n/\nPick any operation : ")
        second_number = int(input("Enter Second number : "))
        calculator(first_number,operand,second_number)
    elif newInput=='n':
        first_number = int(input("Enter First number : "))
        operand = input("+\n-\n*\n/\nPick any operation : ")
        second_number = int(input("Enter Second number : "))
        calculator(first_number, operand, second_number)
    elif newInput=='x':
        print("Thanks for using the Calculator...Have a nice day!!")
        exit()
    else:
        print("Invalid Input....Thanks for using the Calculator...Have a nice day!!")
        exit()

first_number = int(input("Enter First number : "))
operand = input("+\n-\n*\n/\nPick any operation : ")
second_number = int(input("Enter Second number : "))
calculator(first_number,operand,second_number)