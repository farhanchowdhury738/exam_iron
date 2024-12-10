class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You've borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")
    
    def return_book(self):
        self.available = True
        print(f"'{self.title}' by {self.author} has been returned and is now available.")

    def view_book_info(self):
        availability = "Available" if self.available else "Unavailable"
        print(f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nAvailability: {availability}")


class Library:
    book_list = []

    @classmethod
    def add_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def view_all_books(cls):
        if not cls.book_list:
            print("No books available in the library.")
        else:
            for book in cls.book_list:
                book.view_book_info()


def main_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            Library.view_all_books()

        elif choice == "2":
            book_id = int(input("Enter the book ID to borrow: "))
            book = next((b for b in Library.book_list if b.book_id == book_id), None)
            if book:
                book.borrow_book()
            else:
                print("Book not found!")

        elif choice == "3":
            book_id = int(input("Enter the book ID to return: "))
            book = next((b for b in Library.book_list if b.book_id == book_id), None)
            if book:
                book.return_book()
            else:
                print("Book not found!")

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    book1 = Book(1, "24", "Hello")
    book2 = Book(2, "kallo", "malllo1")
    Library.add_book(book1)
    Library.add_book(book2)

    
    main_menu()
