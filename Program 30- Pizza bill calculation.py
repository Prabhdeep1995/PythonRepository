# Pizza bill calculation
small_pizza_price,medium_pizza_price,large_pizza_price = 100,200,300
pizzaSize= input('Which size pizza you want S/M/L"?? : ')
if pizzaSize=="S" or pizzaSize=="s":
    pepperoni= input("Do you want to add Pepperoni... Y or N? ")
    extraCheese = input("Do you want to add extra cheese... Y or N? ")
    if pepperoni=="Y" or pepperoni=="y":
        if extraCheese=="Y" or extraCheese=="y":
            totalBill = small_pizza_price+30+20
        else:
            totalBill = small_pizza_price+30
        print(f"Total bill is {totalBill}")
    else:
        if extraCheese == "Y" or extraCheese=="y":
            totalBill = small_pizza_price + 20
        else:
            totalBill = small_pizza_price
        print(f"Total bill is {totalBill}")
elif pizzaSize=="M" or pizzaSize=="m":
    pepperoni = input("Do you want to add Pepperoni... Y or N? ")
    extraCheese = input("Do you want to add extra cheese... Y or N ? ")
    if pepperoni=="Y" or pepperoni=="y":
        if extraCheese=="Y" or extraCheese=="y":
            totalBill = medium_pizza_price + 50 + 20
        else:
            totalBill = medium_pizza_price + 50
        print(f"Total bill is {totalBill}")
    else:
        if extraCheese=="Y" or extraCheese=="y":
            totalBill = medium_pizza_price + 20
        else:
            totalBill = medium_pizza_price
        print(f"Total bill is {totalBill}")
elif pizzaSize=="L" or pizzaSize=="l":
    pepperoni = input("Do you want to add Pepperoni... Y or N ? ")
    extraCheese = input("Do you want to add extra cheese... Y or N? ")
    if pepperoni=="Y" or pepperoni=="y":
        if extraCheese=="Y" or extraCheese=="y":
            totalBill = large_pizza_price + 50 + 20
        else:
            totalBill = large_pizza_price + 50
        print(f"Total bill is {totalBill}")
    else:
        if extraCheese=="Y" or extraCheese=="y":
            totalBill = large_pizza_price + 20
        else:
            totalBill = large_pizza_price
        print(f"Total bill is {totalBill}")
else:
    print("Invalid Choice")
