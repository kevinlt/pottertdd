from src.purchased_book import PurchasedBook


class Cart:

    _books: [PurchasedBook] = []
    _discounts = {
        1: 1,
        2: 0.95,
        3: 0.9,
        4: 0.85,
        5: 0.8,
        6: 0.75,
        7: 0.7
    }

    def __init__(self):
        self._books = []

    def get_bill(self):
        bill = 0
        if self._books:
            for book in self._books:
                bill += book.price * book.quantity
            different_books = len(self._books)
            bill = bill * self._discounts[different_books]
        return bill

    def add_a_book(self, purchased_book: PurchasedBook):
        self._books.append(purchased_book)
