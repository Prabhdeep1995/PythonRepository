# Write a program to calculate product of all the digits of a number

num = input("Enter any number : ")
if num.replace('.','').replace('-','').isdigit():
    product=1
    while num>0:
        temp = num%10
        product = product*temp
        num=num//10
    print(f"The product of all the digits of a number is {product}")
else:
    print("Invalid Input")
    
