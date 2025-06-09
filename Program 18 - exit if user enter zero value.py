# Take an input from the user and do sum of positive or negative integer, exit if user enter zero value
num = input("Enter any number(Enter 0 to quit) : ")
if num.replace('.','').replace('-','').isdigit():
    num=int(num)
    sum=0
    while num!=0:
        sum= sum+num
        num = input("Enter any number(Enter 0 to quit) : ")
        num = int(num)
    print(f"The sum of integers is : {sum}")
else:
    print("Wrong Input")