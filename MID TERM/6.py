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
