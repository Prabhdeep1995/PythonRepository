# Add new student dictionary in a list using function

def add_new_student(data, name, roll_no,age,course):
    data.append({'name': name,
                         'roll_no' : roll_no,
                         'age' : age,
                         'course': course})
    return data



student_data= [{"Name": "Ram",
               "roll_no": 10,
               "age": 20,
               "Course": 'Python'},
               {"Name": "Mohan",
                "roll_no": 20,
                "age": 23,
                "Course": 'Java'},
               ]

new_list= add_new_student(student_data, 'Rahul', 23, 28,'Java')
print(f"The updated student list is : {new_list}")






