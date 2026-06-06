class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True
        print(f"You have borrowed '{self.title}' by {self.author}. And the variable is_borrowed is now set to {self.is_borrowed}.")

    def return_book(self):
        self.is_borrowed = False
        print(f"You have returned '{self.title}' by {self.author}. And the variable is_borrowed is now set to {self.is_borrowed}.")

book1 = Book("The Secret", "Rhonda Byrne")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

for book in (book1, book2, book3):
    book.borrow()
    book.return_book()

    

