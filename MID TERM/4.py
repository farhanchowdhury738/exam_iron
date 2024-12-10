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
