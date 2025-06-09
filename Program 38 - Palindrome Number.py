# Palindrome number

num = input("Enter any number : ")
if num.isdigit():
    num= int(num)
    orginal_num= num
    rev=0
    while num>0:
        temp = num%10
        rev = rev *10 + temp
        num= num//10

    if rev == orginal_num:
        print("The entered number is Palindrome")
    else:
        print("Not Palindrome")
else:
    print("Invalid Input")