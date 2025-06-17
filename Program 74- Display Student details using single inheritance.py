# Create a class Person with attributes name and gender.
# Create a derived class Employee that adds employee_id and designation.
# Write a method to display all details.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, designation):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.designation = designation

    def display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Employee Id is {self.employee_id}")
        print(f"Designation is {self.designation}")


student1 = Employee("Ajay", 24, 101, 'QA Engineer')
student1.display()


