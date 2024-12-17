from Customer import Customer

class Admin:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def add_menu_item(self, item, price, quantity):
        self.restaurant.add_menu_item(item, price, quantity)

    def remove_menu_item(self, item):
        self.restaurant.remove_menu_item(item)

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.restaurant.add_customer(customer)

    def remove_customer(self, email):
        self.restaurant.remove_customer(email)

    def view_customers(self):
        self.restaurant.view_customers()
