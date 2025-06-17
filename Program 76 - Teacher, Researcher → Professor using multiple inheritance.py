# Teacher, Researcher → Professor using multiple inheritance
# Teacher: subject, experience
# Researcher: field, papers_published
# Professor inherits both and adds designation. Display all info.

class Teacher:
    def __init__(self, subject, experience):
        self.subject = subject
        self.experience = experience

class Researcher:
    def __init__(self, field, paper_published):
        self.field = field
        self.paper_published = paper_published

class Professor(Teacher,Researcher):
    def __init__(self, subject, experience, field, paper_published, designation):
        Teacher.__init__(self,subject,experience)
        Researcher.__init__(self,field,paper_published)
        self.designation = designation

    def display(self):
        print(f"The Professor Subject is {self.subject}")
        print(f"Years of experience is {self.experience} ")
        print(f"The Research field is {self.field}")
        print(f"The papers published is {self.paper_published}")
        print(f"The Designation is {self.designation}")

professor1 = Professor('English',12,'Research', 5,'Manager')
professor1.display()
