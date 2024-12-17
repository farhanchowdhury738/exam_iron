from Restaurant import Restaurant
from Admin import Admin
from Customer import Customer

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
