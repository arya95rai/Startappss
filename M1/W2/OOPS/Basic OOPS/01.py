class Book:

    def __init__(self, book_id, title, author, price, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.available_copies = available_copies

    def issue_book(self):
        if self.available_copies >= 1:
            self.available_copies -= 1
            print("Book issued!")
            print("Remaining copies:", self.available_copies)
        else:
            print("Book not available")

    def return_book(self):
        self.available_copies += 1
        print("Book returned!")
        print("Available copies:", self.available_copies)

    def show_details(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Available Copies:", self.available_copies)

    def update_price(self, amount):
        self.price += amount
        print("Updated price:", self.price)

    def check_availability(self):
        if self.available_copies > 0:
            print("Book is available")
        else:
            print("Book not available")