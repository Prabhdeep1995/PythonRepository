class Instructor:
    def __init__(self,instructor_name, address):
        self.name= instructor_name
        self.address = address


instructor_1= Instructor('Raj','Delhi')
print(f"The name of the Instructor 1 is {instructor_1.name} and his address is {instructor_1.address}")

instructor_2= Instructor('Prabh','Noida')
print(f"The name of the Instructor 2 is {instructor_2.name} and his address is {instructor_2.address}")


instructor_3= Instructor('Kartar','Ghaziabad')
print(f"The name of the Instructor 3 is {instructor_3.name} and his address is {instructor_3.address}")


instructor_4= Instructor('Rahul','Agra')
print(f"The name of the Instructor 4 is {instructor_4.name} and his address is {instructor_4.address}")
