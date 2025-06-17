# University → College → Student
# Class Structure:
# University: university_name, location
# College: Inherits from University, adds college_name, college_code
# Student: Inherits from College, adds student_name, roll_number
# Track a student’s academic background — university → college → student. Display all related info from the student level

class University:
    def __init__(self,university_name, location):
        self.university_name = university_name
        self.location = location

class College(University):
    def __init__(self, university_name, location,college_name, college_code):
        super().__init__(university_name,location)
        self.college_name = college_name
        self.college_code = college_code

class Student(College):
    def __init__(self, university_name, location,college_name, college_code,student_name, roll_number):
        super().__init__(university_name,location,college_name,college_code)
        self.student_name = student_name
        self.roll_number = roll_number

    def display_student_details(self):
        print(f"The Student name is {self.student_name} having roll number {self.roll_number}\nThe college name is {self.college_name} with college code {self.college_code} which is affilated to {self.university_name} university locate at {self.location}")


student1 = Student('Jiwaji University','Gwalior','Prestige',234,'Prabhdeep',135)
student1.display_student_details()