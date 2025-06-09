# Remove spaces from a string without using .replace()

# name ='Prabhdeep Singh'
name = input("Enter any string : ")
name_without_space=''
for i in name:
    if i!=" ":
        name_without_space+=i
    else:
        continue
print(f"The name without space is : {name_without_space}")