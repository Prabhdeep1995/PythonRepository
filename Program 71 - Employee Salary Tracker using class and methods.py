# Create a class Employee with name, designation, and monthly salary. Add a method to calculate the annual salary and display details.
from tkinter.font import names


class Employee:
    def __init__(self,name,designation,monthly_salary):
        self.name = name
        self.designation = designation
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        annual_salary = self.monthly_salary * 12
        return annual_salary

    def display_details(self):
        print(f"My name is {self.name}, I am working as a {self.designation} and my monthly salary is Rs {self.monthly_salary} ")

name = input("Enter your name : ")
designation = input("Enter your Designation : ")
monthly_salary = int(input("Enter your monthly salary : "))

employee_1= Employee(name,designation,monthly_salary)
employee_1.display_details()
annual_salary = employee_1.calculate_salary()
print(f"My annual salary is Rs {annual_salary}")

