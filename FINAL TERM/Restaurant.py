class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = {}

    def show_menu(self):
        if not self.menu:
            print("The menu is currently empty.")
        else:
            print("*****Menu*****")
            print("Name\tPrice\tQuantity")
            for item, details in self.menu.items():
                print(f"{item}\t${details['price']:.2f}\t{details['quantity']}")

    def add_menu_item(self, item, price, quantity):
        self.menu[item] = {"price": price, "quantity": quantity}
        print(f"Added {item} to the menu at ${price:.2f} with quantity {quantity}.")

    def remove_menu_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"Removed {item} from the menu.")
        else:
            print(f"{item} is not in the menu.")

    def add_customer(self, customer):
        self.customers[customer.email] = customer
        print(f"Customer {customer.name} added to the system.")

    def remove_customer(self, email):
        if email in self.customers:
            del self.customers[email]
            print(f"Customer with email {email} removed from the system.")
        else:
            print(f"No customer found with email {email}.")

    def view_customers(self):
        if not self.customers:
            print("No customers in the system.")
        else:
            print("*****Customers*****")
            print("Name\tEmail\tAddress")
            for email, customer in self.customers.items():
                print(f"{customer.name}\t{email}\t{customer.address}")
