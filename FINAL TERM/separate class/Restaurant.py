class Restaurant:
    def __init__(self):
        self.menu = {
            "pizza": {"price": 8.99, "quantity": 10},
            "burger": {"price": 5.49, "quantity": 15},
            "pasta": {"price": 7.99, "quantity": 12},
            "salad": {"price": 4.99, "quantity": 20}
        }
        self.customers = {}

    def show_menu(self):
        if not self.menu:
            print("The menu is currently empty.")
        else:
            print("*****Menu*****")
            print("Name\tPrice\tQuantity")
            for item, details in self.menu.items():
                print(f"{item}\t${details['price']:.2f}\t{details['quantity']}")
    
    def view_customers(self):
        if not self.customers:
            print("No customers in the system.")
        else:
            print("*****Customers*****")
            print("Name\tEmail\tAddress")
            for email, customer in self.customers.items():
                print(f"{customer.name}\t{email}\t{customer.address}")

    def add_menu_item(self, item, price, quantity):
        self.menu[item] = {"price": price, "quantity": quantity}
        print(f"Added {item} to the menu at ${price:.2f} with quantity {quantity}.")

    def remove_menu_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"Removed {item} from the menu.")
        else:
            print(f"{item} is not in the menu.")
    
    def modify_menu_item(self, item, new_name=None, new_price=None, new_quantity=None):
        if item in self.menu:
            if new_name:
                self.menu[item]["name"] = new_name
            if new_price is not None:
                self.menu[item]["price"] = new_price
            if new_quantity is not None:
                self.menu[item]["quantity"] = new_quantity
            
            updated_details = []
            if new_name:
                updated_details.append(f"Name: {new_name}")
            if new_price is not None:
                updated_details.append(f"Price: ${new_price:.2f}")
            if new_quantity is not None:
                updated_details.append(f"Quantity: {new_quantity}")
            
            print(f"Updated {item}-> " + ", ".join(updated_details))
        else:
            print(f"{item} is not in the menu.")
    
    def add_customer(self, customer):
        self.customers[customer.email] = customer
        print(f"Added customer {customer.name} with email {customer.email}.")

    def remove_customer(self, email):
        if email in self.customers:
            del self.customers[email]
            print(f"Removed customer with email {email}.")
        else:
            print(f"Customer with email {email} not found.")
    
    def modify_customer(self, email, new_name=None, new_email=None, new_address=None):
        if email in self.customers:
            customer = self.customers[email]
            if new_name:
                customer.name = new_name
            if new_email:
                self.customers[new_email] = self.customers.pop(email)
                customer.email = new_email
            if new_address:
                customer.address = new_address

            updated_details = []
            if new_name:
                updated_details.append(f"Name: {new_name}")
            if new_email:
                updated_details.append(f"Email: {new_email}")
            if new_address:
                updated_details.append(f"Address: {new_address}")

            print(f"Updated customer details-> " + ", ".join(updated_details))
        else:
            print(f"Customer with email {email} not found.")
