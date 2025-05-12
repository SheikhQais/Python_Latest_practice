class Book:
    def __init__(self, _title, _author, _available_status):
        self.title = _title
        self.author = _author
        self.available_status = _available_status
    
    def __str__(self):
        return f'Title: {self.title} \nAuthor: {self.author} \nAvailable Status: {self.available_status}'
    
    
class Library:
    def __init__(self):
        self.books = []
        
    def Add_book(self, book):
        self.books.append(book)
        print(f'Book Added: {book.title}')
        
    def Remove_book(self, book):
        for x in self.books:
            if x.title.lower() == book.title.lower():
                self.books.remove(x)
        print(f'Book Removed: {book.title}')
                
    def Available_books(self):
        print('Available Books:')
        for x in self.books:
            if x.available_status:
                print(x)
                
book1 = Book('Fuck You', 'Qais', True)
print(book1)
book2 = Book("Clean Code", "Robert C. Martin", False)
print(book2)

lib = Library()
lib.Add_book(book1)
lib.Add_book(book2)

lib.Available_books()
lib.Remove_book(book2)