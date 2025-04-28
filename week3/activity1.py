# Manage a small library — add and show books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(f"Title: {self.title}, Author: {self.author}")

class library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        print("Books in the library:")
        for book in self.books:
            book.show()

book1 = Book('Mastering Graphics Programming with Vulkan', 'MARCO CASTORINA | GABRIEL SASSONE')
book2 = Book('The Art of Computer Programming', 'Donald E. Knuth')

lib = library()
lib.add_book(book1)
lib.add_book(book2)
lib.show_books()