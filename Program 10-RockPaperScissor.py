# 0 for rock
# 1 for paper
# 2 for scissor
# import random
# num = int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissor : "))
# rock=0
# paper=1
# scissor=2
#
#
# c_input = random.randint(rock,scissor)
# print("user input : ", num)
# print("computer input : ", c_input)
#
# if num == rock and c_input == scissor:
#     print("You won")
# elif num == rock and c_input == paper:
#     print("You loose")
# elif num == paper and c_input == scissor:
#     print("You loose")
# elif num == paper and c_input == rock:
#     print("You won")
# elif num == scissor and c_input == rock:
#     print("You loose")
# elif num == scissor and c_input == paper:
#     print("You won")
# else:
#     print("It's a tie...try again..")

# -----------------------------------------------------

# import random
# num = input("Enter 0 for Rock, 1 for Paper or 2 for Scissor : ")
# rock=0
# paper=1
# scissor=2
#
# c_input = random.randint(rock,scissor)
# print("user input : ", num)
#
# if num.isdigit():
#     num= int(num)
#     if num>=0 and num<=2:
#         print("computer input : ", c_input)
#         if num == rock and c_input == scissor:
#             print("You won")
#         elif num == rock and c_input == paper:
#             print("You loose")
#         elif num == paper and c_input == scissor:
#             print("You loose")
#         elif num == paper and c_input == rock:
#             print("You won")
#         elif num == scissor and c_input == rock:
#             print("You loose")
#         elif num == scissor and c_input == paper:
#             print("You won")
#         else:
#             print("It's a tie...try again..")
#     else:
#         print("Wrong Input")
# else:
#     print("Wrong Input")


# ---------------------------------

import random
num = input("Enter 0 for Rock, 1 for Paper or 2 for Scissor : ")
rock=0
paper=1
scissor=2

c_input = random.randint(rock,scissor)
if num.isdigit():
    num= int(num)
    if num>=0 and num<=2:
        print("User input:", ["Rock", "Paper", "Scissor"][num])
        print("computer input : ", ["Rock", "Paper", "Scissor"][c_input])
        if num == c_input:
            print("It's a tie...try again..")
        elif (num == rock and c_input == scissor) or num == paper and c_input == rock \
                or num == scissor and c_input == paper:
            print("You won")
        else:
            print("You loose")
    else:
        print("Wrong Input. Please enter 0, 1, or 2.")
else:
    print("Wrong Input. Please enter a valid number.")