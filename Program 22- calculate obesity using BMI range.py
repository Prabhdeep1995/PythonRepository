weight = int(input("Enter your weight : "))
height = float(input("Enter your height : "))
BMI = round((weight/height**2),2)
print(BMI)
if BMI<18.5:
    print("Under weight")
elif BMI>=18.5 and BMI<=24.9:
    print(f"Normal range- Your BMI is {BMI}")
elif BMI>=25.0 and BMI<=29.9:
    print(f"Overweight(Pre-obese)- Your BMI is {BMI}")
elif BMI>=30.0 and BMI<=34.9:
    print(f"Obese(Class I)- Your BMI is {BMI}")
elif BMI>=35.0 and BMI<=39.9:
    print(f"Obese(Class II)- Your BMI is {BMI}")
else:
    print(f"Obese(Class III)- Your BMI is {BMI}")