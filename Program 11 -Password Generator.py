# Password Generator
import random
import string

print("Welcome to password Generator!")
lettersLength = input("How many letters would you like in your password? ")
symbolLength = input("How many symbols would you like? ")
numbersLength = input("How many numbers would you like? ")

lettersLength,symbolLength,numbersLength= int(lettersLength),int(symbolLength),int(numbersLength)
l_string=""
for i in range(lettersLength):
    l_pass = random.choice(string.ascii_lowercase)
    l_string= l_string+l_pass
# print(l_string)

s_string=""
for i in range(symbolLength):
    l_pass = random.choice(string.punctuation)
    l_string= l_string+l_pass
# print(s_string)

n_string=''
for i in range(numbersLength):
    l_pass = random.choice(string.digits)
    l_string= l_string+l_pass
# print(n_string)

generatedPassword= l_string
print(generatedPassword)
list1 = list(generatedPassword)
random.shuffle(list1)
print(list1)
password=""
for i in range(len(list1)):
    password= password + list1[i]
print(password)