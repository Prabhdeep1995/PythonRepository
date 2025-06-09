year= int(input("Enter any year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year is Leap year")
        else:
            print("Not a leap year")
    else:
        print("The year is Leap year")
else:
    print("Not a leap year")
