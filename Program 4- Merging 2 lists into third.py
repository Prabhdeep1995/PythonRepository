# Write a program that inputs two lists and creates a third,
# that contains all elements of the first followed by all elements of the second.

list_1_elements= input("Enter values of List 1, use comma(,) to seperate values: ")
list_1= list_1_elements.split(',')
print(f"The elements of List 1 are : {list_1}")
list_2_elements= input("Enter values of List 2, use comma(,) to seperate values: ")
list_2= list_2_elements.split(',')
print(f"The elements of List 2 are : {list_2}")

list_3 = list_1+list_2
print(f"The combination of List 1 and List 2 is : {list_3}")