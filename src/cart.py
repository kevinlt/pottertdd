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
            for _ in reversed(range(1,len(self._discounts)+1)):
                books = self.get_books_for_quantity(_)
                if books:
                    bill += self.get_discount_bill(books)
        return bill

    def get_discount_bill(self, books: list[PurchasedBook]) -> float:
        discount_bill = 0
        booksCopy = books.copy()
        while booksCopy:
            bill = 0
            batch = booksCopy[:len(self._discounts)]
            for book in batch:
                bill += book.price
                booksCopy.remove(book)
            discount_bill += bill *self._discounts[len(batch)]
        return discount_bill

    def get_books_for_quantity(self, quantity: int) -> list[PurchasedBook]:
        return list(filter(lambda book: book.quantity >= quantity, self._books))

    def add_a_book(self, purchased_book: PurchasedBook):
        self._books.append(purchased_book)
