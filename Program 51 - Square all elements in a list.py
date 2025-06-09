# Square all elements in a list and store in a new list

list1= input("Enter elements of List 1, use comma for seperation : ").split(',')
list2=[]

for i in range(len(list1)):
    if list1[i].replace('.','').isdigit() :
        list1[i]=float(list1[i])
        k= list1[i]**2
        list2.append(k)
    else:
        print("Invalid Input")
        exit()
print(f"The Square of the list elements is : {list2}")
