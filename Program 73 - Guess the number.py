import random

def guess_number(attempt,num):

        while attempt != 0:
            print(f"You have {attempt} attempts remaining to guess the number")
            input_num = int(input("Make a guess : "))
            if input_num == num:
                attempt -= 1
                print("Correct guess")
            elif input_num < num and input_num > 0 and input_num < 50:
                print("Your Guess is Too Low\nGuess again")
                attempt -= 1
            elif input_num > num and input_num > 0 and input_num < 50:
                print("Your Guess is Too High\nGuess again")
                attempt -= 1
            else:
                print("Invalid input")

        else:
            print("Your attempts are over.. You Losses")


print("Let me think a number between 1 to 50.")
num = random.randint(1,50)
print(num)
difficulty_level = input("Choose the level of difficulty... Type 'easy' or 'hard' : ").lower()


if difficulty_level == 'easy':
    attempt = 10
    guess_number(attempt,num)
elif difficulty_level == 'hard':
    attempt = 5
    guess_number(attempt, num)
else:
    print("You have entered Invalid difficulty level")
