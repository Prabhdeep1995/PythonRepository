# Write a program that takes any two lists L and M of the same size
# and adds their elements together to form a new list N
# whose elements are sums of the corresponding elements in L and M. For instance,
# if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4,6,13].

list1= input("Enter elements of List 1, use comma for seperation : ").split(',')
list2= input("Enter elements of List 2, use comma for seperation : ").split(',')

list3=[]

if len(list1) == len(list2):
    for i in range(len(list1)):
        if list1[i].replace('.','').isdigit() and list2[i].replace('.','').isdigit():
            list1[i]=float(list1[i])
            list2[i] = float(list2[i])
            k= list1[i]+list2[i]
            list3.append(k)
        else:
            print("Invalid Input")
            exit()
    print(f"The sum of elements of both lists is : {list3}")
else:
    print("The size of both the list are not equal")
