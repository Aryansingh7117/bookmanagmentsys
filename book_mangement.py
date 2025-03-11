class Book:
    
    def __init__(self,title,author,isbn :int):  
        self.title = title
        self.author =author
        self.isbn = isbn
        self.available = True #initial state should be true

    def display_info(self):  #shows all the information about book
        return f"-----------------\ntitle = {self.title}\nauthor = {self.author}\nISBN = {self.isbn}\nAvailable = {self.available}\n-----------------"
    
    def is_available(self):  #shows if book is available
        if self.available == True:
            return f'{self.title} is available'
        else:
            return f'{self.title} is unavailable'
        
    def mark_issue(self):   #run when book is given to customer
        if self.available == True:
            self.available = False
        else:
            print(f"{self.title} already issued")
        
    def mark_return(self):  #run when book is given back
        self.available = True



class Member:
    
    def __init__(self, name , member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self ,book):
        if book.available:
            book.mark_issue()
            self.borrowed_books.append(book)
            print(f'{self.name} has borrowed {book.title}')
        else:
            print(f'{book.title} has already been issued')

    def return_book(self,book):
        if book in self.borrowed_books:
            book.mark_return()
            self.borrowed_books.remove(book)
            print(f'{book.title} has been returned by {self.name}')
        else:
            print(f'{self.name} never borrowed {book.title}')

    def view_borrowed_book(self):
        if self.borrowed_books:
            print(f"\n{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(f"{book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")



class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        title = input("enter title of book")
        author = input("enter author of book")
        isbn = input("enter isbn of book")


        if isbn in self.books:
            print("book with same isbn already exists in our system")
            return
        
        book_1 = Book(title, author,isbn)
        self.books[isbn]= book_1
        print(f"'{title}' by {author} added to the library.")

    def add_member(self):
        name = input("enter your name")
        member_id = input("enter your member_id")


        if member_id in self.members:
            print("member_id already exists in our system")
            return
        
        member_1 = Member(name,member_id)
        self.members[member_id]= member_1
        print(f"'{name}' is add to our system with member_id {member_id} .")
    
    def find_book(self,isbn_or_title):
        
        if isbn_or_title in self.books:
            book = self.books[isbn_or_title]
            print(f'Book found: {book.title} by {book.author} (isbn {book.isbn})')
            return book 
        
        for book in self.books.values():
            if book.title.lower() == isbn_or_title.lower():
                print(f"Book found: '{book.title}' by {book.author} (ISBN: {book.isbn})")
            return book
        
        print("Book not found.")
        return None
    
    def display_book(self, identifier=None):
        if not self.books:
            print("No books available in the library.")
            return

        if identifier is None:
            print("\n📚 List of Books:")
            for book in self.books.values():
                print(book.display_info())  # Assuming `Book` class has `display_info()`
        
        else:
            if identifier in self.books:
                print("\n📖 Book Found:")
                print(self.books[identifier].display_info())
                return
            
            for book in self.books.values():
                if book.title.lower() == identifier.lower():
                    print("\n📖 Book Found:")
                    print(book.display_info())
                    return
            
            print("❌ Book not found.")

        
        