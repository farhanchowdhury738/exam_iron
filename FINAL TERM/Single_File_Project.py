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

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.past_orders = []

    def view_menu(self, restaurant):
        restaurant.show_menu()

    def place_order(self, restaurant, item_name, item_quantity):
        if item_name not in restaurant.menu:
            print(f"{item_name} is not available in the menu.")
            return

        item_details = restaurant.menu[item_name]
        price_per_unit = item_details["price"]
        available_quantity = item_details["quantity"]

        if item_quantity > available_quantity:
            print(f"Insufficient quantity of {item_name}. Available: {available_quantity}.")
            return

        total_cost = price_per_unit * item_quantity
        if self.balance < total_cost:
            print(f"Insufficient balance to order {item_quantity} {item_name}(s). Total cost: ${total_cost:.2f}. Add more funds.")
        else:
            self.balance -= total_cost
            self.past_orders.append(f"{item_quantity}x {item_name}")
            restaurant.menu[item_name]["quantity"] -= item_quantity
            print(f"Order placed for {item_quantity} {item_name}(s). Remaining balance: ${self.balance:.2f}.")

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added ${amount:.2f} to balance. Current balance: ${self.balance:.2f}.")
        else:
            print("Amount must be greater than zero.")

    def view_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def view_past_orders(self):
        if not self.past_orders:
            print("No past orders.")
        else:
            print("Past Orders:")
            for order in self.past_orders:
                print(f"- {order}")

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

def main():
    restaurant = Restaurant()
    admin = Admin(restaurant)

    admin_username = "farhan"
    admin_password = "farhan"

    while True:
        print("\n------Restaurant Management System-----------")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username == admin_username and password == admin_password:
                print("\nAdmin - Manage System")
                while True:
                    print("1. Manage Menu")
                    print("2. Manage Customers")
                    print("3. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        while True:
                            print("\nManage Menu")
                            print("1. Add Menu Item")
                            print("2. Remove Menu Item")
                            print("3. View All Menu")
                            print("4. Modify Menu Item")  
                            print("5. Back to Admin Menu")
                            menu_choice = input("Enter your choice: ")

                            if menu_choice == "1":
                                item = input("Enter item name: ")
                                try:
                                    price = float(input("Enter item price: "))
                                except ValueError:
                                    print("Invalid input! Price must be a number.")
                                    continue
                                try:
                                    quantity = int(input("Enter item quantity: "))
                                except ValueError:
                                    print("Invalid input! Quantity must be a whole number.")
                                    continue
                                admin.add_menu_item(item, price, quantity)
                            elif menu_choice == "2":
                                item = input("Enter item name to remove: ")
                                admin.remove_menu_item(item)
                            elif menu_choice == "3":
                                restaurant.show_menu()
                            elif menu_choice == "4":
                                item = input("Enter item name to modify: ")
                                admin.modify_menu_item(item)
                            elif menu_choice == "5":
                                print("Returning to Admin Menu...")
                                break
                            else:
                                print("Invalid choice. Try again.")

                    elif admin_choice == "2":
                        while True:
                            print("\nManage Customers")
                            print("1. Add Customer")
                            print("2. Remove Customer")
                            print("3. Modify Customer")
                            print("4. View All Customers")
                            print("5. Back to Admin Menu")
                            customer_choice = input("Enter your choice: ")

                            if customer_choice == "1":
                                name = input("Enter customer name: ")
                                email = input("Enter customer email: ")
                                address = input("Enter customer address: ")
                                admin.add_customer(name, email, address)
                            elif customer_choice == "2":
                                email = input("Enter customer email to remove: ")
                                admin.remove_customer(email)
                            elif customer_choice == "3":
                                email = input("Enter customer email to modify: ").lower()
                                admin.modify_customer(email)
                            elif customer_choice == "4":
                                admin.view_customers()
                            elif customer_choice == "5":
                                print("Returning to Admin Menu...")
                                break
                            else:
                                print("Invalid choice. Try again.")

                    elif admin_choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("\ninvalid user name or passwod!")

        elif choice == "2":
            print("\nCustomer Login")
            email = input("Enter your email: ")

            if email not in restaurant.customers:
                print("No customer found with this email. Please contact admin.")
                continue

            customer = restaurant.customers[email]

            while True:
                print("\nCustomer Menu")
                print("1. View Menu")
                print("2. Place Order")
                print("3. Add Funds")
                print("4. View Balance")
                print("5. View Past Orders")
                print("6. Logout")
                customer_choice = input("Enter your choice: ")

                if customer_choice == "1":
                    customer.view_menu(restaurant)
                elif customer_choice == "2":
                    item_name = input("Enter item name: ")
                    try:
                        item_quantity = int(input("Enter item quantity: "))
                    except ValueError:
                            print("Invalid input! quantity must be a whole number.")
                            continue
                    customer.place_order(restaurant, item_name, item_quantity)
                elif customer_choice == "3":
                    try:
                        amount = float(input("Enter amount to add: "))
                    except ValueError:
                        print("Invalid input! Funds must be a number.r")
                        continue
                    customer.add_funds(amount)
                elif customer_choice == "4":
                    customer.view_balance()
                elif customer_choice == "5":
                    customer.view_past_orders()
                elif customer_choice == "6":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
