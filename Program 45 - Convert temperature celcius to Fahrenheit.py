# Convert temperature celcius to Fahrenheit
# Formula :  F = (C * 9/5) + 32.

temp_in_celcius = input("Enter temperature in celcius : ")

if temp_in_celcius.replace('.','').replace('-','').isdigit():
    temp_in_celcius = float(temp_in_celcius)
    temp_in_fahrenheit= (temp_in_celcius * 9/5) + 32
    print(f"The temperature in Fahrenheit is {temp_in_fahrenheit}")
else:
    print("Invalid Input")