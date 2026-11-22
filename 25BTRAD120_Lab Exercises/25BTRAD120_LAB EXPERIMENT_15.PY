class LibraryItem:
def _init __ (self, title):
self.title = title
self.available = True
def issue(self):
if self.available:
self.available = False
print(f'"{self.title}" issued successfully.')
else:
print(f'" {self. title}" is not available.'
def return_item(self):
if not self.available:
self.available = True
print(f'"{self. title}" returned successfully. ')
else:
print(f'"{self. title}" was not issued.')
# Book inherits the common properties and methods of LibraryItem.
class Book(LibraryItem)
def _init_(self, title, author, book_id):
super()._init_(title)
self.author = author
self.book_id = book_id
def display(self):
status = "Available" if self. available else "Issued"
print(f"{self.book_id} | {self.title} |"
f"{self.author} | {status}")
class Library:
def_init __ (self):
self.books = []
def add_book(self, book):
self.books.append(book)
print(f'"{book. title}" added to the library.')
def show_books(self):
print("\nBOOK ID | TITLE | AUTHOR | STATUS")
print("------------------------------")
for book in self.books:
book.display ()
# Demonstration of library operations.
Library = Library()
book1 = Book("Python Basics", "R. Sharma", "B101")
book2 = Book("Data Structures", "A. Kumar", "B102")
Library.add_book (book1)
library.add_book(book2)
library.show_books ()
book1.issue ()
book1.issue ()        # Tests issuing an unavailable book
bookl.return_item()
book1.return_item()   # Tests returning a book that is available
library.show_books()
book1.return_item()   # Tests returning a book that is available
