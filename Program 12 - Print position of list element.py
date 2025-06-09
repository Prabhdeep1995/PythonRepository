# Write a program to check if a number is present in the list or not.
# If the number is present, print the position of the number.
# Print an appropriate message if the number is not present in the list.

list1 =[2,4,55,66,21,43,56,44]
num = input("Enter any number : ")
num= int(num)

if num in list1:
    print(f"The number is at {list1.index(num)+1} position")
else:
    print("Number not present")



