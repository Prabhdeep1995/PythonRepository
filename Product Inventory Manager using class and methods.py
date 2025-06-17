# Create a class Product with attributes name, price, and quantity.
# Add methods to purchase items (reduce stock) and check availability.

class Inventory:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def purchase_item(self):
        purchased_price = self.price * self.quantity
        return purchased_price

    def check_availability(self):
        


