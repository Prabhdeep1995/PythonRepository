# Write Python program that accepts marks in 5 subjects and outputs average marks.

maths_marks = input("Enter marks of Maths subject : ")
english_marks = input("Enter marks of English subject : ")
science_marks = input("Enter marks of Science subject : ")
computer_marks = input("Enter marks of computer subject : ")
hindi_marks = input("Enter marks of Hindi subject :")

sum = 0

if (maths_marks.replace('.','').isdigit() and english_marks.replace('.','').isdigit()
        and science_marks.replace('.','').isdigit()
        and computer_marks.replace('.', '').isdigit()
        and hindi_marks.replace('.','').isdigit()):
    maths_marks=float(maths_marks)
    english_marks=float(english_marks)
    science_marks= float(science_marks)
    computer_marks= float(computer_marks)
    hindi_marks= float(hindi_marks)
    sum= maths_marks+english_marks+science_marks+computer_marks+hindi_marks
    avg = sum/5
    print(f"The average of Five subject marks is : {avg}")
else:
    print("Invalid Input")