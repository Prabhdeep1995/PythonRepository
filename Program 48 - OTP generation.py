# Otp Generation
import random

num = input("Enter number of digits for OTP generation : ")
otp=''
if num.isdigit():
    num=int(num)
    if num>0:
        for i in range(num):
            otp_digit= random.randint(0,9)
            otp = otp+str(otp_digit)
        print(f"The generated OTP of {num} digits is {otp}")
    else:
        print("Please enter number greater than 0")
else:
    print("Invalid Input")
