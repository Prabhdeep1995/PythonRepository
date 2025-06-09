# Write a program that asks for your height in centimetres and then converts your height to feet and inches.
# (1 foot = 12 inches, 1 inch = 2.54 cm).

height_in_centimeter = input("Enter height in Centimeter : ")
if height_in_centimeter.replace('.','').replace('-,','').isdigit():
    height_in_centimeter= float(height_in_centimeter)
    one_cm_inch= 1/2.54
    one_cm_ft = 1/(12*2.54)
    height_in_inch= round(height_in_centimeter * one_cm_inch,2)
    height_in_foot= round(height_in_centimeter *one_cm_ft,2)
    print(f"The height in inch is : {height_in_inch}")
    print(f"The height in foot is : {height_in_foot}")
else:
    print("Invalid input")

