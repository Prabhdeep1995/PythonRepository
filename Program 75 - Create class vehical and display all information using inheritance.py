# Create a class Vehicle with attributes brand and speed.
# Create a class Car that inherits from Vehicle and adds fuel_type.
# Create an object and display all information.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand,speed)
        self.fuel_type = fuel_type

    def display_details(self):
        print(f"The Car Brand is {self.brand}")
        print(f"The car speed is {self.speed}")
        print(f"The Fuel type is {self.fuel_type}")

car1 = Car('Maruti', 90, 'Petrol')
car1.display_details()