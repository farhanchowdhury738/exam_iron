# For Question 1
class Library:

    book_list = []
    
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)
        print(f"Book '{book.title}' by {book.author} has been added library.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


if __name__ == "__main__":
    book1 = Book("1", "a")
    book2 = Book("dd ", "yr")
    

    Library.entry_book(book1)
    Library.entry_book(book2)


# For Question 2 

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability



# For Question 3
class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        Library.entry_book(self)




# Question 4
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
       

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is currently unavailable.")

# For Question 5
class Book:
    def __init__(self, title, author, available=True):
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


if __name__ == "__main__":
    book1 = Book("4643", "hello book")

    book1.borrow_book()
    book1.return_book()


# For Question 6
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


if __name__ == "__main__":
    book1 = Book(1, "4535", "Hello Book!")
    book1.view_book_info()
    book1.borrow_book()
    book1.view_book_info()
    book1.return_book()
    book1.view_book_info()


# For Question 7
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

# For Question 8
class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow_book(self):
        if not self.available:
            raise ValueError(f"'{self.title}' is already borrowed.")
        self.available = False
        print(f"You've borrowed '{self.title}' by {self.author}.")

    def return_book(self):
        if self.available:
            raise ValueError(f"'{self.title}' was not borrowed, so it cannot be returned.")
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
            try:
                book_id = int(input("Enter the book ID to borrow: "))
                book = next((b for b in Library.book_list if b.book_id == book_id), None)
                
                if book:
                    book.borrow_book()  
                else:
                    print("Error: Invalid book ID.")  
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                book_id = int(input("Enter the book ID to return: "))
                book = next((b for b in Library.book_list if b.book_id == book_id), None)
                
                if book:
                    book.return_book()  
                else:
                    print("Error: Invalid book ID.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    book1 = Book(1, "424", "Hello")
    book2 = Book(2, "kallo", "mallo")
    Library.add_book(book1)
    Library.add_book(book2)

    main_menu()


# For Question 9
class Book:
    def __init__(self, book_id, title, author, available=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available = available

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def borrow_book(self):
        if not self.__available:
            raise ValueError(f"'{self.__title}' is already borrowed.")
        self.__available = False
        print(f"You've borrowed '{self.__title}' by {self.__author}.")

    def return_book(self):
        if self.__available:
            raise ValueError(f"'{self.__title}' was not borrowed, so it cannot be returned.")
        self.__available = True
        print(f"'{self.__title}' by {self.__author} has been returned and is now available.")

    def view_book_info(self):
        availability = "Available" if self.__available else "Unavailable"
        print(f"Book ID: {self.__book_id}\nTitle: {self.__title}\nAuthor: {self.__author}\nAvailability: {availability}")


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
            try:
                book_id = int(input("Enter the book ID to borrow: "))
                book = next((b for b in Library.book_list if b.get_book_id() == book_id), None)
                if book:
                    book.borrow_book()
                else:
                    print("Error: Invalid book ID.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                book_id = int(input("Enter the book ID to return: "))
                book = next((b for b in Library.book_list if b.get_book_id() == book_id), None)
                if book:
                    book.return_book()
                else:
                    print("Error: Invalid book ID.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    book1 = Book(1, "424", "Hello")
    book2 = Book(2, "kallo", "mallo")
    Library.add_book(book1)
    Library.add_book(book2)

    main_menu()










