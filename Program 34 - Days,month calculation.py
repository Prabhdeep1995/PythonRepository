# age= int(input("Enter your age in years: "))
# lastAge=90
# lastAge_inDays= lastAge*365
# yearsLeft= lastAge-age
# weeksLeft= (lastAge*52)- age*52
# monthsLeft= (lastAge*12)-age*12
# daysLeft= lastAge_inDays-age*365
# print(f"You have {daysLeft} days, {weeksLeft} week, {monthsLeft} months and {yearsLeft} years left")
# -------------------------------------------------------------------------

age= int(input("Enter your age in years: "))
lastAge=90
yearsLeft=lastAge-age
daysLeft= yearsLeft*365
monthsLeft=yearsLeft*12
weeksLeft=yearsLeft*52
print(f"You have {daysLeft} days, {weeksLeft} week, {monthsLeft} months and {yearsLeft} years left")