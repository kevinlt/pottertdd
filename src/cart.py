from src.purchased_book import PurchasedBook


class Cart:

    _books: [PurchasedBook] = []

    def __init__(self):
        self._books = []

    def get_bill(self):
        bill = 0
        if self._books:
            for book in self._books:
                bill += book.price * book.quantity
            different_books = len(self._books)
            if different_books == 2:
                bill = bill * 0.95
            elif different_books == 3:
                bill = bill * 0.9
        return bill

    def add_a_book(self, purchased_book: PurchasedBook):
        self._books.append(purchased_book)
