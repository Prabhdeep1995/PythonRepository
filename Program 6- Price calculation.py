# A store charges ₹120 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is ₹100 per item.
# If you buy 100 or more items, the cost is ₹70 per item.
# Write a program that asks the user how many items they are buying and prints the total cost.

num_of_items = input("Enter number of items you want to buy : ")
total_cost = 0
if num_of_items.isdigit():
    num_of_items= int(num_of_items)
    if num_of_items>0:
        if num_of_items>0 and num_of_items< 10:
            total_cost= num_of_items * 120
        elif num_of_items>=10 and num_of_items<=99:
            total_cost= num_of_items*100
        else:
            total_cost=num_of_items*70
        print(f"The Total cost is : {total_cost}")
    else:
        print("Please enter value greater than 0")
else:
    print("Invalid Input")