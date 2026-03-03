class Library:
    def __init__(self):
        self.books = {}
    def add_books(self, bookID, title, author, copies):
        self.books[bookID] = {"title": title, "author": author, "total": copies, "available": copies}
    def borrow_book(self, bookID):
        if bookID in self.books and self.books[bookID]["available"] > 0:
            self.books[bookID]["available"] -= 1
        else:
            print("book not available")
    def return_book(self, bookID):
        if bookID in self.books:
            if self.books[bookID]["available"] < self.books[bookID]["total"]:
                self.books[bookID]["available"] += 1
                print(f"Book {bookID} successfully returned.")
            else:
                print(f"Cannot return book {bookID}. No book was borrowed.")
        else:
            print("Book ID does not exist.")
    def display_books(self):
        for bid, info in self.books.items():
            print(f"ID: {bid}, Title:{info['title']}, Author:{info['author']}, Copies:{info['available']}")
        
lib = Library ()
lib.add_books("OP001","One Piece", "Eiichiro Oda", 3)
lib.add_books("OP002","Blood moon", "Michael", 5)
lib.borrow_book("OP001")
lib.return_book("OP001")
lib.display_books()


