# Ask the user to enter a list containing numbers between 1 and 12.
# Then replace all of the entries in the list that are greater than 10 with 10.

list1= input("Enter a list containing numbers between 1 and 12. Use comma(,) to seperate values : ").split(',')
for i in range(len(list1)):
    if list1[i].isdigit():
        list1[i]=int(list1[i])
        if list1[i]>=1 and list1[i]<=12:
            if list1[i]>10:
                list1[i]=10
        else:
            print("Enter values between 1 and 12")
            exit()
    else:
        print("Invalid Input")
        exit()
print(list1)




