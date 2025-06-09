# Convert each word in a list to uppercase

list1= input("Enter elements of List 1, use comma for seperation : ").split(',')
list2 =[]
for i in range(len(list1)):
    if list1[i].isalpha():
        list2.append(list1[i].upper())
    else:
        print("Invalid Input")
        exit()

print(f"The upper case converted lis is {list2}")