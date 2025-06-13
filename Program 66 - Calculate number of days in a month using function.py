# Calculate number of days in a month using function

def check_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calculate_days(year,month):
    if month==2:
        check_year =check_leap_year(year)
        if check_year== True:
            no_of_days=29
        else:
            no_of_days=28
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        no_of_days=31
    else:
        no_of_days=30
    return no_of_days



year = input("Enter year : ")
month = input("Enter month : ")
if year.isdigit() and month.isdigit():
    year=int(year)
    month=int(month)
    if year >=1800 and year<=4000:
        if month>=1 and month<=12:
            days_in_month= calculate_days(year,month)
            print(days_in_month)
        else:
            print("Please enter correct Month")
    else:
        print("Please enter correct Year")
else:
    print("Invalid Input")