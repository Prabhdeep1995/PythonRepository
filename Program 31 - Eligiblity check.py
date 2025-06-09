scienceMarks= input("Enter marks of science subject : ")
mathsMarks = input("Enter marks of Maths subject : ")
englishMarks = input("Enter marks of English subject : ")

if scienceMarks.replace('.',"",1).isdigit() and mathsMarks.replace('.',"",1).isdigit() and englishMarks.replace('.',"",1).isdigit():
    scienceMarks=float(scienceMarks)
    mathsMarks= float(mathsMarks)
    englishMarks=float(englishMarks)
    avgMarks = (scienceMarks+mathsMarks+englishMarks)/3

    print("The average score is : ",avgMarks)

    if (scienceMarks>=40 and mathsMarks>=40 and englishMarks>=40) or avgMarks>=50:
        print("Pass")
    else:
        print("Fail")
else:
    print("wrong input")
