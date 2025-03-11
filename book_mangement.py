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


        
        








# 🟢 Create Book instances
book1 = Book("Python Basics", "John Doe", 12345)
book2 = Book("Data Science", "Jane Smith", 67890)

# 🟢 Create Member instance
member1 = Member("Aryan", 101)

# 🔹 Test 1: View borrowed books before borrowing (should be empty)
print("\n📌 Test 1: View Borrowed Books Before Borrowing")
member1.view_borrowed_book()  # Expected: No books borrowed

# 🔹 Test 2: Borrow a book (should succeed)
print("\n📌 Test 2: Borrowing a Book")
member1.borrow_book(book1)  
# Expected: Aryan has borrowed 'Python Basics'

# 🔹 Test 3: Try borrowing the same book again (should fail)
print("\n📌 Test 3: Borrowing the same book again")
member1.borrow_book(book1)  
# Expected: 'Python Basics' has already been issued.

# 🔹 Test 4: Borrow another book (should succeed)
print("\n📌 Test 4: Borrow another book")
member1.borrow_book(book2)  
# Expected: Aryan has borrowed 'Data Science'

# 🔹 Test 5: View borrowed books after borrowing (should list both books)
print("\n📌 Test 5: View Borrowed Books After Borrowing")
member1.view_borrowed_book()  
# Expected: Python Basics & Data Science should be listed

# 🔹 Test 6: Return a book (should succeed)
print("\n📌 Test 6: Returning a Book")
member1.return_book(book1)  
# Expected: 'Python Basics' has been returned by Aryan

# 🔹 Test 7: Return the same book again (should fail)
print("\n📌 Test 7: Returning the same book again")
member1.return_book(book1)  
# Expected: Aryan never borrowed 'Python Basics' (because it was already returned)

# 🔹 Test 8: View borrowed books after returning (should only show Data Science)
print("\n📌 Test 8: View Borrowed Books After Returning")
member1.view_borrowed_book()  
