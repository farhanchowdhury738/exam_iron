from Restaurant import Restaurant

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

