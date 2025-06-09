# Remove all odd numbers from a list

list1= input("Enter elements of List 1, use comma for seperation : ").split(',')
list2= []
for i in range(len(list1)-1):
    if list1[i].isdigit():
        list1[i]=int(list1[i])
        if list1[i]%2==0:
            list2.append(list1[i])
    else:
        print("Invalid Input")
        exit()
print(f"After removing the odd item from the list is {list2}")