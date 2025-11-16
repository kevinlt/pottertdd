from src.purchased_book import PurchasedBook
from src.cart import Cart


class TestBuyingBooks:

    _discount_dataset = [
        (1, 1, 8),
        (1, 2, 8 * 2 * 0.95),
        (1, 3, 8 * 3 * 0.9),
        (1, 4, 8 * 4 * 0.85),
        (1, 5, 8 * 5 * 0.8),
        (1, 6, 8 * 6 * 0.75),

    ]

    def test_should_return_0_if_no_books_to_buy(self):
        cart = Cart()
        assert cart.get_bill() == 0

    def test_should_return_8_if_cart_has_1_book(self):
        cart = Cart()
        cart.add_a_book(BookBuilder().of_id(1).build())
        assert cart.get_bill() == 8

    def test_should_return_16_if_cart_has_2_books(self):
        cart = Cart()
        cart.add_a_book(BookBuilder().of_id(1).quantity(2).build())
        assert cart.get_bill() == 16

    def test_should_apply_discount_when_cart_has_different_books(self):
        cart = Cart()
        for book_quantity, different_books, expected_bill in self._discount_dataset:
            cart.add_a_book(BookBuilder().of_id(1).quantity(book_quantity).build())
            assert cart.get_bill() == expected_bill

class BookBuilder:

    _id: int = 0
    _name: str = ""
    _price: float = 8.0
    _quantity: int = 1

    def build(self):
        return PurchasedBook(self._id, self._name, self._price, self._quantity)

    def of_id(self, id: int):
        self._id = id
        return self

    def quantity(self, quantity: int):
        self._quantity = quantity
        return self