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
    
