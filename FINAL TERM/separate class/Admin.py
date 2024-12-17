from Customer import Customer

class Admin:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def add_menu_item(self, item, price, quantity):
        self.restaurant.add_menu_item(item, price, quantity)

    def remove_menu_item(self, item):
        self.restaurant.remove_menu_item(item)

    def modify_menu_item(self, item):
        if item in self.restaurant.menu:
            print(f"\nCurrent details for {item}:")
            print("Name\tPrice\tQuantity")
            details = self.restaurant.menu[item]
            print(f"{item}\t${details['price']:.2f}\t{details['quantity']}")
            print("\nWhat would you like to change?")
            print("1. Change Name")
            print("2. Change Price")
            print("3. Change Quantity")
            print("4. Cancel")
            choice = input("Enter your choice: ")

            if choice == "1":
                new_name = input(f"Enter new name for {item}: ")
                if new_name:
                    price = self.restaurant.menu[item]["price"]
                    quantity = self.restaurant.menu[item]["quantity"]
                    del self.restaurant.menu[item]
                    self.restaurant.menu[new_name] = {"price": price, "quantity": quantity}
                    print(f"Item name updated to {new_name}.")
                else:
                    print("No change made to name.")
            elif choice == "2":
                new_price = input(f"Enter new price for {item}: ")
                if new_price:
                    try:
                        new_price = float(new_price)
                        self.restaurant.modify_menu_item(item, new_price=new_price)
                    except ValueError:
                        print("Invalid price input! Must be a number.")
                else:
                    print("No change made to price.")
            elif choice == "3":
                new_quantity = input(f"Enter new quantity for {item}: ")
                if new_quantity:
                    try:
                        new_quantity = int(new_quantity)
                        self.restaurant.modify_menu_item(item, new_quantity=new_quantity)
                    except ValueError:
                        print("Invalid quantity input! Must be a whole number.")
                else:
                    print("No change made to quantity.")
            elif choice == "4":
                print("Cancelling modification.")
            else:
                print("Invalid choice. Try again.")
        else:
            print(f"{item} is not in the menu.")

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.restaurant.add_customer(customer)

    def remove_customer(self, email):
        self.restaurant.remove_customer(email)

    def modify_customer(self, email):
        if email in self.restaurant.customers:
            customer = self.restaurant.customers[email]
            print(f"\nCurrent details for {customer.name}:")
            print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")
            print("\nWhat would you like to change?")
            print("1. Change Name")
            print("2. Change Email")
            print("3. Change Address")
            print("4. Cancel")
            choice = input("Enter your choice: ")

            if choice == "1":
                new_name = input(f"Enter new name for {customer.name}: ")
                if new_name:
                    self.restaurant.modify_customer(email, new_name=new_name)
            elif choice == "2":
                new_email = input(f"Enter new email for {customer.email}: ")
                if new_email:
                    self.restaurant.modify_customer(email, new_email=new_email)
            elif choice == "3":
                new_address = input(f"Enter new address for {customer.name}: ")
                if new_address:
                    self.restaurant.modify_customer(email, new_address=new_address)
            elif choice == "4":
                print("Cancelling modification.")
            else:
                print("Invalid choice. Try again.")
        else:
            print(f"Customer with email {email} not found.")

    def view_customers(self):
        self.restaurant.view_customers()

