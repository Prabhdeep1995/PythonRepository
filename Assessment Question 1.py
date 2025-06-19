# In a given string find the word which has a digit in it.
# Ex- str1 = My email is karan50 and its unique

str1 ="My email is karan50 and its20 unique".split()
num_list = ['0','1','2','3','4','5','6','7','8','9']
for word in str1:
    for char in word:
        if char in num_list:
            print(word)
            break
