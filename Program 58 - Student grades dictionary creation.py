# Approach 1- Creating new dictionary for grades

student_marks ={'Jenny':92, 'Harry': 78, 'Dimpy': 56, 'Rahul':41}
student_Grades={}
for marks in student_marks:
    if student_marks[marks]>=91 and student_marks[marks]<=100:
        student_Grades[marks]= 'A+'
    elif student_marks[marks]>=81 and student_marks[marks]<=90:
        student_Grades[marks]= 'A'
    elif student_marks[marks]>=71 and student_marks[marks]<=80:
        student_Grades[marks]= 'B+'
    elif student_marks[marks]>=61 and student_marks[marks]<=70:
        student_Grades[marks]= 'B'
    elif student_marks[marks]>=51 and student_marks[marks]<=60:
        student_Grades[marks]= 'C'
    elif student_marks[marks]>=41 and student_marks[marks]<=50:
        student_Grades[marks]= 'D'
    else:
        student_Grades[marks]= 'F'

print(f"The Dictionary with student Grades is {student_Grades}")





# Approach 2- replacing the values of existing dictionary
# student_marks ={'Jenny':92, 'Harry': 78, 'Dimpy': 56, 'Rahul':41}
# for marks in student_marks:
#     if student_marks[marks]>=91 and student_marks[marks]<=100:
#         student_marks[marks]= 'A+'
#     elif student_marks[marks]>=81 and student_marks[marks]<=90:
#         student_marks[marks]= 'A'
#     elif student_marks[marks]>=71 and student_marks[marks]<=80:
#         student_marks[marks]= 'B+'
#     elif student_marks[marks]>=61 and student_marks[marks]<=70:
#         student_marks[marks]= 'B'
#     elif student_marks[marks]>=51 and student_marks[marks]<=60:
#         student_marks[marks]= 'C'
#     elif student_marks[marks]>=41 and student_marks[marks]<=50:
#         student_marks[marks]= 'D'
#     else:
#         student_marks[marks]= 'F'
#
# print(f"The Dictionary with student Grades is {student_marks}")







