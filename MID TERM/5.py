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


# Example usage
if __name__ == "__main__":
    book1 = Book("4643", "hello book")

    book1.borrow_book()
    book1.return_book()
